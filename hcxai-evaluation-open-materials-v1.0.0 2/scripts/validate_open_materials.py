#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED = {
    "data/hcxai_extraction.tsv": 15,
    "data/in_scope_hcxai_eval.tsv": 107,
    "data/theme_map_hcxai_eval.tsv": 277,
    "data/llm_xai_contextual_catalog.tsv": 477,
    "data/llm_xai_T2_evaluation.tsv": 422,
    "data/llm_xai_T3_risks.tsv": 422,
}

REQUIRED_COLUMNS = {
    "data/in_scope_hcxai_eval.tsv": {
        "paper_id",
        "doi",
        "year",
        "title",
        "venue",
        "domain",
        "metrics_trust",
        "metrics_reliance",
        "metrics_understanding",
        "metrics_performance",
    },
    "data/theme_map_hcxai_eval.tsv": {"theme", "doi", "bibkey"},
    "data/llm_xai_T2_evaluation.tsv": {"paper_id", "year", "title", "C_tags"},
    "data/llm_xai_T3_risks.tsv": {"paper_id", "year", "title", "E_tags"},
}

RISKY_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}"),
    "local_pdf_path": re.compile(r"(papers_openalex|pdftxt|\\.pdf\\b)", re.IGNORECASE),
    "review_correspondence": re.compile(r"\\b(referee|reviewer|editor-in-chief|manuscript central)\\b", re.IGNORECASE),
}


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return reader.fieldnames or [], list(reader)


def main() -> int:
    failures: list[str] = []

    for rel, expected_rows in EXPECTED.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing file: {rel}")
            continue

        fields, rows = read_tsv(path)
        if len(rows) != expected_rows:
            failures.append(f"{rel}: expected {expected_rows} rows, found {len(rows)}")

        missing = REQUIRED_COLUMNS.get(rel, set()) - set(fields)
        if missing:
            failures.append(f"{rel}: missing required columns {sorted(missing)}")

        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in RISKY_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"{rel}: risky pattern detected ({label})")

    if failures:
        print("Validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Validation passed.")
    for rel, expected_rows in EXPECTED.items():
        print(f"- {rel}: {expected_rows} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
