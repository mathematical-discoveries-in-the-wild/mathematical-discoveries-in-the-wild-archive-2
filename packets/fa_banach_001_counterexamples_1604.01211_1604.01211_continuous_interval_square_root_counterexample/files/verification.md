# Verification record

Date: 2026-08-11

Status: candidate full counterexample, likely valid, subject to human review.

## Mathematical audit

- The convergent sequence plus its limit is closed in a compact Hausdorff
  space, and the prescribed alternating values converge to zero.
- Compact Hausdorff spaces are normal, so Tietze extends the prescribed
  function without increasing its range beyond `[-1,1]`.
- The interval `[f,1]` has continuous canonical boundary functions and
  satisfies the source paper's necessary inequalities.
- Source Lemma 3.1(i) converts a hypothetical interval square root into the
  exact scalar square-root identity at each point.
- For a positive lower endpoint `a`, equality at the lower endpoint of a
  scalar interval square forces both factor moduli to equal `sqrt(a)`.
- For a negative lower endpoint `a`, equality at the lower endpoint forces
  the factors to be the two interval endpoints, one of modulus `1`.
- Because the lower boundary itself belongs to the target interval, it must
  have a global factorization by two continuous members of the hypothetical
  root interval.
- The positive subsequence makes both factor values tend to zero; the
  negative subsequence keeps their maximum modulus equal to one. Continuity
  at the common limit gives the contradiction.
- In the finite case, scalar roots can be selected coordinate by coordinate,
  proving the converse direction of the first-countable characterization.
- The simplest example `K=[-1,1]`, `f(t)=t`, `g(t)=1` avoids the extension
  theorem and independently tests the core argument.

## Literature audit

- The registry, solution, attempt, and proof-gap indexes had no hit for this
  paper or square-root question before reservation.
- Exact local-corpus searches found the source but no later arXiv answer.
- Bounded web searches for the exact question, source title, authors, and
  continuous-boundary variants found the 2016 paper but no later resolution.
- The result strengthens the source obstruction by keeping both boundary
  functions continuous. It does not claim a classification on arbitrary
  compact Hausdorff spaces.

This is a bounded novelty check, not an exhaustive bibliographic priority
claim.

## Artifact audit

- The archived source was compiled locally into a 17-page PDF.
- Source page 14 was rendered and copied as a full-width evidence image.
- The final packet was compiled with all disposable build output under
  `tmp/` and checked for LaTeX errors, undefined references, and overfull
  boxes.
- Every page of the final packet and the source evidence image was rendered
  and visually inspected for clipping, overlap, and legibility.

## Human-review focus

Check the scalar equality cases and the invocation of source Lemma 3.1(i).
Those are the only substantive joints; the explicit interval example makes
the continuity contradiction otherwise self-contained.
