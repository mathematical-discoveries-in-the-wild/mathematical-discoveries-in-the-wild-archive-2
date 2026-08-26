# Sharp negative-moment inequality in the large-coefficient regime

Status: `candidate_partial_likely_valid`.

Source: Giorgos Chasapis, Salil Singh, and Tomasz Tkocz, *Haagerup's
phase transition at polydisc slicing*, arXiv:2206.01026.

## Result

Let `xi_k` be independent and uniform on the unit sphere in `R^d`, let
`d >= 2`, and put `q=-p` with `d-2 < p < d-1`. The conjectured sharp
two-summand Khinchin inequality

```text
|| sum_k a_k xi_k ||_q >= c_{d,2}(q) (sum_k a_k^2)^(1/2)
```

holds whenever

```text
max_k a_k^2 >= (1/2) sum_k a_k^2.
```

Equality occurs only for two nonzero coefficients of equal magnitude, up to
signs and permutation.

This covers the complete large-coefficient region in both low-dimensional
open strips singled out by the source: `d=2, -1<q<0` and
`d=3, -2<q<-1`. It also applies in every dimension throughout the last
negative-moment strip `-(d-1)<q<-(d-2)`.

## Mechanism

The source's hypergeometric expansion implies that the spherical Riesz
potential

```text
U(r) = E |r e_1 + xi|^(-p)
```

is strictly increasing up to `r=1` and strictly decreasing thereafter. After
conditioning on the sum of all but the largest summand, the whole moment is
therefore bounded by the value at the two-equal-summand configuration.

## Remaining scope

The all-small regime `max a_k^2 < (1/2) sum a_k^2` remains open. A deep
upgrade attempt derives an explicit scalar inequality that would settle the
three-summand `d=3` case, and a second reduction isolates weighted sharp
Ball-type Bessel integral inequalities for arbitrary all-small vectors. These
last inequalities are not proved and are not part of the promoted claim.

The script in `code/check_upgrade_reduction.py` checks the derived
three-summand scalar inequality on finite grids and audits its proved endpoint;
these computations are evidence only and are not used in the theorem.

Packet PDF: `solution_packet.pdf`.
