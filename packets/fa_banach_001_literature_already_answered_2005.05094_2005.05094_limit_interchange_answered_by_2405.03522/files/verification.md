# Verification record

## Exact source question

- Source: Ole Fredrik Brevig and Karl-Mikael Perfekt, arXiv:2005.05094.
- Location: Section 8.1, PDF page 34, Problem 1.
- Question: whether the `T -> infinity` and `sigma -> 0+` limits in the mean
  counting function can be interchanged for every `f in N_u` and every
  `w != f(+infinity)`.

## Later answer

- Source: Ole Fredrik Brevig, Athanasios Kouroupis, and Karl-Mikael Perfekt,
  arXiv:2405.03522.
- The introduction explicitly restates `[12, Problem 1]` using the quantity
  `N_f(xi,T)`.
- Theorem 1.6 gives a bounded Dirichlet series for which the `T`-limit exists
  quasi-everywhere but differs strictly from `M_f`.
- Theorem 1.7 gives a bounded Dirichlet series for which the `T`-limit fails
  to exist quasi-everywhere on any prescribed annulus.
- PDF page 5 explicitly says that Theorems 1.6 and 1.7 resolve `[12,
  Problem 1]`.

## Artifact QA

- Both source PDFs are retained in this directory.
- The exact source-question page and the later paper's introduction and
  theorem pages were text-extracted and checked against the packet.
- The final two-page packet compiled without overfull/underfull boxes,
  unresolved references, or substantive warnings.
- Both final packet pages were rendered at 150 dpi and visually inspected;
  all text and equations are legible and no content is clipped.
- The ledger JSON was parsed successfully with `python -m json.tool`.

## SHA-256

- `solution_packet.pdf`: `a6d69bb17dd6b5a4273dcb73a1afd848d3f126ba9e5d719caf434994877f8691`
- `source_paper.pdf`: `9371ee5da9d87bbd1eb51ff68a5ef4cce88c86ca2dfa4f425559735758129015`
- `supporting_paper_2405.03522.pdf`: `ec8b53c58a4b09b93cbb859ce8edbf807cf42965393b4c7f1ddc6b72aa919cf2`
