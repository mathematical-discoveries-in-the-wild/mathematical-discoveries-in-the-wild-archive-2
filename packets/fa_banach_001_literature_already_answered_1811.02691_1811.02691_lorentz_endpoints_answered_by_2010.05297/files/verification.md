# Verification record

## Mathematical match

- Source arXiv:1811.02691, PDF page 4, contains Questions 1.1 and 1.2.
- Supporting arXiv:2010.05297v3, abstract, explicitly states
  `||nabla^{m-1} f||_{L^{d/(d-1),1}} <= C ||Af||_1` for every canceling
  elliptic differential operator `A` of order `m`.
- `m=1` is source Question 1.1; `m=k>=2` is source Question 1.2.
- The dimensions match: the supporting theorem holds for `d>=2`, covering
  `n>=3` in Question 1.1 and `n>=2` in Question 1.2.
- Example 1.4 defines `Omega(zeta)=Im A(zeta)`. The paper's cancellation
  condition is exactly the source operator cancellation condition.
- Corollary 1.7 with `alpha=1`, followed by the standard elliptic
  degree-zero multiplier reconstruction, yields the stated derivative
  inequality.

## Provenance

- `source_paper.pdf` was downloaded from the official arXiv PDF endpoint on
  12 August 2026.
- `supporting_paper_2010.05297.pdf` is copied byte-for-byte from
  `data/raw/arxiv/2010.05297/2010.05297.pdf`.
- `source_excerpt_page_4.pdf` was extracted from the source PDF with
  Ghostscript.
- `supporting_excerpt_pages_1_4.pdf` was extracted from the supporting PDF
  with Ghostscript.

## Packet QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`: passed
  after two stable runs.
- Log warning scan: zero warnings, overfull/underfull boxes, undefined
  references, multiply-defined labels, or errors.
- Rendered-page inspection: all 3 pages rendered at 144 dpi and inspected;
  no clipping, overlap, missing glyphs, blank pages, or illegible figures.
- Final SHA-256:
  `26e2ecdabf27d08abd486439ed53f9b990ac0dd6c61c46dc94cd475dce508a63`.
