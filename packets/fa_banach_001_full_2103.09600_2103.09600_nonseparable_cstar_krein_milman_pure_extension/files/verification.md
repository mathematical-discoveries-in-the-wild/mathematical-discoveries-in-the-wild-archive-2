# Verification record

## Mathematical checks

- The BW topology is used only through its finite basic neighborhoods.
- `C*(1,a_1,...,a_m)` is separable for every finite test set.
- The UCP extension fiber is nonempty (Arveson), BW-compact, and a face.
- An extreme point of that fiber is pure; edge cases `t=0,1` were checked.
- Vector compression of a pure extension remains pure by irreducibility/cyclicity.
- Every C*-extreme block actually used in the source's Lemma 5.1 lifts; no claim is
  made that arbitrary C*-extreme maps lift.
- The fixed residual block may be chosen as an amplification of a pure state and also
  lifts.
- Original C*-convex coefficients remain valid after extension, and restriction to the
  separable subalgebra is exact.
- The neighborhood argument proves membership in BW closure without metrizability.

## Source checks

- Open statement: source PDF page 19, Section 5.
- Separable/type-I theorem: source Theorem 5.3.
- Pure-sum approximation: source Lemma 5.1 and proof of Theorem 5.3.
- C*-extremity of the blocks: source Theorem 3.6.

## Artifact checks

- Source PDF copied locally.
- Open-question crop rendered from the source PDF and visually inspected.
- LaTeX built with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Final PDF rendered at 150 dpi after the last edit; every page visually inspected.
