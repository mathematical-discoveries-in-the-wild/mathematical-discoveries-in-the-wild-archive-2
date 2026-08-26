# Verification audit

Status: literature-implied full answer, likely valid, high mathematical
confidence, moderate novelty confidence.

## Statement audit

- `mu` is a probabilistic frame, hence `S_mu` is symmetric positive definite.
- `h in H_mu` is square-integrable and satisfies the exact matrix constraint
  `integral x h(x)^t dmu=0`.
- Convex order is oriented so the martingale starts at
  `(S_mu^{-1}id+h)_#mu` and ends at `nu`.
- Every measure in the theorem has a finite second moment, so all conditional
  barycenters and mixed moments used in the proof are integrable.

## Necessity

1. Disintegration is available because Euclidean spaces are standard Borel.
2. Conditional Jensen gives `T_#mu <=_cx nu` for
   `T(x)=E[Y|X=x]`.
3. Conditional Jensen for `|.|^2` gives `T in L2(mu)`.
4. The dual mixed moment is exactly `integral x T(x)^t dmu=Id`.
5. Subtracting the canonical map gives
   `integral x(T-S_mu^{-1}x)^t dmu=Id-S_mu S_mu^{-1}=0`.

## Sufficiency

1. Strassen's theorem converts `T_#mu <=_cx nu` into a martingale kernel
   `K_z` with barycenter `z` and second marginal `nu`.
2. The lifted kernel `K_{T(x)}` is measurable and defines a coupling of
   `mu` and `nu`.
3. Its conditional barycenter is `T(x)`, so its mixed moment is
   `integral xT(x)^t dmu=Id`.
4. Hence `nu` is dual. The standard Cauchy--Schwarz estimate also supplies a
   positive lower frame bound, so no separate frame hypothesis is missing.

## Sanity checks

- For `mu=delta_a` on the line, the condition reduces to `mean(nu)=1/a`,
  matching Chen--Schmoll Proposition 5.12.
- Taking `h=0` and equality in convex order returns the canonical dual
  `(S_mu^{-1})_#mu`.
- Taking equality in convex order for arbitrary admissible `h` returns the
  source's full class of pushforward-type duals.
- Adding conditionally mean-zero noise to any admissible pushforward dual
  produces the expected non-pushforward dual and preserves the mixed moment.

## Novelty/search audit

The full texts of arXiv:2505.13885 and arXiv:2501.02602 were searched for
`convex order`, `martingale`, `Strassen`, `barycenter`, and
`conditional expectation`; there were no hits. Bounded web searches for the
exact dual-frame/convex-order combination found the two source papers and
general statements of Strassen's theorem, but no prior frame-theoretic
classification. Because the decisive theorem is classical, the packet is
classified as literature-implied and makes no priority claim.

## Human review recommendation

Verify the convex-order orientation and the transpose in the mixed moment,
then confirm that the source's broad phrase "characterizing all" accepts a
union-over-admissible-barycenters characterization. The theorem is
measure-level and removes the unknown coupling using a standard stochastic
order, but it is not an extreme-point or algorithmic parametrization.

## Artifact verification

- `solution_packet.pdf` compiled twice after the final edit with no LaTeX
  warnings, undefined references, overfull boxes, or underfull boxes.
- All three pages were rendered at 150 dpi and visually inspected; no text,
  equations, status box, or references are clipped or overlapping.
- Packet PDF SHA-256:
  `31e416347855483c21b1c93ba8cce7a170053fb8ef250d3beb59580ed8d8fcb3`
- Source PDF SHA-256:
  `20a81e7562db777c83a5f20e5b3930796d35a90c2362f1dfb00b1eada9e593b7`
- Supporting theorem PDF SHA-256:
  `6b51f6b439c89a92f13a683bafb53df9660711e6c2a4ee26012020c9a18318ba`
