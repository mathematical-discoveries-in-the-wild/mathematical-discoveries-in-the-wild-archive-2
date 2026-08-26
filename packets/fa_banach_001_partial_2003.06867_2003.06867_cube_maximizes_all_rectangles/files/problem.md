# Exact source problem and scope

Source: Rodrigo Bañuelos, Phanuel Mariano, and Jing Wang, *Bounds for exit
times of Brownian motion and the first Dirichlet eigenvalue for the
Laplacian*, arXiv:2003.06867, Remark 5.5 and equations (5.22)--(5.23), printed
pages 19--20.

Let

```text
R_a={x in R^d: |x_k|<a_k for k=1,...,d},   a_k>0,
Q_d=(-1,1)^d.
```

For standard Brownian motion started at zero, with exit time `tau_D`, the
source asks to prove, for every `p>0`,

```text
lambda_1(R_a)^p E_0[tau_{R_a}^p]
    <= lambda_1(Q_d)^p E_0[tau_{Q_d}^p].            (5.22)
```

It states equality only for `R_a=Q_d` after using scale invariance to normalize
the side lengths (the source subsequently assumes `a_1=1`).  Without that
normalization, the correct equality class is all homothetic cubes.

The source says that it could not verify (5.22) for all rectangles even for
`d=2`, `p=1`.  This packet proves (5.22) for every `d>=2` and `p>0`, with a
strict equality characterization and a stronger stochastic-order statement.

The parent Conjecture 5.4 ranges over all bounded convex domains symmetric in
every coordinate axis.  That broader conjecture remains outside the scope of
this packet.
