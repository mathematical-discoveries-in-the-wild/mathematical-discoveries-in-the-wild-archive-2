# Verifier report

Verdict: `candidate full classification; likely valid`.

## Mathematical audit

- Checked the source's inner factorization and Toeplitz-product condition.
- Checked the typed identity
  `T^m = M_Gamma (M_Psi^* M_Gamma)^(m-1) M_Psi^*` by induction.
- Proved separately that `V A W^*` is a partial isometry iff `A` is whenever
  `V,W` are isometries; the reverse implication does not assume surjectivity.
- Checked directly that `M_Psi^* M_Gamma = T_{Psi^* Gamma}`.
- Applied Halmos--Wallen only after the overlap was shown to be power partial
  isometric, retaining every canonical summand and multiplicity.
- Treated zero and constant symbols without relying on the source's
  nonconstant hypothesis.
- Derived the analytic symbol criterion independently for every power.
- Verified the rank-one `2 x 2` counterexample exactly and symbolically.
- Nonuniqueness of the inner factorization causes no ambiguity: every overlap
  reflects the PPI status of the same outer operator.

## Literature and novelty audit

- Cheap run indexes had no duplicate for arXiv:2407.10609 or the overlap route.
- The current 36-page arXiv PDF still states Question IV on page 35.
- Bounded searches on 13 August 2026 covered the exact question, title,
  overlap and compressed-inner-product terms, the 2022 scalar result, the
  2025 Babbar--Maji PPI and characteristic-function papers, and arXiv records
  through 2026.
- The 2025 characteristic-function paper advances the source's Question III
  in one variable, but no later answer to Question IV or this overlap
  classification was found.
- Novelty is plausible, not certified, and priority is not claimed.

## Scope audit

- The result characterizes all nonzero PPI Toeplitz operators via the source's
  complete inner-factor parametrization and the complete Halmos--Wallen
  canonical form of one explicit overlap Toeplitz operator.
- The zero operator and all constant symbols are covered separately.
- A human reviewer should decide whether this canonical overlap
  parametrization matches the intended granularity of “characterize.” It is
  mathematically necessary and sufficient and contains no unresolved
  condition.

## Source and rendering audit

- `source_paper.pdf` is the current 36-page arXiv:2407.10609 PDF.
- `figures/open_problem_crop.png` is a genuine readable crop of page 35 and
  includes the complete closing question block.
- `sanity_check.py` completed with `counterexample_verified=true` and printed
  the exact initial, final, and squared initial matrices.
- Final PDF: `solution_packet.pdf`, 5 pages, SHA-256
  `c6302a153036cb3849fac0a97d33afdabbc1fb55fdc4fc23cac22999569a7423`.
- The final LaTeX log contains no warnings, overfull boxes, underfull boxes, or
  undefined references.
- All five final pages were rendered at 120 dpi and visually inspected. The
  source crop and all equations are readable, no theorem or proof is clipped,
  and no overlap or malformed glyph was found.
