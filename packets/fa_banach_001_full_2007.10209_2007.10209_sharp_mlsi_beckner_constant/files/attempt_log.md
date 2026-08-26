# Attempt log

1. **Normalization audit.** Extracted Assumption 1, mLSI, Beckner-p, and the
   authors' factor conventions from the source. Confirmed that the question is
   universal over the abstract comparison-form setting, not just diffusions.
2. **Direct scalar-energy comparison.** Tried to compare
   `(a^p-b^p)(log a-log b)` directly with
   `(a-b)(a^(p-1)-b^(p-1))`. The ratio is unbounded for separated values, so
   this route cannot give a uniform sharp implication.
3. **Two-point extremizers.** Reduced biased two-point chains to one-variable
   variational formulas. Numerical exploration indicated ratio at least 1/2;
   the symmetric chain was then proved exactly to have optimal constants
   `rho_0=8 gamma` and `alpha_p=4 gamma`. This established the sharp upper
   bound `K_p^opt <= 1/2` for every p.
4. **Higher-state counterexample search.** Optimized the two functional
   constants numerically on random weighted three- and four-state reversible
   graphs. Robust re-optimization removed apparent sub-1/2 artifacts and found
   no counterexample. This was diagnostic only and is not used in the proof.
5. **Entropy-decay reformulation.** Recast the desired inequality as equal-rate
   decay of the power entropy under mLSI. This exposed the need for a positive
   representation of power entropy in terms of logarithmic entropy.
6. **Deep upgrade: Stieltjes mixture.** Used
   `integral_0^infty s^(p-2)/(x+s) ds` to represent `x^p` modulo affine terms
   as a positive mixture of `(x+s) log(x+s)`. Applying mLSI to every shift and
   integrating produced exactly `rho_0 H_p <= p E(f,f^(p-1))`, i.e.
   `alpha_p >= rho_0/2`.
7. **Abstract-domain audit.** Replaced a potentially invalid interchange of
   the abstract bilinear form with an integral by positive Riemann sums,
   uniform derivative comparison on the bounded range, and Assumption 1. The
   full-kernel pointwise bound then passes to the limit without closedness or
   continuity assumptions on the form.
8. **Endpoint and sharpness audit.** Treated p=2 by linearizing mLSI, checked
   the source's bounded-to-unbounded truncation lemma, and proved equality of
   the two-point optimal constants by power series and near-constant tests.

Outcome: candidate full proof, likely valid, pending human review.
