from __future__ import annotations

import json
import os
import tempfile
import time
import zipfile
from io import BytesIO
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from src.agent import (
    PROVIDER_PRESETS,
    analyze_with_gpt,
    build_markdown_report,
    merge_results,
)
from src.deterministic_engine import analyze_structured_files
from src.exporter import export_report
from src.file_reader import file_to_markdown
from src.rule_loader import DEFAULT_RULES, load_rules, parse_rule_catalog
from src.session_store import list_sessions, save_session


APP_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = APP_DIR / "output"
SUPPORTED_TYPES = ["xlsx", "xls", "csv", "docx", "pdf", "md", "txt"]

PROVIDER_OPTIONS = [
    ("offline", "Offline Rule Engine"),
    ("openai", "OpenAI GPT"),
    ("gemini", "Google Gemini"),
    ("groq", "Groq"),
    ("openrouter", "OpenRouter"),
    ("ollama", "Ollama Local"),
    ("lmstudio", "LM Studio Local"),
]
PROVIDER_LABELS = dict(PROVIDER_OPTIONS)

RULE_APPEND = "Bo sung rule mac dinh"
RULE_REPLACE = "Chi dung rule upload"
FEASIBILITY_GROUP = "Tính khả thi phương án"


load_dotenv()


def _env_bool(name: str, default: str = "0") -> bool:
    return os.getenv(name, default).lower() in {"1", "true", "yes", "on"}


def _env_int(name: str, default: int) -> int:
    try:
        return int(float(os.getenv(name, str(default)) or str(default)))
    except Exception:
        return default


def _default_provider() -> str:
    provider = os.getenv("AI_PROVIDER", "").strip().lower()
    if not provider:
        provider = "offline" if _env_bool("OFFLINE_MODE", "1") else "openai"
    valid = {key for key, _ in PROVIDER_OPTIONS}
    return provider if provider in valid else "offline"


def _default_model(provider: str) -> str:
    if provider == "offline":
        return ""
    generic = os.getenv("AI_MODEL", "").strip()
    if generic:
        return generic
    preset = PROVIDER_PRESETS.get(provider, {})
    model_env = preset.get("model_env")
    if model_env and os.getenv(model_env):
        return os.getenv(model_env, "").strip()
    return preset.get("default_model", "")


def _default_base_url(provider: str) -> str:
    return os.getenv("AI_BASE_URL", "").strip() or str(
        PROVIDER_PRESETS.get(provider, {}).get("base_url") or ""
    )


def _provider_key_env(provider: str) -> str:
    return PROVIDER_PRESETS.get(provider, {}).get("api_key_env", "AI_API_KEY")


def _missing_ai_config_message(provider: str) -> str:
    label = PROVIDER_LABELS.get(provider, provider)
    key_env = _provider_key_env(provider)
    return (
        f"{label}: chua co API key. Nhap API key trong sidebar hoac khai bao "
        f"{key_env} trong Secrets/.env. Bao cao da duoc tao bang rule engine local."
    )


def _friendly_ai_error(provider: str, error: Exception) -> str:
    label = PROVIDER_LABELS.get(provider, provider)
    raw = str(error)
    if "403" in raw or "Forbidden" in raw:
        if provider == "gemini":
            return (
                f"{label}: bi tu choi 403. Kiem tra GEMINI_API_KEY, dam bao API key "
                "duoc phep dung Generative Language API, khong bi han che sai domain/IP, "
                "va model dang chon duoc tai khoan cap quyen."
            )
        if provider == "openrouter":
            return (
                f"{label}: bi tu choi 403. Kiem tra OPENROUTER_API_KEY, quota/tai khoan, "
                "quyen truy cap model va cau hinh Site URL neu tai khoan yeu cau."
            )
        if provider == "groq":
            return (
                f"{label}: bi tu choi 403. Kiem tra GROQ_API_KEY, quota va model dang chon."
            )
        if provider == "openai":
            return (
                f"{label}: bi tu choi 403. Kiem tra OPENAI_API_KEY, project/quota va "
                "quyen truy cap model dang chon."
            )
        return f"{label}: bi tu choi 403. Kiem tra API key, base URL, quota va quyen model."
    if "401" in raw or "Unauthorized" in raw:
        return f"{label}: API key khong hop le hoac het hieu luc."
    if "429" in raw or "rate" in raw.lower() or "quota" in raw.lower():
        return f"{label}: vuot quota/rate limit. Thu lai sau hoac chon model/provider khac."
    return f"{label}: {raw}"


def _default_rules() -> list[str]:
    paths: list[str] = []
    for rel_path in DEFAULT_RULES:
        path = APP_DIR / rel_path
        if path.exists():
            paths.append(str(path))
    return paths


def _unique_upload_path(folder: Path, filename: str) -> Path:
    safe_name = Path(filename).name or "upload"
    candidate = folder / safe_name
    if not candidate.exists():
        return candidate
    stem = candidate.stem or "upload"
    suffix = candidate.suffix
    index = 2
    while True:
        next_candidate = folder / f"{stem}_{index}{suffix}"
        if not next_candidate.exists():
            return next_candidate
        index += 1


def _save_uploads(uploaded_files, folder: Path) -> list[str]:
    folder.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    for uploaded in uploaded_files or []:
        path = _unique_upload_path(folder, uploaded.name)
        path.write_bytes(uploaded.getvalue())
        paths.append(str(path))
    return paths


def _prepare_rules(uploaded_rules, tmp: Path, use_default: bool, rule_mode: str) -> list[str]:
    rule_paths: list[str] = []
    if use_default and rule_mode == RULE_APPEND:
        rule_paths.extend(_default_rules())
    uploaded_paths = _save_uploads(uploaded_rules, tmp / "rules")
    if uploaded_paths:
        if rule_mode == RULE_REPLACE:
            rule_paths = []
        rule_paths.extend(uploaded_paths)
    return rule_paths


def _configure_runtime(
    provider: str,
    model: str,
    base_url: str,
    api_key: str,
    timeout_seconds: int,
) -> None:
    os.environ["AI_PROVIDER"] = provider
    os.environ["OFFLINE_MODE"] = "1" if provider == "offline" else "0"
    os.environ["RUN_TIMEOUT_SECONDS"] = str(timeout_seconds)
    os.environ["AI_TIMEOUT_SECONDS"] = str(timeout_seconds)

    if model.strip():
        os.environ["AI_MODEL"] = model.strip()
        os.environ["OPENAI_MODEL"] = model.strip()
    else:
        os.environ.pop("AI_MODEL", None)

    if base_url.strip():
        os.environ["AI_BASE_URL"] = base_url.strip()
    else:
        os.environ.pop("AI_BASE_URL", None)

    if api_key.strip():
        os.environ["AI_API_KEY"] = api_key.strip()
    else:
        os.environ.pop("AI_API_KEY", None)


def _result_label(result_code: str) -> str:
    labels = {
        "DAT": "DAT",
        "CAN_BO_SUNG": "CAN BO SUNG",
        "KHONG_DAT": "KHONG DAT",
        "KHONG_DU_DU_LIEU": "KHONG DU DU LIEU",
    }
    return labels.get(str(result_code), str(result_code or "N/A"))


def _checks_frame(result: dict) -> pd.DataFrame:
    rows = result.get("checks", []) or []
    if not rows:
        return pd.DataFrame()
    preferred = [
        "rule_group",
        "rule_name",
        "result",
        "severity",
        "source_file",
        "source_sheet",
        "source_row",
        "source_cell",
        "source_value",
        "gap",
        "recommendation",
    ]
    df = pd.DataFrame(rows)
    cols = [col for col in preferred if col in df.columns]
    cols.extend([col for col in df.columns if col not in cols])
    return df[cols]


def _feasibility_frame(result: dict) -> pd.DataFrame:
    df = _checks_frame(result)
    if df.empty or "rule_group" not in df.columns:
        return pd.DataFrame()
    return df[df["rule_group"].astype(str) == FEASIBILITY_GROUP].copy()


def _render_feasibility(result: dict) -> None:
    df = _feasibility_frame(result)
    if df.empty:
        st.warning(
            "Chua co du lieu thẩm định tính khả thi. Hay upload file phương án dạng DOCX/PDF/MD/TXT "
            "cùng với phụ lục CSDL, sau đó chạy thẩm định lại."
        )
        return

    rule_names = df["rule_name"].astype(str) if "rule_name" in df.columns else pd.Series("", index=df.index)
    conclusion_mask = rule_names.str.contains("Kết luận sơ bộ", case=False, na=False)
    conclusion = df[conclusion_mask]
    if not conclusion.empty:
        row = conclusion.iloc[0]
        c1, c2, c3 = st.columns(3)
        c1.metric("Ket luan kha thi", _result_label(row.get("result", "N/A")))
        c2.metric("Muc do", row.get("severity", "N/A"))
        c3.metric("So muc can xem", len(df))
        if row.get("evidence"):
            st.info(str(row.get("evidence")))
        if row.get("gap"):
            st.warning(str(row.get("gap")))
        if row.get("recommendation"):
            st.success(str(row.get("recommendation")))

    issue_df = df[~conclusion_mask]
    if issue_df.empty:
        st.success("Không phát hiện thiếu sót rõ ràng trong các nhóm căn cứ khả thi tối thiểu.")
    else:
        st.dataframe(issue_df, use_container_width=True, hide_index=True)


def _run_review(
    input_files,
    uploaded_rules,
    use_default_rules: bool,
    rule_mode: str,
    provider: str,
    model: str,
    base_url: str,
    api_key: str,
    fast_mode: bool,
    timeout_seconds: int,
) -> dict:
    started = time.perf_counter()
    _configure_runtime(provider, model, base_url, api_key, timeout_seconds)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        input_paths = _save_uploads(input_files, tmp / "input")
        rule_paths = _prepare_rules(uploaded_rules, tmp, use_default_rules, rule_mode)

        if not input_paths:
            raise ValueError("Can import it nhat 1 file can tham dinh.")
        if not rule_paths:
            raise ValueError("Can chon rule mac dinh hoac upload it nhat 1 file rule.")

        progress = st.progress(5, text="Dang doc file dau vao...")
        progress.progress(20, text="Dang chay rule engine...")
        deterministic_result = analyze_structured_files(input_paths)

        ai_result = None
        ai_error = ""
        if provider != "offline":
            markdown_parts: list[str] = []
            for index, path in enumerate(input_paths, 1):
                progress.progress(
                    25 + int(index / max(len(input_paths), 1) * 25),
                    text=f"Dang chuyen Markdown: {Path(path).name}",
                )
                markdown_parts.append(
                    f"# FILE: {Path(path).name}\n" + file_to_markdown(path, fast=fast_mode)
                )

            progress.progress(58, text="Dang nap rule...")
            rules_markdown = load_rules(rule_paths)
            joined_markdown = "\n\n---\n\n".join(markdown_parts)
            progress.progress(
                70,
                text=f"Dang goi AI ({PROVIDER_LABELS.get(provider, provider)})...",
            )
            try:
                ai_result = analyze_with_gpt(
                    joined_markdown,
                    rules_markdown,
                    deterministic_result,
                    model=model,
                    provider=provider,
                )
                if ai_result is None:
                    ai_error = _missing_ai_config_message(provider)
            except Exception as exc:
                ai_error = _friendly_ai_error(provider, exc)
        else:
            progress.progress(65, text="Offline mode: bo qua AI va Markdown preview...")

        progress.progress(82, text="Dang tong hop ket qua...")
        result = merge_results(deterministic_result, ai_result)
        if not result.get("report_markdown"):
            result["report_markdown"] = build_markdown_report(result)

        progress.progress(92, text="Dang xuat bao cao...")
        exports = export_report(result, str(OUTPUT_DIR), "bao_cao_tham_dinh_pctt_bts")
        session_path = save_session(
            result,
            [Path(path).name for path in input_paths],
            [Path(path).name for path in rule_paths],
        )
        progress.progress(100, text="Hoan thanh")

    return {
        "result": result,
        "exports": exports,
        "session": str(session_path),
        "elapsed": round(time.perf_counter() - started, 1),
        "provider": provider,
        "ai_error": ai_error,
    }


def _preview_rule_catalog(uploaded_rules, use_default_rules: bool, rule_mode: str) -> pd.DataFrame:
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        rule_paths = _prepare_rules(uploaded_rules, tmp, use_default_rules, rule_mode)
        if not rule_paths:
            return pd.DataFrame()
        return parse_rule_catalog(rule_paths)


def _export_mime(kind: str) -> str:
    return {
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "markdown": "text/markdown",
        "json": "application/json",
    }.get(kind, "application/octet-stream")


def _existing_exports(exports: dict[str, str]) -> list[tuple[str, Path]]:
    files: list[tuple[str, Path]] = []
    for kind, path in exports.items():
        file_path = Path(path)
        if file_path.exists():
            files.append((kind, file_path))
    return files


def _exports_zip_bytes(exports: dict[str, str]) -> bytes:
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for _, file_path in _existing_exports(exports):
            archive.write(file_path, arcname=file_path.name)
    buffer.seek(0)
    return buffer.getvalue()


def _zip_file_name(exports: dict[str, str]) -> str:
    files = _existing_exports(exports)
    if not files:
        return "ket_qua_tham_dinh.zip"
    return files[0][1].with_suffix(".zip").name


def _render_downloads(exports: dict[str, str], key_prefix: str = "downloads") -> None:
    if not exports:
        st.info("Chua co file bao cao. Hay chay tham dinh truoc.")
        return

    files = _existing_exports(exports)
    if not files:
        st.warning("Khong tim thay file ket qua da xuat. Hay chay tham dinh lai.")
        return

    labels = {
        "docx": "Bao cao Word",
        "xlsx": "Bang Excel",
        "markdown": "Markdown",
        "json": "JSON",
    }

    zip_col, note_col = st.columns([1, 2])
    with zip_col:
        st.download_button(
            "Tai tat ca ket qua (.zip)",
            data=_exports_zip_bytes(exports),
            file_name=_zip_file_name(exports),
            mime="application/zip",
            type="primary",
            use_container_width=True,
            key=f"{key_prefix}_zip",
        )
    with note_col:
        st.caption("File ZIP gom day du bao cao Word, bang Excel, Markdown va JSON cua phien tham dinh vua chay.")

    columns = st.columns(4)
    for idx, (kind, file_path) in enumerate(files):
        with columns[idx % 4]:
            st.download_button(
                labels.get(kind, kind.upper()),
                data=file_path.read_bytes(),
                file_name=file_path.name,
                mime=_export_mime(kind),
                use_container_width=True,
                key=f"{key_prefix}_{kind}",
            )


def _render_history() -> None:
    sessions = list_sessions()[:12]
    if not sessions:
        st.caption("Chua co phien nao.")
        return
    for path in sessions:
        st.write(path.name)


def _inject_css() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background: #f5f7fb;
        }
        div[data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid #d9e2ec;
        }
        h1, h2, h3 {
            letter-spacing: 0;
        }
        .pctt-title {
            padding: 18px 0 8px 0;
            border-bottom: 1px solid #d9e2ec;
            margin-bottom: 18px;
        }
        .pctt-title h1 {
            font-size: 1.9rem;
            line-height: 1.2;
            margin: 0;
            color: #102a43;
        }
        .pctt-title p {
            color: #52616b;
            margin: 8px 0 0 0;
        }
        div[data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid #d9e2ec;
            border-radius: 8px;
            padding: 14px 16px;
        }
        .stButton > button,
        .stDownloadButton > button {
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="PCTT_APP_REVIEW Web",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    _inject_css()

    if "last_run" not in st.session_state:
        st.session_state.last_run = None

    default_provider = _default_provider()

    with st.sidebar:
        st.header("Cau hinh")
        provider = st.selectbox(
            "AI Provider",
            options=[key for key, _ in PROVIDER_OPTIONS],
            index=[key for key, _ in PROVIDER_OPTIONS].index(default_provider),
            format_func=lambda key: PROVIDER_LABELS.get(key, key),
        )
        model = st.text_input(
            "Model",
            value=_default_model(provider),
            key=f"model_{provider}",
        )
        base_url = st.text_input(
            "Base URL local/API",
            value=_default_base_url(provider),
            key=f"base_url_{provider}",
        )
        api_key = st.text_input(
            "API key tuy chon",
            value="",
            type="password",
            key=f"api_key_{provider}",
        )
        timeout_seconds = st.number_input(
            "Tu dung AI sau (giay)",
            min_value=30,
            max_value=3600,
            value=_env_int("RUN_TIMEOUT_SECONDS", 300),
            step=30,
        )
        fast_mode = st.toggle(
            "Fast mode - chi preview du lieu lon",
            value=_env_bool("FAST_MODE", "1"),
        )

        st.divider()
        use_default_rules = st.checkbox("Dung 2 rule mac dinh", value=True)
        rule_mode = st.radio(
            "Che do rule upload",
            options=[RULE_APPEND, RULE_REPLACE],
            format_func=lambda value: {
                RULE_APPEND: "Bo sung vao rule mac dinh",
                RULE_REPLACE: "Thay the bang rule upload",
            }[value],
        )

    st.markdown(
        """
        <div class="pctt-title">
            <h1>PCTT_APP_REVIEW Web</h1>
            <p>Tham dinh phuong an PCTT/UCTT tram BTS bang rule engine local va AI tuy chon.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    upload_col, rule_col = st.columns([1.3, 1])
    with upload_col:
        input_files = st.file_uploader(
            "File can tham dinh",
            type=SUPPORTED_TYPES,
            accept_multiple_files=True,
        )
    with rule_col:
        uploaded_rules = st.file_uploader(
            "File rule bo sung/thay the",
            type=SUPPORTED_TYPES,
            accept_multiple_files=True,
        )

    action_col, preview_col, hint_col = st.columns([1, 1, 2])
    run_button = action_col.button(
        "Chay tham dinh",
        type="primary",
        use_container_width=True,
    )
    preview_button = preview_col.button(
        "Xem catalog rule",
        use_container_width=True,
    )
    with hint_col:
        if provider == "offline":
            st.caption("Offline Rule Engine khong gui du lieu ra AI.")
        elif provider in {"ollama", "lmstudio"}:
            st.caption("Hay dam bao server local dang chay truoc khi bam tham dinh.")
        else:
            st.caption("Neu de trong API key, app se dung bien trong file .env neu co.")

    if preview_button:
        try:
            catalog = _preview_rule_catalog(uploaded_rules, use_default_rules, rule_mode)
            if catalog.empty:
                st.warning("Chua co rule de xem.")
            else:
                st.dataframe(catalog, use_container_width=True, hide_index=True)
        except Exception as exc:
            st.error(f"Khong doc duoc catalog rule: {exc}")

    if run_button:
        try:
            with st.spinner("Dang tham dinh..."):
                st.session_state.last_run = _run_review(
                    input_files=input_files,
                    uploaded_rules=uploaded_rules,
                    use_default_rules=use_default_rules,
                    rule_mode=rule_mode,
                    provider=provider,
                    model=model,
                    base_url=base_url,
                    api_key=api_key,
                    fast_mode=fast_mode,
                    timeout_seconds=int(timeout_seconds),
                )
            st.success("Hoan thanh tham dinh va xuat bao cao.")
        except Exception as exc:
            st.error(str(exc))

    last_run = st.session_state.last_run
    if not last_run:
        st.info("Import file can tham dinh, kiem tra rule, sau do bam Chay tham dinh.")
        with st.expander("Lich su phien gan day"):
            _render_history()
        return

    result = last_run["result"]
    summary = result.get("summary", {})
    checks = result.get("checks", []) or []

    if last_run.get("ai_error"):
        st.warning(
            "AI provider chua chay duoc nen bao cao da duoc tao bang rule engine local. "
            + last_run["ai_error"]
        )

    metric_cols = st.columns(4)
    metric_cols[0].metric("Diem tong", summary.get("overall_score", "N/A"))
    metric_cols[1].metric("Ket luan", _result_label(summary.get("overall_result", "N/A")))
    metric_cols[2].metric("So phat hien", len(checks))
    metric_cols[3].metric("Thoi gian", f"{last_run.get('elapsed', 0)}s")

    st.subheader("Tham dinh tinh kha thi")
    _render_feasibility(result)

    st.subheader("Download ket qua tham dinh")
    _render_downloads(last_run.get("exports", {}), key_prefix="quick_downloads")

    feasibility_tab, report_tab, table_tab, json_tab, download_tab, history_tab = st.tabs(
        ["Tinh kha thi", "Bao cao", "Bang chi tiet", "JSON", "Tai bao cao", "Lich su"]
    )
    with feasibility_tab:
        _render_feasibility(result)
    with report_tab:
        st.markdown(result.get("report_markdown", ""))
    with table_tab:
        df = _checks_frame(result)
        if df.empty:
            st.info("Khong co phat hien chi tiet.")
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)
    with json_tab:
        st.code(json.dumps(result, ensure_ascii=False, indent=2), language="json")
    with download_tab:
        _render_downloads(last_run.get("exports", {}), key_prefix="tab_downloads")
        st.caption(f"Da luu phien: {last_run.get('session', '')}")
    with history_tab:
        _render_history()


if __name__ == "__main__":
    main()
