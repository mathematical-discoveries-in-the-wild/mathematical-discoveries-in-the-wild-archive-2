# Verification record

Status: `artifact verified; substantial partial result pending human review`

## Mathematical checks

- Re-read the arXiv PDF, not only the source TeX.  PDF p. 11 prints
  `(2^k sqrt(t))^n` in Lemma 3.4(B), while the mean defining `g^(j,t)` is
  taken on the fixed side-`2 sqrt(t)` cube.
- Checked the one-dimensional cube geometry with the source convention that
  `Q(a,s)` has side length `s`: for `R=2^k`, the outer cube is `[0,2R]`
  and the `k`th annulus contains `[0,R/2]`.
- Checked that the smooth cutoff can be zero on `[R-1,R+1]`, one on the
  entire annulus, and compactly supported with its outer transition beyond
  `[0,2R]`.
- Recomputed the counterexample numerator:
  `N_k <= 4 + 2R*gamma([R-2,R+2])`; after division by `R=2^k`, it tends to
  zero, while the annular Gaussian mass tends to `1/2`.
- Checked admissibility of the standard Gaussian under the source condition:
  `(1-epsilon)|V'|^2/2-V''=(1-epsilon)x^2/2-1` tends to infinity.
- Derived the corrected local estimate directly from Jensen on the actual
  mean cube.  Its volume is a dimensional constant times `t^(n/2)`.
- Re-ran the global counting: enlarged-cube multiplicity contributes
  `2^(kn)` and the lower endpoint of the `t` integral contributes
  `2^(k(n+alpha))`, giving the safe total `2^(k(2n+alpha))`.
- Checked the dyadic tail
  `sum 2^(beta k) exp(-c 2^k)` from its first admissible scale; it is bounded
  by `C exp(-c' r)`, so the repaired source theorem has the claimed kernel.
- Checked the `L^p` interpolation exponent separately on `(1,2]` and
  `[2,infinity)`, obtaining `theta_p=2 min(1/p,1/p')`.
- The intended global `L^p` square-function comparison is explicitly not
  claimed; the remaining vector-valued step is recorded as a limitation.

## Artifact checks

- `latexmk` completed with stable cross-references and no warnings, errors,
  overfull boxes, or underfull boxes.
- Poppler reports a five-page, unencrypted letter-size PDF.
- `pdftotext -layout` confirms the source transcription, counterexample,
  corrected lemma, repaired summation, scalar `L^p` lemma, limitations, and
  references are present.
- All five pages were rendered at 144 dpi and inspected visually.  Both
  source crops and their captions remain together; equations, superscripts,
  headings, and page boundaries are legible with no clipping or overlap.
- Human mathematical review remains pending, as declared in the packet.

## SHA-256

```text
9d2337e2c90a7bd9a5a71e44c50e4995807f3b9b5b7ea48f18dec52e1569802d  source_paper.pdf
c14c5b3d91b062146a881860e5f26e4694cb5a47aed6f5afc5d62d57e3bb3b82  solution_packet.pdf
8c2dc2146b0353e8c237a486626854db6dcd816c9edf48f9575903b4f7bcdcbe  main.tex
6d82920a6914fe343efa110f4e55e6d8d202d83213e4ce38e98f95d07999907c  README.md
09d42b5f5f55de142048f63d34bb180d8a42296424fd62f485672dfba68a3859  figures/lemma_3_4_B_crop.png
88b405da24eb578e89da98b9a476993181e2f2a122a2b68ef0193285165b144a  figures/proof_and_lp_question_crop.png
```

