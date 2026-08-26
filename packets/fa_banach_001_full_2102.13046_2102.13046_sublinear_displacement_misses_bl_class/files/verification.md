# Verification record

Status: final packet checks passed; mathematical claim remains pending human
review.

## Proof checks

- Exact target: source PDF page 7, paragraph after Conjecture 1.8 and before
  Theorem 6.1.
- The non-realizable density is the same Burago--Kleiner input explicitly used
  by the source in its proof of Theorem 6.1.
- Nested-shell sampling is an adaptation of source Lemma 6.4; the old-cube
  and fixed-interface errors vanish after normalization.
- Kirszbraun plus density of the rescaled Delone sets passes both upper and
  lower Lipschitz bounds to the limit.
- The reverse lattice-filling inclusion uses global bijectivity, sublinear
  displacement in the reverse localization estimate, invariance of domain,
  and the zero `d`-measure of a Lipschitz image of the cube boundary.
- The positive linear-scale direction is exactly source Proposition 2.6.

## Source provenance

The external arXiv PDF request was unavailable because the environment had
reached its external-action usage limit. `source_paper.pdf` was therefore
compiled locally from the complete arXiv TeX source archive already stored at
`data/parsed/arxiv_sources/2102.13046/`. The compilation completed and gives
the 32-page author-source version containing the target on page 7.

## Build and visual QA

- `code/crop_open_problem.py` reproduced the 1095-by-330-pixel crop from
  source page 7. The crop was visually inspected and contains the exact open
  question and its `remains open` sentence without clipping.
- `main.tex` was compiled twice with pdfLaTeX after the last mathematical and
  crop edits. The final packet log contains no warnings, undefined
  references, overfull boxes, or underfull boxes.
- `solution_packet.pdf` has four pages. Every final page was rendered at 160
  dpi with Ghostscript's RGB PNG device and visually inspected after the last
  source change. All equations, theorem statements, the source crop,
  bibliography, margins, and page transitions are legible; no clipping or
  overlap was found.
- The proof is analytic and uses no computer-assisted assertion.
