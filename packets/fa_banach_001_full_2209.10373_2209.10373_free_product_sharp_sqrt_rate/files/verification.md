# Verification audit

Status: `candidate_full_solution_likely_valid`

## Definition and orientation checks

- With `R_x e_w=e_{wx}` and `R_y e_w=e_{wy}`, the operator
  `A=(I-R_y)(I-R_x)` satisfies
  `A e_w=e_w-e_{wx}-e_{wy}+e_{wxy}`.  This is exactly right multiplication
  by `(1-x)(1-y)`.
- Therefore `(A^*h)_w=h_w-h_{wx}-h_{wy}+h_{wxy}`.  Orthogonality to
  `A H_n` imposes precisely these relations for `|w|<=n`.
- Constraints through depth `n` use coordinates only through depth `n+2`;
  zeroing deeper coordinates is norm-decreasing and preserves feasibility.

## Tree recursion checks

- At a root with values `(a,b,c,d)` at `(w,wx,wy,wxy)`, feasibility is
  `d=b+c-a`.
- The `x`-subtree and `y`-subtree are disjoint.  Within the `x`-subtree,
  `d` is the `y`-child of `b`, which gives the state
  `F_{m-1}(b,b+c-a)`.
- Completing the square in
  `F_{m-1}(b,b+s)` gives
  `det(Q)/(Q_11+2Q_12+Q_22) * |s|^2`.
- Substituting the resulting matrix `Q_m` gives both scalar recurrences in
  the theorem with base values `e_{-1}=1`, `kappa_{-1}=1/2`.

## Independent computation

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2209.10373_free_product_sharp_sqrt_rate/code/verify_recurrence.py \
  --exact-through 4 --asymptotic-n 100000
```

The checker builds the primal least-squares Gram matrix over exact rational
arithmetic.  It compares its residual with `1/e_n`; this is independent of
the dual tree elimination used in the proof.  The expected exact matches are

```text
n=0: 3/4
n=1: 7/11
n=2: 14/25
n=3: 56/111
n=4: 322/697
```

At `n=100000`, the long-run floating-point check returned
`sqrt(n)c_n=1.0023431484`.  Numerical output is corroborative and is not used
by the proof.

## Asymptotic proof checks

- The positive fixed point of `u -> 1+ku/(k+u)` is the root of `u^2-u=k`.
- The invariant `e_n<=r(kappa_n)` makes `e_n` monotone and yields the upper
  square-root bound.
- The elementary induction `e_n>=sqrt(kappa_n)/2` proves divergence and the
  lower square-root bound.
- At the relative boundary `(1-epsilon)r`, the update has a positive limiting
  size `epsilon(2-epsilon)`, while the boundary moves by `O(1/r)`.  This
  justifies the trapping step and yields `e_n/r(kappa_n)->1`.
- Since `e_n->infinity`, the increments of `kappa_n` tend to one, hence
  `kappa_n/n->1` by Cesaro convergence.

## Remaining human-review focus

The candidate proof is self-contained and has no conditional external lemma.
The recommended review focus is the two-state subtree decomposition and the
eventual-invariance step in the moving-boundary asymptotic argument.
