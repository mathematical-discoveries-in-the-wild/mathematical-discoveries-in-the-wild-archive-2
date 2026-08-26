# Verification

Status: candidate full counterexample; mathematical, source, build, and visual
checks completed on 12 August 2026.

## Mathematical checks

- `F=L^1([0,1])` is a Banach right `C([0,1])`-module under pointwise
  multiplication, since `||xa||_1 <= ||x||_1 ||a||_infty`.
- The action is unital, so `F C([0,1])=F`; in particular the module is
  essential in the source paper's sense.
- For fixed `omega`, the cutoff `a_m(t)=min(1,m|t-omega|)` is continuous,
  vanishes at `omega`, is bounded by one, and hence belongs to `K_omega`.
- The cutoffs converge to one outside the singleton `{omega}`.  This is
  almost-everywhere convergence for Lebesgue measure, and
  `|xa_m-x| <= |x|`; dominated convergence therefore gives
  `||xa_m-x||_1 -> 0` for every `x in F`.
- Thus every `x` is in `closure(F K_omega)`, so `K_omega^F=F` for every
  `omega`.  Every quotient fiber is zero and the canonical map is the zero
  map on the nonzero space `F`, proving noninjectivity.
- The stated `L^p` extension was checked independently: atomlessness gives
  `mu({omega})=0`, regularity supplies neighborhoods of arbitrarily small
  measure, normality supplies Urysohn cutoffs, and absolute continuity of
  the integral of `|x|^p` gives norm convergence.
- Scope was audited: this refutes the injectivity question and the proposed
  proof route in Remark 4.10(b), but does not by itself refute the broader
  assertion about all local maps.

## Novelty and source checks

- The official arXiv source PDF has 18 A4 pages; Remark 4.10(b) on printed
  page 13 was inspected visually and matches the question stated in the
  packet.
- The source passage is embedded from the visually inspected crop
  `figures/source_open_question.png`.
- Cheap run-index searches found no prior packet or ledger for this problem.
- Bounded exact-phrase, title/citation, canonical-fiber, and `L^1`-module
  searches found the source and background literature but no published
  answer matching this counterexample.  This is a bounded novelty check,
  not a priority claim.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully after the final edit.
- The final log has no warnings, overfull boxes, underfull boxes, undefined
  references, or multiply-defined labels.
- Final artifact: two A4 pages, 218471 bytes, PDF 1.7, unencrypted.
- Both pages were rasterized at 150 dpi and inspected at original detail.
  The title, mathematics, embedded source excerpt, proof, corollary, scope,
  references, margins, and page breaks are clear; no clipping, overlap, or
  stray glyphs were found.
- Ghostscript text extraction was inspected through the full document and
  contains the theorem, proof, scope qualification, and reference.

## Artifact hashes (SHA-256)

- `solution_packet.pdf`:
  `c44e09477d3c3ce81ca1338c231662f61e8b0a68cd6da4e19f8a5d44513b38af`
- `source_paper.pdf`:
  `2be0cf73043a8323ee34d7d9499674a190360db55a024ec5e34a1fc3f55bf447`
- `figures/source_open_question.png`:
  `14516d3221a53f565262196e50fd07d879c1675ed1b4f9ed2234212d8dfc68a2`
- `attempts/1005.4561_canonical_bundle_injectivity_counterexample.md`:
  `22fc3efed8c988ecc282f98d1975e0a3f79150185afbcbeb8452e560cf3ea861`
