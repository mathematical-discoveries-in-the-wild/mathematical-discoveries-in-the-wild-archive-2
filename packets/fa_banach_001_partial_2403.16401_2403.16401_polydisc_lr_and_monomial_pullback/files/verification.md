# Verification audit

Date: 2026-08-11

## Source and target

- The crop is from PDF page 10 of arXiv:2403.16401 and contains the complete
  concluding paragraph asking for the measurable polydisc extension.
- The introduction independently states that McDonald's result handles only
  continuous unimodular functions and calls the measurable polydisc problem
  open.
- The packet does not claim the general measurable essential-supremum result.

## Theorem 1: finite-`L^r` density

1. A finite phase net gives a measurable simple unimodular `s` with pointwise
   error below `eta`, modulo an irrelevant null set.
2. Haar measure on the compact torus is regular, so disjoint compact cores
   `K_j subset E_j` can be chosen with total omitted measure below `delta`.
3. A finite family of disjoint compact sets in the normal space `T^d` has
   pairwise disjoint open neighborhoods.  Urysohn functions supported there
   make `c=exp(i sum theta_j rho_j)` continuous, unimodular, and equal to the
   chosen phase on every `K_j`.
4. McDonald's 1979 theorem gives a quotient of rational polydisc inner
   functions uniformly `eta`-close to `c`.
5. On the compact cores the total error is below `2 eta`; off them both
   functions are unimodular, so the error is at most 2.  Thus
   `integral |f-q|^r <= (2 eta)^r + 2^r delta`, valid for every `r>0`.
6. Choosing `L^1` errors below `2^-n` makes the sum of pointwise errors finite
   almost everywhere by Tonelli, hence yields almost-everywhere convergence.

No use of the triangle inequality for a quasi-norm is needed when `r<1`.

## Theorem 2: monomial pullbacks

1. The one-variable Douglas--Rudin theorem gives inner quotients uniformly
   approximating every measurable `g_j:T->T`.
2. For nonzero `a in N_0^d`, the continuous character
   `chi_a(zeta)=zeta^a` is onto `T`; therefore its pushforward of normalized
   Haar measure is normalized Haar measure.  Null exceptional sets pull back
   to null sets.
3. If `phi` is inner on `D`, then `phi(z^a)` is bounded and holomorphic on
   `D^d`.  Along radial approach,
   `phi((r zeta)^a)=phi(r^|a| zeta^a)` tends to the one-variable boundary
   value for almost every `zeta`, and that value has modulus one.  Hence the
   composition is polydisc inner.
4. Finite products of inner functions are inner.  The telescoping inequality
   for unit-modulus factors bounds the final uniform error by the sum of the
   one-variable errors.

## Scope and stress tests

- The exponents must be nonnegative for `z^a` to be holomorphic in the
  polydisc.  Negative torus characters are not silently included.
- Repeated or nonprimitive exponent vectors cause no problem: every nonzero
  integer character of `T^d` is onto, even when the coordinates have a common
  divisor.
- The first theorem gives rational inner factors; the second claims only inner
  factors, matching the general one-variable measurable theorem.
- The full uniform problem reduces to arbitrary measurable signs, but the
  packet does not infer uniform approximation from convergence in measure or
  almost everywhere.

## Reproducibility

- `main.tex` compiled with `latexmk -pdf` under the sandbox environment.
- The resulting PDF was rendered page by page and visually inspected for
  clipping, missing glyphs, broken references, and crop legibility.
- No numerical experiment is used as mathematical evidence.
