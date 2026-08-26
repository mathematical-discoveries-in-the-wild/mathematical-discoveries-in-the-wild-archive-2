# Verification record

- Checked the arXiv source and the published-author PDF.  Both display an
  ordinary square in Remark 7.4, and neither imposes real-valuedness on `eta`.
- Re-derived the exact stereographic expression for `I_ell(a)` and the `4 pi`
  normalization from Steps 1--2 of the source proof of Theorem 7.3.
- Checked that the paper's weighted spherical cancellation condition becomes
  `int tan(theta/2) eta(theta) dtheta = 0` for an axisymmetric profile.
- Checked the small-`c` estimate using Markov's polynomial inequality and the
  exact identity `1-cos(2 arctan(at))=2a^2t^2/(1+a^2t^2)`.
- Checked that all integration-by-parts boundary terms vanish because the
  transformed profile is smooth and compactly supported in `[r,R]` with
  `0<r<R<infinity`.
- Checked the order of limits in the tightness argument: first `ell`, then the
  fixed truncation `M`, then the far-tail parameter `A`.
- Checked phase covariance directly: the finite-`ell` left side is invariant
  under `eta -> i eta`, while the printed right side changes sign.
- Compiled `main.tex` with `latexmk` and inspected every rendered page for
  clipping, overlap, broken equations, and unreadable source evidence.

