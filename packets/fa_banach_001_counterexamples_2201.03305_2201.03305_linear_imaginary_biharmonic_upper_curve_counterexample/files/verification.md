# Verification report

## Result and source

- Source: Tho Nguyen Duc, *Pseudomodes for biharmonic operators with complex
  potentials*, arXiv:2201.03305.
- Exact signal: source PDF page 7, paragraph after Theorem 2.2 and equation
  (2.17).
- Claimed result: the upper curve is not necessary for the full-line
  pseudospectrum.  For `H=d^4/dx^4+i x`, pseudomodes exist whenever
  `alpha -> infinity`, uniformly in the imaginary coordinate `beta`.
- Classification: candidate counterexample to the universal/full-line
  optimality belief; likely valid.

## Proof audit

1. **Fourier sign.** With `F(xf)=i partial_xi Ff`, multiplication by `i x`
   becomes `-partial_xi`, while the fourth derivative becomes `xi^4`.
2. **Imaginary translation.** Multiplication by `exp(-i beta xi)` cancels the
   `-i beta` term exactly.
3. **Homogeneous solution.** For `alpha=a^4`, the derivative of
   `exp(xi^5/5-a^4 xi)` is `(xi^4-alpha)` times the same function.
4. **Denominator.** A window of width `a^(-3/2)` around the phase maximum at
   `xi=-a` yields norm at least `c a^(-3/4) exp(4a^5/5)`.
5. **Numerator.** An asymmetric cutoff has derivative only where the scaled
   phase is at most `-4/5+epsilon`; its residual norm is at most
   `C a^(-1/2) exp((-4/5+epsilon)a^5)`.
6. **Ratio and source curve.** Division gives the claimed residual.  For the
   source choice `tau(beta) asymp beta^(-1)`, its upper exponent is below
   `8/3`; `alpha=beta^3` violates it while the new residual tends to zero.
7. **Domain.** Compact Fourier support is smooth, so the inverse transform is
   Schwartz and belongs to the maximal full-line domain.

No numerical experiment is used as proof.

## Upgrade-attempt log

- Route 1 examined whether the polynomial WKB boundary could be made
  necessary by energy or commutator estimates.
- Route 2 identified the exactly solvable linear model and removed `beta` by
  the full-line translation/Fourier symmetry.
- Route 3 constructed a cutoff homogeneous solution and obtained an explicit
  exponentially small residual outside the proposed curve.
- Deep upgrade: an initially fixed exponential gap was sharpened to every
  exponent below the phase-barrier value `8/5`, uniformly for all real
  `beta`, not only along `alpha=beta^3`.
- A half-line upgrade was investigated but not claimed: beyond the upper
  curve the natural spatial width exceeds the distance of the turning point
  from the boundary, so the full-line construction does not directly survive
  a boundary cutoff.

## Novelty audit

Bounded primary-literature searches through 2026-08-11 used the source title,
its optimality language, `biharmonic`, `fourth-order complex Airy`,
`pseudomode`, `resolvent`, and `d^4/dx^4+i x`.  No later source explicitly
recording this counterexample was located.  Search results concerned mainly
the second-order complex Airy operator or unrelated polyharmonic problems.
Novelty confidence is moderate.

## Source and render audit

- `source_paper.pdf` was compiled locally from the archived arXiv source and
  has 39 pages.
- The complete relevant source page 7 was visually inspected.
- `figures/open_problem_crop.png` includes full page width, equation (2.17),
  the theorem context, and the entire open-problem paragraph.
- The final packet was compiled with `latexmk`, rendered with Poppler, and
  all 5 pages were visually inspected after the last material edit.
- Final packet SHA-256:
  `0dcdf08b6725cc529cc7f96d606af19d33662e7e14d71899518dd72f6558b621`.
- Compiled source-paper SHA-256:
  `4d5235824bbdbabead9754d770b1ec160da4fbd1e5297fca7e2caef2070a6d48`.
- Source-context crop SHA-256:
  `c9a970e689d66987167f2e65da50d45270f567e206ce188eb341a9c7fba1d0eb`.

## Human verifier focus

Check the Fourier convention, cutoff support and phase extrema, the norm power
`a^(1/4)` after division, and the scope distinction between the original
full-line operator and a half-line/boundary-supported variant.
