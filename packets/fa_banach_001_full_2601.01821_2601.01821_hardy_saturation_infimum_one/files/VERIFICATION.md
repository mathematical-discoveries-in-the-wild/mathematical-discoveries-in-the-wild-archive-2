# Verification record

## Mathematical checks

1. The source's Theorem 1 supplies the lower bound
   `||U_{psi,psi}-I|| >= 1` for every generator in the class and every
   `0<p<=1`.
2. The smooth radial annular generator constructed in the source has a smooth
   dilation-periodic Calderon multiplier. Standard anisotropic Hardy
   multiplier boundedness therefore gives a finite operator norm `M_p`.
3. Positive scalar multiplication preserves all decay, moment, radiality, and
   support hypotheses. The source itself explicitly makes this rescaling in
   the proof of its Hilbert-endpoint proposition.
4. Directly from the frame-operator definition,
   `U_{t psi,t psi}=t^2 U_{psi,psi}` for real `t>0`.
5. The same exact `p`-power quasi-triangle inequality used by the source yields
   the upper bound `(1+t^(2p) M_p^p)^(1/p)`, which converges to one.

No numerical or symbolic computation is part of the proof.

## Source and layout checks

- The archived arXiv TeX compiled locally to a 20-page PDF.
- PDF page 15, containing the complete source problem statement, was rendered
  at 180 dpi and visually checked.
- The candidate packet was compiled with `latexmk` into `tmp/`.
- All packet pages were rendered to PNG and visually checked.
- The final build was checked for undefined references, overfull boxes, and
  missing citations.

## Novelty boundary

A bounded primary-source search through 2026-08-12 used the exact arXiv id and
title plus “saturation infimum”, `epsilon_p`, anisotropic Hardy wavelets, and
scalar rescaling/damping. No later primary-source resolution was found. This
is not exhaustive historical proof of novelty; specialist review is required
before a priority claim.
