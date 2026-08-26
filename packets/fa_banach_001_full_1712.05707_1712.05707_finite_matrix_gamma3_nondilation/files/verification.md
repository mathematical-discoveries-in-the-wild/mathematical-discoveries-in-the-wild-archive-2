# Verification record

## Exact source question

- Source: Sourav Pal, arXiv:1712.05707.
- Location: PDF page 28, at the end of Section 5's examples.
- Exact scope: whether every `Gamma_n`-contraction consisting of commuting
  matrices dilates to a `Gamma_n`-unitary.

## Supporting non-dilation input

- Source: Sourav Pal, arXiv:1610.00425.
- Section 7, beginning on PDF page 38, defines the infinite-dimensional tuple
  used here and proves it is a `Gamma_3`-contraction.
- The fundamental-operator obstruction on PDF page 40 shows that the adjoint
  tuple has no `Gamma_3`-isometric, hence no `Gamma_3`-unitary, dilation.
- The finite family in the packet is obtained by replacing the unilateral
  shift by its first-`m` truncated shift and retaining the first-coordinate
  nilpotent block.

## Mathematical audit

- Every product of two components of the finite tuple is zero; this makes its
  full scalar polynomial calculus the exact compression of the supporting
  infinite tuple's polynomial calculus.
- Adjoint invariance follows from coordinatewise conjugation invariance of
  `Gamma_3`.
- Componentwise strong convergence holds for the finite sections and their
  adjoints after zero extension to the ambient Hilbert space.
- Uniform boundedness makes every fixed matrix polynomial converge strongly.
- Arveson's complete-spectral-set/dilation equivalence converts known
  non-dilation of the limit into one strict matrix-polynomial inequality.
  Testing that inequality on a finite-support approximate norming vector makes
  it persist for every sufficiently large finite section.

## Computational and artifact QA

- `code/verify_finite_sections.py` was run in the `sandbox` conda environment.
  For `1 <= m <= 8` it checked the `8m x 8m` dimensions, all degree-two-zero
  relations, adjoint commutativity, `||S_1||=1/4`, `||P||=1`, and exact
  blockwise compression compatibility. All checks passed.
- Both arXiv PDFs are retained in this directory and their relevant pages were
  text-extracted and checked.
- The final three-page packet compiled without overfull/underfull boxes,
  unresolved references, or warnings.
- All three packet pages were rendered at 150 dpi and visually inspected;
  equations, block matrices, and references are legible with no clipping.
- The result ledger parsed successfully with `python -m json.tool`.

## Novelty search

On 13 August 2026, bounded web and local-corpus searches covered the exact
question, its title/authors, finite-dimensional and matrix `Gamma_3` dilation,
symmetrized-tridisc rational dilation failure, and finite-section variants.
They found the known infinite-dimensional failure and later conditional/model
results, but no finite-matrix answer or this finite-section argument.

## SHA-256

- `solution_packet.pdf`: `b6b610a0cf9c426ddc8e5df3e57612638cf53ec3dbb5876057eef53638de6249`
- `source_paper.pdf`: `c553faa63fac030e4df20b5f9b794302bb10aaf804fd62cdad9242f4fd1281a6`
- `supporting_paper_1610.00425.pdf`: `f2998c0581c7fcfa5a51655cba92200706b7ae877d59a488ddf1a13b1986a9a3`
- `code/verify_finite_sections.py`: `13a9b7e745c15c6d5c23bc945bf39a7720db045b77f9521091ee7191841ca900`
