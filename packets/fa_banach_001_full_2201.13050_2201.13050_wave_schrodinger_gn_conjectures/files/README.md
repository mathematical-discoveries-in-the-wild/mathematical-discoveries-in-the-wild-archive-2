# Wave and Schrödinger Gagliardo–Nirenberg conjectures

Status: **candidate full solution, likely valid**

Source: Rainer Mandel, *On Gagliardo–Nirenberg inequalities with vanishing
symbols*, arXiv:2201.13050, Analysis & PDE 17 (2024), closing conjecture on
source PDF page 29.

The packet proves both conjectured exponent regions. On one Fourier annulus,
the source's Theorem 4 and Remark 1(d) give exactly the required estimate:
the wave cone has `d-2` nonzero principal curvatures, while the paraboloid has
`d-1`. The averaged vanishing order is `1-kappa`.

Ordinary homogeneous Littlewood–Paley projections globalize the wave
estimate. Parabolic projections for

`(xi,tau) -> (lambda xi,lambda^2 tau)`

globalize the Schrödinger estimate. The summation closes precisely because
`r<=2<=q`: `L^r` is 2-concave and `L^q` is 2-convex. A separate transverse
one-dimensional GN argument handles the flat two-dimensional wave cone.

Packet contents:

- `main.tex` and `solution_packet.pdf`: theorem and full proof
- `source_paper.pdf`: original 30-page source PDF
- `figures/source_conjecture_crop.png`: rendered source evidence
- `code/verify_exponents.py` and `code/verification_output.txt`: symbolic and
  randomized sanity checks
- `VERIFIER_REPORT.md`: proof audit and review priorities

Bounded local-index and primary-source searches through 2026-08-13 found no
later answer. Novelty confidence is moderate, not certified.

Human review should focus on uniform application of the source compact-piece
theorem to the unit-annulus patches and the parabolic square-function
normalization. The global sequence summation is elementary.
