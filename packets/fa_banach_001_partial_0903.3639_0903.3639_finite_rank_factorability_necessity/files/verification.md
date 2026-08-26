# Verification record

## Source and question

- Official source PDF: arXiv:0903.3639.
- Theorem 4.3 is on PDF page 13.
- The exact open question is on PDF page 14; it records dimensions 1 and 2
  and says the general case is open.
- The matrix Szego criterion used in the proof is Theorem 4.7 on PDF page 16.

## Mathematical checks

1. If `F=A* A` is bounded and `A` is a Smirnov-class factor, its boundary
   norm is essentially bounded, hence `A` is bounded analytic.
2. Outerness plus bounded evaluation at zero gives
   `closure ran A(0)=E`.  Finite-dimensional `E` makes `A(0)` onto.
3. Choosing a finite-dimensional isometry `V` with `A(0)V` invertible gives
   a nonzero bounded analytic determinant `Delta`.
4. `VV*<=I` gives `AA*>=AVV*A*`; determinant monotonicity yields
   `det(AA*)>=|Delta|^2`.
5. Jensen's theorem controls the negative part of `log|Delta|`; boundedness
   controls the positive part of `log det(AA*)`.  Thus the source's matrix
   spectral-factor theorem applies.
6. Equality `(A*)*A*=Q*Q` produces a measurable partial isometry `U` with
   `UA*=Q`; it is isometric on `closure ran A*`.
7. `psi=JU` satisfies `psi F=JQA`, and
   `closure ran F=closure ran A*` by equality of orthogonal complements.
8. Uniform finite boundary rank forces every larger analytic minor of `A`
   to vanish, hence the outer output space is finite dimensional.

## Computational check

`code/verify_linear_algebra.py` tests random complex matrices of sizes
`1<=r<=6`, `r<=n<=r+4`.  It checks the equal-Gram partial-isometry formula,
its initial projection, isometry on the relevant range, the identity
`U(A*A)=QA`, and the determinant inequality.

## Literature audit

The cheap run indexes and bounded web searches on 2026-08-17 used the exact
question and combinations of `necessary for factorability`, `psi F`,
`psi G*`, finite-dimensional spectral factorization, and later citations of
the survey.  No later explicit solution or all-finite-dimensional extension
was found.  This is a bounded novelty audit, not a claim of exhaustive
bibliographic coverage.

## Human-review boundary

The finite-output proof is considered mathematically high-confidence.  A
human expert should particularly check the measurable partial-isometry
selection in the stated weak measurability convention and the passage from
uniform finite boundary rank to finite outer multiplicity.  The packet does
not settle the unrestricted infinite-dimensional question.

