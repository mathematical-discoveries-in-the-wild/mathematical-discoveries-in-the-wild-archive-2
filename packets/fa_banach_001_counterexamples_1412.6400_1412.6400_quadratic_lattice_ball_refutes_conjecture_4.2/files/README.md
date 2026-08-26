# Lattice-ball counterexamples to Conjecture 4.2

**Status:** candidate full counterexample to Conjecture 4.2 in
arXiv:1412.6400 as printed, subject to human review.

The conjecture says that if

```text
K(t) = {k in Z^d : |P(k)| <= t}
```

is finite for every `t`, then

```text
card K(t) asymp t^(alpha/beta) (log t)^nu
```

for integers satisfying `0<alpha<=beta` and `0<=nu<d`. Thus the permitted
power exponent is at most one.

## Proof intuition

Take a coercive even polynomial whose sublevel sets are ordinary
full-dimensional lattice balls. For even `m>=2` and `d>m`, set

```text
P_{d,m}(x) = 1 + x_1^m + ... + x_d^m.
```

Its `t`-sublevel set is the lattice `ell_m` ball of radius
`R=(t-1)^(1/m)`. It lies between two coordinate cubes of side comparable
to `R`, so

```text
card K(t) asymp R^d asymp t^(d/m).
```

Since `d/m>1`, no allowed power `alpha/beta<=1`, even multiplied by an
allowed logarithmic factor, can be comparable to this count.

The smallest simple example is

```text
P(x_1,x_2,x_3) = 1 + x_1^2 + x_2^2 + x_3^2,
card K(t) asymp t^(3/2).
```

## Scope and interpretation

This refutes Conjecture 4.2 exactly as printed in both the arXiv and the
authors' published-version PDF. It does not refute the natural corrected
statement obtained by dropping `alpha<=beta`: the family then fits the
formula with `alpha=d`, `beta=m`, and `nu=0`.

A bounded literature search through 2026-08-09 found no erratum, correction,
or later paper recording this counterexample. The likely issue is a persistent
typographical restriction, but that intent requires human confirmation.

No computation or external theorem is used. The proof consists of two cube
inclusions and elementary lattice-point counts.

Files:

- `solution_packet.pdf`: compiled counterexample and audit note.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: Conjecture 4.2 on source PDF page 19.
- `main.tex`: packet source.

Ledger:
`runs/fa_banach_001/ledger/results/1412.6400_quadratic_lattice_ball_refutes_conjecture_4.2.json`.
