# Verification report

## Statement mapping

- Checked the sole queue signal in the introduction of arXiv:1605.03861.
- Checked the equivalent nonnegative diagonal formulation immediately after
  its Theorem 1.1.
- Checked Theorem 5 of arXiv:1507.02268v3 in the official PDF: diagonal `S`,
  `O(k/epsilon^2)` support, additive Gram error at most `epsilon`, and a
  deterministic polynomial-time algorithm.
- Verified dimensions under `B=A^*/||A||` and the identity
  `(S B)^T(S B)=A S^2 A^*/||A||^2`.
- Checked `||B||=1`, `||B||_F^2=srank(A)`, preservation of support under
  `D=S^2`, and the harmless ceiling of stable rank.
- Scope is limited to the arbitrary diagonal-weight formulation; no
  equal-weight strengthening is asserted.

## Chronology

- arXiv:1507.02268v3: 2 March 2016.
- arXiv:1605.03861v1: 12 May 2016.
- ICALP publication of the answer: August 2016, DOI
  `10.4230/LIPIcs.ICALP.2016.11`.

## Packet/render QA

- `main.tex` was compiled repeatedly with `pdflatex -halt-on-error`; the final
  log has no undefined references, overfull boxes, or compilation warnings.
- Ghostscript text extraction contains both theorem statements, the
  polynomial-time conclusion, the one-line reduction, chronology, and scope.
- Both final pages were rendered at 140 dpi and visually inspected.  No
  clipping, overlap, malformed mathematics, or illegible text remains.
