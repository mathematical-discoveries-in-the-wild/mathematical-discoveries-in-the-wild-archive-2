# Verification report

## Mathematical checks

- Checked the real-to-square coordinate identity
  `|x|+|y| = max(|x+y|,|x-y|)`.
- Checked the half-plane Poisson--Jensen normalization on `F(z)=z+i`.
- Differentiated the phase integral independently; all logarithmic boundary
  terms cancel and the derivative has the stated sign.
- Checked the chord inequality for `sin^2 h` on `[0,pi/4]`.
- Checked the Cayley transform in both directions and the exact boundary
  weight `W=max(|1-w|,|1+w|)`.
- Derived the boundary jump from the periodic Hilbert-transform integral.
  With `b=tan(theta/2)`, the rational principal-value integrand decomposes as
  `-b/(t-b)+1/(1+bt)-2/(1+t^2)`, giving the displayed positive density.
- Checked that coefficientwise real and imaginary parts preserve the real-axis
  constraint and lose at most a factor two at the evaluation point.
- Checked that the lower-bound evaluation point has complex l1 norm one,
  transformed ratio `v/u=-i`, and `|u|=1/sqrt(2)`.

## Literature checks

- Searched the run registry, solution index, attempts index, and source index
  for arXiv:2311.03531 and the core exact-value terms; no duplicate result.
- Inspected the full text of Rodríguez, *On the norm of the complexification
  of polynomials*, Studia Mathematica 282 (2025). It retains the
  fourth-root-of-two lower bound for the real l1 plane and does not contain
  the Catalan formula.
- Searched exact formula and decimal variants on the public web; no prior
  occurrence in this problem was found.
- Verified the needed compact continuous-weight polynomial realization in
  Theorem 1.1 of arXiv:2305.08260v3.

## Rendering checks

- Compiled twice with pdfLaTeX; the final log has no warnings, overfull boxes,
  undefined references, or errors.
- Rendered the six-page final packet at 144 dpi with Poppler.
- Visually inspected every rendered page after the final crop and typography
  corrections. No clipping, overlap, broken formula, or illegible source image
  remains.
- Final packet SHA-256:
  `cd14bfc75ad543026b48e3e4597590eb8dacca30df081bbb6361e625c8575523`.
