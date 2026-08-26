# Verification report

Target: Question 2 on p. 3, Section II.B of arXiv:1703.01787.

1. **Normalization.** For
   `Q_phi=sqrt(m/(m-1))(P_phi-I/m)`, direct trace expansion gives unit norm
   and `(Q_phi,Q_psi)=(m|<phi,psi>|^2-1)/(m-1)`.
2. **Tightness.** Summing the affine projector identity shows that a unit-norm
   family is tight exactly when its `Q` vectors sum to zero.
3. **Attainment.** The unit-norm tight-frame manifold is compact, so equality
   of the constrained and ordinary constants supplies a tight minimizer of
   coherence `1/sqrt(m)`.
4. **Canonical splitting.** Strict negative inner products define the graph
   components. Cross-component `Q` vectors are orthogonal. Their component
   sums are therefore mutually orthogonal and have total zero, forcing every
   component sum to vanish. Translating back makes every component a UNTF;
   cross-component orthogonality is exactly mutual unbiasedness.
5. **Rank count.** A component Gram matrix has diagonal one, nonpositive
   off-diagonal entries, and zero row sums. It is the weighted Laplacian of
   the connected strict-edge graph, so its kernel is the constants and its
   rank is the component size minus one.
6. **Dimension budget.** Component spans are mutually orthogonal in the
   `d_F(m)-1` dimensional traceless-matrix space. Summing their ranks yields
   `n-r<=d_F(m)-1`, hence `r>=n-d_F(m)+1`. Every UNTF block spans, so it has
   at least `m` vectors.
7. **Converse.** Pairwise mutually unbiased UNTF blocks have a tight union
   with coherence at most `1/sqrt(m)`; the orthoplex bound makes it optimal.
8. **Cardinality.** Combining `r<=n/m` and `r>=n-d_F(m)+1` gives exactly
   `n<=m(m+1)` over `C` and `n<=m(m+2)/2` over `R`. Equality forces every
   block to have size `m`, hence to be an orthonormal basis.

No computation is used. The result is partial because parameter-wise
existence of the resulting mutually unbiased tight blocks remains open and
contains the complete-MUB problem at the complex upper endpoint.
