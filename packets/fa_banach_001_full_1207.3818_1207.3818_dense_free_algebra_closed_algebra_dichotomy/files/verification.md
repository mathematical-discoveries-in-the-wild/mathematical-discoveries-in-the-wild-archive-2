# Verification report

Result: **candidate full answer in intended setting; no proof gap found in the
bounded audit**.

## Dense-algebra audit

- The source partition has pairwise disjoint `B_j`, positive intersection
  with every nonempty open set, and `mu(B_j)<=1/j!`.
- `g_theta=sum theta^j chi_(B_j)` belongs to every finite `Lq`; factorial
  decay beats any fixed exponential.
- `L-infinity intersect Lp` is dense in `Lp` by truncation for every `p>0`.
- Repeating each dense bounded function with perturbation norm tending to zero
  makes the generator set itself dense.
- Rational independence of the logarithms makes distinct monomial rates
  distinct. The maximal original monomial supplies the only occurrence of the
  maximal expanded rate; all bounded-perturbation terms have strictly smaller
  rates.
- Off the union of `B_j`, a polynomial without constant term in bounded `Lp`
  functions remains in `Lp`; this avoids any finite-measure assumption on
  `X`.
- The proof uses only finite sums and the `p`th-power integral, so no convexity
  is hidden when `0<p<1`.

## Closed-algebra audit

- `E_m={g:||fg||p<=m}` is closed: take an almost-everywhere convergent
  subsequence and apply Fatou.
- A closed subalgebra of `Lp` is a complete metrizable vector space for all
  `p>0`, so Baire applies in the quasi-Banach range.
- Subtracting the two bounded products inside a Baire ball uses the ordinary
  triangle inequality for `p>=1` and the `p`-triangle inequality for `p<1`.
- Homogeneity yields a global multiplier bound on the closed algebra.
- Iterating the multiplier bound gives uniform control of `||f||_(np)`.
- A positive-measure level set `{|f|>t}` has finite measure because `f in Lp`;
  its lower moment bound contradicts the uniform estimate whenever `t` exceeds
  the multiplier constant.

## Computational sanity check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1207.3818_dense_free_algebra_closed_algebra_dichotomy/code/check_dominance.py
```

The script checks 2,000 deterministic finite polynomial/perturbation cases,
verifies eventual domination by the predicted unique maximal exponential
rate, and checks factorial weighted `p`-sum convergence for representative
values on both sides of `p=1`. It is not used as proof.

## Novelty bounds

Searched on 11 August 2026: the four run indexes, the local parsed arXiv
corpus, and current arXiv-domain results for the exact problem and close core
phrases. Only the source and its predecessor arXiv:1204.6404 were found; both
state the dense/closed algebra issue as open. The search is bounded rather
than exhaustive.
