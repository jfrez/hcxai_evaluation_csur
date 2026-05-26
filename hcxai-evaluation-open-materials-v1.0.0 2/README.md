# Open Materials for Human-Centered XAI Evaluation Survey

This repository contains the open materials for:

> Evaluating Explainable AI with Humans: Trust, Reliance, Understanding, and Performance: A Structured Survey and Reporting Guidelines

The materials support the revised ACM Computing Surveys manuscript by making the DOI-identified corpus, extraction sheet, theme mapping, and LLM-era contextual catalog inspectable.

## Contents

| Path | Rows | Description |
| --- | ---: | --- |
| `data/in_scope_hcxai_eval.tsv` | 107 | DOI-identified corpus used in the manuscript synthesis. |
| `data/hcxai_extraction.tsv` | 15 | Project extraction sheet for construct and study-design fields. |
| `data/theme_map_hcxai_eval.tsv` | 277 | Non-exclusive theme-to-paper mapping used for synthesis counts. |
| `data/llm_xai_contextual_catalog.tsv` | 477 | Sanitized LLM-era contextual catalog used to support the generated/dialogic explanation discussion. |
| `data/llm_xai_T2_evaluation.tsv` | 422 | LLM-XAI evaluation taxonomy staging tags. |
| `data/llm_xai_T3_risks.tsv` | 422 | LLM-XAI risk taxonomy staging tags. |
| `metadata/` | - | Release notes, data dictionary, manifest, and privacy/copyright review. |
| `scripts/validate_open_materials.py` | - | Lightweight validation script for row counts, schema, and risky text patterns. |

## Scope

The corpus is a structured narrative review resource informed by systematic mapping. It is not a claim of exhaustive systematic-review coverage across all databases and venues. Records were de-duplicated by DOI when available, with manual checks for title/preprint/published-version overlap.

## Public-Release Sanitization

This release intentionally excludes:

- PDF files and local PDF/text paths.
- Long abstract or full-text extraction columns copied from source papers.
- Non-public reviewer correspondence or manuscript-review files.
- Participant-level data. The included sheets only summarize published studies.

The retained fields are bibliographic identifiers, study descriptors, construct-level extraction fields, theme tags, and author-curated summary fields.

## Reproducing The Checks

From the repository root:

```sh
python3 scripts/validate_open_materials.py
sh scripts/make_checksums.sh
```

Expected result: all row-count and schema checks pass. Bib/PDF/manuscript builds are not part of this open-materials package.

## Citation

Please cite the archived Zenodo record and the associated manuscript. A machine-readable citation file is included as `CITATION.cff`.

## License

The dataset and metadata in this release are licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). See `LICENSE`.
