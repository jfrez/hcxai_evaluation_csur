# Data Dictionary

All data files are UTF-8 tab-separated value files (`.tsv`). Row counts below exclude the header row.

## `data/in_scope_hcxai_eval.tsv`

DOI-identified corpus used in the manuscript synthesis (`107` rows).

Core identifier fields: `paper_id`, `doi`, `arxiv_id`, `year`, `title`, `venue`.

Study/context fields: `domain`, `user_group`, `task`, `model`, `data_modality`, `explanation_techniques`, `interaction_design`, `evaluation_design`, `n_participants`, `participant_type`.

Construct fields: `metrics_trust`, `metrics_reliance`, `metrics_understanding`, `metrics_performance`.

Synthesis fields: `main_findings`, `conclusions`, `limitations`.

## `data/hcxai_extraction.tsv`

Project extraction sheet used for construct and study-design fields (`15` rows). This sheet preserves the original column naming used during staging, including `metrics_comprehension` for understanding/comprehension-related measures.

## `data/theme_map_hcxai_eval.tsv`

Non-exclusive mapping from synthesis themes to DOI records (`277` rows). A paper can appear under multiple themes.

Fields: `theme`, `doi`, `bibkey`.

## `data/llm_xai_contextual_catalog.tsv`

Sanitized LLM-era contextual catalog (`477` rows). This file supports the manuscript subsection on generated rationales, retrieval-grounded citations, and dialogic explanation. It excludes long abstract/full-text extraction fields from the staging sheet.

## `data/llm_xai_T2_evaluation.tsv`

LLM-XAI evaluation taxonomy staging tags (`422` rows).

Fields: `paper_id`, `year`, `title`, `in_scope`, `secondary`, `C_tags`.

## `data/llm_xai_T3_risks.tsv`

LLM-XAI risk taxonomy staging tags (`422` rows).

Fields: `paper_id`, `year`, `title`, `in_scope`, `secondary`, `E_tags`.

## Missing Values

Empty cells mean that the field was not applicable, not reported, or not captured during extraction. Empty cells should not be interpreted as evidence that the corresponding construct was absent from the original paper.
