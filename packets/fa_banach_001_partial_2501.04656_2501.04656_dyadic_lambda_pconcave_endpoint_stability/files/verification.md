# Verification record

## Mathematical checks

1. The nested `p`-mean coefficients were expanded directly; after combining
   the two endpoint points, their relative barycentric weights are
   `r(1-t)/(1-rt)` and `(1-r)/(1-rt)`.
2. The zero convention in the source definition was checked separately: any
   nested term involving a zero input is zero, while all positive terms are
   covered by the power/logarithm calculation.
3. The Borell--Brascamp--Lieb exponent is `q=p/(np+1)`.  Backward iteration
   was checked in the three cases `q>0`, `q=0`, and `q<0`.
4. The midpoint theorem is invoked only at weight `1/2`; hence its constant
   depends on `n,p` but not on the dyadic depth.
5. The cube lower bound allows arbitrary translations and arbitrary common
   approximants: the triangle inequality reduces it to the maximal overlap
   of a unit cube and a translated larger cube.

Run the symbolic verifier with:

```bash
conda run --no-capture-output -n sandbox python code/verify_cube_expansion.py
```

Expected output reports four `PASS` checks, including the quadratic deficit
coefficient `n*lambda*(1-lambda)*(n*p+1)` and distance coefficient `2*n`.

## Source evidence

`figures/source_question_crop.png` is cropped from page 5 of
`source_paper.pdf` and contains Remark 1.8, including both the endpoint-
parameter observation and the exact future-work question about
`sqrt(delta/lambda)`.

## Packet QA

The final PDF is compiled into `tmp/`, copied to the packet root, checked for
LaTeX warnings, rendered page-by-page, and visually inspected.

- Final length: 4 pages.
- Final warning scan: no warnings, overfull boxes, underfull boxes, undefined
  references, or multiply defined labels.
- Ghostscript null-device validation: passed.
- All four RGB page renders at 160 dpi were visually inspected; no clipping,
  overlap, malformed equations, missing glyphs, or stray source-crop text was
  found.
- `solution_packet.pdf` SHA-256:
  `4a45528110ed35fa38eed8874556f9dfea23288a132794d595145654660a3652`.
- `source_paper.pdf` SHA-256:
  `ef85d6218db753b04acb67eed933814c66751a23cc436d997469f714b5325ac7`.
