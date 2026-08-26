# Verification Record

## Analytic checks

- The Fourier coefficient identity for `f(x)=x` was recomputed directly.
- The boundary formula was reduced to a Riemann sum jointly continuous in
  `(u,t)` after defining `sin(ut)/t=u` at `t=0`.
- The lower bound uses only two fixed disjoint rescaled intervals, so the
  `N^-2` Jacobian cancels the `N^-2` denominator exactly.
- The perturbation estimate was checked in the periodic Fourier
  `H^(1/2)` norm and then restricted continuously to the interval.
- Basis coefficients are forced to be Fourier coefficients by the continuous
  embedding `H^(1/2)(-pi,pi) -> L^2(-pi,pi)` and uniqueness in `L^2`.

## Reproducibility

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/0104130_harmonic_near_symmetric_order_obstruction/code/verify_boundary_profile.py
```

The script must print decreasing maximum profile errors for
`N=64,128,256`, a positive separated-interval gap, and `PASS`.

## PDF QA

- `solution_packet.pdf` was compiled from `main.tex` after the required
  one-time artifact-operation marker.
- Every final PDF page was rendered to PNG and visually inspected after the
  latest source edit.
- The LaTeX log was checked for errors, undefined references, and box
  warnings.

Final SHA-256:
`668b0a9f05bf75eabd790514fd4d2f494c2ac2c3a385c07a25e4adc0b55b978f`.
