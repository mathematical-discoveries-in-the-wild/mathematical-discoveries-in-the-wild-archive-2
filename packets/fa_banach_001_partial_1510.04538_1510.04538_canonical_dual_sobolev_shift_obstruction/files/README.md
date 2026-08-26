# Canonical-dual Sobolev regularity: a sharp obstruction and a positive interval

Status: `candidate_substantial_partial_likely_valid`

Source: Philipp Grohs, Gitta Kutyniok, Jackie Ma, Philipp Petersen, and Mones
Raslan, *Anisotropic Multiscale Systems on Bounded Domains*, arXiv:1510.04538
(2015; revised 2017), especially PDF pages 5 and 18.

The packet proves two complementary results about the source's analytically
open canonical-dual estimate (GFA2).

1. The estimates available in the source do **not** formally imply (GFA2).
   For the Riesz basis `phi_n=(I-aR)e_n` on a dyadically weighted Hilbert
   scale, (GFA1) and the exact primal coefficient characterization hold for
   every nonnegative smoothness, whereas (GFA2) holds exactly when
   `a 2^s<1`. It fails on the single vector `e_0` when `a 2^s>=1`.
   The Gramian is tridiagonal, and after spacing scale labels the ordinary
   frame can be arbitrarily close to Parseval while failure persists.
2. For every frame satisfying the source's endpoint analysis and synthesis
   estimates at some positive regularity, the frame operator is invertible on
   a nonzero interval of Sobolev exponents around zero. Consequently (GFA2),
   and hence the Gelfand-frame property, holds for all sufficiently small
   nonnegative exponents. This follows from self-adjoint duality and
   Sneiberg interpolation stability.

The concrete boundary-shearlet (GFA2) problem at the intended integer
regularities is not settled. A full proof requires a quantitative
inverse-closed localization estimate for the full hybrid Gramian/frame
operator, with decay strong enough to dominate the exponential scale weight.

## Files

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source passage explaining why (GFA2) is
  analytically unresolved.
- `code/crop_source.py`: reproducible source-crop script.
- `verification.md`: symbolic and PDF checks.
- `tmp/`: LaTeX and rendering intermediates.

## Review recommendation

Expert review should focus on the orientation of the unilateral shift in the
counterexample, the identity between canonical-dual analysis and `D^{-1}`, and
the hypotheses needed to apply Sneiberg's theorem to the Sobolev scale. The
novelty claim is deliberately bounded: searches through 2026-08-17 found no
exact statement, but this is not a priority claim.

