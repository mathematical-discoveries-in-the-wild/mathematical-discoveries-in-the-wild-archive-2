# Verification record

## Proof checks

- Parameters are consistent: `0<alpha<beta`,
  `alpha=1/sigma-1/p`, and `q=min(sigma,2)` are exactly the range in which the
  source proves both `A_q^alpha -> V_{sigma,p}` and
  `V_{sigma,p} -> A_infinity^alpha` under BI.
- For a coordinate projection with at most `2^n` coefficients, rearranged
  selected coefficients satisfy `b_m <= a_m`; the `A_infinity` envelope
  bounds each of the `n+1` dyadic `A_q` summands. This yields precisely
  `(n+1)^(1/q)`, including `q<1`.
- The greedy set is selected only once from `f`. Thereafter its coordinate
  projection is linear, so applying it separately to `g` and `f-g` is valid.
- Unconditionality bounds that fixed coordinate projection on `L^p` uniformly.
- Every `N`-term Phi combination belongs to `Sigma_(nu N)^C`; the source's
  Bernstein estimate therefore gives `||P_Lambda h||_V <= C N^alpha
  ||P_Lambda h||_p`, with the fixed `nu^alpha` absorbed in `C`.
- The outside scale is `N^(-alpha)`, so its product with the Bernstein factor
  is exactly one.
- Greediness plus source equation (4.9) controls the approximation error of
  an arbitrary K-functional competitor.
- The lower K-functional bound is immediate because the finite greedy
  approximant belongs to the variation space.
- Only a two-term quasi-triangle inequality is used when `sigma<1`.

## Upgrade attempts and computation

Eight distinct routes are recorded in
`attempts/2310.17309_greedy_kfunctional_upgrade.md`: direct ring estimates,
endpoint interpolation, balanced-tree counterexample search, adaptation of
the source's bad-chain example, the modulus formula, Abelization, block-greedy
projections, and a literature/theorem audit.

`code/finite_tree_search.py` evaluates `V_{1,2}` exactly on finite dyadic
trees by a binary linear program over all disjoint atoms and rings. Random
searches produced maximum full-norm greedy ratios `1.010860` at depth 4 over
120 trials and `1.004614` at depth 5 over 50 trials. These finite experiments
neither prove boundedness nor rule out a counterexample and are not used in
the theorem.

## Provenance and literature audit

- `source_paper.pdf` was downloaded from the official arXiv PDF endpoint on
  12 August 2026.
- PDF page 19 contains the open question as equation (4.3) and explicitly
  reduces it to greedy boundedness on the variation space.
- The required screenshot is rendered from a vector crop of that source page
  and includes the complete question and surrounding hypotheses.
- Cheap run indexes and bounded searches by the exact id/title and core terms
  found no later explicit resolution through 12 August 2026. This is a
  bounded novelty audit, not a priority claim.

## Packet QA

- LaTeX build: passed twice with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error`; the final packet has four pages.
- Warning scan: passed; the final log contains no `Warning`, `Overfull`,
  `Underfull`, `undefined`, or `multiply defined` entries.
- Rendered-page inspection: passed at 140 dpi for all four pages. The source
  passage is readable at normal review zoom, all displays are legible, and no
  page has clipping, overlap, orphaned headings, or stray literal markup.
- Text-extraction audit: passed for every page; page 2 is intentionally an
  image plus caption and therefore has only caption text in extraction.
- Final SHA-256:
  `9beafd754cf0b357e678269f139404e7627662bdfc819c9a6bb7137f2733ba01`.
