# Verification record

Status: `artifact verified; candidate full result pending human mathematical review`

## Mathematical checks

- Re-expanded the two-height identity over the common denominator
  `t-conj(z1)`: its right-hand numerator is
  `1-conj(b2)b(t)+(conj(b2)-conj(b1))b(t)
  =1-conj(b1)b(t)`.
- Checked the vertical multiplier exactly:
  `|(t-conj(z2))/(t-conj(z1))|^2=((t-x)^2+y2^2)/((t-x)^2+y1^2)<=1`.
- Checked the disk inequality by subtraction of squares:
  `|1-conj(a)w|^2-|w-a|^2=(1-|a|^2)(1-|w|^2)`.
- Checked the upper-half-plane Cauchy normalization.  With unnormalized
  Lebesgue measure `dt`, the factor is `1/(2*pi)`, and
  `||1/(t-z)||_s=A_s y^(1/s-1)`.  For `s=q'` this gives the exponent
  `-1/q` used in the packet.
- Recomputed the absorption step:
  `|z1-conj(z2)|=y1+y2<=2y1`, hence the error coefficient contributes at
  most `A_q A_q'/pi` times the lower kernel norm.
- Checked constant, unimodular-constant, `q=2`, and `y2 down to 0` edge
  cases.  The finite boundary case is explicitly conditional on the usual
  `H^q` boundary kernel existing; an infinite lower norm is automatic.

## Artifact checks

- `latexmk` completed successfully after all cross-references stabilized.
- Final log contains no warnings, undefined references, overfull/underfull
  boxes, or errors.
- Poppler reports a four-page, unencrypted letter-size PDF.
- `pdftotext -layout` confirms that the full source question, theorem,
  numbered proof, scope, novelty note, and reference are present.  Overbars
  lost by plain-text extraction were checked directly in the rendered PDF.
- All four pages were rendered at 144 dpi and inspected visually.  Equations,
  conjugation bars, source crops, captions, headings, and page boundaries are
  legible; no clipping or overlap was found.
- Human mathematical review remains pending, as declared in the packet.

## SHA-256

```text
76ee678d4bdc917dca912e6b29845876ba803e977613a5484802e4d4d939dd62  source_paper.pdf
f51e3a93350522e4f703607177d37d11fc0c6dacd9d98a813f9b3ea91dee7c11  solution_packet.pdf
434d1a9451d4df1bb93b06c57afa0d0729f56aa0b7ecc395d17fc1f96052ea72  main.tex
1a39ac1eb7534ad99e32f2c61dacc1b15a7687abc4c9a493c8f316d832775ea3  README.md
e939425745437521682fdb93fb25ec42b2a99ac7d5dc5abd65478193ef3d8095  figures/equation_6_9_context_crop.png
63b3e4cb5019588acdb5c5d1c51c8e27e3029111967005c3b9b386710dd0b7c7  figures/open_problem_crop.png
```
