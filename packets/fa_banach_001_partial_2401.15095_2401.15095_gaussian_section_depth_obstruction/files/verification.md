# Verification record

Verified on 2026-08-17 for `fa_banach_001`, lane 9.

## Mathematical checks

- For a spherical Gaussian `N(c,sigma^2 I)`, minimizing the mass of a
  halfspace through `x` over its unit normal gives exactly
  `Phi(-||x-c||/sigma)`.
- Normalizing a nowhere-zero section of `E^(direct-sum (m-1))` makes the sum
  of the squared center displacements equal to one.  Hence one displacement
  is at least `1/sqrt(m-1)`, and every candidate point is at distance at least
  `1/(2 sqrt(m-1))` from one of the two associated centers.
- Bundlewise spherical Gaussians are weakly continuous in orthonormal local
  trivializations and agree on overlaps because their covariance is
  rotationally invariant.
- For the flag tautological bundle, projections of an orthonormal basis of a
  fixed `(n-k+1)`-plane cannot vanish simultaneously on a `k`-plane.  This is
  all that is required for the stated negative range `m >= n-k+2`.
- The auxiliary exact-minimality claim uses the standard facts that the
  flag-to-Grassmannian pullback is injective in mod-2 cohomology and that
  `w_k(nu_i)^(n-k)` is nonzero.  Human review of this standard cohomological
  step remains recommended, as stated in the packet.

## Artifact QA

- `latexmk` completed successfully in two passes and the final log contains
  no warnings, undefined references, overfull boxes, or errors.
- Poppler `pdfinfo` reports a four-page, unencrypted letter-size PDF.
- Poppler `pdftotext -layout` recovered all headings, theorem statements,
  equations, source excerpt, and references.
- All four pages were rendered at 144 dpi and visually inspected.  No
  clipping, overlap, illegible text, or malformed symbols were observed.
- Review status is intentionally retained as `pending human review`.

## SHA-256

- `source_paper.pdf`: `5e0ff928dcb5d42fbf17c1608c60f2161a19b8dc82806a4a2287c721ff7381b1`
- `solution_packet.pdf`: `73483c6b01e3207439bd3128c0ceb11d13d5f67be42b21e242c1c32bff86f1ee`
- `main.tex`: `445b49cf21dae2427472210c152b1f4742bbbb3a4a855629d952d4b52e6df7f4`
- `figures/open_problem_crop.png`: `d7c6bed5604b693bc7fe61bd51e73d8e4975861fae4504854488aecf561f506b`
- `README.md`: `a12205c3bd8cb353841877141dc1d4632cf1aba3aeae17dfe2d45bc254cfb739`
