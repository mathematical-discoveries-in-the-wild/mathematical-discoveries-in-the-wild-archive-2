# Verification record

## Proof checks

- The sectorial normalization is explicit: `F=f` on the selected component
  and `F=0` on the opposite component; `f=1` recovers the source projection.
- The frozen family varies only through its principal symbol, so the standard
  full-symbol topology required by the supporting calculus is available
  without strengthening the topology on the original family.
- For `m>=1`, the right resolvent gains `m-1` derivatives with decay
  `|lambda|^(-1/m)` and the left resolvent contributes `|lambda|^-1`.
- For `0<m<1`, the lower-order difference is smoothing and both resolvents
  contribute `|lambda|^-1`, giving the stronger `|lambda|^-2` bound.
- The compact connecting arc is controlled by ordinary local resolvent
  continuity.
- The estimate is uniform in bounded decaying regularizers, so the standard
  bounded-calculus convergence lemma passes to arbitrary bounded `f`.
- The two terms in the final estimate correspond exactly to the two defining
  components of the source topology `T`.

## Provenance

- `source_paper.pdf` was downloaded from the official arXiv PDF endpoint on
  12 August 2026; PDF page 17 contains Remark 5.1 and the open problem.
- `supporting_0901.3160_hinfty_calculus.pdf` was downloaded from the official
  arXiv PDF endpoint on 12 August 2026; PDF pages 5--6 contain Theorems 3.2
  and 3.5 and their relevant estimates.
- Exact source/support pages are bundled as PDF excerpts and rendered PNGs.

## Literature audit

Cheap run indexes and bounded official-arXiv searches by exact ID, exact
title, citation, `f(A)`, sectorial perturbation, and bounded holomorphic
calculus found no later paper explicitly closing Remark 5.1 through
12 August 2026. This is not a priority claim.

## Packet QA

- LaTeX build: passed twice with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error`; final packet has three pages.
- Log warning scan: passed; no `Warning`, `Overfull`, `Underfull`,
  `undefined`, or `multiply defined` entries in the final log.
- Rendered-page inspection: passed at 130 dpi for all three final pages. The
  full source question is visible, all displayed formulas are legible, and
  there are no clipped, overlapping, orphaned, or stray literal elements.
- Text-extraction audit: passed; three pages extract and contain no stray
  `qquad` or `,quad` tokens.
- Final SHA-256:
  `057b92d881eda0c23954441ba0deb22ad1bb8b30500a5c51ad3ec695fa2d954f`.
