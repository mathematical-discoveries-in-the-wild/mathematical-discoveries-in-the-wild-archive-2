# Verification report

Verdict: `candidate_counterexample_likely_valid`.

## Formal proof audit

The proof has four independently checkable steps.

1. For unit vectors `u_i,v_i` and `A_i=u_i v_i^T`, one has
   `|A_i|=v_i v_i^T`.
2. The eigenvalues of `|A_1|+|A_2|` are `1+beta` and `1-beta`.
3. The squared singular values of `A_1+A_2` are
   `(1+alpha)(1+beta)` and `(1-alpha)(1-beta)`.  This follows because the
   left and right Gram matrices are simultaneously diagonalized by
   `(1,1)` and `(1,-1)`.
4. With `q=p/2<1` and `alpha=1-delta`, the change in the numerator's
   `p`-th power is at least

   ```text
   (1-beta)^q delta^q - q(1+beta)^q delta,
   ```

   which is strictly positive for the explicit sufficiently small `delta`
   chosen in the proof.

No external theorem or numerical lemma is used.

## Deterministic high-precision check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/\
2510.16846_rank_one_split_counterexample/code/verify_rank_one_split.py
```

Result: passed at 100 decimal digits for
`p=1.05,1.2,4/3,1.5,1.75,1.9`.  The separate rational-correlation
illustration `p=4/3`, `alpha=9/10`, `beta=13/20` gives

```text
actual   = 1.01791549015466577995682703563
proposed = 1.01375834364417921376942970795
gap      = 0.0041571465104865661874
```

This computation is corroboration, not part of the proof.

## Exploratory search

The seeded PyTorch optimizer searched arbitrary complex `2x2` and `3x3`
matrices.  For `p=1.2,m=n=2`, 40 restarts of 4,000 Adam steps all converged
to violations, with best ratio `1.00731398772` against proposed
`1.00247692996`.  The optimized matrices were numerically rank one and had
distinct left and right correlations, revealing the analytic two-parameter
family used in the proof.

The search is reproducible with `code/lee_cp_extremal_search.py`; it is not
needed for validity.

## Suggested reviewer focus

- Confirm that nonzero eigenvalues of `V G_U V^T` coincide with those of
  `G_U G_V`, including the rank-deficient endpoint `alpha=1` by continuity
  or direct calculation.
- Confirm the inequality
  `2^q-(2-delta)^q <= q delta` for `0<q<1`, `0<delta<1`.
- Confirm that the source formula at `m=2` equals the constructed ratio at
  `alpha=1` under `beta=(x-1)/(x+1)`.

