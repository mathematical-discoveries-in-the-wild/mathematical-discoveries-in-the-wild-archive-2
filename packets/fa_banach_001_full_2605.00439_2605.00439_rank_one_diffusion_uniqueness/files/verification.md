# Verification report

Verdict: `candidate_full_sufficient_condition_theorem_likely_valid`

## Current-source audit

The packet uses the official arXiv:2605.00439v3 PDF dated 7 July 2026, not
the older locally cached v2 source. The concluding uniqueness and VMO bullets
remain unchanged. Definition 1.2 specifies bounded weak solutions, Corollary
1.5 gives bounded-data existence, and Proposition 3.4(b) gives local `L2`
attainment of the initial trace for bounded linearized solutions.

## Structural reduction audit

For fixed directions and spatially homogeneous weights,
`D_e beta_r(t,u) = alpha_r(t,u) D_e u` by the Sobolev chain rule. Thus the
difference of two equations is exactly
`w_t = sum_r D_e_r^2 z_r`, with
`z_r = beta_r(t,u)-beta_r(t,v)`. Positivity of every `alpha_r` gives sign
agreement and a Lipschitz bound `|z_r| <= L_r |w|` on the compact joint range.

## Kato audit

The finite-direction Kato inequality is the standard parabolic Kato argument
applied separately along lines parallel to each fixed direction. The signs
of all `z_r` agree with the sign of the single time variable `w`; summing the
directional inequalities is therefore legitimate. The packet records both
the Steklov/convex approximation and implicit-time derivations. This is the
main point requiring expert scrutiny.

## Weighted estimate audit

For `omega=(1+|x|^2)^(-p)`, `p>n/2`, direct differentiation gives
`|D_e^2 omega| <= (2p+4p(p+1)) |e|^2 omega`. The weight and its first two
derivatives are integrable, so cutoff errors vanish for bounded nonlinear
flux differences. Distributional Gronwall gives the one-sided estimate.

## Initial-trace audit

Each quasilinear solution is a bounded solution of a linear homogeneous
equation with bounded uniformly elliptic coefficient `a(t,x,u)`. Source
Proposition 3.4(b) yields local `L2` convergence to its distributional trace.
Local Cauchy--Schwarz plus the integrable weighted tail upgrades this to the
weighted `L1` convergence required by Gronwall.

## Novelty audit

Exact-title, exact-equation, nonlinear-diffusion, Kato, bounded non-integrable,
and rank-one searches on 2026-08-11 found classical isotropic entropy
contraction theory (especially Endal--Jakobsen, arXiv:1404.6418) but no exact
fixed-rank-one-cone result for the source's bounded weak class. The isotropic
case is classical; the packet's substantive extension is the finite fixed
direction cone and its direct compatibility with the source trace theorem.

## Computational sanity check

`code/check_weight_hessian.py` checks the exact Hessian formula and samples
the advertised global directional bound. The proof is symbolic and does not
depend on computation.

## Render audit

Final `latexmk` compilation completed without warnings, overfull/underfull
boxes, or unresolved references.  All four rendered pages were inspected at
full resolution and are clean, legible, and free of clipping or layout
defects.  The SHA-256 digest of `solution_packet.pdf` is
`cc23e6fc9136607de9c70615b38021f6020d48ad8b6e85b5d93d10152f1d214b`.

## Human verifier focus

1. Check the finite-direction Kato lemma at the stated weak regularity.
2. Check cutoff passage in the weighted inequality.
3. Check that source Proposition 3.4(b) applies separately to both nonlinear
   solutions after freezing their respective coefficients.
