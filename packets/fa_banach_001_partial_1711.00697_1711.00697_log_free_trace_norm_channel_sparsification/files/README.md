# Log-free trace-norm channel sparsification

Status: **substantial partial result; complete solution of the uniform trace-norm variant; likely valid, subject to expert review**.

Source: Cécilia Lancien and Andreas Winter, *Approximating quantum channels by completely positive maps with small Kraus rank*, arXiv:1711.00697, PDF page 6.

## Result

For every CPTP map `N : L(A) -> L(B)` and every `0 < epsilon < 1`, there is a CPTP map `Nhat` with

`Kraus-rank(Nhat) <= C (dim(A) + dim(B)) / epsilon^2`

and

`sup_rho ||Nhat(rho) - N(rho)||_1 <= epsilon`.

Thus the logarithmic factor in the source's universal channel-compression bound is unnecessary for the operational uniform output trace-norm metric. The result does **not** establish the stronger two-sided operator-order approximation in source Theorem 3.1.

## Mechanism

Gaussian linear combinations of a Stinespring Kraus family turn every fixed pure-input output into an empirical covariance matrix. A trace-norm covariance lemma gives mean error `O(sqrt(dim(B)/m))` and tail `exp(-c m t^2)`. A constant input net suffices because the global Hermitian `1 -> 1` error norm controls its own net interpolation. The sampled Kraus family is then normalized by `S^{-1/2}` to make the map exactly trace preserving.

## Upgrade attempts

1. The log-free trace-norm theorem above was completed.
2. For each fixed input, the same Gaussian construction also attains the source's stronger relative operator-order estimate with `O(dim(B)/epsilon^2)` samples.
3. The uniform strong upgrade was recast as a near-isometry problem for normalized Stinespring slices. Constant nets fail near output probabilities `1/dim(B)`; fine nets reproduce the source logarithm, while full spectral sparsification costs the environment dimension. This remains open in the packet.

## Packet files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question on PDF page 6.

Novelty search: bounded local-corpus and targeted arXiv search through 2026-08-11 found no later removal of the logarithm for this uniform trace-norm problem. This is not a definitive literature review.

Human review should focus on the Gaussian truncation/concentration lemma and the constant-net self-bounding argument.
