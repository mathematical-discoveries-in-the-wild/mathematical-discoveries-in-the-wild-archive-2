# Verification Report

Candidate: arXiv:2603.23056, effective eigenvalue moduli on compact classes

## Claims checked

1. An optimal `delta^(1-alpha)` modulus into `C^{0,alpha}` on every
   Lipschitz-bounded Hermitian class.
2. A linear `W^{1,q}` modulus on uniformly gapped families.
3. A one-parameter diagonal `W^{1,q}` modulus with power
   `min{beta/(1+beta),1/q}` (and a critical logarithm), plus power-sharp
   examples.

## Verdict

`likely valid` (substantial partial resolution of Problem 1.15)

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Source scope | valid | Problem 1.15 asks broadly for effective moduli on interesting compact subspaces and explicitly exhibits the bounded `C^{1,beta}` ball. The packet does not claim to solve all compact classes. |
| Sup--Lipschitz interpolation | valid | `|h(x)-h(y)|` is bounded by both `2||h||inf` and `Lip(h)|x-y|`; optimizing gives the stated interpolation inequality. |
| Hoffman--Wielandt input | valid | Ordered eigenvalues of Hermitian matrices are 1-Lipschitz from Frobenius to Euclidean norm, pointwise and for Lipschitz constants. |
| `C^{0,alpha}` constant | valid | The eigenvalue difference has sup norm at most `delta` and Lipschitz constant at most `2C`, producing `delta+2C^alpha delta^(1-alpha)`. |
| Hölder sharpness | valid | Shifted diagonal crossings have input distance `sqrt(2)t` and eigenvalue-difference Hölder seminorm at least `2sqrt(2)t^(1-alpha)`. They lie in a common smoothness ball. |
| Riesz contour | valid | Radius `gamma/3` and `delta<=gamma/6` give resolvent bounds `3/gamma` and `6/gamma`; the contour length yields projection difference at most `6delta/gamma`. |
| Eigenvalue derivative formula | valid | Under simple spectra, `partial lambda_i=tr(P_i partial A)`. Frobenius duality and the projection estimate give the linear derivative modulus. |
| Thin-sublevel root count | valid | Consecutive regular roots in a derivative band have a Rolle zero between them; Hölder continuity of `h'` forces separation `c(s/H)^(1/beta)`. |
| Coarea summation | valid | The 1D area formula converts the root count into derivative mass. Dyadic summation above `r=eps^(beta/(1+beta))` gives the subcritical, critical-log, and supercritical regimes. |
| Sorting reduction | valid | A disagreement of sorting permutations contains only pair inversions with scalar gap at most `2delta`. At most `d(d-1)/2` swaps reduce the derivative error to thin-sublevel estimates for coordinate differences. |
| Crossing `1/q` obstruction | valid | The derivative difference has constant norm `2sqrt(2)` on an interval of length `t`, hence order `delta^(1/q)`. |
| Oscillatory obstruction | valid | Amplitude `k^(-(1+beta))` keeps a uniform `C^{1,beta}` bound. The input distance is order `k^(-(1+beta))` and the derivative error order `k^(-beta)`. |
| Normal extension | valid within scope | Only the `C^{0,alpha}` theorem is extended to unordered normal spectra, using Hoffman--Wielandt and a fixed Almgren embedding. No diagonal Sobolev analogue is claimed for arbitrary normal matrices. |

## Computational verification

`code/verify_effective_moduli.py` checks:

- exact log--log slopes `1-alpha=0.65` and `1/q=0.25` for shifted crossings;
- slope `beta/(1+beta)=1/3` for the oscillatory construction;
- the interpolation upper bound; and
- Riesz-projection/eigen-derivative bounds on 100 random gapped Hermitian
  perturbations.

All checks passed. The maximum observed-to-proved ratios were approximately
`0.1011` for projections and `0.0479` for derivatives.

## Counterexample and loophole search

- Compactness alone does not provide an explicit formula; the results exploit
  bounded Lipschitz or `C^{1,beta}` constants, or a uniform gap.
- The diagonal sorting proof is genuinely one-dimensional. Multiparameter
  coarea geometry would require a separate estimate.
- A uniform gap cannot be silently inferred from compactness of K; the gapped
  theorem is a separate subclass result.
- General eigenvalue branches may lose derivative Hölder control near avoided
  crossings, so the diagonal lemma cannot simply be applied branchwise.
- The critical logarithm is an upper bound not proved sharp; only the power is
  certified sharp.

## External dependencies

The proof uses Hoffman--Wielandt, Weyl eigenvalue perturbation, the elementary
Riesz projection formula/resolvent identity, the derivative formula for a
simple Hermitian eigenvalue, and the one-dimensional area formula.

## Gaps and scope limitations

The general no-gap, nondiagonal `W^{1,q}` effective modulus in Problem 1.15
remains unresolved. No gap was found in the three promoted subresults.

## Confidence

Score: 97/100

Residual uncertainty is concentrated in expert confirmation of the dyadic
thin-sublevel constants and novelty, not in the exponent calculations.

## Human review recommendation

`send to human`

Primary review focus: Lemma 4 (thin sublevel derivative mass), the sorting
network argument in Theorem 5, and the exact scope statement.
