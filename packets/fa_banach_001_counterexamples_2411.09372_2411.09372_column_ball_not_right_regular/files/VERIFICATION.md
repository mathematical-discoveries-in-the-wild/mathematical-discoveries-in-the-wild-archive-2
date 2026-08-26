# Verification Report

Verdict: `counterexample_likely_valid`

Verifier model: `GPT5.6`

Date: 2026-08-11

## Claim audited

The nc column unit ball `C_d` is not right regular for every `d >= 2`.
Indeed, its length-`N` word-row supremum is exactly `d^(N/2)`.

## Audit

1. **Upper bound.** From `sum_j X_j^* X_j < I`, every `X_j` is a contraction.
   Hence every length-`N` word has norm at most one, and the norm of the row
   of `d^N` such words is at most `d^(N/2)`.

2. **Finite-dimensional lower-bound tuple.** On words of length at most `N`,
   the truncated creation operators `L_j` have mutually orthogonal ranges
   whose sum is the non-vacuum subspace. Thus, for `X_j=r L_j^*`,

   ```text
   sum_j X_j^* X_j = r^2 (I-P_vacuum) < I.
   ```

   Therefore `X` is an actual interior point of the nc column ball.

3. **Word-row norm.** For every length-`N` word `w`, the adjoint of `X^w`
   sends the vacuum to `r^N` times the reversed word, and `X^w` sends it back.
   Hence

   ```text
   sum_{|w|=N} X^w X^{w*} e_vacuum = d^N r^(2N) e_vacuum.
   ```

   This gives row norm at least `r^N d^(N/2)`. Letting `r -> 1`, together
   with the upper bound, proves the exact supremum.

4. **Test function.** For `f_N=Z_1^N`, column contractivity gives
   `||f_N|| <= 1`, while scalar points `(r,0,...,0)` show `||f_N||=1`.

5. **Right TT coefficients.** At order `N`, the expansion is simply
   `f_N(Z)=Z_1^N * 1`. Thus the coefficient column indexed by all length-`N`
   words has one entry equal to the constant one and all other entries zero;
   its supremum norm is one.

6. **Contradiction to regularity.** The left side of the defining estimate is
   `d^(N/2)` for this `f_N`. No constant independent of `N` exists when
   `d>=2`.

7. **Boundary case.** `C_1` equals the one-variable row ball, already known
   to be right regular in the source paper.

## Computational cross-check

`code/verify_truncated_shifts.py` checked `d=2,3`, `N=1,...,4`, at radius
`r=0.83`. All matrix norm identities matched the exact formulas.

## Remaining review risk

No mathematical gap was found. The remaining uncertainty is bibliographic:
the bounded search did not locate a prior answer but was not exhaustive.

