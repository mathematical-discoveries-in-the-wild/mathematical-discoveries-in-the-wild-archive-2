# Verification report

## Claim audited

Open Problem 1 of arXiv:1209.2970 is true at `p=3/2`; since the source proves
failure below `3/2`, this is the optimal exponent and also answers Open
Problem 2.

## Analytic checks

1. Weighted duality was recomputed: the dual of
   `L^(3/2)(sin^(1/2)t dt)` is `L^3(dt/sin t)`.
2. The harmonic sine mode `r^k sin(kt)` has upper-half-disk energy `pi*k/2`.
3. `(1+e^(it))/(1-e^(it)) = i*cot(t/2)` and
   `|d log(cot(t/2))/dt| = 1/sin t`, so the conformal boundary Jacobian is
   exact.
4. The strip trace multiplier is `|xi| coth((pi/2)|xi|)`, with zero-frequency
   limit `2/pi`; it controls the inhomogeneous `H^(1/2)(R)` norm.
5. Hausdorff--Young plus Holder proves `H^(1/2)(R) -> L^3(R)`; the remaining
   weight is integrable because `(1+xi^2)^(-3/2)` is integrable.
6. For `sigma=mu-nu`, the logarithmic kernel gives
   `Hcal=2 sum m_k^2/k`, while
   `sin(t) Hsigma(2cos t) = -2 sum m_k sin(kt)` distributionally.
7. The semicircle substitution gives exactly
   `integral |Hsigma|^(3/2) d alpha = (2/pi) integral |F|^(3/2) sin^(1/2)t dt`.
8. The source's explicit family rules out every `p<3/2`; probability-space
   norm monotonicity propagates the endpoint estimate to every larger `p`.

## Independent sanity check

`code/numerical_sanity.py` evaluates random finite sine polynomials of degrees
4--64. It is an optional check only and no numerical bound is used in the
proof.

## Search and novelty audit

The run's cheap indexes had no exact 1209.2970 packet. Bounded web and arXiv
searches used the exact paper title/id, quoted endpoint text, exact
sine-series weights, `free Log-Sobolev 3/2 Popescu`, and the author's later
arXiv:1511.05274. The later paper was searched at source level for `3/2`,
`open problem`, and the original citation; no resolution was found. No paper
claiming the endpoint or this conformal-strip proof was located. Novelty
confidence is moderate.

## Artifact QA

- `main.tex` compiled successfully with two `pdflatex` passes.
- The final log has no undefined-reference, overfull-box, underfull-box, or
  multiply-defined-label warning.
- `solution_packet.pdf` is a five-page, letter-size PDF 1.7 document.
- Ghostscript `txtwrite` extraction recovered the main theorem, both lemmas,
  the measure passage, all nine numbered displays, and the reference.
- All five pages were rasterized at 140 dpi and visually inspected. The source
  crop, equations, page breaks, theorem text, proof endings, and links are
  legible with no clipping or overlap.
- `source_paper.pdf` is the official 18-page arXiv PDF and opens as PDF 1.5.
- The open-problem crop was rendered from source page 16 at 160 dpi and
  visually checked against the page.
- The optional numerical check ran for degrees 4, 8, 16, 32, and 64 with no
  anomalous growth in the tested ratios.
- SHA-256 of the final packet:
  `13f96c1858b827a832926d632417d5faf01513ca2b130f3fd5185fd3616d47bf`.
