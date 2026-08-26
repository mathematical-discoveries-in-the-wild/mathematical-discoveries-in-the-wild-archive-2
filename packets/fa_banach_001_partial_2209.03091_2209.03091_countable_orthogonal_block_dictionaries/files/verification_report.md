# Verification report

## Proof audit

- Exact maximization and symmetry give
  `rho(r-cg) >= |rho(r)-c|`, hence monotonicity of
  `||r_n||^2-rho(r_n)^2`.
- The energy identity and `sum c_n = infinity`, `c_n -> 0` force
  `liminf rho(r_n)=0`.
- Before the first threshold time at `s_N`, every tail block is untouched;
  this is an induction using strict inequality at all earlier times.
- The head estimate uses the common local width `alpha`; the tail estimate is
  exact because those components retain their initial values.
- For decreasing square-summable `s_N`, the bound
  `(N/2)s_N^2 <= sum_{ceil(N/2)}^N s_j^2` proves `N s_N^2 -> 0`.
- The liminf-to-limit lemma is proved independently in the packet and needs
  only exact greediness, symmetry, and `c_n -> 0`.

## Edge cases

- If a trajectory reaches zero, it terminates and convergence is immediate.
- If the initial vector has only finitely many nonzero blocks, the union is
  globally norming with constant `alpha/sqrt(N)`.
- Local attainment plus square-summable block norms ensures the global maximum
  is attained.
- Closed finite-dimensional augmentation sets in the coordinate corollary are
  compact, so local attainment is automatic.

No computational claim is used. Recommended status:
`substantial_partial_result_likely_valid`; human review requested.

## Packet verification

- Final PDF: 4 A4 pages, 283430 bytes.
- SHA-256:
  `e7480b996c6e28e5862a6c62d851d0ea2f7af4b036f4a1c679c2b41fa82910e3`.
- All four final rendered pages were visually inspected at original resolution.
  No clipping, overlap, broken formulas, or unreadable text was found.
