# Verification Report

Candidate: `1912.03112_affine_wigner_sqrt_exponential_positive`

## Claim Checked

For every `p,beta > 0`, a normalized multiple of
`psi(r)=r^p exp(-beta sqrt(r))` belongs to `L^2(R_+,dr/r)`, has an
everywhere nonnegative affine Wigner distribution in the convention of
arXiv:1912.03112, and is not a generalized Klauder wavelet. Hence it
disproves the paper's Affine Positivity Conjecture.

## Verdict

likely valid

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Match to source definition | valid | The packet uses exactly the source's `lambda(u)` and Fourier convention. The conjecture is on printed/PDF pages 25–26. |
| Hilbert-space hypothesis | valid | The norm integral is `2 Gamma(4p)/(2 beta)^(4p)`, finite exactly for `p>0`; the displayed normalization is correct. |
| Slice factorization | valid | `lambda(u)=h(u)e^(u/2)`, `lambda(-u)=h(u)e^(-u/2)`, and `2 sqrt(h) cosh(u/4)=sqrt(u coth(u/4))`. The normalization by the value at zero is positive. |
| Positive definiteness of `h^(2p)` | valid | Euler's `sinh` product has the stated constants. Each inverse-power factor is a positive Gaussian mixture for arbitrary real `p>0`; products and the continuous pointwise limit preserve positive definiteness. |
| Conditional negative definiteness of `q` | valid | The partial fraction `v coth(v/2)-2 = 4 v^2 sum_n (v^2+4 pi^2 n^2)^(-1)` is correct. Each summand is `1` minus a normalized positive-definite Cauchy kernel. Positive locally uniform sums preserve conditional negative definiteness. |
| Square-root exponential factor | valid | `f=sqrt(4+q)-2`. The subordination identity expresses `exp(-c f)` as a positive normalized mixture of `exp(-t q)`, which are positive definite by Schoenberg. |
| Fourier positivity | valid | The kernel is real, even, positive definite, and `L^1`; `h^(2p)=O(|u|^(2p)e^(-p|u|))`. Bochner plus Fourier uniqueness gives a continuous nonnegative Fourier transform, pointwise. |
| Exclusion from Klauder family | valid | Klauder moduli are `|C| r^alpha exp(-b r)` with `alpha,b>0`; logarithmic derivatives cannot agree with `r^p exp(-beta sqrt(r))`. |

## Counterexample Search Against the Proposed Proof

Small cases checked:

- Algebraic identities were evaluated on 2,001 points in `[-25,25]`.
- Positive-definiteness Gram matrices were checked for both factors and their
  product on a nonuniform ten-point set.
- The centered conditional-negative-definiteness matrix for `q` was checked
  on the same set.
- FFT approximations were checked for 60 triples with
  `p in {0.1,0.3,1,2.5}`, `beta in {0.2,1,3}`, and
  `a in {0.05,0.3,1,5,20}`.

Result: no contradiction found. These finite checks are not used as proof.
The run reported a smallest tested positive-definite Gram eigenvalue of
`2.589e-09`, a largest centered conditional-negative-definite eigenvalue of
`-4.663e-16`, and a worst FFT real value of `-3.123e-15` (roundoff scale),
with zero reported imaginary residual.

## External Dependencies

- Euler's product for `sinh`: standard and used with the correct rescaling.
- Schoenberg's equivalence between conditionally negative definite kernels
  and positive definiteness of `exp(-t q)`: standard; cited to Berg,
  Christensen, and Ressel.
- Bochner's theorem and Fourier uniqueness: standard; the packet supplies the
  needed continuity and integrability.

## Gaps and Residual Risks

- No mathematical gap was found in the proof.
- The novelty check is bounded. A specialist should still search older
  signal-analysis literature that may describe the same family in different
  parametrizations.
- The packet disproves the stated classification but does not propose a new
  complete classification of nonnegative affine Wigner states.

## Confidence

Score: 94/100

Reason: every parameter and constant in the two analytic factorizations was
independently recomputed, the named theorems apply with their hypotheses
present, and numerical diagnostics found no conflicting slice. The remaining
uncertainty is primarily literature novelty, not proof completeness.

## Human Review Recommendation

send to human

Prioritize review of the `coth` partial-fraction constants, the normalization
in the square-root subordination formula, and whether the historical
literature uses a convention equivalent to the source's affine Wigner
distribution.
