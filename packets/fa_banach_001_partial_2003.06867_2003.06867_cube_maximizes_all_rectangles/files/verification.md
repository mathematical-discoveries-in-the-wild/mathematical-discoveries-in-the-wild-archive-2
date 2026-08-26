# Verification report

## Mathematical checks

- **Brownian convention:** standard Brownian motion has generator
  `(1/2) Delta`; the first Dirichlet eigenvalue in the source is for `-Delta`.
  Therefore `lambda_1(R_a)=(pi^2/4) sum a_k^{-2}`.
- **Laplace transform:** `u(x)=E_x exp(-sT)` solves
  `u''/2=su`, `u(-1)=u(1)=1`, giving
  `u(0)=1/cosh(sqrt(2s))`.
- **Infinite convolution:** with
  `lambda_n=(2n+1)^2 pi^2/8`,
  `sum 1/lambda_n=1`; the exponential sum is finite almost surely and has the
  required product Laplace transform.
- **Log-concavity closure:** exponential laws are log-concave; finite
  convolutions and weak limits are log-concave.  The tail is log-concave by
  applying the set definition to upper rays.
- **Moment range:** the pointwise tail inequality is independent of `p` and
  `E X^p=p integral_0^infinity t^(p-1)P(X>t)dt` is valid for every `p>0`.
- **Starting point:** interval survival is even and decreases away from zero
  (equivalently, apply the parabolic maximum principle to its spatial
  derivative).  Independence then makes zero maximize every rectangular exit
  moment.
- **Equality:** scale invariance requires equality for every homothetic cube,
  not only the unit cube.  The packet states the normalized and unnormalized
  versions separately.

## Adversarial checks

- The Jensen direction is correct: concavity of `log S` makes the balanced
  vector maximize the product at fixed `sum b_k`.
- The scaling is `P(tau_{(-a,a)}>t)=S(t/a^2)=S(a^{-2}t)`.
- Multiplying the stochastic comparison by `lambda_1(R_a)` cancels `bar b`
  exactly.
- The proof does not assume `p>=1`; no convexity of the moment function is
  used beyond monotonicity.
- The full coordinate-symmetric convex-domain conjecture is not inferred from
  the rectangle theorem.

## Reproducibility check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2003.06867_cube_maximizes_all_rectangles/code/check_rectangle_inequality.py
```

The script checks the `cosh` product numerically and samples Jensen gaps for
several unbalanced rectangles.  It is a sanity check, not part of the proof.

## PDF QA

`solution_packet.pdf` was compiled from `main.tex`.  All pages of the final
render were visually inspected; the build log was checked for warnings,
overfull boxes, and unresolved references.
