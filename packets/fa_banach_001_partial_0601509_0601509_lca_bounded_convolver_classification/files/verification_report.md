# Verification Report

Candidate: arXiv:math/0601509 bounded-convolver questions, restricted to LCA
groups.

## Claim Checked

For an LCA group `G`, bounded `L^2`-convolution kernels all lie in `L^2(G)`
iff `G` is compact or discrete; and the norm closure of their convolution
operators is a star-subalgebra of `VN(G)` iff `G` is compact or discrete.

## Verdict

**likely valid**

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Fourier multiplier characterization | valid | Translation-invariant bounded operators on `L^2(G)` diagonalize under Plancherel; distributional equality identifies the multiplier with the Fourier transform of the bounded kernel. |
| Compact positive case | valid | Finite Haar measure gives `L^infty subset L^2`; bounded functions are in `L^1`, and their convolution operators are dense in `C_r^*(G)`. |
| Discrete positive case | valid | Applying a bounded convolution operator to `delta_e` recovers its kernel in `ell^2(G)`; all of `VN(G)` is realized this way. |
| LCA structural split | external/standard | Every LCA group has an open subgroup `R^d times K`; if `d=0`, noncompactness and nondiscreteness force both `G/K` and `K-hat` to be infinite. |
| Euclidean chirp | valid | The Fresnel identity gives a bounded unimodular multiplier. Extension by zero from an open subgroup corresponds to pullback along dual restriction. |
| Euclidean product obstruction | valid | The product multiplier is compact-subgroup averaging. The subgroup is non-open and the source distance theorem applies because LCA groups are amenable. |
| Compact-open coset/character kernel | valid | Finite coset truncations have multipliers of modulus one on pairwise disjoint restriction fibers. Pointwise dominated convergence of kernels and `L^2` dominated convergence of multipliers identify the limiting bounded convolution operator. |
| Non-`L^2` property | valid | Infinitely many disjoint cosets each contribute Haar mass one. |
| Product projection outside closure | valid | Averaging a hypothetical approximant along `K^perp` is contractive, fixes the fiber-union indicator, and Fourier-inverts to restriction of the bounded kernel to `K`. Riemann--Lebesgue contradicts coefficients bounded away from zero on distinct characters. |
| Exhaustion of cases | valid | Compact/discrete are positive; every group that is neither falls into one of the two negative structural branches. |

## Counterexample Search

Small structural edge cases checked:

- `R^d` with trivial compact factor;
- `R^d times K` with nontrivial compact factor;
- compact-open split example `Z times T`, where the construction specializes
  to `phi(n,t)=exp(2 pi i n t)`;
- finite compact-open subgroup (forces the ambient group discrete, so it is
  correctly excluded from the negative branch);
- finite quotient by a compact subgroup (forces the ambient group compact,
  so it is also correctly excluded).

No counterexample to the claimed classification was found.

## External Dependencies

- LCA structure theorem and Pontryagin character extension: standard, but a
  human should confirm the chosen reference and Haar normalizations.
- Forrest--Spronk--Wood Theorem 3.1: checked against the local source; it gives
  distance equal to operator norm for operators supported on a non-open closed
  subgroup with a contractive approximate indicator.  The source also records
  that amenability supplies the required indicator.
- Riemann--Lebesgue for compact abelian groups: standard.

## Gaps

- No proof gap found.
- The novelty search is bounded and cannot certify absence from all published
  harmonic-analysis literature.

## Confidence

Score: **91/100**.

The main identities are direct Fourier calculations and the compact-open
obstruction is self-contained.  Remaining risk is bibliographic novelty and
standard Haar-normalization bookkeeping, not the core argument.

## Human Review Recommendation

**send to human**.  Review especially the compact-open finite-truncation limit
and the fiber-average identity.
