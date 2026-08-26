# Verification Report

Candidate: arXiv:2505.00155, exchangeable-selection lower bound for the endpoint Orlicz subset problem.

## Claim checked

Along the explicit dimensions

`n_m = m^(ceil(Cm)+1)`, with `C = 2(alpha+2)`,

every exchangeable selector returning at least

`ceil(n_m / (e log^(alpha+1) n_m))`

trigonometric characters has Fourier synthesis norm at least

`c(alpha) (log log n_m)^(alpha/2)`

with probability tending to one.

## Verdict

`likely valid; expert review requested`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Dimension sequence and target density | valid | `log n_m = (ceil(Cm)+1) log m`, so `log log n_m = log m + log log m + O(1)`. |
| Full-block probability for a uniform `k_m`-subset | valid | It is exactly `(k_m)_m/(n_m)_m`; since `m^2/k_m -> 0`, its logarithm is `m log(k_m/n_m)+o(1)`. |
| Expected number of full blocks | valid | Its logarithm is `(C-rho)m log m - rho m log log m + O(m)`, which tends to infinity because `C>rho=alpha+1`. |
| Negative correlation for two disjoint blocks | valid | Conditioning on the first block changes the second-block probability to `(k-m)_m/(n-m)_m`, and the factorwise comparison with `(k)_m/(n)_m` is correct. |
| Second-moment lower bound | valid | `E X^2 <= lambda + lambda^2`; Cauchy-Schwarz gives `P(X>0) >= lambda/(1+lambda) -> 1`. |
| Dirichlet-kernel pointwise lower bound | valid | On `[0,1/(8m)]`, every cosine is at least `1/sqrt(2)`, so the normalized sum is at least `sqrt(m/2)`. |
| Luxemburg modular estimate | valid | At scale `c(log m)^(alpha/2)`, the high-value interval contributes a constant proportional to `1/c^2`; choosing `c` small forces modular greater than one. |
| Conditioning an exchangeable law on cardinality | valid | Permutation invariance makes the conditional law uniform on each cardinality layer. |
| Monotonicity from `k_m` to larger cardinalities | valid | A uniform larger subset can be coupled to contain a uniform `k_m`-subset, and the synthesis norm is monotone under adding indices. |
| Relation to the source question | valid as partial only | The theorem covers all exchangeable randomized selectors, not arbitrary deterministic subsets. The packet states this limitation throughout. |

## Stress tests and rejected overclaims

- The proof does not claim that every target-size subset contains a consecutive block; that statement is false.
- The source's Bernoulli result is not repackaged as new. The new scope is fixed-cardinality sampling and, by conditioning, every exchangeable selector with the target minimum cardinality.
- The dimension subsequence is explicit and integral; it avoids the divisibility shorthand in the source's parameterization.
- No independence between block indicators is assumed. Only their proved negative correlation is used.
- The lower bound is a probability statement about a randomized selector. It cannot by itself establish a worst-case lower bound for the best deterministic subset.

## Artifact verification

- The source crop is a genuine render of page 13 and contains the full Theorem 2.10 / Remark 2.11 context and the sentence that optimality remains open.
- The packet cites the source paper and uses no unproved external theorem.
- No computational experiment is used as mathematical evidence.

Confidence: 91/100.

Recommended action: send to an analyst familiar with Lambda(p) selection and Orlicz norms, with particular attention to the exchangeability scope and the `B_m p_m` asymptotic.
