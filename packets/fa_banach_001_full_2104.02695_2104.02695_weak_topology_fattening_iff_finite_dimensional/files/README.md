# Candidate full result: weak Banach-space groups are fattening iff finite-dimensional

Status: `candidate_full_solution_subquestion_likely_valid`

Source: Davide Ravasini, *Compactivorous Sets in Banach Spaces*,
arXiv:2104.02695, Open Question 1 on PDF page 8.

## Result

The packet completely answers the weak-topology branch of Open Question 1:

```text
(X, sigma(X,X*)) is fattening if and only if X is finite-dimensional.
```

For every infinite-dimensional Banach space, the norm unit ball is a concrete
compactivorous set that is not strongly compactivorous.  Thus the Schur
hypothesis in the source paper's nonfattening example is unnecessary.

## Proof idea

Every weakly compact subset of a Banach space is fragmented by the norm, so it
has a nonempty relatively weak-open piece of norm diameter less than one.
Translating one point of that piece to zero puts the piece in the norm unit
ball, proving compactivorousness.

Conversely, every basic weak neighbourhood restricts only finitely many
functionals and therefore contains their unbounded common kernel.  It contains
a two-point compact set with diameter greater than two; no translate of that
set can fit in the unit ball.  This rules out strong compactivorousness.
Finite-dimensional weak topology equals norm topology and is locally compact.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:2104.02695.
- `figures/open_problem_crop.png`: full-width crop of the source open questions.
- `code/crop_source_page.py`: reproducible page renderer/cropper.
- `verification.md`: definition, dependency, and edge-case audit.

## Scope and novelty

This is a focused full answer to the question about weak topologies of Banach
spaces, not an answer to the same item's broader clauses about arbitrary
Hausdorff or Polish groups.  It also does not address Open Question 2.

A bounded run-index and web/arXiv search on 9 August 2026 found the source
article and related later compactivorous/Haar-null work, but no later answer to
the weak-topology branch.  Novelty remains subject to specialist review.

## Human review focus

Confirm the standard nonseparable theorem that every weakly compact Banach-space
subset is norm-fragmented, and then check its exact match to the source's
definition of compactivorousness.  The remaining diameter and weak-neighbourhood
arguments are elementary.
