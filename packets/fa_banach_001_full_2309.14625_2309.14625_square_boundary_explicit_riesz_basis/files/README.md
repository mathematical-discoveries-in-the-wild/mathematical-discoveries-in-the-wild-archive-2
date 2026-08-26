# An explicit exponential Riesz basis for the square boundary

Status: `candidate full affirmative solution; likely valid; high-priority
human review`.

The packet answers Question (Qu) on PDF page 3 of arXiv:2309.14625. For the
unit square `Q=[0,1]^2`, with arclength measure on its boundary, define

```text
Lambda_1 = {(n,       n+1/2) : n in Z}
Lambda_2 = {(n,       n+1  ) : n in Z}
Lambda_3 = {(n-1/2,  -n+1/2) : n in Z}
Lambda_4 = {(n-1/2,  -n    ) : n in Z}.
```

The exponentials with frequencies in their union form a Riesz basis of
`L2(boundary Q)`. The sharp squared Riesz bounds for this basis are
`4-2 sqrt(2)` and `4+2 sqrt(2)`.

The proof identifies the four edges with `L2(0,1)^4`, splits opposite edges
into symmetric and antisymmetric channels, and groups each frequency family
by a Fourier coefficient function. Unimodular multipliers and one reflection
then reduce the synthesis operator exactly to `sqrt(2)` times the constant
matrix

```text
[[1, 0,  1, 0],
 [0, 1,  0, 1],
 [1, 1,  0, 0],
 [0, 0, -1, 1]].
```

Its determinant is `-2`, and the eigenvalues of its Gram matrix are
`2-sqrt(2)` and `2+sqrt(2)`, each twice. Invertibility gives completeness as
well as the Riesz inequalities.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: genuine crop of Question (Qu), PDF page 3.
- `code/verify_basis.py`: exact matrix and randomized synthesis checks.
- `VERIFIER_REPORT.md`: proof, novelty, and rendering audit.

The construction is outside the horizontal finite-coset class excluded by
the source paper. It answers the square-boundary question only; it does not
settle the analogous plus-space problem.

