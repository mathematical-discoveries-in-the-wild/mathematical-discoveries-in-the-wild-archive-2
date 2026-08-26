# Verification notes

## Claim audited

For compact star-shaped `S` in `R^d`, the source threshold

```text
k >= (d-1)(d-2)
```

can be replaced by the exact sufficient coefficient condition

```text
k >= d-1 and (k-d+2)(k+1)^(d-1) > k^d.
```

In particular, `k >= binom(d,2)-1` is sufficient. The equality
characterization from the source remains valid.

## Internal proof checks

1. **Range of the source transport estimate.** Before its final scalar
   positivity bound, the proof of source Lemma 2 uses cubical layers indexed
   from `t=k-d+1` through `k-1`. Thus `k>=d-1` makes every index nonnegative.
   The endpoint `k=d-1` starts with `t=0`, where the stars-and-bars count is
   `N_d(0)=1`; all identities remain valid. No earlier line uses
   `k>=(d-1)(d-2)`.

2. **Exact affine coefficient.** Source equation (10) is

   ```text
   new_volume >= alpha * old_volume + (1-alpha) * V,
   alpha = k^d / ((k-d+2)(k+1)^(d-1)),
   V = vol(conv B).
   ```

   Since `old_volume<=V`, the desired inequality and its rigidity follow
   whenever `alpha<1`, exactly the stated polynomial condition.

3. **Stability needed for global equality.** The same affine inequality gives
   `V-old_volume <= delta/(1-alpha)`. After rescaling, this is precisely the
   local deficit estimate used when summing the simplicial cones.

4. **Global passage.** The source's finite-polytope approximation,
   boundary triangulation, and summation use only the local monotonicity and
   stability conclusions. Replacing the scalar range does not change any
   geometric step.

5. **Closed-form threshold.** With `x=k+1` and `t=1/x`, coefficient positivity
   is `(1-t)^d < 1-(d-1)t`. Taylor's theorem gives the strict upper bound
   `(1-t)^d < 1-dt+binom(d,2)t^2`; if `x>=binom(d,2)`, the last expression is
   at most `1-(d-1)t`.

6. **Equality converse.** If `S[k]/k=conv(S)`, its volume is already maximal.
   The proved monotonicity and the universal containment
   `S[k+1]/(k+1) subset conv(S)` force equality of the consecutive volumes.

## Computational check

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1910.06146_half_quadratic_star_minkowski_threshold/code/verify_thresholds.py
```

The script uses exact integers. It verifies the displayed exact cutoffs for
dimensions 3 through 12, strict positivity of the clean threshold for all
dimensions 3 through 1000, and the algebraic equivalence of the two scalar
forms through dimension 200. These checks do not replace the analytic proof.

## Literature and duplicate check

The cheap run indexes contained no packet or attempt for arXiv:1910.06146 or
this threshold refinement. Focused arXiv searches on 2026-08-09 used:

- the exact source title;
- the scalar phrase `(k-d+2) (k+1)` with Minkowski sums;
- `star-shaped Minkowski sum volume monotonicity threshold`;
- searches for later work citing or refining arXiv:1910.06146.

The searches found the source paper, the earlier counterexample paper
arXiv:1512.03718, and broader subset-sum literature, but no later paper stating
the exact coefficient refinement or the half-quadratic bound. This is a
bounded novelty check, not an exhaustive priority claim.

## Human-review recommendation

Candidate substantial partial, likely valid. The priority check is the range
audit for source equation (10): verify independently that all cubical-layer
identities before the final scalar estimate remain valid at `k=d-1`, including
the `t=0` boundary layer. The remaining algebra is elementary and exact.

## Limitation

This method gives no conclusion below the exact coefficient cutoff. It leaves,
for example, `k=2,3,4` open in dimension 4 and `k=2,...,7` open in dimension 5.
It is not a full solution of the BMW conjecture.
