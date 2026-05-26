# Privacy and Copyright Review

Review date: 2026-05-25

## Included Data

The release contains bibliographic identifiers, paper-level extraction fields, theme mappings, and author-curated summaries of published research.

## Excluded Data

The release excludes:

- PDF files and downloaded full texts.
- Local file paths to PDFs or extracted text.
- Long abstract/full-text extraction columns copied from source papers.
- Reviewer letters, referee comments, and non-public editorial correspondence.
- Participant-level data.

## Residual Caveats

Some rows summarize published papers and may include short phrases such as method names, venues, or terminology from those papers. These are used as bibliographic/extraction metadata rather than as redistributed article text.

Before creating a public GitHub repository, run:

```sh
python3 scripts/validate_open_materials.py
```

The script checks row counts, required columns, and common risky patterns such as emails, local PDF paths, and review-correspondence terms.
