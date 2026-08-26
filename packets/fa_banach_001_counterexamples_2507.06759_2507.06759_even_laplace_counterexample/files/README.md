# An even log-concave counterexample to the Gaussian Grünbaum bound

Status: candidate full counterexample, likely valid, pending human review.

Source: Matthieu Fradelizi, Dylan Langharst, Jiaqian Liu, Francisco Marín
Sola, and Shengyu Tang, *Grünbaum's inequality for Gaussian and convex
probability measures*, arXiv:2507.06759v2.

The source asks whether its one-dimensional Gaussian-form Grünbaum bound may
continue to hold when the probability measure is merely even.  The packet
gives a negative answer in a substantially narrower class.

Let

`d mu(x) = exp(-|x|) dx / 2`

be the centered Laplace law and take `B=(-5,0)`.  This measure is even and
log-concave, and it is a convex measure in the paper's sense because the
reciprocal of its density is convex.  The conditional barycenter `g` satisfies

`mu((-5,g]) < 1/5 < Phi(-I_gamma(mu(B))/mu(B))`.

All estimates are elementary and exact.  Moreover, the strict violation
persists after convolution with a sufficiently narrow centered Gaussian, so
there are positive smooth even log-concave counterexamples as well.

Files:

- `solution_packet.pdf`: complete review packet;
- `main.tex`: proof source;
- `source_paper.pdf`: current arXiv v2 paper;
- `figures/open_problem_crop.png`: source page 30;
- `code/verify_laplace_example.py`: high-precision non-proof regression;
- `VERIFICATION.md`: proof, novelty, and artifact audit.

Human review should focus on the source-question interpretation, the two
elementary estimates separated at `1/5`, and the continuity argument for the
smooth upgrade.

