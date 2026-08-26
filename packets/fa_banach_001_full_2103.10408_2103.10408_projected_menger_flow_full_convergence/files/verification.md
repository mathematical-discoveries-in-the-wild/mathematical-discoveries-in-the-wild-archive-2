# Verification record

## Classification

- Result type: candidate full proof.
- Mathematical target: full convergence of the projected flow asked about on
  PDF page 5 of arXiv:2103.10408.
- Excluded target: the ordinary unprojected ambient flow.

## Source checks

- `source_paper.pdf`, page 5: exact question and Corollary 1.4.
- arXiv:1308.2499, Proposition 4.1 and Lemma 4.2: Fourier multiplier
  `rho_k ~ c |k|^(3p-4)` and structural lower-order remainder.
- arXiv:2505.02719: Hilbert submanifold/Palais--Smale framework and the
  analogous pure tangent-point argument; the introduction explicitly notes
  that the pure Menger result carries over.
- arXiv:2511.07214: abstract Lojasiewicz--Simon theorem and full-convergence
  finite-length argument for arclength-restricted knot-energy flows.

## Novelty search

Bounded searches through 2026-08-13 used:

- exact source title and arXiv id;
- `full convergence integral Menger curvature`;
- `Lojasiewicz Simon Menger curvature`;
- `projected critical point Menger gradient flow`;
- authors Knappmann, Schumacher, Steenebruegge, von der Mosel, Freches, and
  Doehrer.

No paper claiming the packet theorem was found.  arXiv:2511.07214 is limited
to tangent-point energy.  arXiv:2505.02719 supplies Palais--Smale and strong
subconvergence technology, not full Menger-flow convergence.  Novelty
confidence: moderate, pending a specialist database/citation search.

## Internal proof audit

- Parameter identity checked: with `s=3p/2-2`, the multiplier order
  `3p-4` equals `2s`.
- The fixed-speed pullback uses one time-independent Sobolev diffeomorphism,
  so it induces an equivalent fixed Hilbert metric rather than a
  time-dependent metric.
- The barycenter/point constraint removes the constant kernel of `Q`.
- The source energy identity gives `dE/dt=-||grad_M E||^2` and the source
  proves the projected gradient tends to zero.
- In the Palais--Smale projection defect, the small norm is an intermediate
  `H^r` norm with `3/2<r<s`, obtained by compact interpolation; no unsupported
  `C^1 -> H^s` implication is used.
- The Lojasiewicz--Simon inequality plus one strong accumulation point gives
  finite tail length and hence full convergence.

## Reviewer focus

The main technical audit is the compact-remainder estimate in Lemma 3 of the
packet.  It is obtained by differentiating the finite structural
representation in Blatt--Reiter and applying the same fractional Leibniz
estimate with a small positive Sobolev gain.  A reviewer should confirm that
the gain remains uniform for every differentiated summand.

## Render checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed without unresolved references, warnings, or overfull boxes.
- Final packet: 7 US-letter pages.
- All seven pages were rendered at 150 dpi and visually inspected at original
  resolution.  The evidence crop is readable, all displayed formulas stay
  inside the margins, and no page has overlap or clipping.
- Final SHA-256 hashes:
  - `solution_packet.pdf`: `7fae28284d0d1f2bc8960999ecbe25b5981d1f73e51b40e1f011a0324a48c9bc`
  - `source_paper.pdf`: `d4463cbca6000068474094195f953d3933eb6baab14cd02f338fce63970ef450`
  - `supporting_paper_1308.2499.pdf`: `3b20abdc0e1b0ba9efe4819ac385e38fa76fa0f0714465753cb931a49666c5bb`
  - `supporting_paper_2505.02719.pdf`: `1803d10aa55c18cf0c92c3c0a19755f22dd355dd84c8a9406dfae09898d2b013`
  - `supporting_paper_2511.07214.pdf`: `836d9910d0a26e3be12cfe8171c600b660cbcaadda5bbd80f5e2d42529a559f0`
