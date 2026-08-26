# Full criterion for Hausdorff-null modifications of complex activations

Status: `candidate_full_likely_valid`

This packet materially strengthens and supersedes the earlier partial packet
`2012.03351_approximate_continuity_deep_cvnn_obstruction`.

## Source request

Felix Voigtlaender, *The universal approximation theorem for complex-valued
neural networks*, arXiv:2012.03351; *Applied and Computational Harmonic
Analysis* 64 (2023), 33–61, doi:10.1016/j.acha.2022.12.002.

The remark after Theorem 1.4 on arXiv PDF page 4 asks for natural conditions
weaker than continuity under which the necessary non-universality criterion
for fixed-depth deep complex networks remains valid.

## Claimed full resolution

Let `h:C->C` be continuous, let `sigma` belong to the source class `M`, and
assume the exceptional set `{sigma != h}` has zero one-dimensional Hausdorff
measure. For every input dimension and every fixed number `L>=2` of hidden
layers, the `sigma`-network class is universal exactly when `h` is none of:

- a polynomial in `z` and `conj(z)`;
- an entire function;
- the conjugate of an entire function.

Thus the entire source dichotomy is stable under arbitrary changes on an
`H^1`-null set. This supplies a broad natural hypothesis strictly weaker than
continuity and completely answers the stated future-work request in its
literal form. It does not claim a classification of every possible
discontinuous representative in `M`.

## Mechanism

A nonconstant real-analytic map pulls an `H^1`-null planar set back to a
Lebesgue-null set. Layer by layer, every network for an obstructed `sigma`
therefore agrees almost everywhere with a surrogate that is either a uniformly
bounded-degree polynomial or holomorphic/antiholomorphic. Constant
preactivations merely supply constants. The source's polyharmonic obstruction
then gives one positive local-`L^1` error bound for the whole network class.

The condition is genuinely weaker than both continuity and the prior packet's
everywhere approximate continuity: changing `Re(z)` only at the origin gives a
discontinuous, non-approximately-continuous activation covered by this theorem.
The source's universal pathological example changes `Re(z)` on a half-line,
which has positive `H^1` measure and lies outside the theorem.

## Confidence and search

Mathematical confidence: high. Novelty confidence: moderate-high. Bounded
searches through 9 August 2026 covered the run indexes, the exact source
future-work wording, arXiv/web combinations of complex-valued networks with
Hausdorff measure/null-set modifications, and the main later CVNN approximation
papers. No direct statement was found.

## Files

- `source_paper.pdf`: arXiv:2012.03351.
- `figures/open_problem_crop.png`: source Theorem 1.4 and future-work remark.
- `main.tex`, `solution_packet.pdf`: complete proof packet.

Ledger: `runs/fa_banach_001/ledger/results/2012.03351_hausdorff_null_modification_cvnn_criterion.json`.
