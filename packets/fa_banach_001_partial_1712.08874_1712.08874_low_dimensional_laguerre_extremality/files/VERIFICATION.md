# Verification audit

## Source match

Page 25 of arXiv:1712.08874 says that the associated Laguerre polynomial is
believed to be extremal but that the authors cannot prove this.  Section 7.2,
page 346, of the primary Annals paper gives the precise optimization problem:
under `sum A_i=I` and `Tr(A_i)<=epsilon`, maximize the largest root of the
mixed characteristic polynomial.  Its proposed optimizer is the capped scalar
packing, including one residual scalar block and zero blocks.  The packet uses
exactly this formulation.

## Global dimensions two and three

1. **Coefficient formula, (d=2\).**  Expanding the mixed characteristic
   polynomial and using `sum A_i=I_2` gives
   `mu(x)=x^2-2x+1-sum det(A_i)`.  This was also independently checked by the
   direct determinant-expansion code.
2. **Matrix optimization, (d=2\).**  For PSD (2\times2) (A\) of trace
   (t\), `det(A)<=t^2/4`, with equality only at `(t/2)I`.  The capped trace
   packing majorizes every feasible trace vector, so it maximizes the sum of
   squares.
3. **Coefficient formula, (d=3\).**  Put
   `S_2=sum e_2(A_i)` and `S_3=sum det(A_i)`.  Quadratic expansion gives the
   coefficient `3-S_2`.  In the determinant of `sum A_i`, the repeated-label
   terms sum to `S_2-2S_3`; hence the distinct-label mixed discriminant is
   `1-S_2+2S_3`.  Therefore
   `mu(1+y)=y^3-S_2 y-2S_3`.
4. **Matrix optimization, (d=3\).**  Maclaurin/AM--GM gives
   `e_2(A)<=t^2/3` and `det(A)<=t^3/27`, simultaneously sharp only for
   `(t/3)I`.  The capped packing simultaneously maximizes both power sums.
5. **Root monotonicity.**  If (a,b\) increase in `y^3-a y-2b`, evaluation at
   the old nonnegative largest root becomes nonpositive.  Since the new
   polynomial is monic, its largest root cannot decrease.

## Balanced second variation

For (A_i(t)=cI+tH_i\), (c=1/m\), with zero individual traces and
`sum H_i=0`, multilinearity gives no first-order term.  For every pair,

\[
D(H_i,H_j)= -\operatorname{tr}(H_iH_j),
\]

and summing pairs gives one half of `sum tr(H_i^2)`.  Counting the subsets
containing each pair yields exactly

\[
\mu_t=P_{d,m}+\frac{t^2}{2}
\Big(\sum_i\operatorname{tr}H_i^2\Big)P_{d-2,m-2}+O(t^3).
\]

Here both (P\)'s are scaled Laguerre polynomials with the same parameter
(m-d\).  For (m\geq d\), their largest zeros strictly interlace, so the
lower-degree polynomial and the derivative of the higher-degree polynomial
are positive at the latter's largest zero.  The implicit-function sign is
therefore strictly negative in every nonzero direction.

## Computational checks

`code/check_mcp_extremality.py` performs three independent audits:

- the determinant expansion agrees with the closed (d=2\) formula on 40
  normalized PSD tuples and with the scalar derivative formula in dimensions
  3 and 4;
- symmetric finite differences for ((d,m)=(3,4)) and ((4,5)) agree with
  every coefficient in the balanced second-variation identity (errors below
  `4e-8`) and decrease the largest root for both perturbation signs;
- 2,700 normalized commuting, rank-one, and full-rank tuples in dimensions 3
  and 4 were compared with the exact residual scalar packing.  No violation
  occurred; the closest root gap was approximately `-1.44094e-3`.

The random check is corroboration only; neither global proof relies on it.

## Upgrade and obstruction audit

Five materially different stages were pursued: exact problem isolation,
direct computational falsification, global invariant reductions in dimensions
2 and 3, a dimension-4 coefficient comparison, and an all-dimensional
second-variation calculation.  In dimension four, the shifted constant term
contains a positive ((2,2)\) mixed-discriminant contribution.  The stress test
found shifted constant-coefficient gaps down to about `-1.17474e-1`, so the
needed coefficientwise inequality is genuinely false.  A full proof now needs
a coupled inequality at the largest Laguerre zero, not another separate
Maclaurin bound.

## Novelty and limitations

The cheap run indexes were searched by arXiv id, title, exact conjecture
phrases, `mixed characteristic polynomial`, `Laguerre`, `dimension 3`, and
`extremal`.  Bounded external searches recovered the 2015 source and adjacent
mixed-characteristic-polynomial work, but no source stating these exact
low-dimensional or balanced-local results.  Because the (d\leq3\) argument
is elementary once the correct shift is made, novelty confidence is moderate
pending specialist review.

This packet is a partial result.  It does not settle the global conjecture in
dimension four or higher.

