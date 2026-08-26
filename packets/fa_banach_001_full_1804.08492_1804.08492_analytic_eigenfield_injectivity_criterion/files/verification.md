# Verification Record

- The original source is stored as `source_paper.pdf` (32 pages).
- The open question is on PDF page 16, immediately after Theorem 4.8; the
  source crop is `figures/open_problem_crop.png`.
- The proof was checked against Lemma 4.7 and equations (4.19)--(4.31) on PDF
  pages 13--15, as well as the parsed source around lines 1214--1407.
- Arithmetic command:

  `conda run --no-capture-output -n sandbox python code/verify_weighted_shifts.py`

  It verifies the product formula, the hyperrange witnesses, and the `n!`
  coefficient growth for `w_n=1/(n+1)` through the stated finite checks.
  This is a consistency check, not part of the proof.
- `solution_packet.pdf` was compiled after the required one-time PDF artifact
  marker. Every final page was rendered and visually inspected after the
  latest source edit, and the final LaTeX log was checked for warnings and
  errors.

Final SHA-256: `6b6a06e85b2bbdbc66be263c55ed8128e183d2824d3b0f7c306f0fb6adf7413c`.
