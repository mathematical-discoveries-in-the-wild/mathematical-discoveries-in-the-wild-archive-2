# Verification report

Verdict: `likely valid candidate counterexample`

Date: 2026-08-09
Model: GPT5.6

## Claim checked

For the operator-valued Hardy algebra
`A = H^infinity(T) bar-tensor D`, where `D` is a Bernoulli crossed-product
finite von Neumann algebra, the packet's bounded element `h=dv` is right outer
but not left outer in every `H^p`, `1 <= p <= infinity`, and has
Fuglede-Kadison determinant zero.

## Independent proof audit

1. **Ambient algebra:** The analytic tensor algebra is a finite maximal
   subdiagonal algebra with diagonal `D`.  Both `d` and every coefficient of
   `v=b_r(zu)` lie in `D`, so `h` is bounded and analytic.

2. **Inner factor:** Since `zu` is unitary on the boundary and `b_r` is a
   scalar Blaschke factor, `v` is unitary-valued.  With
   `W=L_(zu)`, the standard calculation
   `ker b_r(W)^* = sqrt(1-r^2)(1-rW)^(-1) ker W^*` gives exactly the model
   vectors used in the proof.  The coefficients and normalization were
   recomputed and agree with the packet.

3. **Right-module orientation:** Orthogonality to `dvA` is equivalent to
   `dy` lying in `H^2 minus vH^2`, because left multiplication by the positive
   bounded `d` is self-adjoint on `L^2`.  This is the correct model space for
   right outerness `[hA]_2=H^2`.

4. **Energy identity:** Solving `dy=k_x` coefficientwise gives
   `y_n=sqrt(1-r^2) r^n d^(-1)u^n x`.  Squaring and tracing yields the stated
   series with `u^(-n)d^(-2)u^n`; the order of the noncommuting factors is
   correct.

5. **Heavy-tail divergence:** For `X=exp(1/omega_0)`,
   `P(X>t)=1/log(t)` for `t>=e`.  The events
   `X_n>q^(-2n)` are independent and have a divergent harmonic sum.  The
   second Borel-Cantelli lemma therefore gives
   `sum q^n X_n=infinity` almost surely.

6. **Arbitrary defect coefficient:** For nonzero `x in L^2(D)`, faithfulness
   of the canonical expectation gives nonzero
   `g=E_N(xx^*) in L^1(N)_+`.  Spectral truncation, trace cyclicity, and the
   expectation identity turn every partial energy into `integral S_N g`.
   Monotone convergence makes this infinite, so no nonzero orthogonal vector
   exists.

7. **Failure on the left:** Full support of `d` gives bounded diagonal
   truncations `a_m` with `a_m d -> 1`.  Hence `[Ad]_2=H^2`, while right
   multiplication by inner `v` has proper closed range `H^2v`.  This checks
   `[Ah]_2=H^2v != H^2`.

8. **All indices:** Blecher-Labuschagne Lemma 4.1 makes right outerness
   independent of `p` for a fixed element in `L^p`; applying the same lemma to
   the opposite algebra gives the left-handed version.  Since `h` is bounded,
   the `H^2` asymmetry propagates to all `1 <= p <= infinity`.

9. **Determinant:** `integral log d=-infinity`, hence `Delta(d)=0`; unitary
   `v` has determinant one, so multiplicativity gives `Delta(h)=0`.

## Stress tests and possible failure points

- Reversing the module convention would invalidate the conclusion, but the
  packet explicitly follows the source paper's convention and the two closure
  calculations have been checked in that convention.
- The proof would fail for a merely long-tailed but integrable inverse weight.
  The selected `1/log t` tail is sufficiently heavy for the exact
  Borel-Cantelli threshold used.
- No assumption that `d^(-1)` belongs to any `L^s` is made.  All unbounded
  products are treated as affiliated operators and justified by spectral
  truncation.

## Recommendation

Promote as a candidate counterexample and request specialist review.  The
highest-value review point is the model-space/conditional-expectation passage;
no unresolved lemma or computational dependency remains in the written proof.

