# Nonemptiness of the Clifford Spectrum for Three Hermitian Matrices

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Alexander Cerjan, Vasile Lauric, and Terry A. Loring, “Clifford spectrum of
  three 2 by 2 matrices,” arXiv:2602.15302v1 (2026).
- Open-conjecture discussion: page 3 of the source PDF.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

For every integer `n >= 1` and every three Hermitian `n`-by-`n` matrices
`A_1,A_2,A_3`, the standard Pauli Clifford spectrum is nonempty. More
quantitatively, if

```text
K = A_1 tensor sigma_1 + A_2 tensor sigma_2 + A_3 tensor sigma_3,
```

then there is a singular localizer at some `lambda in R^3` satisfying
`|lambda| <= ||K||`.

This proves the arbitrary-finite-size, three-matrix extension highlighted by
the source paper, whose theorem covers only `n=2`.

## Proof mechanism

If the localizer were invertible throughout a ball of radius `R > ||K||`, its
negative spectral subspaces would form a rank-`n` complex vector bundle over
that ball. On the boundary sphere, the localizer is connected through
invertible Hermitian matrices to

```text
-R I_n tensor (omega dot sigma).
```

The negative bundle of this model is `n` copies of the positive-eigenvalue
Hopf line bundle. Its determinant transition function has winding `-n`, so it
cannot be the restriction of a bundle over a ball. This contradiction forces
a singularity inside every ball of radius `R > ||K||`; a limiting argument
gives the stated norm bound.

## Files

- `main.tex`: self-contained proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of the page-3 open-problem
  discussion and the source paper's `2 x 2` scope.
- `code/verify_boundary_obstruction.py`: numerical sanity checks for the
  boundary gap, negative rank, and Hopf transition winding; not part of the
  proof.
- `VERIFICATION.md`: independent proof audit and reviewer focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

A bounded check on 2026-08-09 searched the run's registry, solution, attempt,
and proof-gap indexes for arXiv:2602.15302 and the core Clifford-spectrum
phrases. Web/arXiv searches used the exact source title and combinations of
“Hopf line bundle,” “negative spectral subspace,” “Chern class,” “Pauli,” and
“Clifford spectrum nonempty.” They found the source `2 x 2` theorem and the
earlier general conjecture in Cerjan--Loring, *Even spheres as joint spectra
of matrix models* (arXiv:2305.12026), but no arbitrary-`n` proof for three
matrices and no use of this boundary Hopf obstruction. Novelty confidence is
moderate pending a specialist literature review.

## Human review focus

Please check:

- that the source's arbitrary-size three-matrix conjecture uses the standard
  Pauli localizer addressed here;
- the passage from the gap estimate to a homotopy of negative spectral
  bundles on the boundary;
- the sign and winding of the two explicit local frames (only nonzero winding
  matters);
- the limiting argument yielding `|lambda| <= ||K||`.

