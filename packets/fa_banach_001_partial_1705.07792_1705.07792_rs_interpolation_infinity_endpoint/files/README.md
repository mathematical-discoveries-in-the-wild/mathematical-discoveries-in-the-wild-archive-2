# Missing infinity endpoint for interpolation of the atomic variation spaces

Status: `candidate substantial partial result, likely valid; human review requested`.

Source: Alex Amenta, Emiel Lorist, and Mark Veraar, *Fourier multipliers in
Banach function spaces with UMD concavifications*, arXiv:1705.07792,
Theorem 4.4 (published in *Transactions of the AMS* 371 (2019), 4837-4868).

## Result

Let `1 <= q < infinity`, `0 < theta < 1`, and
`1/r = (1-theta)/q`. For every bounded interval `J` and complex Banach
space `Y`,

`R^r(J;Y) -> [R^q(J;Y), L^infinity(J;Y)]_theta`.

The inclusion is contractive with the standard norms. The ordered
multi-interval `R_0^s` version also holds. Consequently, the restrictions
`q_1 != infinity` in the two `R^s` statements of source Theorem 4.4 can be
deleted.

The proof interpolates, for each disjoint interval family `I`, the same
atomic synthesis map

`ell^q(I;Y) -> R^q(J;Y)` and
`ell^infinity(I;Y) -> L^infinity(J;Y)`.

This puts every `R^r` atom in the desired interpolation space uniformly.
The defining outer `ell^1` atomic sum then proves the result, with the
limit identified through the continuous embedding into `L^infinity`.

## Scope

This is a complete proof of the missing `q_1=infinity` endpoint, but it is
classified as a substantial partial/adjacent result relative to the source's
broader open questions. It does not remove the epsilon loss for `V^s`, and it
does not prove the reverse `R^s` inclusion. A January 2026 follow-up already
proves the reverse `V^s` inclusion, so that fact is not claimed as novel.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source page 13, showing the endpoint
  restrictions and adjacent interpolation questions.
- `verification.md`: proof, literature, and render audit.

## Novelty

Cheap run indexes, exact local corpus searches, and bounded web searches on
11 August 2026 found no statement removing the `R^s` infinity-endpoint
restriction. Novelty confidence is moderate because the argument is a short
application of standard complex interpolation to the printed atomic
definition.
