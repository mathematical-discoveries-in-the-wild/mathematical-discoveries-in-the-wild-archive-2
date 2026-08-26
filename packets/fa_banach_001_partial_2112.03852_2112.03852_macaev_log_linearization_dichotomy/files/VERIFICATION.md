# Verification report

Verdict: `likely valid partial result`.

## Checks

1. **Finite local constant.** After subtracting the linear map agreeing with a
   quasilinear map on an orthonormal basis, a balanced binary-tree expansion
   gives `Lambda(m) <= 4 sqrt(m)`. Thus the definition is finite.

2. **Positive implication.** If `Lambda(m) <= C log(m+1)`, every rank-`m`
   orthogonal projection has a lifting of norm `O(log(m+1))` through each
   fixed twisted Hilbert extension. For decreasing singular values `s_m`,
   `D = sum_m (s_m-s_(m+1)) P_m`. Summation by parts gives
   `sum_m (s_m-s_(m+1)) log(m+1) <= C sum_m s_m/m`, so the series of liftings
   converges in an equivalent Banach norm on the twisted Hilbert space.

3. **Block twist.** The Hilbertian direct sum of normalized finite-dimensional
   quasilinear maps is quasilinear with the same constant on the algebraic
   direct sum. Completing its twisted sum produces an exact sequence of
   Hilbert spaces. Restricting any lifting to a quotient block and projecting
   to the corresponding kernel block gives the necessary uniform bound
   `sup_k a_k dist(Phi_k,Lin) < infinity`.

4. **Macaev calculation.** With `a_k=1/(k^2 log(m_k+1))` and increasing
   `m_k`, the singular values are `a_k` repeated `m_k` times. If
   `N_k=sum_(i<=k)m_i`, the contribution of block `k>=2` is at most
   `a_k log(N_k/N_(k-1)) <= a_k log(m_k+1) = 1/k^2`. Hence the operator is in
   the Macaev ideal.

5. **Failure of lifting.** Choosing block distances at least
   `k^4 log(m_k+1)` makes `a_k dist(Phi_k,Lin) >= k^2`, contradicting the
   necessary block bound.

6. **Scope.** The proof establishes an equivalence with a finite-dimensional
   asymptotic estimate. It does not prove or disprove that estimate, and the
   universal Macaev question is therefore not labeled solved.

No numerical experiment is used as proof.

## 2026-08-11 finite-range audit

- Checked Kalton, *A remark on quasi-isometries*, Theorem 2.2: a continuous
  normalized quasilinear map `R^n -> R^n` is `O(log(n+1))`-close to a linear
  map.
- Padding a map `ell_2^m -> ell_2^r` to dimension `max(m,r)`, followed by
  restriction and orthogonal projection, preserves its quasilinearity constant
  and proves `O(log(m+r))`.
- Kalton's Proposition 2.1 supplies the matching logarithmic order in the
  comparable-dimension regime.
- The corollary for polynomial finite-range profiles uses exactly the already
  audited Abel series. No new convergence step is introduced.
- This does **not** prove the target-dimension-free estimate. The tempting
  dual Maurey-projection argument requires a type/projection bound equivalent
  to the missing splitting constant and is circular.
- Rebuilt the four-page packet PDF and rendered every page to PNG. Visual QA
  found no clipped text, overlap, broken formulas, missing citations, or
  unreadable source evidence.
