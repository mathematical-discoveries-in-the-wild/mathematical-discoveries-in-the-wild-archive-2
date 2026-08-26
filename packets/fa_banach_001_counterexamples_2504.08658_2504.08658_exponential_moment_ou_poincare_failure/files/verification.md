# Verification record

## Mathematical audit

- `a_k=2^k` and `p_k=Z^{-1}e^{-a_k}` define a probability distribution.
- Symmetric mixing of `N(+a_k,1)` and `N(-a_k,1)` makes the measure centered.
- For every `0<theta<1`, the exponential moment is finite by
  `E exp(theta|Z+/-a_k|) <= E exp(theta|Z|) exp(theta a_k)`.
- The mixture-density Fisher bound
  `(sum q_i g_i')^2/(sum q_i g_i) <= sum q_i (g_i')^2/g_i`
  yields `I(mu|gamma)<=sum p_k a_k^2<infinity`; hence `sqrt(f)` lies in
  `H^1(gamma)`.
- Mehler's formula sends the relative density of `N(m,1)` to that of
  `N(e^{-t}m,1)`, so the evolved measure is explicit.
- The compact cutoff around the `k`th positive well has variance at least
  `p_k/16` for all large `k`.
- Both transition strips are at least `e^{-t}2^{k-2}` from every component
  mean.  Standard Gaussian tail bounds give Dirichlet energy at most
  `C exp(-(e^{-t}2^{k-2}-1)^2/2)`.
- Dividing by `p_k` gives a Rayleigh quotient tending to zero for every fixed
  finite `t`.  This is exactly the negation of the source's Poincare property.
- Lipschitz compactly supported cutoffs may be smoothed without changing the
  estimates, matching the source's `C_c^infinity` test class.

## Source audit

The question persists in the current arXiv PDF created 14 November 2025:
Section 3.2.2, PDF page 17.  The page and focused crop were visually checked.

## Bounded novelty search

Checked through 2026-08-11:

- all cheap run indexes, attempts, and the registry;
- arXiv:2504.08658v2 and DOI `10.1007/s44007-025-00180-y`;
- exact question phrases and combinations of OU flow, finite exponential
  moment, Gaussian convolution, Gaussian mixtures, bottlenecks, and Poincare
  inequality.

No later answer or the explicit construction was found.  Novelty confidence
is moderate; bounded search is not a proof of priority.

## Human review focus

Check the transition-strip Gaussian bound and confirm that the source's
finite-time property means membership in its class `V`, i.e. a positive
Poincare constant for `|w(t)|^2 gamma`.  Both identifications appear direct.

Verdict: `candidate_full_counterexample`.

