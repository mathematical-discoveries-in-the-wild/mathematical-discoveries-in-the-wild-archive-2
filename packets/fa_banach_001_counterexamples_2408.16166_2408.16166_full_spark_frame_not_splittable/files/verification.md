# Verification report

Verdict: **candidate full counterexample, likely valid**.

## Structural checks

1. Every column is a rational Euclidean unit vector.
2. All three `2 x 2` minors are nonzero, hence the frame is full spark.
3. The atomic unit ball is the centrally symmetric hexagon with vertices
   `+/-a,+/-b,+/-c`. Each of the three stated covectors has absolute value at
   most one on all atoms and equals one on the corresponding facet endpoints.
   This proves the max formula for the norm.
4. The line-distance formulas follow from annihilating covectors. Their dual
   norms are attained at unique opposite atom pairs, so equality forces the
   residual onto a unique atom line. The strict distance comparisons then
   prove uniqueness of every best approximant used.

## Witness 1

For `x=(-4/5,3/5)` the line distances are

```text
(d_a,d_b,d_c)=(39/40,5/8,40/209).
```

For `y=(7/15,-8/15)` they are

```text
(d_a,d_b,d_c)=(28/45,5/9,65/1881).
```

Thus both best lines are uniquely the `c`-line. The exact decompositions are

```text
x_1=(-156/209,819/1045)=(-1131/1045)c,
x-x_1=(40/209)a,
y_1=(896/1881,-1568/3135)=(6496/9405)c,
y-y_1=(65/1881)a.
```

Substitution gives `L_1=-391/13167`, `D_1=-295/1881`, and forces
`beta>=391/2065`.

## Witness 2

For `x'=b`, the zero residual makes the unique best point `x'_1=b`. For
`y'=(-3/10,-1/5)`,

```text
(d_a,d_b,d_c)=(29/120,5/24,515/1254),
y'_1=(-29/120,0)=(-29/120)b,
y'-y'_1=(5/24)a.
```

Thus the best point is again unique. Substitution gives `L_2=23/840`,
`D_2=5/24`, and forces `beta<=23/175`.

## Independence from computation

`computations/verify_exact.py` reproduces every rational identity with
`fractions.Fraction`. It is an audit aid, not a premise of the proof.
