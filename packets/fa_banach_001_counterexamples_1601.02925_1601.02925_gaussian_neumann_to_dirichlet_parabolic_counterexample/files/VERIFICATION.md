# Verification report

Verdict: `counterexample_likely_valid`.

Verifier: `agent_lane_14` (independent second pass after proof assembly).

## Exact-statement audit

- The current source PDF is arXiv:1601.02925v2. The target is Question 3.4
  on page 11, referring to condition (3.2).
- For the constructed `u`, `Lu=1`; with `f=u_nu`, Gaussian integration by
  parts gives total boundary flux `gamma_2(K)`.
- At `gamma_2(K)=1/2`, the proposed coefficient is `F(1/2)=2`, so the source
  inequality demands energy at least `1/2`.

## Algebra audit

- `w=Phi/phi` obeys `w'=1+xw`, `L_x w=w`, and `L_x w'=2w'`.
- `rho=(1-y^2)/sqrt(2)` obeys `L_y rho=-2rho`, has Gaussian mean zero,
  variance one, and derivative energy two.
- Therefore `u=W+epsilon A w' rho` has `Lu=1` exactly.
- At the origin, `w=sqrt(pi/2)`, `w'=1`, `w''=sqrt(pi/2)`, and `w'''=2`.
- The second-variation quadratic is `1+2AL+2A^2`, with
  `L=(pi+4)/(2sqrt(2pi))`. Its minimum is
  `-(4-pi)^2/(16pi)`.

## Geometry and limiting audit

- The parabolic graph is concave for positive `epsilon`, hence its hypograph
  is convex.
- The volume correction has zero first and second derivatives at zero.
- The ellipse family has positive curvature and its right boundary converges
  pointwise to the parabolic graph while its left boundary tends to minus
  infinity.
- Volume normalization is local near the limiting shift; no global
  monotonicity of Gaussian mass under translation is claimed.
- The constructed energy density has a Gaussian-integrable majorant, so the
  strict parabolic deficit passes to a finite compact ellipse.

## Computational check

Command:

```text
conda run --no-capture-output -n sandbox python code/check_second_variation_and_ellipses.py
```

The exact coefficient identity agrees to `2.84e-16`. A finite check with
`epsilon=0.03`, `R=100`, and numerically normalized volume `0.5` gives energy
`0.49999660148`. This is supporting evidence only; the proof uses the exact
second variation and dominated convergence.

## Remaining human-review focus

Check the Taylor expansion's cross-energy boundary term and the uniform
domination used for the ellipse limit. No unproved mathematical dependency is
known.
