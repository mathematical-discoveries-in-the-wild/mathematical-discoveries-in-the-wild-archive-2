# Uniform Regular-Polygon Cauchy-Dual Dichotomy

Status: `candidate_partial_likely_valid`

Source: Saee A. Joshi, Geetanjali M. Phatak, and Vinayak M. Sholapurkar,
*An example of a cyclic analytic 2-isometry with defect operator of rank 3,
whose Cauchy dual is not subnormal*, arXiv:2511.04565, Epilogue (PDF p. 10).

## Claimed contribution

For `N >= 1`, `c > 0`, and any rotation `xi`, put

`mu = c sum_{j=0}^{N-1} delta_{xi exp(2 pi i j/N)}`.

The packet proves that the Cauchy dual of multiplication by `z` on `D(mu)` is
subnormal if and only if `N <= 2`.  In particular, it upgrades the source's
unit-mass equilateral theorem to every common positive mass and extends the
negative result to every uniform regular polygon with at least three vertices.

This is a complete theorem for the regular-polygon family but only a partial
answer to the source conjecture: arbitrary three-point support and arbitrary
positive weights remain open.

## Proof mechanism

Root-of-unity orthogonality gives the exact spectral factor
`q(z)=z^N-rho`.  Fourier diagonalization of Costara's circulant Gram matrix
then gives the numerator kernel

`G(z,w)=sum_{k=1}^N A_k (z conjugate(w))^k`

with explicit positive coefficients.  The collision-safe necessary atomic
measure for subnormality would force this polynomial to vanish at all `N-1`
off-diagonal pole products.  Those roots prescribe a geometric coefficient
ratio, while the explicit coefficients give a strictly different ratio for
every `N>=3`.  The exceptional equality at `N=2` matches the known antipodal
subnormal theorem.

## Packet contents

- `solution_packet.pdf`: five-page proof and review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: rendered crop of the epilogue conjecture.
- `figures/general_problem_crop.png`: rendered crop of the broader
  characterization problem.
- `code/verify_uniform_ngon.py`: independent numerical reconstruction of the
  Gram matrix and numerator coefficients.
- `code/verification_output.txt`: saved 20-case PASS summary.
- `VERIFIER_REPORT.md`: adversarial step-by-step review.
- `main.tex`: packet source; build intermediates and rendered pages are under
  `tmp/`.

## Reproduce the verification

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2511.04565_uniform_regular_polygon_cauchy_dual/code/verify_uniform_ngon.py \
  --suite
```

## Human-review focus

Check the conjugation convention in the finite-kernel formula, the Fourier
eigenvalue indexing, and the grouping of repeated pole-product atoms.  The
bounded novelty search through 2026-08-13 found no prior statement of the
uniform regular-`N`-gon dichotomy; novelty remains plausible rather than
certified.

