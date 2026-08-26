# Intended Steklov exponential-localization conjecture is answered

Status: `literature_already_answered` (with a source-statement correction).

Source:

- Valentin A. Zagrebnov, “From Laplacian Transport to Dirichlet-to-Neumann
  (Gibbs) Semigroups,” arXiv:0801.4145 (2008).
- Signal: Conjecture 2.7, PDF page 6.

Supporting answer:

- Jeffrey Galkowski and John A. Toth, “Pointwise Bounds for Steklov
  Eigenfunctions,” arXiv:1611.05363; *Journal of Geometric Analysis* 29
  (2019), 142–193.
- Identification: Introduction and Theorem 1, PDF pages 2–3.

## Identification

The intended problem is the Hislop–Lutzer conjecture that harmonic extensions
of Dirichlet-to-Neumann eigenfunctions decay exponentially into the interior
for real-analytic geometry, at a rate governed by the spectral frequency.
Galkowski–Toth explicitly state that their Theorem 1 proves this conjecture in
arbitrary dimension and establish a sharp near-boundary estimate of the form
`exp(-d(x)/h)`, where `h^{-1}` is the Dirichlet-to-Neumann eigenvalue.

## Important source correction

Conjecture 2.7 in arXiv:0801.4145 is not an accurate standalone formulation of
the original conjecture: it assumes only smooth geometry and writes
`exp(-k dist)` after using `k` as the ordinal eigenvalue index.  The intended
Hislop–Lutzer statement requires real analyticity and uses spectral frequency,
not ordinal position.  The same source's ball computation uses spherical
degree `l`, consistent with spectral frequency and inconsistent with ordinal
index once multiplicities are counted.

Thus the analytically corrected intended conjecture is answered, while the
literal smooth/index wording should not be cited as the theorem proved by the
supporting paper.

## Other signal in the source

The trace-norm approximation conjecture later in arXiv:0801.4145 is claimed
proved “at least for the ball” in the same section.  That is a same-paper
ask-and-answer passage for the ball, not a separate literature result.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: arXiv:0801.4145.
- `supporting_paper_1611.05363.pdf`: explicit later answer.
- `tmp/`: build intermediates and rendered QA pages.

