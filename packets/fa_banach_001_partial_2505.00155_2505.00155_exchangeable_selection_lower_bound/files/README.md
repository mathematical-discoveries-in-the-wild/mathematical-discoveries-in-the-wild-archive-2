# 2505.00155 - exchangeable selection retains the endpoint Orlicz loss

Status: `partial_result_likely_valid`; `human_review_needed`.

Superseded in scope on 2026-08-11 by the deterministic full-result packet at `solutions/full/2505.00155_walsh_affine_cube_optimality`. This packet is retained as proof history for the stronger-than-Bernoulli exchangeable-selector subcase.

Model: `GPT5.6`.

Source: Will Burstein, *Lambda_p Style Bounds in Orlicz Spaces Close to L^2*, arXiv:2505.00155v2.

## Result

The source leaves open whether its `(log log n)^(alpha/2)` loss is optimal when selecting at least

`n / (e log^(alpha+1) n)`

functions from a bounded orthogonal system. Its matching lower bound treats independent Bernoulli selection.

This packet proves a stronger randomized-selection obstruction. Along an explicit sequence `n_m`, for the first `n_m` trigonometric characters, every permutation-invariant (exchangeable) random selector that returns at least the target number of characters has synthesis norm at least

`c(alpha) (log log n_m)^(alpha/2)`

with probability tending to one.

## Proof mechanism

Partition the frequencies into consecutive blocks of length `m`, where `log m` is comparable to `log log n_m`. A complete block supports a normalized Dirichlet kernel whose Luxemburg norm is at least `c(alpha) (log m)^(alpha/2)`.

For a uniform fixed-cardinality subset, indicators of containing two disjoint blocks are negatively correlated. The expected number of complete blocks tends to infinity, and a direct second-moment inequality makes the probability of at least one complete block tend to one. Conditional on its cardinality, every exchangeable subset is uniform, and the bad event is monotone under inclusion.

## Scope

This is a substantial partial result, not a full solution. It rules out every exchangeable randomized selector, but it does not rule out a label-dependent deterministic subset that avoids all complete consecutive blocks. The unrestricted optimality question remains open.

## Verification and novelty

The proof is elementary after the source construction and has no computational or unproved external dependency. The accompanying verifier report checks the fixed-size hypergeometric probability, negative correlation, the second moment, the Dirichlet-kernel Luxemburg estimate, and the exchangeability reduction.

A bounded local-index and arXiv search on 2026-08-11 found the source paper and background work on Lambda(Phi) sets and Orlicz sampling, but no later full resolution and no matching exchangeable-selector lower bound.

## Files

- `main.tex`: complete partial-result proof packet.
- `solution_packet.pdf`: rendered packet.
- `verification_report.md`: step-by-step adversarial verification.
- `attempt_log.md`: full-resolution routes tried and the precise remaining obstruction.
- `source_paper.pdf`: arXiv v2 source paper.
- `figures/open_problem_crop.png`: page-13 source evidence containing Theorem 2.10 and Remark 2.11.

## Human review recommendation

Review as a likely valid partial result. Focus on the asymptotic `B_m p_m -> infinity`, the negative correlation of disjoint complete-block events under sampling without replacement, and the fact that exchangeability is essential to the conclusion.
