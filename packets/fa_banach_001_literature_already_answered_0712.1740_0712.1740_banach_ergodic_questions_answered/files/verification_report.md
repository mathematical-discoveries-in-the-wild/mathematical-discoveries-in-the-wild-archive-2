# Verification report

Verified: 2026-08-17

## Source identification

- Source questions checked directly on PDF pages 19--20 of arXiv:0712.1740.
- Question 1 asks for a Banach-valued ergodic theorem on finitely generated
  discrete polynomial-growth groups.
- Question 2 asks for one framework covering both Z^d and R^d equivariance.

## Later-answer identification

- arXiv:1003.3620v2, Assumption 2.5 and Remark 2.6: the authors explicitly
  state that every group of polynomial volume growth fits their framework.
- arXiv:1003.3620v2, Theorem 3.1: Banach-norm convergence for
  colouring-invariant almost-additive functions, with an explicit error
  estimate.
- arXiv:1211.2089v2, preliminaries: the framework is second-countable locally
  compact unimodular amenable groups with Haar measure, and all discrete and
  all abelian groups are included.
- arXiv:1211.2089v2, Theorem 5.7: mean ergodic theorem for Banach-valued
  almost-additive set functions along strong Følner sequences.
- Therefore the first answer covers the requested polynomial-growth class,
  and the second single theorem includes Z^d/counting measure and
  R^d/Lebesgue measure.

## Artifact checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error`: PASS.
- Final LaTeX warnings, undefined references, overfull boxes, and underfull
  boxes: none.
- PDF pages: 2.
- PDF SHA-256:
  `d1d5ef57ce380a0b0e44b9b9cc99ccc2bb720ede237d0ee82a9208d9e2d73de9`.
- Both final pages were rendered at 150 dpi and visually inspected.
- Source PDF and both decisive supporting PDFs are present.
