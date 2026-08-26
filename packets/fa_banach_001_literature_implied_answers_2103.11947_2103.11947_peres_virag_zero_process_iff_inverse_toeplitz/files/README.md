# Peres–Virág zero-process classification for arXiv:2103.11947

**Classification:** literature-implied answer; high confidence.

Sodin's Calabi-rigidity theorem (arXiv:math/0007030, Theorem 2) implies an
exact converse to the same-Bergman-process result in Mukeru–Mulaudzi:

- a nondegenerate proper complex Gaussian power series has the Peres–Virág
  zero process iff it is, in law, `h` times the iid Gaussian series for a
  zero-free analytic function `h`;
- equivalently, its coefficients are a lower-triangular convolution of iid
  Gaussians by the Taylor coefficients of `h`;
- when the coefficient covariance is a bounded positive invertible operator
  on `ell_2`, this is equivalent to its inverse being Toeplitz.

Thus the source's inverse-Toeplitz condition is necessary as well as
sufficient in that natural operator regime. The unrestricted problem of
classifying Gaussian series whose zeros form *some* determinantal process is
not resolved.

Files:

- `solution_packet.pdf`: review-ready literature-implication packet.
- `main.tex`: LaTeX source and complete proof of the specialization.
- `source_paper.pdf`: Mukeru–Mulaudzi, arXiv:2103.11947.
- `supporting_paper_math_0007030.pdf`: Sodin, arXiv:math/0007030.
- `tmp/`: extracted text, evidence-page renders, build files, and final-page
  renders used for visual verification.
