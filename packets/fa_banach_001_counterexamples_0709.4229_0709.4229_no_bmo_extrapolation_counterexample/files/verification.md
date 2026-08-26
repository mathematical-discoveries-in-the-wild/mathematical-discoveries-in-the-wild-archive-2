# Verification record

Status: all analytic, computational, source-evidence, build, and visual checks
completed; candidate remains `counterexample_likely_valid` pending independent
expert review.

## Analytic audit

- The intervals `I_n` are pairwise disjoint dyadic atoms at generation
  `m_n=n+1`.
- Each local Rademacher term is exactly one global martingale difference.
- At each global level only finitely many `(n,k)` pairs occur.
- The symbol is strongly measurable and Bochner integrable in operator norm;
  it actually lies in every finite `L^q(T;M)`.
- The paraproduct series converges in `L^2` with norm at most one by
  martingale orthogonality, orthogonal matrix-corner ranges, conditional
  expectation contraction, and the row identity
  `||e_(1,k)x||_2=||e_(k,k)x||_2`.
- The test projection has Schatten norm `n^(1/p)`, while its image is a
  rank-one row with norm `sqrt(n)`, producing the divergent ratio
  `n^(1/2-1/p)` for every `p>2`.
- On `I_n` the symbol average is zero and its operator norm is `sqrt(n)`, so
  its source-paper `BMO_M` norm is infinite.
- The weighted product-algebra variant gives the same ratio in a finite
  tracial algebra.

## Computational check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/0709.4229_no_bmo_extrapolation_counterexample/code/verify_counterexample.py
```

Result: PASS on all checks.

## Source evidence

`figures/open_problem_crop.png` is rendered directly from official arXiv PDF
page 9 by `code/make_source_crop.py`; it is not a retyped image.

## Remaining reviewer focus

1. Confirm the literal scope of “remove the assumption” includes the source's
   ambient Bochner-integrable `M`-valued symbols.
2. Recheck the orthogonality when several matrix blocks occur at the same
   global martingale level.
3. Check the bounded novelty search independently.

## Render QA

Compiled with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
pdftoppm -png -r 150 solution_packet.pdf tmp/final_render/page
```

Final PDF: 5 letter-sized pages, 295,995 bytes.  The final LaTeX log has no
undefined references, overfull boxes, or underfull boxes.  All five rendered
pages were inspected individually at 150 dpi on 2026-08-11.  The source crop
is full-width and legible; all displayed formulas, page breaks, references,
and margins are clean.

SHA-256:

```text
solution_packet.pdf  7c4252c0c7d7eaa9453e303f9467367339baf8d15acb40a2a90dc43658e528b9
source_paper.pdf     4ae8c8c5b1bc1a32be201313cafc7e293c5e08f21ae58ce35a53cc5755ba6650
open_problem_crop    6cafe127fb3bf713a59d791c8fbee9c4a276abcc85ce9cd1c7fff0f7636cf59d
```
