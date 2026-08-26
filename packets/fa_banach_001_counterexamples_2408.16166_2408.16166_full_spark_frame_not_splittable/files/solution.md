# Exact counterexample

Put

```text
a=(-7/25,-24/25), b=(1,0), c=(20/29,-21/29).
```

All three vectors have Euclidean norm one. Moreover

```text
det(a,b)=24/25, det(a,c)=627/725, det(b,c)=-21/29,
```

so the frame is full spark.

Its atomic unit ball is `conv{+/-a,+/-b,+/-c}`. The three pairs of opposite
facets give

```text
N(z1,z2) = max(
  | z1 + 3 z2/4 |,
  | -3 z1/11 + 37 z2/33 |,
  | -z1 + 3 z2/7 |
).
```

The exact distances to the three atom lines are

```text
d_a(z)=|24 z1-7 z2|/24,
d_b(z)=25|z2|/24,
d_c(z)=25|21 z1+20 z2|/627.
```

The dual maximizer in each formula is a unique opposite pair of atoms. Hence
whenever one of the displayed distances is strictly smallest, the best atom
line and the best point on it are unique.

For

```text
x=(-4/5,3/5), y=(7/15,-8/15),
```

the unique best one-term approximants lie on the `c`-line and satisfy

```text
||x_1||=1131/1045,       ||x-x_1||=40/209,
||y_1||=6496/9405,       ||y-y_1||=65/1881,
||x+y||=38/105.
```

Thus the splitting inequality is

```text
-391/13167 >= beta (-295/1881),
```

and therefore `beta >= 391/2065`.

For the second pair

```text
x'=b=(1,0), y'=(-3/10,-1/5),
```

the unique best one-term approximants lie on the `b`-line and

```text
||x'_1||=1,              ||x'-x'_1||=0,
||y'_1||=29/120,         ||y'-y'_1||=5/24,
||x'+y'||=11/14.
```

The splitting inequality now implies

```text
23/840 >= beta (5/24),
```

so `beta <= 23/175`. Since

```text
391/2065 - 23/175 = 598/10325 > 0,
```

no real constant, and in particular no positive constant, satisfies both
necessary inequalities. The frame is not 1-splittable.
