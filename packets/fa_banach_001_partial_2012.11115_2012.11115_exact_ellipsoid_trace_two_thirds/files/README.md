# Exact trace for the source's weighted ellipsoid model

**Status:** candidate substantial partial result, likely valid; human review
requested.

Misra--Pramanick--Sinha conjecture a sharp spectral-volume trace bound for
commuting tuples in their class `BS_{m,vartheta}(Omega)`.  Their principal
non-ball example is the coordinate-multiplication pair on the weighted
Bergman spaces of

`B_{2,1} = {(z1,z2): |z1|^2 + |z2| < 1}`.

The source proves that this pair belongs to `BS_{1,2}(B_{2,1})` for every
parameter `lambda >= 4`, but reports only numerical evidence that its
determinant-commutator trace is approximately `2/3`.

This packet proves exactly, for every `lambda >= 4`,

`trace dEt([[M*,M]]) = 2/3 = (2/pi^2) volume(B_{2,1})`.

The proof diagonalizes the determinant commutator, groups its eigenvalues by
the weighted degree `m+2n`, and exhibits an explicit rational telescoping
certificate.  This settles the source conjecture with equality for its only
non-ball model, but does not prove the conjecture for every tuple in
`BS_{m,vartheta}(Omega)`.

Files:

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/source_numerical_crop.png`: source Remark 5.5.
- `figures/source_conjecture_crop.png`: source Conjecture 5.6.
- `code/crop_source.py`: reproducible source-page crops.
- `code/verify_telescoping.py`: exact SymPy certificate for all rational
  identities in the telescoping proof.
- `tmp/`: build and rendered-page QA files.

The most direct later source found, a revised 2025 doctoral thesis by Paramita
Pramanick, repeats the conjecture and still describes the ellipsoid value as
numerical evidence.  Novelty confidence is therefore moderate-high.
