# Scalar first-order necessity on stratified groups

**Status:** candidate partial result, likely valid; human review recommended.

**Source:** Jean Van Schaftingen and Po-Lam Yung, *Limiting Sobolev and
Hardy inequalities on stratified homogeneous groups*, arXiv:2007.14532,
Annales Fennici Mathematici 47 (2022), 1065-1098.

The source asks whether its endpoint estimate forces maximal
hypoellipticity and a compatible cocanceling operator on a general
stratified homogeneous group.  This packet gives a complete affirmative
answer for scalar first-order operators

\[
 A_T(D)u=T(X_1u,\ldots,X_mu),\qquad T:\mathbb R^m\longrightarrow E.
\]

For every stratified group of homogeneous dimension \(Q\geq2\), the endpoint
estimate

\[
 \|u\|_{L^{Q/(Q-1)}}\leq C\|A_T(D)u\|_{L^1}
\]

holds if and only if \(T\) is injective.  Injectivity immediately gives
maximal hypoellipticity, and the compatible cocanceling operator constructed
in the source for the horizontal gradient can be transported through a left
inverse of \(T\).  A pure-derivative block handles any unused part of the
codomain.

The new necessity argument is a transverse anisotropic cutoff.  If
\(0\ne c\in\ker T\), keep a test function compact in the horizontal direction
\(c\), but dilate all remaining coordinates according to their homogeneous
weights.  The left side grows as \(R^{Q-2+1/Q}\), whereas the right side grows
at most as \(R^{Q-2}\), which is impossible.

This does **not** settle higher-order operators or operators with
vector-valued domain.

Files:

- `main.tex` and `solution_packet.pdf`: complete theorem and proof.
- `source_paper.pdf`: the original paper.
- `figures/`: rendered source crops for (1.7), conditions (i)-(ii), and the
  open question on PDF pages 2-4.
- `verification.md`: proof audit and novelty-search bounds.

