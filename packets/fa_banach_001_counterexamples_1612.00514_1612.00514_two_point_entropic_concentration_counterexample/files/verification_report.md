# Verification report

Verdict: candidate full counterexample, likely valid; expert review required.

## Mathematical checks

- Recomputed the generator spectrum: the nonzero eigenvalue of -L is
  p+(1-p)=1.
- Derived the two-state action directly from the source convention, including
  the directed-edge factor 1/2: A=K_p(m)(psi(1)-psi(0))^2.
- Checked the continuity equation against the Markov evolution:
  m'=-K_p H_p'=p-m.
- Recomputed the one-dimensional Riemannian Hessian:
  Hess H / G = (1+K_p/[m(1-m)])/2 >= 1/2.
- Audited all four pieces of the diameter integral; their sum is strictly
  below 7 sqrt(log(1/p)) for p<=1/4.
- Checked the strict tail convention at r=D_p; the tail is zero there.
- Checked both readings of the source exponent. The intended positive
  exponent is contradicted as p tends to zero; the literal negative exponent
  is contradicted by time rescaling.

## Computational regression

Command:

    conda run --no-capture-output -n sandbox python code/verify_two_point.py

Result: PASS for six probabilities from 1/4 through 10^-8. Numerical
quadrature satisfies D_p^2/log(1/p)<3.90, far below the proved bound 49;
dense-grid curvature minima stay above 0.533 at the smallest probability.
This computation is only a regression check, not part of the proof.

## Novelty and scope

The four lightweight indexes and bounded exact/variant web and arXiv searches
were checked. arXiv:2309.06493 treats an Ollivier-curvature analogue and does
not establish the original entropic-curvature/intrinsic-metric statement. No
prior two-state counterexample to the exact source conjecture was found.
Novelty is plausible, not certified. Conjecture 6.10 is not resolved.

## Artifact checks

- Five-page PDF compiled with no LaTeX warnings, overfull boxes, underfull
  boxes, or unresolved references.
- All five rendered pages were visually inspected.
- Source crop contains the full statements of Conjectures 6.9 and 6.10.
- Extracted text contains both theorem statements, the constant 49, the scope
  limitation, and both bibliography entries.
- Final packet SHA-256:
  cdd547a74087569783d88201321d1ecd236b2273d83745ce871f28ce5363242b.

Most important human-review points: the action normalization, extension of
the interior Hessian bound to endpoint measures, and the source exponent
interpretation. The construction defeats both exponent readings.

