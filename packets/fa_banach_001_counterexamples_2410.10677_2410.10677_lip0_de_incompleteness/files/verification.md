# Verification record

## Mathematical checks

- The source definition and Remark 3.3 were checked in the official PDF.
- `eta` is supported in `[1/4,3/4]`, so division by `|x|` costs at most a
  factor 4 on every nonzero error point.
- For each `n`, the displayed derivative of `r_n` is bounded; hence the
  product `eta*r_n` is globally Lipschitz and compactly supported.
- Subadditivity of the fourth root gives the uniform bound
  `0 <= r_n-r <= n^{-1/2}` and therefore `d_e(f_n,f)<=4n^{-1/2}`.
- The limit is extensively bounded because its support is separated from
  zero.
- At `a=1/2`, its difference quotient equals
  `(1-4h)/sqrt(h)` for positive small `h`, which diverges.  Thus the limit is
  not Lipschitz.
- The vector-valued corollary follows isometrically by multiplication by a
  unit vector.

## Source provenance

- `source_paper.pdf` is the official arXiv PDF for arXiv:2410.10677,
  SHA-256
  `af511d9731346049c09ad299aee834d9db785d3d5a4482ffb002f4c4afb28287`.
- `source_excerpt_remark_3_3_page_11.pdf` is source PDF page 11.
- `figures/open_problem_crop.png` was rendered from that page at 180 dpi and
  visually inspected.

## Novelty check

Exact-title, exact-question, author, arXiv-id, `Lip_0(M,N)`, `d_e`, and
`extensively bounded` searches through 2026-08-13 found no explicit later
answer.  A current open-problem index still repeats Remark 3.3 as unresolved.
This supports, but does not prove, novelty.

## Final packet QA

- Compiled from the packet directory with `latexmk`; the final log has no
  warnings, undefined references, or overfull/underfull boxes.
- Ghostscript's null-page device parsed the final PDF successfully.
- All three pages were rendered at 170 dpi and inspected at original detail.
  The source crop and formulas are legible, and there is no clipping,
  overlap, malformed glyph, or stray build text.
- Final `solution_packet.pdf` SHA-256:
  `742cef3a252375a902dd0cedfa98f271f7c1e071c40da5483652d934e60ff8bb`.
