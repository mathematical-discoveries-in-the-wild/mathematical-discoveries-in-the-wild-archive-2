# Sharp all-eigenvalue Shannon--Stam stability for Gaussian pairs

Status: candidate substantial partial result; likely valid; human review
recommended.

The packet proves an exact spectral formula and sharp two-sided stability
estimate for every centered Gaussian covariance pair.  With `C` the average
covariance,

`min(lambda,1-lambda) (D(X||G_C)+D(Y||G_C)) <= delta`

and the reverse bound holds with `max(lambda,1-lambda)`.  Both constants are
optimal in dimension one, and at weight one half the lower bound is an exact
identity for every pair.  The result is independent of covariance condition
numbers and therefore shows that ill-conditioned Gaussians do not force the
quadratic or cubic Poincare deterioration in the source theorem.

The global exponent question for arbitrary log-concave inputs remains open.
The associated attempt note records eight focused upgrade routes and their
common nonlinear obstruction.

Files:

- `solution_packet.pdf`: reviewable proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source question and conjectural paragraph.
- `verification.md`: algebraic and presentation checks.
