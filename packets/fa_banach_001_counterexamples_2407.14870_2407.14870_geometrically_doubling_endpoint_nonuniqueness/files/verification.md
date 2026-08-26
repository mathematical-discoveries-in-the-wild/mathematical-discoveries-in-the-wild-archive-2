# Verification report

## Verdict

`candidate_counterexample_likely_valid`

The proof reduces to elementary estimates for two atomic distributions and a
standard Johnson--Schechtman/Rosenthal disjointification theorem. No unproved
lemma or computational dependency remains.

## Adversarial mathematical audit

### 1. Probability and integrability

For the lower family, the p-th moment is `sum 1/w_k`, finite because
`w_(k+1) >= lambda w_k` with `lambda > 1`. For the upper family it is
`sum w_k exp(-(2-p)2^k)`, finite because `w_k` grows at most geometrically
while the exponential factor decays doubly exponentially in `k`. All four
mass sums are smaller still. Adding the unused mass at zero makes probability
laws, and an independent Rademacher sign makes them symmetric and mean zero.

### 2. Modular split

At `s=log(1/t)` and `2^m <= s < 2^(m+1)`, atoms through index `m` lie below
`1/t` and contribute quadratically; later atoms contribute with exponent p.
This gives exactly the two displayed sums in the proof, up to the fixed
comparison `N_p(u) ~ min(u^p,u^2)`.

For the lower family, `sum_(k>m) 1/w_k ~ 1/W(s)` is the two-sided main term;
the quadratic head is bounded by its final summand. For the upper family,
`sum_(k<=m) w_k ~ W(s)` is the two-sided main term; the p-tail is bounded by
its first summand. The odd grid changes the logarithmic ratio from two to four,
and hence changes `(lambda,Lambda)` only to `(lambda^2,Lambda^2)`.

### 3. Sequence-space identification

For disjoint copies, the Luxemburg modular is exactly
`sum_k M_Z(|a_k|/rho)`. The standard disjointification estimate identifies
this with the norm of iid mean-zero copies in `L_p`. Equivalence of the two
modulars near zero is sufficient for equivalence of the canonical Orlicz
bases. The actual modulars are p-convex, 2-concave Orlicz functions.

### 4. Robust tail separation

Given fixed `C`, choose `tau=A_(2j+2)/(2C)`. For large `j`, both `tau` and
`C tau` lie in `(A_(2j+1),A_(2j+2))`. The full tail contains its
`A_(2j+2)` atom; the odd tail starts at `A_(2j+3)`. Subsequent odd atoms form
a rapidly decreasing tail. The decisive mass ratio is at least a constant
times `exp(p 2^(2j+2))` in the lower family and `exp(2 2^(2j+2))` in the
upper family. Therefore the limsup is infinite for every fixed `C`, which is
strictly stronger than failure of pointwise tail comparability.

### 5. Printed-theorem conflict

With `W(s)=s`, the upper modular is `t^2 log(e/t)`. Thus the coefficient norm
condition in Braverman's Theorem 4.2 holds. Taking `x_j=2A_j` shows that the
tail divided by `x_j^-2` tends to zero, so the theorem's pointwise tail
condition with `h=1` at infinity fails. A harmless modification of `h` near
zero makes the defining integral finite there without changing the small-t
asymptotic of `Psi_2`.

## Computational regression check

Command:

```bash
conda run --no-capture-output -n sandbox python code/check_endpoint_examples.py
```

Scope: 3 values of `p`, 3 `(alpha,beta)` weights, 2 endpoint constructions,
2 grids, and 37 logarithmic thresholds, for 1332 modular ratios. All ratios
were finite and bounded. The printed log10 tail-separation lower bounds grow
from 36.4 to 9250.4 in the lower case and from 55.3 to 14230.7 in the upper
case. This is diagnostic evidence only; the proof is symbolic.

## Novelty and duplicate audit

Search date: 2026-08-11.

Searched:

- all run registry, solution, attempt, and ledger indexes;
- arXiv/full-source corpus for 2407.14870 and 1406.4950;
- exact 1993 paper title and Theorem 4.2;
- `t^2 log(1/t)`, independent copies, Orlicz, unique distribution,
  quasi-equivalent, lacunary, and staircase combinations;
- Astashkin--Sukochev--Zanin (2015), Astashkin (2024 source), and
  Astashkin's 2024 Russian Mathematical Surveys article.

No correction or matching upper-endpoint counterexample was found. The 2024
survey still repeats the uniqueness claim. The run contains a distinct
1406.4950 staircase packet, but that packet explicitly stops at pointwise
same-quantile inequivalence and does not prove invariance under tail/quantile
rescaling. The present full/odd construction proves the stronger published
quasi-equivalence separation.

## Remaining reviewer risks

- Confirm the exact conventions for `Psi_2` and distribution tails in the
  scanned 1993 paper; the packet uses the formulas as printed.
- Search non-arXiv probability literature and possible errata not indexed by
  title search.
- The result does not settle the complete necessary-and-sufficient
  characterization asked in the current source.
