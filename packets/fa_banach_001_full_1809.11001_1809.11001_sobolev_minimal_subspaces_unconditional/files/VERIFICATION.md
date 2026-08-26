# Verification record

Status: candidate full solution, pending human mathematical review.

## Mathematical audit

- Exact source statement checked against arXiv:1809.11001v3, PDF page 9 and
  parsed `Sections/minsub.tex`.
- Source definition using decomposable `L^2` functionals was compared with
  the abstract definition using the full Hilbert tensor dual. The two closures
  agree because decomposable tensors are dense and contraction is bounded.
- Directional minimality was proved directly by orthogonal complements.
- The passage from `U_k tensor H_[k]` to
  `U_k tensor (tensor_{j!=k} M_j)` was checked in the common `L^2` ambient
  tensor product using commuting orthogonal projections.
- For `K=J^*J`, injectivity of `J` gives `ker K=0`; hence the spectral cutoffs
  converge strongly even if zero lies in continuous spectrum.
- The cutoff is `L^2`-contractive by the spectral integral for
  `<Kx,x>`, and it extends to an `L^2`-orthogonal projection because it is
  symmetric there and its range is `L^2`-closed.
- On each spectral range, `sqrt(eps)||x||_H1 <= ||x||_L2 <= C||x||_H1`.
  Therefore all directional tensor norms are equivalent at fixed `eps`, so
  their completions coincide and algebraic tensors are simultaneously dense.
- The final diagonal approximation was checked in the maximum intersection
  norm, which is equivalent to the source's `H^1` norm.

## Artifact audit

- `source_paper.pdf` was downloaded from arXiv.
- `figures/open_problem_crop.png` was rendered directly from PDF page 9 and
  visually inspected; it contains the definition, Assumption 3.5, Remark 3.6,
  and Proposition 3.7.
- `main.tex` was compiled with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error`.
- All pages of `solution_packet.pdf` were rendered and visually inspected.
- PDF text extraction was checked for the theorem statement and final
  conclusion.
- Human review remains required; no `human_verified` marker was created.
