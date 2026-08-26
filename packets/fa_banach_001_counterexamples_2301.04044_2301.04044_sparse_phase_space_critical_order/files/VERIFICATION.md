# Verification record

## Mathematical verification

The proof was checked in the following independent layers.

1. **Symbol estimates.** Each frequency packet has height `R_j^m` and radius
   `R_j^rho`; an alpha-th frequency derivative therefore has size
   `R_j^(m-rho|alpha|)`. Coordinate finite differences are integrals of the
   corresponding derivatives. In the second construction, each beta-th
   spatial derivative contributes exactly `R_j^(delta|beta|)`.
2. **Exact order.** At `(x_0,R_j e_1)` the symbol equals `R_j^m`. A hypothetical
   order `m-epsilon` estimate would force `R_j^epsilon` to remain bounded.
3. **Non-ellipticity.** The symbols vanish outside the packet union (and, in
   the second construction, outside a shrinking spatial support), so no
   uniform elliptic lower bound is possible.
4. **Schatten membership for `rho<1`.** The multiplier is diagonal and its
   j-th packet contributes at most
   `R_j^(mr+rho n)=R_j^(-n(1-rho))` to the r-th power sum.
5. **Hilbert--Schmidt membership for `rho=1,delta>0`.** The exact toroidal
   identity `||Op(a)||_S2^2 = integral sum_k |a(x,k)|^2 dx` applies. Height,
   frequency volume, and spatial volume multiply to
   `R_j^(-n) R_j^n R_j^(-delta n)=R_j^(-delta n)`.

Both geometric series converge for `R_j=Q^j`. No numerical computation is
used in the proof.

## Source and layout verification

- The archived source TeX compiled locally to a 33-page PDF.
- Source PDF page 6 was rendered, cropped at full readable text width, and
  visually inspected; both complete open problems are visible.
- The packet was built with `latexmk`, with intermediates in `tmp/`.
- Every rendered packet page was visually inspected.
- The final log was checked for undefined references, missing citations,
  overfull boxes, and fatal errors.

## Novelty check

A bounded primary-source search through 2026-08-12 used the exact arXiv id and
title, the phrases “non-elliptic m<-n/r Schatten pseudodifferential” and
“toroidal Hormander sparse symbol”, and citation-oriented searches around the
source. It found the source, the foundational toroidal quantization paper, and
a later analogous Fourier-integral-operator problem, but no answer or this
packet construction. Novelty confidence is moderate pending specialist review.
