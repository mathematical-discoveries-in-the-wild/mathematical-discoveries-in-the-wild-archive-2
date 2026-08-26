# Verifier report

Verdict: candidate full solution; likely valid pending expert review.

## Statement match

- Source PDF page 2 leaves Theorem 1.1 open exactly when the upper smoothness
  is an integer m>=2 and p=1; the subcritical hypothesis forces m<N.
- Source PDF page 3 leaves Theorem 1.2 open exactly when
  (s_2,p_2)=(m,1), m>=2.
- The packet proves both clauses in precisely those parameter ranges.

## Proof audit

1. For a_f(v)=||partial_v^m f||_1, homogeneity gives the exact radial formula
   |K_f|=(1/N) integral_S a_f(theta)^(-N/m) dtheta.
2. A maximum-determinant tuple exists because K_f is compact. Replacing one
   maximizing column by an arbitrary point of K_f bounds every coordinate by
   one, so |K_f|<=2^N d. No convexity is assumed.
3. Rescaling all maximizing columns by d^(-1/N) gives determinant one and
   total cost at most N 2^m |K_f|^(-m/N), a fixed multiple of E_(m,1)(f).
4. The symbol of A(D)=(partial_1^m,...,partial_N^m) is nonzero for every
   nonzero frequency, hence elliptic. Its range intersection is contained in
   intersection_j span(e_j)={0}, hence it is canceling for N>=2.
5. Van Schaftingen Theorem 1.3 gives the strong critical Lebesgue estimate
   after a standard higher-order Sobolev embedding. Propositions 8.12 and
   8.13 give the integer Triebel-Lizorkin and noninteger Besov lower norms.
6. If T has the selected vectors as columns and g=f circ T, then
   ||partial_i^m g||_1=||partial_(v_i)^m f||_1 because det T=1.
7. In the cross-order proof, only E_(s,p), not the ordinary Sobolev seminorm,
   is transported back through T. This resolves the main uniform-constant
   pitfall.
8. The source’s density lemma approximates in the full order-m L1 seminorm,
   and its standard homogeneous embedding supplies convergence in the
   required lower space. Uniform convergence of a_(f_j) follows from
   convergence of the full derivative tensor.
9. Positivity of a_f on the sphere follows from the source’s
   no-constant-direction lemma whenever the relevant lower norm is nonzero;
   compactness then gives the positive minimum needed for continuity of the
   negative spherical mean.

## Literature/novelty audit

The four cheap run indexes were searched for the arXiv id, title, integer-p=1
endpoint terminology, pure directional derivatives, canceling operators, and
the maximal-determinant star-body mechanism. No duplicate was found.

Bounded web/arXiv searches on 2026-08-11 found the current published source,
which still states both exceptions, and standard canceling-operator papers,
but no later paper closing these affine endpoints by this or another route.

## Scope guard

The proof does not establish the source’s separate integer-L1
minimizing-orbit coercivity or reverse estimates involving the full derivative
tensor. Those are explicitly excluded from the result.
