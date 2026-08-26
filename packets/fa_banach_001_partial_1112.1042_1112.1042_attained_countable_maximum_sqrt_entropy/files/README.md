# Square-root-entropy smoothing of attained countable maxima

Status: `candidate_partial_result_likely_valid`

Source: Daniel Azagra, *Global approximation of convex functions*,
arXiv:1112.1042v7, open question on PDF page 4.

## Result

Let `X` be a real Banach space and

`f(x) = max_i (x_i^*(x) + b_i)`

be an everywhere-attained countable affine maximum with uniformly bounded
slopes. Then, for every `epsilon > 0`, there is a globally defined
`C-infinity` convex function `h` such that

`f - epsilon <= h <= f` on `X`.

The construction maximizes the affine average over the infinite probability
simplex with the bounded bonus

`epsilon * sum_i w_i sqrt(alpha_i)`, where `w` is a positive unit vector in
`ell_2`. The unique optimizer has an explicit scalar Lagrange multiplier.
Attainment of the original maximum puts the multiplier strictly above the
maximum, and a locally uniform series argument plus the Banach-space implicit
function theorem gives `C-infinity` smoothness.

The theorem includes the infinite-simplex support function

`x -> max(0, sup_n x_n)` on `ell_2`,

which defeats ordinary summable-weight log-sum-exp because of its logarithmic
weight penalties.

## Scope

This does not answer the full source question. An arbitrary Lipschitz convex
function need not be an attained countable affine maximum. At nonattainment
points the multiplier gap can close, and the implicit smoothness proof need
not apply. A deep upgrade attempt through uniform approximation by attained
countable maxima runs into the noncompactness of the infinite-dimensional
unit sphere.

A bounded search found the source paper, the later stronger open problems in
arXiv:1411.0471, and unrelated entropy regularizers, but no exact source for
this theorem. Novelty confidence is therefore bounded, not definitive.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem, explicit construction, and proof.
- `source_paper.pdf`: arXiv:1112.1042v7.
- `figures/open_problem_crop.png`: source question on PDF page 4.
- `VERIFICATION.md`: proof and rendering checks.

Human review should focus on the infinite-simplex optimizer and the local
uniform convergence needed for Frechet `C-infinity` smoothness.
