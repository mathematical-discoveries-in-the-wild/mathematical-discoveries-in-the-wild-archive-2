# Noncircular-ellipse dichotomy for complex Busemann--Petty

Status: candidate full counterexample theorem, likely valid, pending expert
review.

Source: Simon Ellmeyer and Georg C. Hofstätter, *Busemann--Petty type
problems on complex vector spaces*, arXiv:2404.05630v3, Indiana Univ. Math.
J. 75 (2026), no. 2, 525--551.

The source asks whether `Phi K subset Phi L` implies the corresponding volume
inequality on the injectivity set.  For the complex `L_p`-intersection
operator in `C^2`, `-2<p<0`, it proves the affirmative case only when the
planar kernel `C` is a disk.

The packet proves a sharp classification for all origin-centered ellipses:

- disks (up to dilation) are affirmative, by the source theorem;
- every noncircular ellipse is negative for every `-2<p<0`.

For a noncircular ellipse all even angular multipliers are nonzero, so every
origin-symmetric convex body is in the injectivity set.  A sign-changing
quadratic angular function has strictly positive convolution with the
kernel measure but is negative on a real Lagrangian circle.  The `L_p`
embedding measure of a thin real ellipsoid concentrates on that circle.  The
source paper's radial perturbation identity then produces smooth strictly
convex `K,L` with

`I_{C,p}K subsetneq I_{C,p}L` but `Vol_4(K)>Vol_4(L)`.

Files:

- `solution_packet.pdf`: review packet;
- `main.tex`: complete proof;
- `source_paper.pdf`: original paper;
- `figures/open_problem_crop.png`: Problem 1 on source page 2;
- `figures/source_scope_crop.png`: source Theorem A on page 3;
- `code/numerical_sanity.py`: deterministic non-proof sign regression check;
- `VERIFICATION.md`: proof and artifact audit.

The arbitrary nonelliptic planar kernel is not classified.  Human review
should focus on the ellipse Fourier coefficients, the strict angular-moment
bound, Lagrangian concentration, and the final inclusion/volume signs.

