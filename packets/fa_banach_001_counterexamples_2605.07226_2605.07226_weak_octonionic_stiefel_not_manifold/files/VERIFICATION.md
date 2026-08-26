# Verification audit

## Exact source match

Source Section 4 asks two modified James questions for weak associative
octonionic Stiefel spaces. Question (1), concerning the projection, is
answered negatively for k=2 in the source itself. Question (2), whether
V^w_k(O^n) is a manifold, is not answered.

Source Theorems 3.12 and 3.16 identify V^w_2(O^2) with the 2-by-2
octonionic isometry locus and prove that every element is pU, where p is a
unit octonion and U belongs to U_{C_J}(2) for some complex slice C_J.

## New proof obligations

### 1. Unique scalar normalization

Near the identity, the upper-left entry a is nonzero. Setting p=a/|a| and
U=conjugate(p)M makes U_11=|a| positive real. The source's classification
proof places U in a complex unitary group. Conversely pU is an octonionic
isometry. Since the upper-left entry of pU is p times a positive real
number, p is uniquely recoverable. This gives an exact local S^7 product.

### 2. Normalized unitary chart

In an ordinary complex slice, a unitary matrix near the identity whose
upper-left entry is positive real has first row (r,z) and second row
eta(-conjugate(z),r), with eta a unit complex number near one. Write
z=s+B and eta=exp(A). The imaginary vectors A and B are multiples of the
same unit J, hence are collinear in R^7. Conversely collinear A,B lie in a
common complex slice and produce a unitary matrix.

The inverse is explicit: s=Re U_12, B=Im U_12, and
A=log(U_22/r). Thus this is a homeomorphism, not merely a dimension count.
Together with the local S^7 factor it gives R^8 times the rank-at-most-one
cone in M_{7,2}(R).

### 3. Link and rational homology

The unit link of the rank-one cone is (S^6 x S^1)/+- because a unit
rank-one matrix is uv^T, uniquely up to simultaneous sign. The covering
transfer identifies rational homology downstairs with deck-invariants
upstairs. Simultaneous antipodal action has degree +1 on the S^1 factor, so
H_1 of the quotient is Q.

### 4. Local manifold obstruction

Nonzero rank-one points of the determinantal cone are smooth of dimension
8, so the product has nearby local dimension 16. For R^8 x C(L), local
homology is reduced homology of L shifted by 9. The nonzero H_1(L;Q)
therefore gives nonzero local homology in degree 10. A topological
16-manifold has local rational homology only in degree 16.

## Computational checks

code/check_local_model.py performs:

1. 21,000 exact vanishing-minor checks for rank-one 7-by-2 matrices;
2. 30,000 exact rational complex-unitary checks for the normalized formula;
3. 30,000 exact recovery checks for s, B, and the unit phase.

The checker is corroborative and does not replace the proof.

## Novelty, scope, and review focus

Four cheap indexes had no hit for the arXiv ID or weak-octonionic Stiefel
keywords. Bounded exact-title and arXiv searches found the source and its
predecessor on weak associative bases, but no separate resolution through
11 August 2026.

The result supplies a full negative answer in general by the case k=n=2.
It does not classify all other k,n. Human review should focus on whether the
source classification supplies the normalized complex slice continuously,
the uniqueness of the unitary parameters near the identity, and the
local-homology shift.
