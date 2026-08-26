# Verification report

Status: candidate full proof; mathematical audit passed locally.

## Source evidence

- `source_paper.pdf` is the official PDF of arXiv:1005.0540.
- The conjecture is on source PDF page 3.
- `figures/source_conjecture_crop.png` is a readable 220-dpi crop containing
  the entire conjecture.
- `supporting_papers/1702.00241.pdf` states the equivalent Federer-density and
  local-isodiametric questions and records uniform pairwise metric blow-up.
- `supporting_papers/1004.1369.pdf` supplies the Carnot-group
  Hausdorff/spherical/isodiametric normalization.

## Mathematical audit

1. Checked that every closed competitor containing `p` and having diameter
   `t` lies in `B(p,t)` and, after dilation by `1/t`, in one fixed compact.
2. Checked that uniform pairwise blow-up at scale `t` gives tangent diameter
   in `[1-a(t),1+a(t)]`, avoiding the fatal cutoff-scale mismatch.
3. Checked the anisotropic Jacobian `t^Q` and a uniform density error bound
   valid for arbitrary varying measurable subsets of the fixed compact.
4. Checked both limsup and liminf of the local supremum; the latter uses a
   compact tangent near-maximizer translated to contain the identity.
5. Checked the direct Federer formula and its Euclidean normalization.
6. Independently checked the reciprocal density using spherical Hausdorff
   density and Rigot's tangent identity.
7. Checked upper and lower semicontinuity of the tangent supremum under
   smoothly varying tangent metrics and Haar densities.
8. Checked that continuity invokes Ghezzi--Jean Proposition 3.10 to obtain
   the ordinary-Hausdorff measured tangent convergence.

## Priority human checks

- Verify that the cited uniform pairwise privileged-coordinate convergence
  is accepted with closed balls; the paper states exactly the required sup
  convergence.
- Audit the smooth family identification of tangent group laws used to pass
  from uniform radial-distance convergence to uniform pairwise convergence
  for the continuity theorem.
- Confirm the Federer-density convention at every regular point and the
  resulting continuous representative of the Radon--Nikodym derivative.

## Final artifact audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed successfully.
- The final log contains no warnings, overfull or underfull boxes, undefined
  references, or fatal errors.
- `solution_packet.pdf` has three pages. All pages were rendered at 150 dpi
  with Poppler and visually inspected after the final bibliography repair.
- The source crop, all equations, citations, proof endings, and page footers
  are readable and unclipped.

## SHA-256

- `solution_packet.pdf`:
  `9084d425cdff76d1e0b7dcd0ec10eccb157bf7b677c63256296e4bb010c54f80`
- `source_paper.pdf`:
  `cf7128c57092335a619ea15e491e32ee487900fece6607d82230c92dbd66178a`
- `figures/source_conjecture_crop.png`:
  `1c1621e198f09e8dcaa4b405cfa54a6b6bdcfc8215bba0a1432239792cfe1fc7`
- `supporting_papers/1702.00241.pdf`:
  `246e0e2e4cd170f2e99ba4b8c7c2033a211ad7de61f3176e32206314385c7052`
- `supporting_papers/1004.1369.pdf`:
  `cd85c12f5af0a2d8d25411d7354a3cb9b4eb0ffacd2bb853f4987dc06729850c`
