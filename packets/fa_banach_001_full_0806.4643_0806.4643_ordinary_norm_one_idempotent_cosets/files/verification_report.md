# Verification report

## Claim and scope

The packet fully answers the source's existence question in the negative and
proves the stronger classification for every discrete group. It does not
claim a locally compact nondiscrete analogue and does not address the source's
later amenability questions.

## Proof audit

- Translation of a multiplier symbol is implemented by conjugating its
  multiplication operator with isometric translations of \(A(G)\).
- The adjoint map on \(VN(G)\) is normal, unital, idempotent, and contractive.
- A proof is included that a unital contraction between C*-algebras is
  positive, so complete boundedness is not imported covertly.
- Positivity makes the range self-adjoint.
- Since the support contains the identity, the canonical faithful normal trace
  is preserved.
- Kadison's self-adjoint inequality and trace faithfulness force the square of
  each self-adjoint range element to remain in the range. Polarization gives
  ambient Jordan closure.
- For support elements \(s,t\), Jordan closure places
  \(\lambda(st)+\lambda(ts)\) in the range. Distinct group unitaries are
  linearly independent, so the Fourier-diagonal formula forces \(st\) back
  into the support.
- The coset converse is verified directly by a coefficient of the
  quasi-regular representation.

No unproved lemma or computational dependency remains.

## Computational sanity check

`code/check_cyclic_groups.py` exhaustively checked all 8,177 nonempty subsets
of \(C_n\) for \(2\le n\le12\). Using the exact finite-abelian Fourier formula
for the ordinary multiplier norm, norm one occurred exactly for subgroup
cosets. This is evidence only; the proof is independent of the computation.

## Novelty check

On 11 August 2026 the run's registry, solution, attempt, and proof-gap indexes
were searched using arXiv id 0806.4643 and the core ordinary-multiplier/coset
terms. External searches used the exact wording of the question and close
variants involving norm-one idempotent multipliers of Fourier algebras. The
source's citation graph and metadata for the closest later work on idempotent
multiplier norms and contractive projections were inspected. No exact answer
or all-discrete-group ordinary-multiplier classification was found.

The check was bounded, not exhaustive. In particular, the full text of one
closed-access general contractive-projection article was unavailable, though
its abstract and bibliographic metadata did not state the present
classification. Novelty therefore remains pending specialist review.

## Human-review focus

Check the trace-to-Jordan step and confirm that no convention mismatch occurs
in identifying the adjoint multiplier with the Fourier-diagonal projection.
The argument is short enough that an independent line-by-line review should be
decisive.

