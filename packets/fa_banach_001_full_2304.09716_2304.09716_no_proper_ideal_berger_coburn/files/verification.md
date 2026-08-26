# Verification record

Date: 2026-08-11

Status: candidate full solution, likely valid, subject to human review.

## Mathematical audit

- Hardy, Bergman, and the corresponding `L2` spaces are separable
  infinite-dimensional Hilbert spaces.
- If a bounded operator `T` is noncompact, some positive spectral subspace of
  `|T|` is infinite-dimensional; otherwise finite-rank spectral truncations
  converge to `|T|` in norm.
- An isometry into that spectral subspace makes `TV` bounded below.
- A bounded-below Hilbert-space operator has closed range and a bounded left
  inverse obtained by extending the inverse by zero on the orthogonal
  complement.
- The identity `STV = I` yields `R = (RS)TV` for every bounded `R`, so a
  two-sided ideal containing one noncompact operator is the full rectangular
  operator class.
- Therefore every proper operator ideal component is contained in the compact
  operators; no closure assumption is used.
- Source Example 2 supplies, in each stated Hardy/Bergman setting, a bounded
  analytic symbol with zero Hankel operator and noncompact conjugate-symbol
  Hankel operator.
- Zero belongs to every operator ideal, while the conjugate Hankel operator
  belongs to no proper ideal. This violates the exact BCP equivalence.

## Literature audit

- Exact registry and cheap-index searches found no prior packet for the paper
  or operator-ideal question.
- Exact local-corpus and bounded web searches found later Berger–Coburn work
  on doubling Fock spaces and symmetrically normed ideals, but no answer to
  the Hardy/Bergman Open Problem 1.
- arXiv:2312.06656 makes explicit partial progress on the source's separate
  doubling-Fock Schatten question, not Open Problem 1.

This is a bounded novelty check, not an exhaustive bibliographic priority
claim.

## Artifact audit

- The archived source was compiled locally into a 12-page PDF.
- Printed source page 4, including Example 2 and the complete open problem,
  was rendered as the evidence image.
- The final packet was compiled with disposable output under `tmp/` and
  checked for LaTeX errors, undefined references, and overfull boxes.
- Every final packet page and the source evidence image was visually inspected
  for clipping, overlap, and legibility.

## Human-review focus

Confirm that “operator ideal” in Open Problem 1 has its standard two-sided
meaning. With that interpretation, the exact factorization argument is the
only new joint and is self-contained.
