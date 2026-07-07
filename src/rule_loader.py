from __future__ import annotations

import os
import re
import unicodedata
from pathlib import Path

import pandas as pd

from .file_reader import file_to_markdown
from .utils import normalize_text

DEFAULT_RULES = ["rules/rule_csdl.xlsx", "rules/rule_phuongan.xlsx"]
MAX_RULE_TEXT_CHARS = int(os.getenv("MAX_RULE_TEXT_CHARS", "1200"))
MAX_RULE_MARKDOWN_CHARS = int(os.getenv("MAX_RULE_MARKDOWN_CHARS", "300000"))


def load_rules(rule_files: list[str]) -> str:
    blocks = []
    for path in rule_files:
        blocks.append(
            f"# RULE FILE: {Path(path).name}\n"
            + file_to_markdown(path, max_chars=MAX_RULE_MARKDOWN_CHARS, fast=False)
        )
    return "\n\n---\n\n".join(blocks)


def _fold_text(value) -> str:
    s = normalize_text(value).lower()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", s).strip()


def _clean_values(values) -> list[str]:
    return [normalize_text(x) for x in values if normalize_text(x)]


def _looks_like_header(values: list[str]) -> bool:
    folded = " ".join(_fold_text(x) for x in values[:6])
    header_tokens = {"stt", "tt", "noi dung", "rule", "yeu cau", "tieu chi", "cot du lieu"}
    return sum(token in folded for token in header_tokens) >= 2


def _looks_like_group(values: list[str]) -> bool:
    if not values:
        return False
    first = values[0].strip().upper().strip(".")
    if first in {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"}:
        return True
    folded = _fold_text(" ".join(values[:2]))
    return folded.startswith(("chuong ", "muc ", "phan ", "nhom "))


def _rule_name(values: list[str]) -> str:
    for value in values:
        folded = _fold_text(value)
        if len(folded) >= 6 and folded not in {"stt", "tt"}:
            return value[:180]
    return "Muc rule"


def _rule_text(values: list[str]) -> str:
    return " | ".join(values)[:MAX_RULE_TEXT_CHARS]


def _read_rule_document(path: Path) -> list[dict]:
    try:
        markdown = file_to_markdown(str(path), max_chars=MAX_RULE_MARKDOWN_CHARS, fast=False)
    except Exception:
        markdown = ""
    blocks = [
        normalize_text(x)
        for x in re.split(r"\n\s*\n|\n(?=#{1,6}\s)", markdown)
        if len(_fold_text(x)) >= 20
    ]
    rows = []
    for idx, block in enumerate(blocks, 1):
        rows.append(
            {
                "file": path.name,
                "sheet": "",
                "row_no": idx,
                "group": "Rule document",
                "rule_no": str(idx),
                "rule_name": block[:180],
                "data_column": "",
                "definition": block[:MAX_RULE_TEXT_CHARS],
                "evidence_required": "",
                "rule_text": block[:MAX_RULE_TEXT_CHARS],
            }
        )
    return rows


def extract_rule_requirements(rule_files: list[str]) -> list[dict]:
    rows: list[dict] = []
    for path in rule_files:
        p = Path(path)
        suffix = p.suffix.lower()
        if suffix not in {".xlsx", ".xls", ".csv"}:
            rows.extend(_read_rule_document(p))
            continue

        try:
            if suffix == ".csv":
                sheets = {"CSV": pd.read_csv(p, dtype=str, header=None)}
            else:
                sheets = pd.read_excel(p, sheet_name=None, dtype=str, header=None)
        except Exception:
            rows.extend(_read_rule_document(p))
            continue

        for sheet, raw in sheets.items():
            raw = raw.fillna("")
            current_group = ""
            for row_index, record in raw.iterrows():
                values = _clean_values(record.tolist())
                if not values or _looks_like_header(values):
                    continue
                if _looks_like_group(values):
                    current_group = " ".join(values[:3])[:240]
                    continue

                first, second, third, fourth = (values + ["", "", "", ""])[:4]
                rows.append(
                    {
                        "file": p.name,
                        "sheet": sheet,
                        "row_no": int(row_index) + 1,
                        "group": current_group,
                        "rule_no": first,
                        "rule_name": _rule_name(values[1:] or values),
                        "data_column": third,
                        "definition": fourth or third or second or first,
                        "evidence_required": fourth,
                        "rule_text": _rule_text(values),
                    }
                )
    return rows


def parse_rule_catalog(rule_files: list[str]) -> pd.DataFrame:
    return pd.DataFrame(extract_rule_requirements(rule_files))
