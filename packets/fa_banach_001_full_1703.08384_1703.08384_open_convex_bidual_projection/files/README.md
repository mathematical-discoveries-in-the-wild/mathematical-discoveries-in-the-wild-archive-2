# Open convex domain bidual projection

Result type: `full`

Status: `candidate_full_solution_likely_valid`, pending specialist review.

Source paper:

- Marek Cúth, Ondřej F. K. Kalenda, and Petr Kaplický, “Finitely additive
  measures and complementability of Lipschitz-free spaces,” arXiv:1703.08384v2.
- Target: Question 1.5, page 2.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The packet answers Question 1.5 affirmatively with the exact requested
constant. If `E` has dimension `d >= 2`, `Omega` is a nonempty open convex
subset of `E`, and `o in Omega`, then there is a projection

```text
P_Omega : F(Omega,o)** -> F(Omega,o)
||P_Omega|| <= d_BM(E, ell_2^d).
```

For a Euclidean ambient space the projection has norm one. The proof passes
from the whole Euclidean space to the closure of the convex domain using the
nonexpansive Hilbert metric projection, identifies the free space of the open
domain with that of its closure by density, and then transports the result
through a Banach--Mazur optimal affine map.

## Files

- `main.tex`: complete proof and audit notes.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: full-width source crop containing Question
  1.5 and its surrounding context.
- `verification_report.md`: independent line-by-line proof audit.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

The run's cheap indexes were searched for the arXiv id and the core question
terms. Bounded arXiv/web searches on 9 August 2026 used the exact question,
the exact source title, and variants of “open convex Lipschitz-free space
complemented in its bidual Banach--Mazur distance.” They found the source and
related later work, but no directly matching later proof. This is a bounded
search, not a guarantee of novelty.

## Human review focus

Please check:

- the passage from `Omega` to `closure(Omega)` via completion invariance of
  Lipschitz-free spaces;
- the bidual sandwich `R Q_H I**` induced by the Hilbert nearest-point
  retraction;
- the affine basepoint normalization and the Banach--Mazur norm accounting;
- whether this short argument has already appeared outside the searched
  corpus.

The packet does not claim to answer Questions 1.4 or 1.6 of the source paper.
