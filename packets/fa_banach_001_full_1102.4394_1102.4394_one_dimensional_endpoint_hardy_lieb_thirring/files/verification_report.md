# Verification report

## Mathematical checks

- Confirmed the exact open sentence after Theorem 1.5 on source PDF page 5.
- Confirmed Ekholm--Frank Theorem 2.1 on supporting PDF page 4; at
  `alpha=0`, `gamma=1/2` it gives the critical half-line estimate with an
  `L1` potential and `C_{1/2,0} <= 1.185`.
- Confirmed source Corollary 2.2 on source PDF page 8 and source Proposition
  2.1 on page 7; at `q=2`, the constant satisfies `C_2 <= 16`.
- Checked that on the two midpoint halves of `I=(a,b)`, the full-component
  distance is exactly `x-a` and `b-x`, respectively.
- Checked the zero-extension comparison: the finite half with a Dirichlet
  condition at the midpoint is a form subspace of the critical half-line
  operator with the potential extended by zero.
- Checked codimension-one form interlacing:
  `mu_j <= nu_j <= mu_{j+1}`.  It bounds every full-interval eigenvalue after
  the lowest by a split eigenvalue with the correct magnitude direction.
- Checked the bottom-eigenvalue calculation: for `||u||_2=1` and
  `A=int_I V_-`, the source pointwise bound gives
  `q[u] >= x^2-4Ax >= -4A^2`, hence `sqrt((-mu_1)_+) <= 2A`.
- Checked rays, positive-potential monotonicity, countable direct sums, scaling,
  and monotone truncation from compact bounded negative parts to general
  `L1` potentials.

## Literature and novelty checks

- Cheap run indexes contained no prior result for arXiv:1102.4394 or the
  `N=1`, `gamma=1/2` endpoint.
- Exact-quotation and arbitrary-domain endpoint searches found no later paper
  stating this resolution.
- The critical half-line endpoint theorem predates the target and is an input,
  not the answer: it does not handle finite intervals with two singular
  endpoints or arbitrary unions.  The new step is midpoint gluing by
  codimension-one interlacing plus the source's pointwise estimate.
- The separate `1<p<2` Hardy--Sobolev--Maz'ya question was not claimed;
  literature as recent as 2024 still describes the local version as unknown.

## Artifact checks

- `main.tex` compiled under `latexmk -halt-on-error`.
- The final LaTeX log contains no undefined references, multiply defined
  labels, overfull boxes, LaTeX errors, emergency stops, or fatal errors.
- `solution_packet.pdf` has 3 pages with extractable text.
- All 3 packet pages were rendered at 1.7x and visually inspected; equations,
  inequalities, page breaks, and source notes are legible with no clipping.
- `source_paper.pdf` has 19 pages and
  `supporting_halfline_paper.pdf` has 17 pages.
- Both evidence crops were rendered at 2.2x and visually inspected.  The first
  contains Theorem 1.5 and the full endpoint sentence; the second contains the
  complete half-line Theorem 2.1 and numerical constant bound.
- The result ledger parses as valid JSON and uses model `GPT5.6`.

