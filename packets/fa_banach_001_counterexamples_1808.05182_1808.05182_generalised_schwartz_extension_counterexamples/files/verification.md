# Verification Record

- `source_paper.pdf` has 37 pages. Corollaries 4.8 and 4.9 and the open
  sentence are on PDF page 21; they are reproduced in
  `figures/open_question_crop.png`.
- The definitions of generalised Schwartz and semi-Montel target spaces,
  and the hypotheses of both source corollaries, were cross-checked against
  source PDF pages 20–22 and parsed-source lines 148–246 of
  `loc_bound_submission.tex`.
- Consistency-check command:

  `conda run --no-capture-output -n sandbox python code/verify_coordinate_patterns.py`

  Result: 128 eventual-stabilization coordinate cases passed; 64 dense
  boundary-point zero patterns and 64 nonzero center coordinates passed.
- `solution_packet.pdf` compiled in three pages with no final LaTeX warnings,
  overfull boxes, or errors after the required PDF artifact marker. Every
  page was rendered at 150 dpi and visually inspected after the latest
  source-image edit; no clipping, overlap, unreadable text, or malformed
  formulas were found.

Final SHA-256: `5a8e368fe4eb00ad59420aa35a37d7b3bf1937855216adb3297b399a3e87e35a`.
