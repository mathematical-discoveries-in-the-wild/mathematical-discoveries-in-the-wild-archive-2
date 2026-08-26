# Approximate continuity restores the deep-CVNN obstruction

Status: `superseded_by_full_result`

Superseded by
`solutions/full/2012.03351_hausdorff_null_modification_cvnn_criterion/`,
which permits arbitrary changes on an `H^1`-null set and includes
discontinuous obstructed activations that are not approximately continuous.

## Source direction

Felix Voigtlaender, *The universal approximation theorem for complex-valued
neural networks*, arXiv:2012.03351; *Applied and Computational Harmonic
Analysis* 64 (2023), 33–61, doi:10.1016/j.acha.2022.12.002.

The remark after Theorem 1.4 on arXiv PDF page 4 asks for natural conditions
on a complex activation function that are weaker than continuity but still
make the theorem's necessary non-universality criterion valid.

## Candidate result

Assume the activation `sigma` belongs to the source class `M` and is
approximately continuous at every point of the complex plane. Then, for every
fixed depth with at least two hidden layers, the source paper's characterization
is an if-and-only-if statement: the network class is universal exactly when
`sigma` does not agree almost everywhere with

- a polynomial in `z` and `conj(z)`, or
- an entire function or the conjugate of one.

The obstruction direction retains the source's stronger uniform positive
lower bound in local `L^1` against a compactly supported continuous target.

The mechanism is pointwise rigidity. An everywhere approximately continuous
function that agrees almost everywhere with a continuous function agrees with
it everywhere. Thus the source's polynomial/holomorphic obstruction applies
unchanged. Approximate continuity is genuinely weaker than continuity even
inside `M`; the packet gives an explicit bounded example with a single ordinary
discontinuity.

## Scope and confidence

This supplies one natural strict weakening of continuity and a full
characterization within that class. It does not claim that approximate
continuity is the weakest possible hypothesis, nor does it classify every
null-set modification of a polynomial or entire activation.

Mathematical confidence: high. Novelty confidence: moderate. Bounded searches
of the run indexes, the exact future-work wording, later CVNN approximation
papers, and arXiv/web searches through 9 August 2026 found no direct statement
of this approximate-continuity extension.

## Files

- `source_paper.pdf`: arXiv:2012.03351.
- `figures/open_problem_crop.png`: Theorem 1.4 and the future-work remark.
- `main.tex`, `solution_packet.pdf`: full candidate-result packet.

Ledger: `runs/fa_banach_001/ledger/results/2012.03351_approximate_continuity_deep_cvnn_obstruction.json`.
