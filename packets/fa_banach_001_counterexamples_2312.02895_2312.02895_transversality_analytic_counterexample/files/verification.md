# Verification record

## Mathematical checks

- `F(r,q,s,t)=s-r^2t` is polynomial and its `s`-derivative is one, so its
  zero set is a real-analytic hypersurface.
- At the origin, the first normal component is zero and the second is
  `(1,0)`, exactly matching the source's proposed weakened hypothesis.
- On `t>0`, `s>r^2t` is equivalent to `r^2<s/t`; on `t<0`, it is equivalent
  to `r^2>s/t`.  The omitted set `t=0` has zero `V`-measure.
- The pushforward of bounded-box Lebesgue measure under `(r,q)->r^2` has an
  integrable `u^{-1/2}` density.  Absolute continuity of the pushforward
  under `(s,t)->s/t` follows by Fubini on `t!=0`.
- Lemma 1.1 of the source transfers the continuous triangular and
  reverse-triangular multiplier bounds to both pieces.  The `t>0` and `t<0`
  cutoffs are contractive orthogonal output projections, so their sum is
  bounded.
- At `y=0`, the section tangent is `span{(r^2,1)}` and changes with `r`,
  directly violating zero curvature.
- If a single representation `{f_1(x)>f_2(y)}` existed, the common boundary
  fiber `(x,0)` would make `f_1` constant.  The explicit pair
  `x=0`, `x=(rho,0)`, `y=(rho^2 t/2,t)` contradicts the resulting
  `x`-independence.

## Source provenance

- `source_paper.pdf` is the official arXiv v2 PDF for arXiv:2312.02895,
  SHA-256
  `f67645bb80856f7be3e002b14fcab3f872022c2636f3818a039a543e16d86605`.
- `source_excerpt_transversality_page_11.pdf` is source PDF page 11.
- `figures/open_problem_crop.png` was rendered from page 11 at 180 dpi,
  tightly cropped to Section 1.7, and visually inspected.

## Novelty check

Exact-title, arXiv-id, transversality, analytic-boundary, and explicit-formula
searches through 2026-08-13 found no later answer, correction, or matching
counterexample.  The published 2025 article still states the question as
open.  This supports, but cannot establish, novelty.

## Final packet QA

- Compiled from the packet directory with `latexmk`; the final log has no
  warnings, undefined references, or overfull/underfull boxes.
- Ghostscript's null-page device parsed the final PDF successfully.
- All three pages were rendered at 170 dpi and inspected at original detail.
  The source crop and formulas are legible, with no clipping, overlap,
  malformed glyphs, or stray build text.
- Final `solution_packet.pdf` SHA-256:
  `16fe736c9f6b8594d4f25c31f99d12309c314f8ebc6afcb94a0a3534ed777303`.
