# Verification record

## Mathematical checks

- The symbol equations were transcribed from Example 6.5, equation (6.9),
  in the official arXiv v1 PDF and source TeX.
- For a nonzero complex covector `zeta`, the gradient rows force all input
  coordinates `v_3,...,v_N` to vanish.
- If any `zeta_j`, `j>=3`, is nonzero, the remaining rows also force
  `v_1=v_2=0`.
- On the first coordinate plane, the remaining 2-by-2 block has determinant
  `zeta_1^2+zeta_2^2`; its zero set is exactly the two complex lines in the
  theorem.
- For every unit `nu=(a,b,0,...,0)`, choosing
  `xi=(b,-a,0,...,0)` gives
  `xi+i nu=(b+i a)(1,i,0,...,0)`, proving failure of boundary ellipticity.
- If `nu` has any nonzero coordinate from 3 through n, no covector
  `xi+i nu` belongs to the characteristic cone, proving sufficiency.
- Complex ellipticity of `B` makes `B[zeta]` injective, hence
  `ker(B[zeta]A[zeta])=ker(A[zeta])` for every nonzero complex `zeta`.

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2211.08167_exact_boundary_ellipticity_directions/code/verify_characteristic_cone.py
```

## Source and novelty checks

- Source checked: arXiv:2211.08167v1, especially Theorems 1.1--1.3 and
  Example 6.5 on page 20.
- Local run indexes were searched for the arXiv id, exact title, and core
  boundary-ellipticity terms.  Only an earlier non-promoted screening claim
  was present.
- Exact web searches covered the authors, title, the phrase “boundary
  elliptic in every direction,” the coordinate-span example, admissible
  outward normals, and later general-domain work.  No separate exact
  characterization or erratum was found.
- The result is therefore provisionally new, subject to specialist review.

## Packet QA

- `source_paper.pdf` is the official 22-page arXiv PDF.
- `figures/future_work_and_example_crop.png` is a real crop of source page 20.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully in two passes.
- The final packet is 4 pages and 383,165 bytes.  Its log has no LaTeX,
  undefined-reference, overfull-box, underfull-box, or compilation warnings.
- All four pages were rendered at 150 dpi and inspected individually.  The
  theorem box, source crop, formulas, proof, scope statement, and reference
  are legible; there are no clipped objects, overlaps, or blank pages.
