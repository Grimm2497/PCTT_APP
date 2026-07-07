from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import re
import unicodedata
import pandas as pd
from rapidfuzz import process, fuzz
from .file_reader import file_to_markdown
from .utils import normalize_text, truthy, to_float

@dataclass
class CheckItem:
    rule_group: str
    rule_name: str
    result: str
    severity: str
    evidence: str
    gap: str
    recommendation: str
    source_file: str = ""
    source_sheet: str = ""
    source_row: str = ""
    source_column: str = ""
    source_cell: str = ""
    source_value: str = ""
    abnormal_type: str = ""
    rule_source: str = ""

CANONICAL_ALIASES = {
    "site_code": ["ma tram", "mã trạm", "site", "site code", "ma site", "trạm", "ten tram", "tên trạm"],
    "priority": ["ut", "ưu tiên", "uu tien", "priority", "loai tram", "loại trạm"],
    "staff": ["em quan", "ém quân", "nhan su", "nhân sự", "ds em quan", "nguoi truc", "người trực"],
    "flood": ["ngap", "ngập", "nguy co ngap", "nguy cơ ngập", "lụt", "lut"],
    "cutoff": ["chia cat", "chia cắt", "co lap", "cô lập", "kho tiep can", "khó tiếp cận"],
    "ats": ["ats"],
    "generator_plan": ["pa cmn", "phuong an chay may no", "phương án chạy máy nổ", "mpd", "mpđ", "may no", "máy nổ"],
    "battery_hours": ["tgx", "thoi gian xa", "thời gian xả", "acquy", "ắc quy", "battery"],
    "distance_km": ["khoang cach", "khoảng cách", "km", "cự ly", "cu ly"],
    "access_time": ["thoi gian tiep can", "thời gian tiếp cận", "tiep can", "tiếp cận"],
}

PLAN_SUFFIXES = {".docx", ".pdf", ".md", ".txt"}

FEASIBILITY_RULES = [
    {
        "name": "Kịch bản thiên tai/rủi ro phải cụ thể",
        "severity": "HIGH",
        "aliases": ["bao", "mua lon", "ngap", "lut", "sat lo", "chia cat", "co lap", "mat dien", "thien tai"],
        "gap": "Chưa thấy mô tả rõ kịch bản thiên tai/rủi ro làm căn cứ cho phương án.",
        "recommendation": "Bổ sung kịch bản theo từng nguy cơ: bão/mưa lớn/ngập/chia cắt/mất điện và phạm vi ảnh hưởng.",
    },
    {
        "name": "Danh sách trạm/địa bàn ảnh hưởng phải đủ căn cứ",
        "severity": "MEDIUM",
        "aliases": ["ma tram", "site", "danh sach tram", "phu luc", "dia ban", "vi tri", "dia chi"],
        "gap": "Chưa thấy căn cứ danh sách trạm/địa bàn bị ảnh hưởng.",
        "recommendation": "Bổ sung phụ lục danh sách trạm, địa chỉ/vị trí, mức ưu tiên và nguy cơ chính của từng trạm.",
    },
    {
        "name": "Nhân sự ứng cứu/ém quân phải có đầu mối và liên hệ",
        "severity": "HIGH",
        "aliases": ["nhan su", "em quan", "doi ung cuu", "truc", "so dien thoai", "sdt", "lien he", "dau moi"],
        "gap": "Chưa thấy đủ thông tin nhân sự, đầu mối trực/ứng cứu hoặc số liên hệ.",
        "recommendation": "Bổ sung họ tên, SĐT, vị trí ém quân, ca trực và đầu mối chỉ huy/điều phối.",
    },
    {
        "name": "Nguồn điện dự phòng phải nêu rõ MPĐ/ắc quy/nhiên liệu",
        "severity": "HIGH",
        "aliases": ["may phat", "may no", "mpd", "mpđ", "ac quy", "acquy", "tgx", "nhien lieu", "dau", "xang"],
        "gap": "Chưa thấy phương án nguồn điện dự phòng đủ rõ.",
        "recommendation": "Bổ sung MPĐ/máy nổ, TGX ắc quy, nhiên liệu, vị trí đặt máy và phương án vận chuyển/cấp dầu.",
    },
    {
        "name": "Phương án tiếp cận phải nêu tuyến/ thời gian/ phương tiện",
        "severity": "MEDIUM",
        "aliases": ["tiep can", "khoang cach", "thoi gian", "phuong tien", "tuyen duong", "di chuyen", "chia cat"],
        "gap": "Chưa thấy phương án tiếp cận hiện trường đủ cụ thể.",
        "recommendation": "Bổ sung tuyến tiếp cận, khoảng cách, thời gian dự kiến, phương tiện và phương án thay thế khi chia cắt.",
    },
    {
        "name": "Phân công thực hiện phải rõ người/việc/thời điểm",
        "severity": "MEDIUM",
        "aliases": ["phan cong", "nhiem vu", "dau moi", "lich truc", "ca truc", "thoi gian thuc hien", "tien do"],
        "gap": "Chưa thấy phân công nhiệm vụ và mốc thời gian thực hiện rõ ràng.",
        "recommendation": "Bổ sung bảng phân công người phụ trách, nhiệm vụ, thời điểm kích hoạt và cơ chế báo cáo.",
    },
    {
        "name": "Thông tin liên lạc/ứng cứu thông tin phải có phương án dự phòng",
        "severity": "MEDIUM",
        "aliases": ["lien lac", "thong tin", "ung cuu thong tin", "kenh lien lac", "truyen dan", "mat song", "mat lien lac"],
        "gap": "Chưa thấy phương án duy trì liên lạc hoặc ứng cứu thông tin khi sự cố.",
        "recommendation": "Bổ sung kênh liên lạc chính/phụ, đầu mối NOC/ứng cứu, phương án truyền dẫn hoặc liên lạc thay thế.",
    },
]

def _norm_col(c: str) -> str:
    return normalize_text(c).lower()

def _fold_text(value) -> str:
    s = normalize_text(value).lower()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", s)

def _find_alias(text: str, aliases: list[str]) -> str:
    folded = _fold_text(text)
    for alias in aliases:
        if _fold_text(alias) in folded:
            return alias
    return ""

def _snippet(text: str, alias: str, radius: int = 90) -> str:
    if not alias:
        return ""
    folded = _fold_text(text)
    folded_alias = _fold_text(alias)
    index = folded.find(folded_alias)
    if index < 0:
        return ""
    start = max(0, index - radius)
    end = min(len(text), index + len(alias) + radius)
    return normalize_text(text[start:end])

def _excel_col_name(n: int) -> str:
    # n is 1-based
    out = ""
    while n:
        n, r = divmod(n - 1, 26)
        out = chr(65 + r) + out
    return out

def _cell_ref(df: pd.DataFrame, row_index: int, col_name: str | None) -> tuple[str, str, str]:
    if not col_name or col_name not in df.columns:
        return "", "", ""
    col_pos = list(df.columns).index(col_name) + 1
    excel_row = row_index + 2
    col_letter = _excel_col_name(col_pos)
    val = df.iloc[row_index, col_pos - 1]
    return col_letter, f"{col_letter}{excel_row}", "" if pd.isna(val) else str(val)

def _make_check(rule_group, rule_name, result, severity, evidence, gap, recommendation, fname, sheet, rowno='', df=None, row_index=None, col_name=None, abnormal_type='', rule_source='Rule engine CSDL'):
    source_column = source_cell = source_value = ""
    if df is not None and row_index is not None and col_name:
        source_column, source_cell, source_value = _cell_ref(df, int(row_index), col_name)
    return CheckItem(rule_group, rule_name, result, severity, evidence, gap, recommendation, fname, sheet, str(rowno), source_column, source_cell, source_value, abnormal_type, rule_source)

def infer_columns(df: pd.DataFrame) -> dict[str, str]:
    cols = list(map(str, df.columns))
    norm_map = {_norm_col(c): c for c in cols}
    result = {}
    for key, aliases in CANONICAL_ALIASES.items():
        candidates = []
        for nc, orig in norm_map.items():
            score = max(fuzz.partial_ratio(nc, a) for a in aliases)
            if score >= 78:
                candidates.append((orig, score))
        if candidates:
            result[key] = sorted(candidates, key=lambda x: x[1], reverse=True)[0][0]
    # Excel column-letter fallback after pandas preserves unnamed or actual headers poorly
    for letter_key, idx in {"staff":20, "cutoff":24, "flood":25, "ats":44, "battery_hours":41}.items():
        if letter_key not in result and len(cols) > idx:
            result[letter_key] = cols[idx]
    return result

def _iter_excel(path: str):
    sheets = pd.read_excel(path, sheet_name=None, dtype=str)
    for sheet, df in sheets.items():
        if len(df) == 0:
            continue
        yield sheet, df.fillna("")

def analyze_structured_files(paths: list[str]) -> dict:
    checks: list[CheckItem] = []
    for path in paths:
        p = Path(path)
        suffix = p.suffix.lower()
        if suffix in PLAN_SUFFIXES:
            checks.extend(_check_plan_document(str(p)))
            continue
        if suffix not in [".xlsx", ".xls", ".csv"]:
            continue
        if suffix == ".csv":
            sheets = [("CSV", pd.read_csv(p, dtype=str).fillna(""))]
        else:
            sheets = list(_iter_excel(str(p)))
        for sheet, df in sheets:
            cols = infer_columns(df)
            if not cols:
                checks.append(_make_check("CSDL BTS", "Nhận diện cột dữ liệu", "KHONG_DU_DU_LIEU", "MEDIUM", f"{p.name}/{sheet}: không nhận diện được cột chuẩn", "Thiếu header hoặc header không rõ", "Chuẩn hóa header hoặc mapping cột trong file CSDL", p.name, sheet, "", abnormal_type="Thiếu mapping/header"))
                continue
            checks.extend(_check_sheet(p.name, sheet, df, cols))
    score = _score(checks)
    return {
        "summary": {"deterministic_score": score, "deterministic_checks": len(checks), "deterministic_failed": sum(c.result in ["KHONG_DAT", "CAN_BO_SUNG", "KHONG_DU_DU_LIEU"] for c in checks)},
        "checks": [asdict(c) for c in checks]
    }

def _check_plan_document(path: str) -> list[CheckItem]:
    p = Path(path)
    try:
        text = file_to_markdown(path, fast=True)
    except Exception as exc:
        return [_make_check("Tính khả thi phương án", "Đọc nội dung phương án", "KHONG_DU_DU_LIEU", "HIGH", f"{p.name}: {exc}", "Không đọc được nội dung file phương án", "Kiểm tra định dạng file hoặc chuyển sang DOCX/PDF có text layer", p.name, "", abnormal_type="Không đọc được file", rule_source="Rule engine phương án")]

    folded = _fold_text(text)
    if len(folded.strip()) < 200:
        return [_make_check("Tính khả thi phương án", "Nội dung phương án đủ để thẩm định", "KHONG_DU_DU_LIEU", "HIGH", f"{p.name}: nội dung đọc được quá ngắn ({len(folded)} ký tự)", "Không đủ dữ liệu để đánh giá tính khả thi", "Upload đầy đủ file thuyết minh/phụ lục hoặc PDF có text layer", p.name, "", abnormal_type="Thiếu nội dung", rule_source="Rule engine phương án")]

    out: list[CheckItem] = []
    missing_names: list[str] = []
    found_count = 0
    for rule in FEASIBILITY_RULES:
        alias = _find_alias(text, rule["aliases"])
        if alias:
            found_count += 1
            continue
        missing_names.append(rule["name"])
        out.append(_make_check(
            "Tính khả thi phương án",
            rule["name"],
            "CAN_BO_SUNG",
            rule["severity"],
            f"{p.name}: chưa tìm thấy nhóm từ khóa/căn cứ: {', '.join(rule['aliases'][:5])}",
            rule["gap"],
            rule["recommendation"],
            p.name,
            "",
            abnormal_type="Thiếu căn cứ khả thi",
            rule_source="Rule engine phương án",
        ))

    numeric_evidence = re.findall(r"\b\d+(?:[,.]\d+)?\s*(?:gio|h|km|lit|l|nguoi|tram|may|ca)\b", folded)
    if len(numeric_evidence) < 3:
        missing_names.append("Căn cứ định lượng nguồn lực/thời gian/khoảng cách")
        out.append(_make_check(
            "Tính khả thi phương án",
            "Căn cứ định lượng phải đủ để kiểm chứng khả thi",
            "CAN_BO_SUNG",
            "MEDIUM",
            f"{p.name}: chỉ tìm thấy {len(numeric_evidence)} căn cứ định lượng rõ ràng",
            "Thiếu số liệu định lượng để kiểm chứng nguồn lực, thời gian tiếp cận, khoảng cách hoặc nhiên liệu.",
            "Bổ sung số lượng nhân sự/MPĐ, TGX, khoảng cách, thời gian tiếp cận, nhiên liệu và danh sách trạm liên quan.",
            p.name,
            "",
            abnormal_type="Thiếu căn cứ định lượng",
            rule_source="Rule engine phương án",
        ))

    if len(missing_names) >= 4:
        result, severity = "KHONG_DAT", "HIGH"
        gap = "Phương án thiếu nhiều nhóm căn cứ tối thiểu nên chưa đủ cơ sở kết luận khả thi."
    elif missing_names:
        result, severity = "CAN_BO_SUNG", "MEDIUM"
        gap = "Phương án có nội dung nhưng cần bổ sung căn cứ trước khi kết luận khả thi."
    else:
        result, severity = "DAT", "LOW"
        gap = ""

    out.insert(0, _make_check(
        "Tính khả thi phương án",
        "Kết luận sơ bộ tính khả thi phương án",
        result,
        severity,
        f"{p.name}: nhận diện {found_count}/{len(FEASIBILITY_RULES)} nhóm nội dung khả thi; thiếu: {', '.join(missing_names) if missing_names else 'không'}",
        gap,
        "Bổ sung các nhóm còn thiếu và đối chiếu với phụ lục CSDL trạm trước khi phê duyệt." if missing_names else "Có thể tiếp tục đối chiếu chéo với phụ lục CSDL và kết quả AI nếu cấu hình provider online.",
        p.name,
        "",
        abnormal_type="Đánh giá khả thi tổng hợp",
        rule_source="Rule engine phương án",
    ))
    return out

def _row_id(row, cols):
    c = cols.get("site_code")
    return normalize_text(row.get(c, "")) if c else ""

def _check_sheet(fname, sheet, df, cols) -> list[CheckItem]:
    out: list[CheckItem] = []
    required = ["site_code", "priority", "staff", "flood", "cutoff", "ats", "generator_plan", "battery_hours"]
    missing = [x for x in required if x not in cols]
    if missing:
        out.append(_make_check("CSDL BTS", "Đủ trường dữ liệu tối thiểu", "CAN_BO_SUNG", "MEDIUM", f"Nhận diện được: {cols}", f"Thiếu/không nhận diện: {', '.join(missing)}", "Bổ sung mapping cột hoặc đổi header theo mẫu rule", fname, sheet, "", abnormal_type="Thiếu trường dữ liệu"))
    for i, row in df.iterrows():
        site = _row_id(row, cols) or f"row {i+2}"
        rowno = str(i + 2)
        priority = normalize_text(row.get(cols.get("priority", ""), "")).upper()
        staff = row.get(cols.get("staff", ""), "")
        flood = row.get(cols.get("flood", ""), "")
        cutoff = row.get(cols.get("cutoff", ""), "")
        ats = row.get(cols.get("ats", ""), "")
        plan = normalize_text(row.get(cols.get("generator_plan", ""), ""))
        batt = to_float(row.get(cols.get("battery_hours", ""), ""), None)
        dist = to_float(row.get(cols.get("distance_km", ""), ""), None)
        access = to_float(row.get(cols.get("access_time", ""), ""), None)
        if ("UT1" in priority) and not truthy(staff):
            out.append(_make_check("CSDL BTS", "100% trạm UT1/UT1_3321 phải có nhân sự ém quân", "KHONG_DAT", "HIGH", f"{site}: priority={priority}, nhân sự ém quân trống", "Thiếu nhân sự ém quân", "Bổ sung họ tên, SĐT, vị trí ém quân và ca trực", fname, sheet, rowno, df, i, cols.get("staff"), "Ô trống/bất thường"))
        if (truthy(flood) or truthy(cutoff)) and not truthy(staff):
            out.append(_make_check("CSDL BTS", "Trạm ngập/chia cắt phải có phương án ém quân", "KHONG_DAT", "CRITICAL", f"{site}: ngập={flood}, chia cắt={cutoff}, nhân sự trống", "Không có lực lượng tại chỗ khi thiên tai", "Bố trí ém quân hoặc nêu rõ PA tiếp cận thay thế có MPĐ dầu + ATS", fname, sheet, rowno, df, i, cols.get("staff"), "Thiếu PA ém quân"))
        if truthy(ats) and plan in {"3", "4", "5", "6"}:
            out.append(_make_check("CSDL BTS", "Logic ATS với phương án chạy máy nổ", "CAN_BO_SUNG", "MEDIUM", f"{site}: ATS={ats}, PA CMN={plan}", "Trạm có ATS nhưng PA CMN thuộc nhóm chạy lưu động/tòa nhà/BKK", "Rà soát lại PA đặt máy nổ; nếu vẫn chọn 3-6 cần ghi rõ căn cứ", fname, sheet, rowno, df, i, cols.get("generator_plan"), "Sai logic ATS/MPĐ"))
        if batt is not None and batt == 0:
            out.append(_make_check("CSDL BTS", "Thời gian xả ắc quy không được bất thường bằng 0", "CAN_BO_SUNG", "MEDIUM", f"{site}: TGX={batt}", "TGX = 0 có khả năng thiếu hoặc sai dữ liệu", "Kiểm tra lại PMCĐ/IMES và cập nhật TGX sau lắp đặt ắc quy", fname, sheet, rowno, df, i, cols.get("battery_hours"), "Giá trị bằng 0"))
        if batt is not None and batt < 2 and ((dist is not None and dist > 30) or (access is not None and access > batt)):
            out.append(_make_check("CSDL BTS", "TGX phải tương quan với thời gian/khoảng cách tiếp cận MPĐ", "KHONG_DAT", "HIGH", f"{site}: TGX={batt}h, khoảng cách={dist}, thời gian tiếp cận={access}", "TGX thấp trong khi tiếp cận xa/khó", "Đổi điểm ém quân, tăng nguồn dự phòng hoặc bố trí MPĐ/nhân sự gần trạm", fname, sheet, rowno, df, i, cols.get("battery_hours"), "Tương quan TGX/tiếp cận bất thường"))
    if not out:
        out.append(_make_check("CSDL BTS", "Rule engine CSDL", "DAT", "LOW", f"{fname}/{sheet}: không phát hiện lỗi cứng trên {len(df)} dòng", "", "Duy trì rà soát bằng AI đối với nội dung thuyết minh và phụ lục", fname, sheet, "", abnormal_type="Không phát hiện"))
    return out

def _score(checks: list[CheckItem]) -> int:
    score = 100
    penalty = {"CRITICAL": 18, "HIGH": 10, "MEDIUM": 5, "LOW": 2}
    for c in checks:
        if c.result == "KHONG_DAT":
            score -= penalty.get(c.severity, 5)
        elif c.result in ["CAN_BO_SUNG", "KHONG_DU_DU_LIEU"]:
            score -= max(2, penalty.get(c.severity, 4)//2)
    return max(0, min(100, score))
