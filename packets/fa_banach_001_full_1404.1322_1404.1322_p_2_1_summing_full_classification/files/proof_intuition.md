# Proof intuition

The answer changes abruptly at `q=1`.

At the endpoint, a finite weakly `ell_1` family in `ell_1` is the same thing
as an operator from `ell_infinity` to `ell_1`.  Grothendieck's factorization
theorem sends that operator through a Hilbert space.  The coordinate columns
of the first factor form a Hilbert--Schmidt operator.  After composing the
second factor with the bilinear form and the weakly `ell_2` family in `ell_p`,
the adjoint is 2-summing by the little Grothendieck theorem, hence the other
operator is Hilbert--Schmidt too.  Their product is trace class.  The diagonal
of this product consists exactly of the values `A(x_j,y_j)`, so its `ell_1`
norm is controlled by the trace norm.  This proves more than requested.

For `q>1`, both `ell_q` and `ell_(p')` contain Euclidean spaces of every finite
dimension with projections and embeddings bounded independently of the
dimension.  Rademacher sign matrices give these copies explicitly.  On the
`n`th copy, make an operator act as a scalar `lambda_n` times the identity.
Choosing `lambda_n` to tend to zero makes the block sum compact, but choosing
it slowly enough leaves a growing gap in the proposed summing inequality.
The test vectors have weak `ell_2` norm bounded, weak `ell_1` norm of order
`sqrt(d_n)`, and `d_n` diagonal values all equal to `lambda_n`.  The quotient
therefore grows like `d_n^(1/(2r))`, where
`1/r=1/p-1/2`, and no summing constant can exist.
