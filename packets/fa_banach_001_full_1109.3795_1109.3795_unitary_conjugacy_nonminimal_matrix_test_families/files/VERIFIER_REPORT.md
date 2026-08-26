# Verifier report

## Claimed result

For every N >= 2, both normalized matrix test-function families in
arXiv:1109.3795 are nonminimal.  Together with known scalar minimality, each
family is minimal exactly when N = 1.

## Mathematical verification

- Checked the source's exact contractive-multiplier criterion.  Under
  psi -> U psi U*, its scalar kernel is changed exactly by the bijective
  dummy-variable substitution X -> U*X.
- Verified both inclusions between the admissible-kernel families after
  deleting an open neighborhood: retained tests give one inclusion, and the
  retained conjugate of every deleted test gives the other.
- Checked the topology argument in the source's pointwise weak-* topology:
  it is Hausdorff, unitary conjugation is a homeomorphism, and distinct
  conjugates have disjoint neighborhoods.
- Verified the explicit constrained-Hardy example.  The antipodal scalar
  measure gives z^2; the rotated cube-root measure has t^3=i and gives
  -i z^3; right normalization gives diag(z^2,z^3).
- Verified extremality of the direct-sum matrix measure directly from
  positivity, disjoint supports, rank-one coordinate ranges, and uniqueness
  of the scalar weights under the mass and first-moment constraints.
- Checked the extension to every N > 2 using further disjoint rotated
  scalar extreme measures.
- Checked the annulus formula in the source: conjugation replaces its unitary
  parameter V by UV, and unequal scalar diagonal tests give a noncentral
  member.
- The conclusion concerns closed-subset minimality of the stated normalized
  families.  It does not decide minimality after quotienting by conjugation.

## Source and novelty verification

- The annulus conjecture is Remark 4.6 on PDF page 32.
- The constrained-Hardy open question is Remark 4.9 on PDF page 36.
- The run registry contains no duplicate.  Bounded exact-phrase, title,
  citation, and conjugacy searches found the source and scalar predecessor
  but no later explicit resolution.  Novelty is provisional.

## Build and visual verification

- Compiled `main.tex` with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error -jobname=solution_packet main.tex`; the build completed
  successfully and produced a four-page PDF.
- Extracted the finished PDF with Poppler and checked for the symmetry
  obstruction theorem, both application corollaries, and the exact
  `if and only if N = 1` conclusion.
- Rendered all four pages at 150 dpi with Poppler.
- Visually audited every rendered page.  Equations, theorem statements,
  source-question crops, captions, page breaks, and references are legible;
  there is no clipping or overlap in the authored content.
- Re-scanned the final LaTeX log for overfull boxes, underfull boxes,
  undefined references, and LaTeX warnings; none remained.
