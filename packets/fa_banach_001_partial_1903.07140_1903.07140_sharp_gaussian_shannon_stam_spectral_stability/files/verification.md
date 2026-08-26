# Verification

## Mathematical checks

- Common whitening sends the average covariance `C` to the identity and the
  two covariances to `I+A` and `I-A`.
- Positive definiteness gives every eigenvalue of `A` in `(-1,1)`.
- The Gaussian relative-entropy formula was substituted directly; all trace
  terms cancel in the deficit and in the sum of the two input entropies.
- For `lambda <= 1/2`, the lower scalar inequality is exactly concavity of
  `log` at `1-ca = c(1-a)+(1-c)`.
- The derivative of `log(1-ca)+c log(1+a)` has sign opposite to `a`, proving
  the upper scalar inequality.
- Swapping `X,Y` sends `(lambda,a)` to `(1-lambda,-a)`, covering the full
  parameter interval.
- One-dimensional limits `a -> -1` and `a -> 1` verify sharpness of both
  constants.
- Direct substitution at `lambda=1/2` gives the claimed exact identity.

## Scope checks

- The theorem assumes positive definite Gaussian covariances; singular
  endpoint behavior is used only as a limit for optimality.
- In the source normalization `Sigma_X+Sigma_Y=2I`, the reference `G_C` is
  exactly the standard Gaussian.
- No claim is made that the Poincare exponent is improved for arbitrary
  non-Gaussian log-concave pairs.
- The nonlinear residual obstructing the extension is stated explicitly in
  the packet and explored in the separate attempt note.

## Build and visual checks

- `latexmk` completed successfully with all references resolved.
- The final packet has four pages.
- All four pages were rendered to PNG at 130 dpi and visually inspected.
- The source crop is legible and complete; no text, equations, or page content
  is clipped or overlapping.
