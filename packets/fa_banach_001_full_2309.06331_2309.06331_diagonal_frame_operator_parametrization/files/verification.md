# Verification report

## Claims checked

1. All bounded M for which {Mv_j} has positive invertible diagonal frame
   operator are D^(1/2) C S^(-1/2), with D positive invertible diagonal and
   C a coisometry.
2. All additive perturbations producing a diagonal-frame-operator frame are
   d_j=D^(1/2)Ce_j-v_j.
3. The canonical dual of a frame with lower bound A satisfies
   sup_j ||S^(-1)v_j|| <= A^(-1/2), sharply.
4. Nonnegative componentwise radii preserve every frame of lower bound at
   least A under every allowed perturbation exactly when the radii belong to
   l2 and have l2 norm strictly below sqrt(A).

Verdict: candidate full solution; likely valid.

## Operator audit

- The transformed synthesis operator is MT, hence its frame operator is
  MSM*.
- If MSM*=D, then C=D^(-1/2)MS^(1/2) satisfies CC*=I.
- Conversely M=D^(1/2)CS^(-1/2) gives MSM*=D.
- For a perturbed synthesis W, the same calculation gives
  C=D^(-1/2)W and W=D^(1/2)C.
- In infinite dimensions C is genuinely a coisometry; it need not be
  unitary. The backward shift provides the elementary distinction.
- The coordinate rows are W*h_k. Their Gram matrix is WW*, so diagonal
  frame operator is equivalent to pairwise orthogonality, with uniform
  positive upper and lower squared row norms.

## Consequence audit

- S^(-1)T synthesizes the canonical dual and has frame operator S^(-1).
  The inequalities AI <= S <= BI give dual bounds 1/B and 1/A.
- The canonical Parseval perturbation W=S^(-1/2)T satisfies WW*=I.
  Its synthesis perturbation E has
  EE*=(S^(1/2)-I)^2, proving the stated norm and trace formulas.

## Sharp-radius audit

- For ||d_j|| <= epsilon_j and epsilon in l2, Cauchy--Schwarz gives
  ||E|| <= ||epsilon||_2.
- Triangle inequalities for (T+E)* give the displayed perturbed frame
  bounds whenever ||epsilon||_2 < sqrt(A).
- If epsilon is not in l2, a rank-one perturbation d_j=epsilon_j h makes
  one analysis coefficient sequence non-l2, so the family is not Bessel.
- If delta=||epsilon||_2 >= sqrt(A), the scaled orthonormal frame
  v_j=sqrt(A)e_j can be perturbed by d_j=-P_y v_j, where
  |<y,e_j>|=epsilon_j/delta. The allowed perturbation puts every new vector
  in y-perp, destroying completeness. This includes equality.

## Upgrade-attempt log

- Attempt 1 obtained the finite-dimensional unitary factorization.
- Attempt 2 replaced unitaries by coisometries and closed the infinite
  dimensional operator and additive classifications.
- Attempt 3 resolved the source's canonical-dual boundedness doubt sharply.
- Attempt 4 upgraded the usual sufficient perturbation estimate to an
  exact universal iff theorem with two distinct obstruction constructions.
- Attempt 5 derived an explicit Parseval diagonalization and its exact
  synthesis displacement, while declining to claim global distance
  minimality over all diagonal target operators.

## Novelty audit

Bounded primary-source searches through 2026-08-11 used the source title,
diagonal frame operator, frame perturbation, MSM*=D, and coisometry
parametrization. Related prescribed-frame-operator work was found, including
arXiv:0710.1258, but no inspected primary source explicitly answered the
two source questions with these parametrizations. Novelty confidence is
moderate because the proof is elementary and could be implicit folklore.

## Source and render audit

- source_paper.pdf was compiled locally from the archived arXiv source and
  has 14 pages.
- Source pages 11 and 12 were visually inspected and fully reproduced.
- The packet compiled without warnings, overfull boxes, undefined
  references, or multiply defined labels.
- The final packet has 7 pages; every page was visually inspected after the
  last material edit.
- Final packet SHA-256:
  058f8ec5b029fcdfe545f87712ce8812e439f2e322dd2bc1e246871d2cc415e0.
- Compiled source-paper SHA-256:
  2adeb5a7cbe45a1f0ac5081136598b9f0a6426641206725eaa9df3a1c13fcd57.
- Source page 11 image SHA-256:
  1f65a625fe89e1a290cd0826b5f536c2c488e7cfe23e96a9a3016714d7ddc48c.
- Source page 12 image SHA-256:
  5804ffd7a895493f170494fc05549c9ff5848c76189d49a5653e3e86711c57b4.

## Human verifier focus

Check the coisometry parametrization in infinite dimension, the row
criterion, and the two sharpness constructions for the universal radii.

