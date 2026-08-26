# Literature answer

The direct follow-up arXiv:1907.06122 proves that the optimal normalized
Hermite--Hadamard constants satisfy

`A_n >= max(n-1,1)`.

Its lower-bound construction uses positive convex functions, so it applies to
the class in the source question.  In particular, `sup_n A_n` is infinite and
the dimension-free version of inequality (1) is false.

For the scale-invariant constants, Proposition 1 of the follow-up states that
on a fixed convex domain the optimal constant for positive subharmonic
functions is the maximum inward normal derivative of the torsion function.
This turns the ellipsoid discussion in the source into a certified lower
bound.

Let

`E_n={x: x_1^2/4 + sum_{j=2}^n x_j^2/(2n-2) < 1}`

and

`q_n(x)=1-x_1^2/4-sum_{j=2}^n x_j^2/(2n-2)`.

The source calls `q_n` the torsion function, but direct differentiation gives
`-Delta q_n=3/2`.  Thus the torsion function normalized by `-Delta u_n=1` is
`u_n=(2/3)q_n`.  At `(2,0,...,0)` its inward normal derivative is `2/3`, while

`|E_n|^(1/n) = [omega_n 2(2n-2)^((n-1)/2)]^(1/n) -> 2 sqrt(pi e)`.

Consequently

`liminf B_n >= 1/(3 sqrt(pi e)) > 0`.

Thus the optimal scale-invariant constants cannot decay to zero.  This is the
qualitative conclusion asserted in the follow-up; the `2/3` factor merely
corrects the source's displayed normalization and does not affect that answer.
