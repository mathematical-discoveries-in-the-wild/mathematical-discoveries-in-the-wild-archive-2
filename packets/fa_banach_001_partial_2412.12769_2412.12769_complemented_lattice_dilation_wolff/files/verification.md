# Verification notes

## Mathematical checks

- The projection and complementary projection are bounded on every `Y_j`, so
  `Y_j -> X_j direct_sum W_j`, `y -> (Py,(I-P)y)`, is a compatible
  topological isomorphism with inverse addition.
- The outer complex method commutes with finite direct sums directly from the
  definition of admissible functions and quotient quasi-norms.
- The two local identities for `X` and `W` therefore give the two local
  identities for `Y` exactly.
- The hypotheses of Egert--Kosmala Theorem 1.2 are assumed for the `Y_j`, so
  its two global identities apply.
- Applying the common projection to the global identities is legitimate by
  the same direct-sum formula (or the retract principle).
- If all complements are one fixed `W`, then `[W,W]_s=W`; hence both local
  complement identities are automatic.
- `P(Y_0 cap Y_3)` lies in `X_0 cap X_3` and is dense in `X_1,X_2`, so the
  range quadruple inherits the density condition.

## Upgrade attempts

Eight materially distinct attempts were recorded in
`runs/fa_banach_001/attempts/2412.12769_general_a_convex_wolff_reiteration.md`.
The final obstruction is not merely technical: common complementability alone
places no interpolation relation on the four complementary spaces.

## Literature check

Search date: 2026-08-12.

Search bounds included exact source title and arXiv id, authors, and the phrases
`Wolff-reiteration`, `A-convex quasi-Banach`, `inner complex interpolation`,
`outer complex interpolation`, `reiteration theorem`, and `counterexample`.
Primary material inspected included:

- Egert--Kosmala, arXiv:2412.12769;
- Kalton--Mitrea, arXiv:math/9709210;
- Kalton--Mayboroda--Mitrea (2007), especially Sections 7--8;
- Bernal--Cerda on A-convex containing spaces;
- Wen Yuan on inner complex interpolation of quasi-Banach lattices.

No later full answer or counterexample for general A-convex spaces was found.
The packet result is a direct corollary of known function-space Wolff
reiteration and the common-projection/retract principle; novelty confidence is
modest.

## Render checks

- `latexmk` completed with no warnings, undefined references, overfull boxes,
  or underfull boxes.
- The final packet has four pages.
- All four pages were rendered to PNG at 150 dpi and visually inspected.
- The source crop is legible and contains Theorem 1.2 and Remark 1.3.
- No clipping, overlap, malformed mathematics, or stray build text remains.
