# GitHub and Zenodo Release Steps

1. Create a public GitHub repository, for example `hcxai-evaluation-open-materials`.
2. Copy the contents of this folder to the repository root.
3. Optionally add `repository-code` to `CITATION.cff` after the final GitHub URL exists.
4. Run `python3 scripts/validate_open_materials.py`.
5. Run `sh scripts/make_checksums.sh`.
6. Commit all files.
7. Create a GitHub release tagged `v1.0.0`.
8. Connect the GitHub repository to Zenodo and archive the release.
9. Copy the final GitHub URL and Zenodo DOI into the manuscript placeholders:
   - `[GitHub URL]`
   - `[Zenodo DOI]`

Do not upload PDFs, downloaded article text, reviewer letters, or manuscript correspondence to the public repository.
