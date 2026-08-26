# Verification report

## Mathematical audit

1. **Admissibility of the counterexample.** Source Definition 4.5.4 states
   `D'(M) subset (gamma^s)' subset (gamma^(s))'`; hence `delta_e` is in the
   target dual.  This is also independently implied by compact Sobolev point
   evaluation.
2. **Fourier block.** The Fourier transform of `delta_e` is the identity in
   every irreducible representation.
3. **Minimum eigenvalue.** For
   `lambda(l,m)=l(l+1)-m^2`, the maximum of `m^2` occurs at `m=+/-l`, giving
   `lambda_min=l` for every positive half-integer `l`.
4. **Divergence.** The two extremal diagonal entries alone give squared
   Hilbert--Schmidt norm at least `2 exp(2 B l^(1/(2s)))`, unbounded for every
   `B>0`.
5. **Corrected duality.** The standard inductive/projective Hilbert-scale
   dual identities reduce both duals to unions/intersections of `H_(-D)`.
   Uniform negative-weight bounds and weighted `l^2` membership are
   equivalent after spending an arbitrarily small extra exponent, since
   `sum_l (2l+1) exp(-c l^a)` converges for every `a,c>0`.

## Automated checks

`code/check_su2_blocks.py` checks exact eigenvalue integrality after doubling
the half-integer indices, verifies the extremal minimum for 50,000 blocks,
checks the lower-bound identity on a parameter grid, and computes corrected
tail majorants for representative `s` and exponent gaps.

Expected terminal line:

    PASS: 50000 exact SU(2) blocks; 60 divergence checks; 24 tail checks

## Source and PDF audit

- The exact arXiv source gzip is retained as `Full_Tex.tex.gz`.
- `source_paper.pdf` is a local compilation of that source after two stated
  TeX-2026 compatibility changes; it has 163 pages.
- Source pages 147--149 are extracted into `source_evidence_pages_147_149.pdf`.
- The final packet is compiled with `-halt-on-error`.
- Every final packet page is rendered at high resolution to RGB PNG and
  visually inspected from the latest render.

## Human-review focus

The Dirac counterexample is independent of any subtle choice of locally
convex topology.  For the strengthened correction, confirm that the source
intends the standard inductive topology on the Roumieu union and projective
topology on the Beurling intersection.  Also confirm Fourier-transform
conventions, though `delta_e_hat(l)=I` is unaffected by the usual adjoint
choice.

