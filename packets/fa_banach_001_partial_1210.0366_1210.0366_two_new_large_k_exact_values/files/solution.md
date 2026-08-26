# Proof companion

Let `m=k+2`. From any `m` unit vectors satisfying the `k`-collapsing
condition, choose a norming functional for each vector. Their evaluations form
an `m x m` real matrix `A` of rank at most `d`, with diagonal entries one and
each row a scalar `k`-collapsing family.

For a scalar row, distinguish its diagonal entry `1` and sort the remaining
entries `x_1>=...>=x_{m-1}`. When `k=m-2`, the subset inequalities reduce to

```text
x_1+...+x_{m-3} <= 0,
x_2+...+x_{m-1} >= -1.
```

The feasible set is a simplex-like polytope. A convex quadratic reaches its
maximum at a vertex. Apart from the two all-equal vertices and the last
degenerate vertex, a vertex has `t` entries equal to

```text
a_t=(m-3-t)/(t+m-3)
```

and `m-1-t` entries equal to

```text
b_t=-t/(t+m-3).
```

Its off-diagonal square sum is

```text
q_m(t)=t*((m-3)^2-(m-5)t)/(t+m-3)^2.
```

This is unimodal, with real maximizer `(m-3)^2/(3m-13)`.

For `m=18`, the exact integer maximum is `2`, attained only at `t=5,6`.
Thus every row has square norm at most `3`. The trace-Frobenius rank inequality
gives `rank(A)>=18^2/(18*3)=6`. In dimension six equality must hold. Hence
`A` is symmetric and all its nonzero eigenvalues equal `18/6=3`.

The two equality row types have off-diagonal values and row sums

```text
t=5:  five 1/2, twelve -1/4; row sum 1/2,
t=6:  six 3/7, eleven -2/7; row sum 3/7.
```

Symmetry forbids mixing the types because their two sets of off-diagonal
values are disjoint. Thus the all-ones vector is an eigenvector with eigenvalue
`1/2` or `3/7`, contradicting that every nonzero eigenvalue is `3`.

For `m=42`, the exact integer maximum is `5`, attained only at `t=13`.
Every row has square norm at most `6`, so `rank(A)>=42^2/(42*6)=7`.
In dimension seven equality makes `A` symmetric with nonzero eigenvalue `6`.
The unique equality row has thirteen entries `1/2`, twenty-eight entries
`-1/4`, and row sum `1/2`, again a contradiction.

Therefore no 16-collapsing family of 18 unit vectors exists in dimension six,
and no 40-collapsing family of 42 unit vectors exists in dimension seven. The
standard balanced family of `k+1` unit vectors gives the reverse inequalities.
