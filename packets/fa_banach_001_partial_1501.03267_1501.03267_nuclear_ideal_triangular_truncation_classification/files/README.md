# 1501.03267 — nuclear-ideal triangular truncation classification

Status: strong partial result, likely valid; human review requested.

Model: GPT5.6.

Source: Jan Rozendaal, Fedor Sukochev, and Anna Tomskova, Operator Lipschitz
functions on Banach spaces, arXiv:1501.03267 / Studia Math. 232 (2016),
Problem 7.4 on source PDF page 25.

## Result

Problem 7.4 asks which sequence-space (p,q)-summing ideals admit bounded
standard triangular truncation, and whether other non-trivial ideals do.

This packet completely classifies the nuclear ideal. For ell_infinity
interpreted as c0, triangular truncation is bounded on

    N(ell_a, ell_b)

if and only if

    b < a,  or  a = b = 1,  or  a = b = infinity.

In every other case, the norms on the first n coordinates are bounded below
by c log n. At the two equal endpoints the norm is exactly one.

The key exact identity is

    ||Delta_n|| on N(ell_a^n,ell_b^n)
      = ||Delta_n|| on L(ell_b^n,ell_a^n).

It follows from trace duality: upper triangular truncation on the nuclear
ideal has lower triangular truncation on the reverse operator space as its
adjoint, and coordinate reversal exchanges the two triangles. The
Bennett/Kwapien--Pelczynski phase diagram quoted in source Proposition 6.3
then gives the classification. Direct rank-one decompositions handle the
ell_1 and c0 endpoint ideals contractively.

This fully answers the existence clause of Problem 7.4 and gives a complete
phase diagram for one classical ideal. It does not solve the first,
(p,q)-summing classification.

## Files

- main.tex: theorem, proof intuition, and complete proof.
- solution_packet.pdf: rendered human-review packet.
- source_paper.pdf: official arXiv PDF.
- figures/open_problem_crop.png: exact readable crop of Problem 7.4.
- code/crop_source.py: reproducible source-crop script.
- verification_report.md: trace-duality, density, endpoint, and quantifier audit.

## Upgrade attempts

The companion attempt note records five focused routes. Besides the successful
nuclear-duality route, integral-ideal duality, Pietsch factorization,
interpolation, and transfer of ambient logarithmic examples were checked and
found to lose either the fixed coordinate order or dimension-free norm
control.

## Novelty bound

The four run indexes and bounded exact-phrase searches through 11 August 2026
found no explicit later answer. The theorem is a short consequence of known
triangular-projection results, so novelty is provisional and likely modest.
