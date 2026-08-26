# Scattered-target and FDI faithful discretizations

**Status:** substantial partial result, likely valid. It answers Question 2.6
of arXiv:1607.03376 positively for two broad classes but does not settle the
question for arbitrary C*-algebras.

## Main result

Let `pi_i:A->B_i` be unital representations into scattered C*-algebras. There
is an explicit compatible W*-discretization

`A -> product_i B_i**`.

It is injective if the representations separate the points of `A`. Its context
map on a commutative subalgebra `C` is injective exactly when the images of
`Spec(pi_i(C))` cover `Spec(C)`. Consequently the discretization is faithful
when both separation and character coverage hold.

Two consequences are:

- every scattered unital C*-algebra has a faithful compatible
  W*-discretization through its bidual;
- every unital FDI (equivalently unital CCR/liminal) C*-algebra has one by
  taking the product of all irreducible representations.

By the source's universal property, its canonical `A->F(A)` is faithful for
both classes. The FDI conclusion strictly extends the source's subhomogeneous
case because irreducible dimensions need not have a uniform bound.

## Files

- `solution_packet.pdf`: theorem, construction, proofs, sharp scope, and failed
  full-resolution routes.
- `source_paper.pdf`: compiled arXiv source.
- `figures/question_2_6_crop.png`: source-page crop of the exact question.
- `code/render_question.py`: reproducible source crop.
- `code/verify_finite_context.py`: finite-set audit of the pullback
  compatibility and exact coverage criterion.
- `VERIFIER_REPORT.md`: proof and render audit.
- Attempt record:
  `runs/fa_banach_001/attempts/1607.03376_compatible_discretization_upgrade_attempts.md`.

Novelty confidence is moderate after a bounded exact-phrase and class-keyword
search; a broader expert citation review remains appropriate.

Final packet SHA-256:
`ac55d2564ef3a27256b5e154d4789f5332e924eefc3da6172b8d83ee0a2f5bac`.
