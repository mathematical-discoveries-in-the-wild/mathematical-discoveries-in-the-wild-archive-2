# Sharp metric-dimension results for finite-dimensional normed spaces

Result type: `partial`

Status: promoted collection of exact theorems, likely valid pending human
review. The universal strictly convex case of Problem 1 remains open.

Source paper:

- György Pál Gehér, “Is it possible to determine a point lying in a simplex if
  we know the distances from the vertices?”, arXiv:1507.05114.
- Open-question location: Section 4, Problem 1, source PDF page 12.
- `source_paper.pdf` is reconstructed from the cached arXiv source.
- `figures/open_problem_crop.png` is an exact source-page crop.

## Claimed contribution

The packet proves four complementary statements.

1. Every finite metric dimension of a `d`-dimensional normed space is at least
   `d+1`. This resolves the lower-bound uncertainty immediately following
   Problem 1.
2. If the unit ball has a facet, then no finite set resolves the space. Hence
   every polyhedral norm has infinite metric dimension; in dimension two this
   applies to every non-strictly-convex norm. This gives a broad negative
   answer to the literal version without the parenthetical strictness.
3. For every `1<p<infinity`, the metric dimension of `ell_p^d` is exactly
   `d+1`; `{0,e_1,...,e_d}` is an explicit optimal resolving set. The same is
   true for weighted and linearly transformed copies.
4. The same exact value holds for a stable class of smooth non-Hilbert norms:
   if `Phi=N^2=|.|_2^2+H` and `Lip(grad H)<2/sqrt(d)`, then the standard
   simplex resolves. This includes
   `N_epsilon(x)^2=|x|_2^2+epsilon ||x||_4^2` for sufficiently small positive
   `epsilon`.

## Files

- `main.tex`: exact statements and proofs, source context, proof intuition,
  limitations, and review notes.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source reconstruction.
- `figures/open_problem_crop.png`: exact crop of Problem 1 and its context.
- `verification.md`: proof audit and human-review checklist.
- `tmp/`: source build, packet build, and full-page visual-QA renders.

## Scope

No claim is made that every strictly convex norm has metric dimension `d+1`.
The successful positive arguments use either coordinate-power separability or
a quantitative global `C^{1,1}` comparison with a Euclidean quadratic. No
priority claim is made; expert review and a dedicated literature check are
recommended.
