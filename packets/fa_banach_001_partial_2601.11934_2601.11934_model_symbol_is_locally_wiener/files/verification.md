# Verification report

Verdict: **likely valid candidate partial result**.

## Source checks

- The source is arXiv:2601.11934v2, last revised 13 May 2026.
- PDF page 6 states Theorem 1.4 with the hypothesis
  `F in_loc W_0(R) cap W_ceil(s)(R)` and then claims in Remark 1.5 that
  `F(x)=|x|x^(2k+1)` is not in that local class.
- PDF page 23 defines
  `W_n(R)={G in C^n(R): G in L_infinity(R), Fourier(G^(n)) in L_1(R)}`.

## Proof audit

1. For `h in H^1(R)`, Cauchy--Schwarz gives
   `||hat h||_1 <= ||(1+xi^2)^(-1/2)||_2
   ||(1+xi^2)^(1/2)hat h||_2`; Plancherel makes the second factor comparable
   to `||h||_H1`. This is correct in one dimension.
2. If `G in C^m` and `G^(m) in H^1_loc`, then for every smooth compact cutoff
   `chi`, Leibniz's formula shows `(chi G)^(m) in H^1`: the top term is
   `chi G^(m)`, while every lower term is compactly supported `C^1`.
3. The same localized function `chi G` is compactly supported `C^1`, hence
   lies in `H^1`; therefore both Fourier conditions for `W_0` and `W_m` hold.
4. For odd `m`, direct differentiation on the two half-lines gives
   `D^m(|x|x^m)=(m+1)!|x|`. Both sides are continuous at zero, so the identity
   holds classically. The derivative of `|x|` is `sgn(x)` almost everywhere,
   which is square-integrable on compact intervals. Thus the top derivative
   is locally `H^1`.
5. The model symbol vanishes at zero, so all hypotheses of Theorem 1.4 are
   met after localizing to the spectrum of the bounded self-adjoint input.

## Scope and contradiction checks

- No step asserts that arbitrary continuous top derivatives have integrable
  Fourier transforms; the `H^1_loc` hypothesis is essential to this proof.
- The result does not settle the general `C^m` versus local-Wiener gap.
- No numerical computation is used or needed.
- Bounded web/arXiv searches on 11 August 2026 used the exact paper title,
  exact model symbol, `remove this gap`, `quantum Besov`, and Wiener-space
  phrases. They found arXiv:2601.11934v2 but no later correction or solution.

Human-review focus: confirm that the source's notation `in_loc` has its stated
cutoff meaning and that the Fourier transform normalization does not alter the
elementary `H^1 -> Fourier L^1` estimate (it only changes a constant).

