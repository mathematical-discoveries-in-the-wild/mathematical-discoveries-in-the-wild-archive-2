# Verification report

Candidate: arXiv:2511.06487 C*-coefficient extension

## Claim checked

For every unital C*-algebra `A` without WEP, there is a finite
`p in A[F_2]` which is strictly positive under every spatial unitary
evaluation but is not a finite sum of hermitian squares in `A[F_2]`.

## Verdict

**Likely valid.**  This is a complete counterexample to the trigonometric half
of the source's broad C*-coefficient question, and therefore gives a complete
negative answer to the question as asked.  The unconstrained self-adjoint
polynomial half remains separate.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| WEP characterization | external / verified | Farenick--Kavruk--Paulsen, arXiv:1107.0418, Theorem 4.3 with `n=3`, gives `A tensor_min C*(F_2) = A tensor_max C*(F_2)` iff `A` has WEP. |
| Algebraic norm witness | valid | Inequality of two completion norms forces a strict gap on the common algebraic tensor product. |
| Group-ring approximation | valid | Approximate each of finitely many second-factor coefficients; both cross norms are bounded by the projective sum, so a sufficiently small perturbation preserves the strict gap. |
| Choice of lambda | valid | The open interval between the squared norms is nonempty. |
| Spatial positivity | valid | `lambda 1-x^*x >= (lambda-||x||_min^2)1`; every unitary evaluation is a representation of the minimal tensor product. |
| No finite SOS | valid | Every algebraic sum of squares is positive in the maximal completion, but `lambda 1-x^*x` is not maximal-positive because `lambda<||x||_max^2`. |
| Scope | valid | Failure of one of the two proposed extensions answers “do the results still hold?” negatively; no claim is made about the other extension. |

## Adversarial checks

- The direction of the norm gap is essential and correct: the maximal norm is
  at least the minimal norm.
- The witness is genuinely a finite trigonometric polynomial after the
  density step, rather than merely an element of a completed tensor product.
- Positivity holds for all Hilbert-space unitary pairs, not only matrices.
- The conclusion excludes every finite sum of squares, which is stronger than
  excluding a single square.
- The construction uses the source's spatial/minimal evaluation convention.
  If one instead defined positivity using all commuting representations (the
  maximal tensor product), the witness would not satisfy the hypothesis.

## Upgrade attempts

Cayley-transform and symmetry-product routes toward the unconstrained
self-adjoint-polynomial theorem were checked.  They introduce noncommuting
denominators or equality constraints, and no rigorous descent from a putative
polynomial SOS to a group-ring SOS was found.  WEP sufficiency was also not
claimed because completed maximal positivity need not be an exact algebraic
SOS certificate.

## Literature / novelty check

Bounded exact-title/id, C*-coefficient, WEP, and operator-valued
trigonometric-polynomial searches on 2026-08-12 found no later answer to the
source problem.  Novelty is plausible, not certified.

## Recommended human review

Confirm the intended evaluation convention in the published source and audit
the invocation of Farenick--Kavruk--Paulsen Theorem 4.3 at `n=3`.  The
remaining argument is elementary C*-norm bookkeeping.

