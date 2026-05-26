# Open Materials Staging Pack

This folder stages the row-level materials referenced by the CSUR revision.
It is intended to be uploaded to GitHub and archived with Zenodo before resubmission.

## Contents

- `data/in_scope_hcxai_eval.tsv`: DOI-identified in-scope corpus used in the manuscript.
- `data/theme_map_hcxai_eval.tsv`: non-exclusive theme-to-paper mapping.
- `data/hcxai_extraction.tsv`: project extraction sheet used for construct and study-design fields.
- `data/llm_xai_manual_extraction.tsv`: LLM-era contextual extraction sheet used to support the new generated/dialogic explanation subsection.
- `data/llm_xai_T2_evaluation.tsv`: LLM-XAI evaluation taxonomy staging data.
- `data/llm_xai_T3_risks.tsv`: LLM-XAI risks taxonomy staging data.

## Before Public Release

- Add a `LICENSE` file.
- Add a short `CITATION.cff`.
- Add table-generation scripts or notebooks if they will be released.
- Run a privacy check to confirm that no non-public reviewer notes or personal data are included.
- Create a GitHub release and archive it on Zenodo.
- Replace `[GitHub URL]` and `[Zenodo DOI]` in the manuscript with the public links.
