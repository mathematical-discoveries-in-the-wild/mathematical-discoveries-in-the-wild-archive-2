# Verification report

## Verdict

`candidate_full_counterexamples_likely_valid`

The two examples satisfy the source definitions and directly negate the two
general questions. No computational assumption is used.

## Base function

For `u in ell_2`, define `g(u)=sum k(2u_k)^(2k)`.

- Since `u_k -> 0`, the tail is dominated by `sum k q^(2k)` for some `q<1`.
- The same domination persists in a sufficiently small norm neighborhood of
  each `u`, so the convergence is locally uniform.
- On the complexification, the summands are holomorphic coordinate
  polynomials. Local uniform convergence proves holomorphy there, hence real
  analyticity on the real form.
- Every summand is nonnegative on real inputs, and
  `g((1/2)e_n)=n` exactly.

## Semigroup checks

Let `X=ell_2(R) direct-sum_2 R`, `D=B_X`,
`R(u)=sqrt(1-||u||^2)`, and
`y(u,sigma)=artanh(sigma/R(u))`. Define

`F_t(u,sigma)=(u,R(u)tanh(y(u,sigma)+t g(u)))`.

- `|tanh|<1`, so `F_t(D) subset D`.
- In the `y` coordinate, `F_t` is translation by `t g(u)`; therefore
  `F_t F_s=F_(t+s)` and `F_0=id`.
- Every `F_t` is real analytic and `F_t(x)->x` as `t->0+` for every `x`.
  Thus this is a semigroup in Definition 2.2 of the source (Definition 2.4 in
  the published-page crop is the strict-inside definition).
- `p_n=((1/2)e_n,0)` has norm `1/2`, so `{p_n}` lies strictly inside `D`.
- `||F_1(p_n)||^2=1/4+(3/4)tanh^2(n) -> 1`. Hence the time-one image has
  distance to the boundary tending to zero. The finite-time orbit set is not
  strictly inside.

## Semicocycle checks

Choose a smooth nondecreasing `Q:R->[0,1]` with `Q=0` on `(-infinity,0]`
and `Q=1` on `[1,infinity)`. Put

`q(x)=Q(y(x)-g(u))`,

`Gamma_t(x)=exp(q(F_t(x))-q(x))`.

- The exponent telescopes, so
  `Gamma_t(F_s x)Gamma_s(x)=Gamma_(t+s)(x)` and `Gamma_0=1`.
- Every `Gamma_t` is smooth and `e^(-1)<=Gamma_t<=e` globally.
- If `S` lies strictly inside the unit ball, choose `r<1` with `||x||<=r`
  on `S`. Then `|sigma|/R(u)<=r` and `|y(x)|<=M=artanh(r)`.
- For `0<h<=1/2`,
  `log Gamma_h=Q(y-(1-h)g)-Q(y-g)`. If `g>=2M`, both arguments are at most
  zero. If `g<=2M`, the absolute difference is at most
  `2||Q'||_infinity M h`. Therefore `Gamma_h->1` uniformly on `S`.
- At `p_n`, `q(p_n)=q(F_1p_n)=0`, hence `Gamma_1(p_n)=1`. For every `h>0`,
  choose `n>=1/h`; then `q(F_(1+h)p_n)=Q(hn)=1`, so
  `Gamma_(1+h)(p_n)=e`. Uniform time continuity fails at `t=1` on the
  strictly-inside set `{p_n}`.

## Stress checks and boundaries

- The distance from a point `x` of an open unit ball to its boundary is
  `1-||x||`; the proof uses the full Hilbert norm after the scalar coordinate
  changes.
- The base space is real, which is expressly allowed in the source setup; the
  Banach algebra is `C`.
- The example does not claim that a holomorphic semigroup on a hyperbolic
  complex domain can fail to act strictly inside.
- No numerical test is needed or used; all estimates are symbolic.

## Reviewer focus

The only slightly nonstandard ingredient is the real-analytic function `g`
unbounded on an interior bounded sequence. Verify local uniform convergence on
the complexification. The rest is an exact coordinate translation and a
two-case estimate.
