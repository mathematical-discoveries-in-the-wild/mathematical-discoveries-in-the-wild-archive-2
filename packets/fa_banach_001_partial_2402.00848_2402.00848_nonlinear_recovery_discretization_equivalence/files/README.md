# Nonlinear recovery is equivalent to one-sided discretization

**Status:** strong partial result, likely valid; human review requested.

For every `1 <= p < infinity`, every dimension `N`, and every sample budget
`m`, the worst-case constant in nonlinear sampling recovery relative to the
`N`th Kolmogorov width in `L_infinity` is equivalent, up to explicit affine
constants, to the worst-case one-sided `L_p`-to-sampled-`L_infinity`
discretization constant:

```text
D_{m,p}(N) - 1 <= R^*_{m,p}(N) <= 2 D_{m,p}(N) + 1.
```

The upper bound is the mechanism of Theorem 5.2 in the source. The new reverse
bound uses the compact class formed from the `L_p` unit ball of a hard
subspace plus pointwise radial clips of that ball. For any chosen sample set,
one clip cancels all observed values of a poorly sampled unit vector; the two
opposite functions then have identical data.

Consequently, Open Problems 3.1 and 5.1 of arXiv:2402.00848 are the same
universal problem up to constants. This does not determine the optimal growth
of `m(N)` and does not give the missing upper bound for linear recovery in Open
Problem 5.2. Eight focused attempts at those upgrades are recorded in the
associated attempt note.

Verification:

```sh
conda run --no-capture-output -n sandbox python code/verify_finite_obstruction.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

