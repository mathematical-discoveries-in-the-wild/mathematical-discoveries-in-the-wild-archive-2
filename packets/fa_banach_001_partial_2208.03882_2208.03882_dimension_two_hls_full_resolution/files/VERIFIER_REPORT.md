# Verification Report

Candidate: arXiv:2208.03882, complete dimension-two resolution

## Verdict

`likely valid` (substantial partial result; full fixed-dimension answer)

## Claims checked

1. The source inequality is exactly a norm-one estimate for its normalized
   spherical Fourier operator.
2. In dimension two and `0<p<1`, the operator is the sharp circle HLS
   operator after a quarter-turn and angle doubling.
3. HLS extremizers correspond exactly to centered ellipses.
4. The multiplier identity `I_(2-p) I_p=Id` proves the reverse inequality
   for `1<p<2`.

## Adversarial proof audit

| Step | Status | Notes |
| --- | --- | --- |
| Exact source scope | valid | Source PDF p. 3 asks both inequalities for real `0<p<n`, reversing at `n/2`, with ellipsoid equality. It separately notes Parseval equality for all bodies at `p=n/2`. |
| Norm reformulation | valid | For `f=rho_K^(n-p)`, the input exponent produces `rho_K^n`, and polar integration gives `integral f^(n/(n-p))=vol(K)/kappa_n`. The source normalization has `I_p 1=1`. |
| Projective measure | valid | An even circle function is pi-periodic; normalized `S^1` measure over `0,2pi` equals `dtheta/pi` over one projective period. |
| Kernel formula | valid | The source formula for `0<p<1` specializes to the displayed gamma coefficient. Shifting the output by `pi/2` changes absolute cosine to absolute sine. |
| Kernel mass | valid | The beta integral gives exactly the reciprocal gamma coefficient, confirming `I_p 1=1`. |
| HLS exponent | valid | In circle dimension one with kernel exponent `p`, the diagonal HLS exponent is `2/(2-p)` and its dual is `2/p`, precisely the source pair for `n=2`. |
| Angle doubling | valid | `x=2theta` maps projective normalized measure to normalized circle measure and `2|sin(theta-phi)|=|e^(ix)-e^(iy)|`. All factors are absorbed by evaluating the sharp constant on constants. |
| Operator bound | valid | Bilinear HLS plus duality gives the required `L^(2/(2-p)) -> L^(2/p)` norm bound; the quarter-turn is an isometry. |
| Equality geometry | valid | The HLS denominator is a positive quadratic form with eigenvalues `(1-r)^2,(1+r)^2`; taking the radial root gives exactly a centered ellipse. |
| Fourier inversion | valid | The degree-`2j` gamma-ratio multipliers at `p` and `2-p` are reciprocal, and the two phases multiply to one. |
| Reverse inequality | valid | Applying the upper estimate for `q=2-p` to `h=I_p f` gives `||f||<=||I_p f||` with the desired exponents. |
| Reverse equality | valid | HLS classification gives `h=C Q^(-p/2)` and its equality equation gives `f=C'Q^(-(2-p)/2)`, again an ellipse. |
| Parseval midpoint | valid | At `p=1=n/2`, all multiplier moduli equal one and the source's Parseval identity gives equality for every body. |

## Counterexample and loophole search

- Omitting the Fourier phase creates false numerical violations. The durable
  script includes `(-1)^(degree/2)`, and corrected searches converge to
  ellipsoids.
- The reverse inequality is stated on the natural Fourier domain. If the
  transform is not an `L^(2/p)` function, its extended norm is infinite, so
  it cannot produce a finite counterexample.
- The equality exception at `p=1` is stated explicitly and does not conflict
  with the source's own midpoint paragraph.
- The proof does not claim a higher-dimensional HLS reduction: orthogonality
  is a hypersurface there rather than the diagonal.

## Literature audit

Bounded primary-source searches through 2026-08-17 covered the exact paper,
the sharp HLS theorem, projective-circle formulations, later generalized
intersection inequalities, and arXiv:2211.16263. The latter proves the
upper-side subfamily `0<p<1`, `n/p` integral after translating notation, but
not continuous `p` or the full dimension-two statement. No exact prior
dimension-two resolution was found. Novelty is plausible, not certified.

## Rendering audit

Compiled with `latexmk` under TeX Live 2026.  The final packet has three US
Letter pages.  All three pages were rasterized at 150 dpi with Poppler and
inspected at original resolution: no clipping, overlap, missing glyphs,
broken equations, or illegible source material was found.

Final SHA-256 values:

- `solution_packet.pdf`: `f141afb788de80aa5f5f0269f3127e8cb55ac662bd1d794b943ce56c507344b0`
- `source_paper.pdf`: `e4fc8ab0b4355aec7bd5428be77f5c98d9b167d7d4164a527dbe9400c180f0db`
- `main.tex`: `36ecff5b733fdc4d008315b9a03455c259a18b096dc530f6bb9665d7e50483b6`
- `figures/open_question_crop.png`: `1214781f80dc086d8d33d4a487af26624b1d90c8e543574e5782ff2ae74c75f8`

## Confidence

Score after mathematical and typography audit: 97/100.

Residual uncertainty concerns literature novelty and the preferred
functional-domain convention for the raw Fourier transform in the reverse
half, not the smooth-body proof.

## Human review recommendation

`send to human`

Primary review focus: normalized constant under angle doubling and the
natural-domain wording for `1<p<2`.
