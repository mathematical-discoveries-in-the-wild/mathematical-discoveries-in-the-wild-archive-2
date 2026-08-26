# Verification report

Verdict: `candidate partial result likely valid`.

## Claim audit

The packet claims a general first-order asymptotic only for the source's
`L2`-Hölder regularity.  It does not claim to compute the Dragon or Bear slope,
does not claim a second-order constant, and does not treat `C`-regularity.

The proof was audited in the following order.

1. **Fourier identification.** The `(l+1)`-fold convolution has Fourier
   transform `F^(l+1)`.
2. **Regularity threshold.** On dyadic annuli, the supremal `H^s` threshold
   equals the supremal `B^s_{2,infinity}` threshold. This matches the source's
   `L2`-Hölder exponent at the level of suprema, independently of endpoint
   conventions.
3. **Concavity.** Hölder's inequality proves convexity of the weighted Fourier
   integrability region, hence concavity of its upper boundary `A_G(p)`.
4. **Origin and slopes.** At `p=0`, radial integration gives `A_G(0)=-d/2`.
   Thus `(A_G(p)+d/2)/p` decreases, proving the limit and finite-order bounds.
5. **Discrete consequences.** Restricting a nondecreasing concave function to
   integers makes regularities nondecreasing and discretely concave. Decreasing
   increments converge to the same Cesàro slope.
6. **Tile upper bound.** Stability and exact sum-rule order give
   `alpha_l <= l+1`, the standard obstruction explicitly used in the 2025
   follow-up, hence `L_G <= 1`.
7. **Geometric lower bound.** The exact identity
   `Delta_h^p(f^(*p)) = (Delta_h f)^(*p)`, Young's inequality, and
   `||Delta f||_1 = ||Delta f||_2^2` for indicators give
   `L_G >= 2 alpha_0`.

## Edge cases and sanity checks

- `|G|=1` ensures `|F|<=1`; this is automatic for a normalized lattice tile.
- Low frequencies are excluded in `A_G`, so negative Sobolev exponents cause
  no origin singularity.
- The proof takes exponents strictly below each supremum, avoiding unjustified
  endpoint membership.
- The `p`th finite-difference characterization is used only for exponent
  strictly less than `p`; this follows from `alpha_0<=1/2` and choosing a
  strict subcritical exponent.
- For the square, the result gives `L_G=1` and is consistent with the exact
  values `alpha_l=l+1/2`.
- The published Bear and Dragon values obey both discrete concavity and the
  monotonicity of `(alpha_l+1)/(l+1)`.

## Literature and novelty audit

The original PDF, exact phrase searches, arXiv/title/author searches, run
indexes, arXiv:2312.11182 / ACHA 75 (2025), and the 2025 Sbornik paper
`Supersmooth tile B-splines` were checked through 2026-08-13. The later papers
compute further finite orders and give classification results but no
large-order slope theorem was found. Novelty is not certified.

## Build and visual audit

- `latexmk` completed with no warnings, undefined references, overfull boxes,
  or underfull boxes in the final log.
- The final packet has five letter-sized pages.
- All five pages were rasterized at 130 dpi and visually inspected. The source
  crop is legible and contains the complete Remark 6 statement; no equations,
  captions, or margins are clipped.
- No exploratory numerical experiment is used as proof or packaged as
  verification evidence.

## Checksums

- `solution_packet.pdf`: `dc4742b9354d94e0406133b73be92f0bd473af24130a112b5b3f8a78ad3aa220`
- `source_paper.pdf`: `bed9ff33d464269b689dd57f8c1c576023bac04dda7b8c11ac8d3b8b06490a3b`
- `main.tex`: `7f0eb76674b4215e8ea65d098bd77fdd28db51c4b453765c1bf834c3e3b9446e`
- `figures/open_problem_crop.png`: `7435b6c328c6ca71dd093292da2eb5caaf04783215c4b3cd2b7373cae0929abb`

Recommendation: high-priority specialist review, especially of the dyadic
threshold identification and the stability/sum-rule upper bound.
