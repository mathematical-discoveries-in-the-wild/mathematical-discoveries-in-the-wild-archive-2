# Verification Report

Candidate: arXiv:2405.04989, Riesz--Feller RKHS/sampling theorem and endpoint
obstructions

## Verdict

`likely valid` (substantial partial resolution of both Section 6 outlook
directions)

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Source scope | valid | The source explicitly asks for a Whittaker--Shannon extension, numerical reconstruction, and an RKHS analysis, then separately proposes `p<=1` and `p=infinity`. The packet states its `p=2` and endpoint-obstruction scope. |
| Source multiplier | valid | The piecewise multiplier is exactly the Fourier representation in the source: the negative Hardy projection for positive height, the identity at the boundary, and the positive projection with skew phase for negative height. |
| Uniform multiplier bound | valid | Admissibility puts `theta` in `(1/2,3/2)`, hence `cos(pi theta)<0`; both half-space scalar exponentials have modulus at most one. The angular Hardy projections have a finite uniform operator norm on the finite-dimensional Clifford coefficient space. |
| Boundary RKHS | valid | Compact Fourier support makes evaluation bounded by Cauchy--Schwarz. Fourier inversion of the ball indicator gives the stated Bessel kernel and the correct diagonal value. |
| Spacetime RKHS | valid | The kernel is `E_z E_w^*`, so positivity and reproduction are automatic. At zero heights it reduces to the boundary kernel. |
| Fourier-series coefficient | valid | On `Q=[-Omega,Omega]^n`, the coefficient is `a^n f(ak)` for `a=pi/Omega` under the source Fourier convention. |
| Clifford order | valid | The multiplier acts on the left. After expanding `f_hat`, the integrated multiplier kernel remains on the left and the sample `f(ak)` remains on the right. |
| Boundary Shannon kernel | valid | At height zero, direct integration over `Q` gives `prod_j sinc(Omega x_j-pi k_j)`. |
| Parseval identity | valid | Fourier-series Parseval plus the source Euclidean Plancherel normalization gives exactly `||f||_2^2=a^n sum |f(ak)|_0^2`. |
| Uniform truncation bound | valid | The multiplier gives the slice `L2` estimate. Evaluation of a `Q`-bandlimited function contributes `a^{-n/2}`, which exactly cancels the `a^{n/2}` from sample Parseval. |
| `L1` obstruction | valid | `f=(sin x/x)^2` has triangular Fourier transform. Direct inversion after multiplication by `-i sign(xi)` gives `Hf=1/x-sin(2x)/(2x^2)`, whose absolute integral diverges logarithmically. |
| `L-infinity` obstruction | valid | For `g=(2/pi)Si`, `g'=(2/pi)sin x/x` is bandlimited. Commuting the Hilbert transform with differentiation gives `(Hg)'=(2/pi)(1-cos x)/x`, and integration gives logarithmic growth. |
| Bandpass repair | valid | Localizing `-i xi/|xi|` away from zero makes it smooth and compactly supported. Its inverse Fourier transform is Schwartz, so Young's inequality works at both endpoints. |

## Computational verification

The deterministic verifier checks:

- the exact sampling Parseval constant for `(sin x/x)^2`;
- improving tensor-sinc reconstruction at cutoffs 40 and 120;
- the logarithmic `L1` divergence with asymptotic slope one;
- the logarithmic `L-infinity` growth with slope `2/pi`;
- propagation of the same samples through a one-dimensional fractional Hardy
  multiplier (`alpha=0.8`, height `0.7`); and
- the proved uniform error bound against the omitted sample `ell2` tail.

All checks pass.

## Counterexample and loophole search

- The theorem uses a containing cube, not a ball-adapted critical sampling
  set. This is deliberate oversampling and does not lose exactness.
- Closed-ball versus open-ball support is irrelevant in `L2`, since the
  boundary has measure zero.
- The source solution is piecewise in the height variable. The reconstruction
  respects that piecewise multiplier and makes no continuity claim across
  height zero beyond the source convention.
- The endpoint examples disprove only the same-space Hardy splitting, not the
  sophisticated `H1/BMO` theory anticipated in the source.
- Clifford boundary sampling was already known in 2007. Novelty is not claimed
  for componentwise Shannon sampling itself.

## Confidence

Score: 98/100

Residual uncertainty is bibliographic novelty and the preferred adjoint
notation for a complexified Clifford module, not the Fourier-series proof or
the endpoint examples.

## Human review recommendation

`send to human`

Check the operator-valued kernel convention, multiplier handedness, and
whether the stable spacetime formula merits promotion beyond a substantial
partial result given the broad wording of the outlook.
