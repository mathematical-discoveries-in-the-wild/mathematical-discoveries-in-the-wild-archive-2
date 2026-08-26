# General-p Toeplitz-kernel partial result

This packet addresses the two explicit open questions on compiled source PDF
pages 14 and 19 of arXiv:1507.05797.

Main proved results:

1. For every `1<p<infinity`, `ker T_g` lies in `H_infinity` exactly when the
   `H^q` distances from the Cauchy kernels to the closed range of
   `T_{conj(g)}` are uniformly bounded.
2. Every Toeplitz kernel with an exact representation `w K_theta^p`, with `w`
   outer, has `w` as a minimal function.  The same representation gives an
   exact weighted evaluation-distance boundedness criterion.

The result is classified as partial because the known general-`p`
extremal representation contains an integrability intersection.  Removing
that intersection—equivalently obtaining a universal outer-multiplier
model-space representation away from `p=2`—remains the unresolved bridge.

Build the packet with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=solution_packet main.tex
```
