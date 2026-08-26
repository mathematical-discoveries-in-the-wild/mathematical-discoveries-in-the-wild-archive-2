# Verification report

Status: `likely valid full negative literature-implied answer`

## Source checks

- The source's Theorem 1 and critical conjecture are on PDF page 2 of
  arXiv:0808.0414. At `q=n/(n-1)`, the radial weight has exponent zero.
- The whole-space theorem is Theorem 1.1 of arXiv:2407.14052's introduction,
  cited there from arXiv:2109.08014.
- The bounded-domain hemisphere characterization is Theorem 1.2 of
  arXiv:2407.14052; its boundary-delta proof is Section 2.
- The same Section 2 explicitly subtracts a fixed unit-mass translate in the
  half-space argument to preserve zero mean while removing only a bounded
  contribution.

## Mathematical checks

- `Phi(v)=|v|^(1/(n-1)) v_1` is positively `n/(n-1)`-homogeneous and smooth
  on the sphere.
- `Phi` is odd, so its full-sphere integral is zero.
- For `K(theta)=c_n theta`, the inward-hemisphere integral is a nonzero
  constant times `integral_{theta_1<0} theta_1`, hence is nonzero.
- Critical scaling was checked: `p(n-1)=n`, so the rescaling of the ball
  integral has no prefactor.
- The far-field expansion has error `O(|y|^(-n-1))` after applying `Phi`,
  which is integrable.
- The boundary-delta term grows logarithmically. Choosing the inner radial
  fraction `gamma` close enough to one prevents the uncontrolled outer
  annulus from cancelling it.
- The compensating convolution is bounded on the unit ball. Weak endpoint
  HLS gives a uniform `L^(p,infinity)` bound for the concentrated term, hence
  a uniform integral of its `(p-1)` power on the finite-measure ball. The
  nonlinear perturbation is therefore `O(1)`.
- Each counterexample is smooth, compactly supported, real valued, has mean
  zero, and has `L1` norm at most two.

## Scope audit

The packet distinguishes the original uniform-truncation conjecture from the
later whole-space formulation. It does not claim that arXiv:2407.14052
explicitly announces the negative answer; the full counterexample is an
implication of its necessity mechanism plus the zero-mean compensation.

## Artifact checks

- Source and both supporting PDFs are stored locally.
- `main.tex` compiled with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error` to a four-page packet.
- The final log has no undefined citations or references, duplicate PDF
  destinations, overfull boxes, or fatal errors. The two harmless underfull
  bibliography paragraphs do not affect layout.
- All four rendered packet pages were visually inspected at readable
  resolution; formulas, the source excerpt, margins, and references are
  legible with no clipping or overlap.

Reviewer focus: the uniform `O(1)` bound for the fixed compensator.
