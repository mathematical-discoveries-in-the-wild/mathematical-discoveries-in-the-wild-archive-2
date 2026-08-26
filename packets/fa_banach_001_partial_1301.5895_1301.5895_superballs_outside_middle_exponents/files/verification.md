# Verification

## BCC cell reduction

The lattice is `Z^3 union (Z^3+h)`, `h=(1/2,1/2,1/2)`, of determinant
`1/2`. Modulo integer translations and coordinate reflections, every point is
represented by `z/2`, `z in [0,1]^3`. Its distance to the lattice is at most
the smaller of the distances to `0` and `h`.

One of `sum z_i` and `sum(1-z_i)` is at most `3/2`. A convex function attains
its maximum over `{0<=z_i<=1, sum z_i<=3/2}` at an extreme point, and those
extreme points give `sum z_i^p<=1+2^{-p}`. The point `(1,1/2,0)/2` is no
closer to any other point of either lattice coset, proving equality.

## Density monotonicity

After setting `t=1/p`, differentiating the logarithm of the explicit BCC
density reduces monotonicity to the scalar inequality `H(t)>=0` on
`1/2<=t<=1`. The proof uses `psi'(u)>1/u` and the calculus decomposition in
the packet. The included script evaluates `Q'` on 5,000 directed intervals
and certifies its positivity, the sign change of `Q` between `0.55` and
`0.56`, and positive lower bounds for all three regions used in the proof.

## Large exponents

The cubic lattice has covering radius `3^{1/p}/2`. Since `B_p^3` lies in the
cube of volume `8`, its covering density is at most `3^{3/p}`. For `p>=9`
this is at most `3^{1/3}<1.443`, while elementary rational lower bounds
`sqrt(5)>2.236` and `pi>3.1415` give
`5 sqrt(5) pi/24>1.4634`.

## Reproduction

Run:

```text
conda run --no-capture-output -n sandbox python code/verify_superball_ranges.py
```

Expected final line: `PASS`.

