# Verification Report

Candidate: arXiv:2408.16593, Question 5.1 on unconditional convergence of
Gabor Schauder-frame reconstructions in modulation spaces.

## Verdict

`likely valid`

Confidence: 91/100.

## Claim checked

For every `1<p<2`, the Heil--Powell endpoint-power critical Gabor Schauder
basis has both its primal and biorthogonal windows in `M^p`, but is
conditional in `M^2=L2`; hence it is a counterexample to Question 5.1 at
`q=2`.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Parameter range is nonempty | valid | `1-1/p>0`, and it is `<1/2` because `p<2`. |
| Heil--Powell construction applies | valid | Example 5.11 uses exactly `0<delta<1/2`, endpoint powers, smooth positive middle, and support `[0,1]`. |
| The system is a Schauder basis | valid | Heil--Powell Theorem 5.10 plus `|Zg|^2=|g|^2 in A_2`, for every enumeration in their class `Lambda`. |
| The dual is `gamma=1/g` on `(0,1)` | valid | Direct time-cell disjointness and Fourier orthogonality prove biorthogonality; uniqueness follows from the basis property. |
| `g in M^p` | valid | Heil--Powell Theorem 6.1 proves the stronger `g in M^1`. |
| Endpoint Fourier asymptotic | valid | The two endpoint phases are conjugate and add to the strictly positive constant `2 Gamma(1-delta)(2 pi)^(delta-1) sin(pi delta/2)`. |
| Exact `ell^r` threshold | valid | The nonzero asymptotic is `|n|^{delta-1}`; the p-series criterion is `r(1-delta)>1`. |
| Fourier coefficients characterize `M^p` here | valid | Yu Corollary 4.1 applies for `1<p<=2`; support in one unit cell collapses the double sequence to the integer Fourier coefficients. For the converse, finite Fourier sums are Cauchy in `M^p` and converge to `gamma` in `L2`. |
| `gamma in M^p` | valid | The choice `delta<1-1/p` is exactly `p(1-delta)>1`. |
| Failure of unconditional convergence | valid | The Zak transform is not bounded away from zero, so the basis is not Riesz. In a Hilbert space unconditional Schauder bases are precisely Riesz bases. |
| The exponent requested by the question is admissible | valid | `q=2`, and for `1<p<2` one has `p<2<p'`. |

## Adversarial checks

- Endpoint cancellation does not occur. At integer frequency the right
  endpoint has phase conjugate to the left endpoint, and their sum is
  `2 sin(pi delta/2)>0` times a positive factor.
- The `O(n^-1)` remainder is lower order because `0<delta<1/2` implies
  `n^-1=o(n^(delta-1))`.
- The dual is in `L2` because `2 delta<1`, so the Hilbert-space
  biorthogonal system is legitimate.
- No claim is made that the expansion is conditional for every vector;
  non-Rieszness yields the needed existence of at least one vector whose
  expansion is not unconditional.
- No claim is made for `p=1`. Indeed Heil--Powell Theorem 7.1 rules out an
  `M^1` dual in this exact setting.
- No claim is made about canonical duals of redundant Hilbert frames.

## External dependencies

1. Heil--Powell Theorem 5.10 and Example 5.11: Schauder basis and non-Riesz
   property for the endpoint-power window.
2. Heil--Powell Theorem 6.1: the primal window belongs to `M^1`.
3. Yu Corollary 4.1: sampled local Fourier-coefficient norm equivalence for
   `M^r`, `1<r<=2`.
4. Standard Hilbert-space theorem: unconditional Schauder basis iff Riesz
   basis.

All three paper-specific dependencies are preserved in the packet, with
page crops for the decisive construction and theorem.

## Novelty caution

The underlying example is from 2006. The apparently new contribution is the
short endpoint-asymptotic observation that its reciprocal dual is in each
prescribed `M^p`, `p>1`, after choosing `delta` sufficiently small. A bounded
search found no later source making this deduction, but cannot certify
novelty.

## Human review recommendation

Send to a time-frequency analyst. The main items to audit are the use of
Yu's Corollary 4.1 at support-cell endpoints and the endpoint oscillatory
integral asymptotic. If accepted, the result is a full counterexample rather
than a partial advance.
