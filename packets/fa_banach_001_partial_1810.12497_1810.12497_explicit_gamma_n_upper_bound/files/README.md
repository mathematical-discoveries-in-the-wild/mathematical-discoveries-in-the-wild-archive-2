# Explicit upper bound for Voiculescu's constants gamma_n

This packet gives a rigorous partial answer to Problem 1 of arXiv:1810.12497:

`0 < gamma_n <= 2 n^n / 12^(n/2)` for every `n >= 2`.

The new contribution claimed here is the explicit upper bound, obtained from
an exact singular-value computation for dyadic conditional-expectation
projections on the unit cube.  The packet also checks rectangular scaling and
proves that higher local tensor-polynomial degree does not improve this
particular construction.  It does not claim sharpness, a new quantitative
lower bound, or a full hybrid result.

Files:

- `solution_packet.pdf` — standalone proof note.
- `source_paper.pdf` — locally compiled source paper.
- `main.tex` — packet source.
- `verification.md` — mathematical, computational, build, and visual checks.

The attempt record and numerical verification script are in
`runs/fa_banach_001/attempts/` with prefix `1810.12497_`.
