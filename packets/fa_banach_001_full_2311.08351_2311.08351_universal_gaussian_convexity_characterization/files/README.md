# Gaussian laws are the only universal carriers of the convexity

Status: candidate_full_classification_likely_valid

The discussion of arXiv:2311.08351 asks whether its normalized log-mgf
convexity extends to more general random vectors. This packet gives a sharp
classification under the direct universal interpretation.

For a random vector X whose linear functionals have all exponential moments,
the following are equivalent:

1. The normalized log-mgf is convex for every exponentially integrable
   convex test F.
2. It is convex for every affine test F.
3. X is a possibly shifted or degenerate multivariate Gaussian.

The necessity proof needs only two tests in each direction v. If

    psi_v(lambda) = log E exp(lambda <v,X>) / lambda,

then the test -v has normalized log-mgf -psi_v(-lambda). Convexity for both
v and -v forces psi_v to be both convex and concave, hence affine. Therefore
every one-dimensional projection has a quadratic cumulant-generating
function and is Gaussian. The converse is exactly the source theorem after
an affine parametrization of a Gaussian vector.

The Rademacher law gives an explicit failure of an unrestricted extension:
log(cosh(lambda))/lambda is not convex on the full real line.

Files:

- main.tex: classification theorem, proof, obstruction, and novelty scope.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: arXiv:2311.08351.
- figures/open_problem_crop.png: source PDF page 7 discussion prompt.
- code/verify_symbolic.py: Gaussian and Rademacher symbolic checks.
- tmp/: build and render intermediates.
