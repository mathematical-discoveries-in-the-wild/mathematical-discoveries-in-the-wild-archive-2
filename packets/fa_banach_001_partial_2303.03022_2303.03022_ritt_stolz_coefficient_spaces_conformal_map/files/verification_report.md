# Verification report

## Scope and source match

- Target: arXiv:2303.03022, open-question subsection on PDF page 15.
- `source_paper.pdf` was downloaded directly from arXiv.
- The page-15 crop visibly contains equation (6.5), the definition of
  `S_{m_1,m_2}`, the request to identify their sum, the request for other
  explicit square functions, and the statement that the conformal map of the
  Stolz region did not seem explicitly known.

## Proof audit

1. The product identity follows directly from the source definition
   `phi_m(k,z)=k^(m-1/2)(1-z)^m z^(k-1)`.
2. Reindexing `n=k-1` proves both weighted-coefficient descriptions, and the
   standard power-series estimate proves every described function is bounded
   on the source Stolz domain.
3. Every finite algebraic sum extends holomorphically to the whole unit disc.
   The chosen pole `z_0=-omega/(omega+1)` lies in the disc but strictly outside
   the closed Stolz domain; the identity theorem therefore proves properness.
4. Under the Cayley transform, the ratio defining the domain becomes
   `2/(|w+1|-|w-1|)`, so the boundary is the stated confocal hyperbola.
5. The maps `cosh:S_beta/(u~-u)->C(Stolz_omega)` and
   `cosh:S_{pi/2}/(v~-v)->{Re q>0}` are bijective. Scaling the strips proves
   conformality and also removes the apparent branch at `w=1`.
6. The hypergeometric formula is the analytic continuation of
   `cosh(kappa arccosh w)` on `C\(-infinity,-1]`, which contains the entire
   Cayley-image domain.
7. The pulled-back monomial-family divergence is the standard asymptotic for
   `sum k^(2m-1)r^(2k)`. The diagonal obstruction uses monotone convergence,
   Cauchy-Schwarz, and the strict inclusion of the Wiener algebra in
   `H^infinity(D)`.

No step in the complete coefficient-space or conformal-map conclusions relies
on the numerical experiment.

## Computational verification

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2303.03022_ritt_stolz_coefficient_spaces_conformal_map/code/verify_map_and_spaces.py
```

The captured output is in `code/verification_output.txt`. For
`omega=1.2,2,5`, boundary modulus errors are at machine precision, explicit
inverse errors are below `3e-15`, all sampled interiors land strictly inside
both domains, and the coefficient identity error is below `5e-14`.

## Literature check

- Searched exact title/id and combinations of `Stolz domain`, `conformal map`,
  `hyperbola`, `cosh`, `arccosh`, `Chebyshev`, `Ritt`, and `explicit square
  functions` through 2026-08-13.
- Checked the locally available source of arXiv:2410.22006. It gives explicit
  contour atoms for generalized Ritt domains and then uses inner-outer
  factorization; it does not state the generalized-Chebyshev Riemann map or
  the coefficient-space obstruction proved here.
- Search coverage is not a proof of priority; the packet says this explicitly.

## PDF build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- Final log contains no warnings, overfull boxes, underfull boxes, or undefined
  references.
- Ghostscript reopened the final PDF successfully with `sDEVICE=nullpage`.
- All six pages were rendered at 150 dpi and inspected at original detail.
  Equations, margins, page numbers, references, and the source crop are visible
  without clipping, overlap, broken glyphs, or stray control words.
- Final PDF SHA-256:
  `f5e9f5ad6ed48ad0547ee1de2185b9329e93890e1c061213542b7977e1239447`.

Classification: strong partial result. The coefficient-space question, the
negative answer for the proposed general formula, and the explicit conformal
map are complete. The broader request for a genuinely new elementary
non-diagonal square-function family remains open after six focused attempts.
