# Verification record

## Statement audited

For `kappa>=3`, identify `x` with a `kappa`-by-`n` matrix `X` whose columns
are its blocks.  If `rank(X)=r`, then

```text
dim span{sigma X : sigma in SO(kappa)} = kappa*r.
```

In particular, `kappa=3`, `n=2`, and `X=[e_1 e_2]` contradict source
Lemma 1: the span dimension is 6 rather than 3.

## Exact checks

1. The six matrices in `verify_counterexample.py` have integer entries,
   determinant one, and orthonormal columns, hence lie in `SO(3)`.
2. Their orbit vectors `(sigma e_1, sigma e_2)` form a `6`-by-`6` matrix of
   exact rank six.
3. Pairwise sums and differences give explicitly
   `(e_i,0)` and `(0,e_i)` for `i=1,2,3`.
4. For the general formula, the even-sign diagonal subgroup of `SO(kappa)`
   spans every diagonal matrix when `kappa>=3`.  Left multiplication by
   rotations then shows every matrix unit lies in `span SO(kappa)`.
5. Therefore the orbit span is `{AX:A in M_kappa(R)}`.  Its rows are exactly
   arbitrary elements of the `r`-dimensional row space of `X`, independently
   in each of `kappa` rows, giving dimension `kappa*r`.

## Propagation check

For the concrete rank-two example, the source's `H_x^perp` is all of `R^6`
and `H_x={0}`, rather than two complementary 3-planes.  The following
definition and parallel-section arguments explicitly require the claimed
fixed dimensions.  The defect is therefore structural, not a harmless error
in the orbit's parametrization.

No assertion is made that the independent `L_{-p}` embedding statement is
false; only its printed proof route is affected.

## Novelty check

- Cheap run indexes: no result for arXiv:1307.3206 or this orbit lemma.
- Exact-source and exact-lemma searches: only the source paper.
- Searches combining the title with `correction`, `erratum`, `SO(kappa)
  orbit`, and `kappa-balanced`: no correction located.

This was a bounded search, not exhaustive bibliographic certification.

