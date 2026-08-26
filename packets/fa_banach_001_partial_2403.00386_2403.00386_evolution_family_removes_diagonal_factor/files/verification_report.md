# Verification report

Status: complete.

## Mathematical checks

- The scalar conjugation formula was expanded directly.
- The Green kernel's scalar L^1 norm is
  (1-exp(-lambda T))/lambda, with its continuous value T at zero.
- Applying the unshifted maximal-regularity estimate to
  L_A u = f-lambda u produces the claimed constant.
- The scalar lower bound was checked by direct integration over the final
  interval [T-1/mu,T].
- The theorem's extra evolution-family hypothesis and the obstruction to the
  unrestricted case are stated explicitly.

## Artifact checks

- Source question: verified against arXiv PDF page 14.
- LaTeX compilation: passed with latexmk on 2026-08-11.
- Undefined references/citations: none in the final log.
- Overfull/underfull boxes: none in the final log.
- Page-by-page visual inspection: all five pages rendered at 144 dpi and
  inspected; no clipping, overlap, missing glyphs, or illegible formulas.
- Source crop inspection: the estimate, both asymptotic regimes, and the open
  extra-factor sentence are legible.
- Text extraction/readability: Ghostscript extracted all five pages and the
  theorem, scalar proposition, scope section, and bibliography were present.
