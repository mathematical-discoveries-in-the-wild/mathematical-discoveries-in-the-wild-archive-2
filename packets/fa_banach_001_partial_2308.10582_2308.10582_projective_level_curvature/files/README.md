# Curved projective levels and homogeneous multiplier powers

Result type: `partial`

Status: promoted new partial result, likely valid pending human review. It
fully answers the source question in dimension 3 and for even phases in
dimensions 4 and 6, but not for unrestricted phases in every `d>=4`.

Source paper:

- Aleksandar Bulj, “Generic norm growth of powers of homogeneous unimodular
  Fourier multipliers”, arXiv:2308.10582.
- Open-question location: Closing Remarks, Remark 1, source PDF page 8.
- `source_paper.pdf` is reconstructed from the cached arXiv source.
- `figures/open_problem_crop.png` is an exact source-page crop.

## Claimed contribution

1. **Curved-level criterion in every dimension.** In the affine chart
   `phi(u)=Phi(u,1)`, a regular point `a=grad phi(u0) != 0` produces the full
   transformed Hessian
   `[[H phi(u0),-a],[-a^T,0]]`. It is invertible exactly when `H phi` is
   nondegenerate on `a^perp`, equivalently when the regular projective level
   has nonzero Gauss--Kronecker curvature. The source stationary-phase proof
   then gives the maximal lower bound
   `||T_Phi^t|| >= c t^(d|1/2-1/p|)`.
2. **Full negative answer in dimension 3.** If every regular level curve on
   `S^2` failed the criterion, every component would be a whole great circle.
   Two distinct regular values exist by Sard and would yield two disjoint
   great circles, impossible because all great circles intersect.
3. **Even phases in dimensions 4 and 6.** Evenness permits descent to
   `RP^(d-1)`. Ishikawa--Morimoto's classification says every compact
   developable smooth hypersurface in `RP^3` or `RP^5` is a projective
   hyperplane. Components at two regular values would be intersecting
   hyperplanes, again impossible.
4. **Necessary condition and stress test.** Any affirmative example must have
   every regular projective level developable. Every nonconstant quadratic
   Rayleigh phase fails this requirement and has maximal growth.

## Files

- `main.tex`: exact transcription, definitions, theorem statements, proofs,
  proof intuition, limitations, references, and human-review notes.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: reconstructed source paper.
- `supporting_ishikawa_1999.pdf`: institutional-repository scan of the primary
  projective-geometry source.
- `figures/open_problem_crop.png`: exact crop of Closing Remark 1 and context.
- `verification.md`: proof audit and review checklist.
- `tmp/`: source build, packet build, and full-page visual-QA renders.

## Scope

No phase with submaximal growth is constructed, and no full answer is claimed
for unrestricted phases in dimensions `d>=4`. Compact nontrivial developable
hypersurfaces exist in `RP^4, RP^7, RP^13, RP^25`; therefore the dimension-3
intersection proof cannot simply be asserted in higher dimensions. Any future
counterexample also needs an analytic multiplier upper bound—failure of the
new lower-bound criterion is not enough.
