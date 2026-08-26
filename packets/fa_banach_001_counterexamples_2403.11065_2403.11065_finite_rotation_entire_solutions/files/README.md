# Finite elliptic groups give rational solutions beyond the unit disk

Status: `candidate_counterexample_likely_valid_full_negative_answer_as_stated`.

Source: Petr Kosenko, *On a complex-analytic approach to stationary measures
on S^1 with respect to the action of PSU(1,1)*, arXiv:2403.11065, Section 6.
The first open question asks whether every solution of the holomorphic
stationarity equation for finitely supported `mu` has radius of convergence
exactly 1.  It also proposes that rational solutions should occur only when
`mu` is supported on a single element.

## Counterexample

Let `h(z)=(z+1/2)/(1+z/2)`, let `omega` be a primitive cube root of unity, and
put

```text
gamma_j = h compose (z -> omega^j z) compose h^{-1},  j=1,2,
mu      = (delta_{gamma_1}+delta_{gamma_2})/2.
```

Both support maps move the origin.  If `m` is normalized Lebesgue measure on
the unit circle, then `nu=h_*m` is invariant under both maps and hence is
`mu`-stationary.  Its Cauchy transform is

```text
f_nu(z) = 1/(2-z).
```

Indeed, the circle moments of `h_*m` are `(1/2)^k`, by the mean-value
property.  The source's stationarity theorem therefore makes `f_nu` a
solution of its equation (13).  This solution is nonzero and rational, its
Taylor series has radius 2, and `mu` has two-point support.

Thus both literal assertions fail, even after imposing the paper's earlier
condition that some support element move the origin.  The example generates a
finite elliptic group; it does not answer a strengthened version in which the
support must generate a non-elementary group or a lattice.

Run the exact symbolic check with:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2403.11065_finite_rotation_entire_solutions/code/verify_counterexample.py
```

The packet PDF is `solution_packet.pdf`.

