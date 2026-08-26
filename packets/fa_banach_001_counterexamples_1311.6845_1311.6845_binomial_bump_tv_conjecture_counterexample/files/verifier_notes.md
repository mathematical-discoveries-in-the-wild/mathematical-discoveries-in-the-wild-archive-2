# Verification notes

Verdict: **likely valid candidate counterexample**.

## Claim audited

For every Case 3 or Case 4 pair of finite intervals `I,J`, no constants
`c1,c2>0` can make

```text
||Hf||_{L2(J)} >= c1 exp(-c2 ||f'||_1/||f||_2) ||f||_2
```

hold for all weakly differentiable `f` supported in `I`.  The failure already
occurs for real `C_c^infty(I)` functions.  Quantitatively, the best stability
envelope is at most `C exp(-c K^(4/3))`.

## Line-by-line audit

1. **Geometry.** In both source configurations, `I \ closure(J)` contains a
   nonempty open interval.  Choose a compact interval `K` inside it and then a
   segment of length `2 rho` inside `K`, with `0<rho<dist(K,J)`.  Thus every
   denominator used below has modulus at least the fixed positive number
   `D=dist(K,J)`.  This also explains why Case 4 contains the Case 3 mechanism,
   exactly as the source paper notes in Sections 1.5 and 2.4.

2. **Smoothness and disjointness.** Taking a nonzero
   `phi in C_c^infty(0,1)` and `h=rho/m`, the translates
   `phi((y-a-jh)/h)`, `0<=j<=m`, have pairwise disjoint supports.  Their total
   span is `(m+1)h<2rho`, so every translate lies in `K` for all `m>=2`.
   The alternating-binomial sum is therefore real and in `C_c^infty(I)`.

3. **Exact norms.** Disjoint supports give
   `||f_m||_2^2=h||phi||_2^2 sum_j C(m,j)^2`, while scaling a derivative gives
   `||f_m'||_1=||phi'||_1 sum_j C(m,j)`.  Vandermonde's identity and the
   binomial theorem turn the sums into `C(2m,m)` and `2^m`.  The standard
   lower estimate `C(2m,m)>=4^m/(2 sqrt(m))` yields
   `kappa_m<=A m^(1/4) h^(-1/2)=A rho^(-1/2)m^(3/4)`.

4. **Finite difference.** After changing variables in each bump, the kernel
   sum is `sum_j (-1)^j C(m,j)q(j)` with
   `q(s)=1/(x-a-h(s+t))`.  The signs agree with
   `(-1)^m Delta^m q(0)`.  Repeated use of the fundamental theorem of calculus
   gives
   `Delta^m q(0)=integral_[0,1]^m q^(m)(u_1+...+u_m)du`.
   Since `|q^(m)|=m!h^m/|x-a-h(s+t)|^(m+1)`, the geometric separation gives
   the asserted uniform bound.  No principal value is needed because the
   support is separated from `J`.

5. **Normalization.** Multiplying by the outer Jacobian `h`, integrating
   `|phi|`, taking the `L2(J)` norm, and dividing by the exact `L2(I)` norm
   gives
   `delta_m <= B m! h^(m+1/2)m^(1/4)/(2^m D^(m+1))`.
   With `h=rho/m` and `m!<=m^m`, this is
   `delta_m<=B' m^(-1/4)(rho/(2D))^m`.  The choice `rho<D` makes the ratio
   strictly below `1/2`.

6. **Envelope conversion.** We have simultaneously
   `kappa_m<=A m^(3/4)` and `delta_m<=B q^m`.  For a large threshold `K`, take
   `m=floor((K/A)^(4/3))` (with a harmless fixed-factor adjustment).  Then
   `kappa_m<=K` and `m>=cK^(4/3)`, proving
   `S(K)<=C exp(-cK^(4/3))`.

7. **Contradiction.** A conjectural exponential lower bound would imply
   `delta_m>=c1 exp(-c2 kappa_m)>=c1 exp(-C m^(3/4))`, incompatible with
   `delta_m<=Bq^m`.

## Computational audit

`code/verify_binomial_bumps.py` checks the two binomial identities exactly and
checks the reciprocal-kernel finite-difference identity with rational
arithmetic.  It also prints the normalized `m^(3/4)` scale and the logarithm
of the analytic transform bound.  These checks are auxiliary only.

## Remaining human-review focus

- Confirm that the source uses the usual oriented Case 4 configuration, so
  `I \ closure(J)` contains an interval.  The paper itself explicitly reduces
  Case 4 to functions compactly supported away from `J`, strongly supporting
  this reading.
- Confirm that the conjecture after Theorem 2.1 is intended as the displayed
  exponential inequality for the natural/maximal stability envelope.  Equation
  (2.1) states exactly that inequality for weakly differentiable functions.
- Check whether the same construction or the `4/3` obstruction has appeared
  outside the bounded searches recorded in `novelty_search.md`.
