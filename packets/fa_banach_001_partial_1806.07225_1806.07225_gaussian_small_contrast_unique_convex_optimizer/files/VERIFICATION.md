# Verification record

## Proof checks

1. The density parametrization forces the high set to have measure
   `theta |Omega|` and keeps `rho_->0` for small contrast.
2. The Gaussian potential Hessian identity follows by differentiating under
   the integral.  Brascamp-Lieb gives covariance at most `2 tau I`; bounded
   support makes equality impossible, and compactness makes the gap uniform
   on the selected level.
3. The threshold quantile changes by no more than the sup-norm perturbation.
4. The symmetric difference of two threshold sets lies in a narrow band
   around a uniformly noncritical level.  Coarea therefore converts the
   sup-norm potential bound into the contraction estimate.
5. Measurable fixed-volume sets modulo null sets are complete for the
   symmetric-difference metric, so Banach's fixed-point theorem applies.
6. Every global optimizer is bang-bang and satisfies the KKT threshold
   condition, hence is the unique fixed point.
7. Uniform `C^2` closeness preserves the positive principal curvatures of the
   selected Gaussian-potential level; intersecting its convex superlevel with
   convex `Omega` leaves a convex high set.

## Source and novelty checks

- The exact Conjecture 3.8 was inspected in the source TeX and PDF page 10.
- The source PDF and a readable full-width crop are included.
- Cheap run indexes had no prior record for arXiv:1806.07225.
- A bounded arXiv/web search through 2026-08-13 used the exact title,
  conjecture wording, and combinations of Gaussian kernel, bang-bang density,
  small contrast, unique optimizer, convex superlevel, and threshold map.
  It found standard log-concavity and nonlocal-perimeter literature but no
  exact small-contrast theorem for this problem.
- Novelty confidence is moderate: the contraction argument appears new for
  this source problem, but its ingredients are classical.

## Computational reconnaissance

The two scripts in `code/` searched for counterexamples and container-
potential non-quasiconcavity.  Their negative output is not evidence for the
theorem and is not used in the proof.

## Reviewer focus

Check the uniform narrow-band/coarea estimate when the reference Gaussian
level meets the boundary of a nonsmooth convex body, and the strictness step
in the truncated-Gaussian covariance bound.  If desired, impose a `C^2`
strictly convex container first; the proof is immediate there, and general
convex bodies follow by the same relative-level argument or approximation.
