# Verification report

Verdict: `candidate full solution to source Remark B.2, likely valid, human review requested`; the inf-sup theorem is a substantial partial result for the separate Remark 4.3.

## Mathematical dependency audit

1. The fixed rectangle `R0=T_L x (0,h0)` lies in every source channel.
2. The mean-zero Poincare constant on `R0`, periodic in `x`, is
   `lambda0=max(L/(2*pi),h0/pi)` by its Fourier spectrum.
3. Averaging the one-dimensional fundamental theorem of calculus gives
   `g(x,h0)=avg_y g + h0^{-1} integral_0^{h0} t p_y(x,t)dt`; Cauchy--Schwarz
   gives the stated coefficients `2/h0` and `2h0/3`.
4. Integrating from `h0` to `h(x)` and interchanging the two vertical
   integrations gives the upper-fiber coefficient `(h(x)-h0)^2`, hence at
   most `D^2`. No derivative of `h` is used.
5. If `c` is the base-rectangle mean and the whole-domain mean of `p` is
   zero, then `||p-c||_2^2=||p||_2^2+|Omega|c^2`. Thus anchoring to the
   different mean cannot weaken the desired estimate.
6. In the oscillatory example, all upper teeth have equal area and the even
   alternating signs make the pressure exactly mean zero; its squared norm
   is `2*pi*D`.
7. Toothwise integration of the divergence leaves only the lower-interface
   trace. The curved-top trace vanishes, and the horizontal flux has zero
   endpoint contribution because each tooth height vanishes there.
8. With the stated Fourier convention, the alternating square wave satisfies
   `sum |w_hat(k)|^2/|k|=14*zeta(3)/(pi^2*N)`. The base bottom condition gives
   the dual `H^{1/2}` trace estimate mode by mode, yielding the displayed
   inf-sup constant exactly.
9. For `h_N=h0+D(1-cos Nx)`, both terms defining the source geometry
   parameter are fixed multiples of `N^2`, so `M_N=kappa N`.

No unproved lemma or computational premise remains in either theorem.

## Scope audit

- Fully answered: source Remark B.2. The mean-zero Poincare bound has no
  dependence on `M=||h'||_infinity`.
- Not claimed: sharpness of the new explicit constant in `L,h0,h1`.
- Substantial partial progress: source Remark 4.3. Smooth periodic channels
  force `beta^{-1} >= c sqrt(M)`.
- Still open: whether the source's `O(M^2)` Stokes inf-sup upper exponent can
  be reduced, and the exact exponent between `1/2` and `2`.

## Upgrade-attempt audit

Eight focused attempts or stress tests are recorded in the attempt note. The
direct vertical-divergence and Piola routes introduce uncontrolled horizontal
derivatives or curvature. Quantitative Bogovskii estimates for star-shaped and
chained domains did not supply a justified universal subquadratic bound for
arbitrary source channels. The remaining full-upgrade probability was judged
low enough to leave the exponent gap explicit.

## Novelty audit

On 13 August 2026, searches covered the exact source title, arXiv id, author,
both quoted optimality phrases, and combinations of `periodic channel`,
`Poincare constant`, `LBB constant`, `slope`, and `oscillating boundary`.
General uniform-Poincare work (arXiv:1208.6045) and quantitative Bogovskii
papers (arXiv:1103.3718 and arXiv:2010.04105) were also checked. No explicit
answer to Remark B.2, no base-rectangle proof, and no alternating-tooth lower
bound for Remark 4.3 were found. Novelty confidence remains provisional
pending expert review.

## Human-review focus

- Check the averaged horizontal trace identity and its `2h0/3` coefficient.
- Check that the whole-domain zero mean makes the base-mean anchoring valid.
- Check the toothwise flux identity at the zero-height endpoints.
- Check the complex Fourier normalization and the factor
  `14*zeta(3)/(pi^2*N)`.

## Artifact verification

- `latexmk` completed successfully; the final log has no warnings, undefined
  references, overfull boxes, or underfull boxes.
- `solution_packet.pdf` is a four-page A4 document. Ghostscript parsed it
  successfully, and `pypdf` reopened all pages and extracted text from each.
- All four final pages were rendered at 170 dpi and inspected at original
  detail. The source crop, prose, equations, references, and page boundaries
  are clean and legible; two spacing defects found in the first render were
  corrected and the affected pages re-rendered and re-inspected.
- SHA-256 of `solution_packet.pdf`:
  `9e1e1d1863d6da4b94c2f2c7366969a86186a8d524ef03aeeca0b0b2c5490778`.
- SHA-256 of `source_paper.pdf`:
  `1ac8eded04143a6bff7ba3cc2a5176b5c722fd4a1702a4db58ddd99c165e532a`.
- SHA-256 of `figures/open_problem_crop.png`:
  `25e6df9aacab8b87c5324f56588acb7a668480fc97d2f917e71097535f1aa81e`.

