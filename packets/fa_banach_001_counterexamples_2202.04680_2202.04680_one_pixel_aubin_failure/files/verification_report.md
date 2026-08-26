# Verification report

## Claim checked

The Aubin property required by the cited nonlinear PDHG convergence theorem is
not automatic for the functional class of arXiv:2202.04680. A valid one-pixel,
two-class, zero-feature instance fails it at a saddle point with zero dual
variable.

## Checks

1. **Admissibility.** The source sets the pixel space to R^(N1 x N2);
   N1=N2=1 is allowed. Two channels are allowed, zero feature maps are allowed,
   and the smoothed denominator remains positive because epsilon>0.
2. **Operator reduction.** The discrete gradient is zero on one pixel. With
   zero features, every average and every data-discrepancy component is zero,
   so both the nonlinear map and its derivative vanish identically.
3. **Saddle map.** Substituting the zero operator into the exact map from the
   cited convergence analysis gives H=N_U x N_C, with no missing affine
   residual.
4. **Reference solution.** The simplex barycenter and zero dual point satisfy
   0 in H; zero lies in the dual constraint set.
5. **Normal-cone computation.** For p_t=t(1,-1), t>0, the unique simplex
   maximizer is e1, hence (N_U)^(-1)(p_t)={e1}.
6. **Aubin quantifiers.** In the residual metric-regularity formulation used
   by the cited paper, the left side is the distance from the barycenter to
   {e1} x C, namely 1/sqrt(2). The residual on the right is the distance from
   t(1,-1) to span{(1,1)}, namely sqrt(2)t. This directly contradicts every
   finite Aubin modulus.
7. **Dual smallness.** The reference dual variable equals zero, so every
   projection onto a nonlinear dual block also equals zero.
8. **Independent obstruction.** The conjugate of the source's norm term is an
   indicator of dual balls. Two distinct interior points violate every positive
   strong-convexity inequality, so the cited theorem's strong-convexity
   hypothesis is not automatic either.

## Scope

The counterexample disproves automatic validity over the whole model class. It
does not prove algorithmic divergence and does not exclude the Aubin property
under strict complementarity, nondegeneracy, or other assumptions for
particular images.

Verdict: candidate full counterexample, likely valid, suitable for human
review.

## Interrupted-lane recovery audit (2026-08-21)

The exact source question and linearized saddle-map definition were rechecked
against the source. The one-pixel zero-feature specialization, normal cones,
fixed-distance inverse image, and residual metric-regularity contradiction
were independently recomputed; the crop script was rerun. `main.tex` was
force-rebuilt to three pages. The log has no LaTeX errors, undefined
references, or overfull boxes. All pages were rendered at 120 dpi and visually
inspected with no clipping, overlap, malformed formulas, or unreadable
evidence.
