# Verification audit

## Exact source match

Remark 3.4 on source PDF page 11 attributes to Horak the conjecture that, for
each `a>1`, there is a `p*(a)>2` such that the second LS eigenvalue equals the
vertical antisymmetric branch on `[2,p*]` and is strictly below it for every
`p>p*`. The source additionally anticipates `p*=infinity` for `a>=2`.

The abstract's broad open-problem language is answered by the same paper, but
this rectangle conjecture is explicitly left as a conjecture in its closing
remarks. The packet therefore targets only the surviving Remark 3.4 question.

## Proof audit

### 1. Geometry

For `1<a<2`, put

`r=(a+1-sqrt(2a))/2`.

Open radius-`r` disks centered at `(r,r)` and `(a-r,1-r)` lie in opposite
corners of `R_a`. They are tangent because

`(a-2r)^2+(1-2r)^2=4r^2`.

Both fit because `r<1/2<a/2`. The decisive strict scale gap is

`r-a/4=(sqrt(a)-sqrt(2))^2/4>0`.

### 2. Genus-two upper bound

Let `delta_i` be distance to the boundary on disk `i`, extended by zero. The
two supports have disjoint interiors and the profiles are congruent. The
unit `L^p` sphere in their two-dimensional span is odd-homeomorphic to a
circle and has Krasnoselskii genus two, so it is admissible in the definition
of `lambda_2`. Every nonzero linear combination has the same quotient. Polar
integration gives

\[
\int |\nabla\delta_i|^p=\pi r^2,
\qquad
\int |\delta_i|^p
=\frac{2\pi r^{p+2}}{(p+1)(p+2)}.
\]

Therefore

\[
\lambda_2(p;R_a)\le
\frac{(p+1)(p+2)}{2r^p}.
\]

Tangency at one boundary point does not affect the Sobolev integrals or the
disjoint-support calculation.

### 3. Antisymmetric-branch lower bound

By the source's definition,
`lambda_bar(p;R_a)=lambda_1(p;(0,a/2)x(0,1))`. For almost every horizontal
slice, sharp one-dimensional Dirichlet Poincare on an interval of length
`a/2`, followed by `|grad u|^p>=|u_x|^p`, gives

\[
\lambda_{\rm bar}(p;R_a)
\ge (p-1)(2\pi_p/a)^p
\ge (p-1)(4/a)^p,
\]

where
`pi_p=2 integral_0^1 (1-s^p)^(-1/p) ds >=2`. The factor `p-1` matches the
Rayleigh-quotient normalization used by the source (and returns the usual
`pi^2/L^2` constant at `p=2`).

### 4. Strict comparison and last contact

Comparing the two preceding displays gives exactly

\[
\frac{(p+1)(p+2)}{2(p-1)}
\left(\frac{a}{4r}\right)^p<1.
\]

Because `a/(4r)<1`, the inequality holds eventually. The standard vertical
two-partition test also gives `lambda_2<=lambda_bar` for every `p>1`.
At `p=2` and `1<a<2`, the `(2,1)` rectangle mode is the second Laplace mode,
so equality holds. Continuity in `p` makes the equality set closed; eventual
strictness makes it bounded. Its supremum is thus a finite maximum, and no
later equality can occur.

## Computational and visual verification

`code/check_rectangle_threshold.py` performs 29,997 dense-grid checks of disk
placement, tangency, and `rho<1`, plus 14 threshold checks. The first passing
integer `p` for `a=1.01, 1.10, 1.25, 1.50, 1.75, 1.90, 1.99` is respectively
`15, 23, 49, 195, 1375, 13016, 2209774`. These checks corroborate, but do not
replace, the proof.

The source excerpt is rendered directly from `source_paper.pdf`. The final
packet is compiled with a halting LaTeX build, checked for warnings, rendered
to RGB PNG images, and every page is visually inspected.

## Upgrade history, novelty, and review focus

Seven materially distinct attempts were made: source/literature triage;
optimal two-disk geometry; an explicit finite-p criterion; near-`p=2` branch
identification; anisotropic rectangle monotonicity; the `a>=2` endpoint; and
domain-stability via critical groups. The last four expose genuine missing
rigidity or nonlinear-branch inputs rather than further consequences of the
present estimate.

Four cheap run indexes and bounded exact-title, exact-conjecture,
rectangle-symmetry, and `p`-to-infinity searches found Bobkov's 2026 source
and Horak's 2011 numerical paper, but no proof or later resolution through 11
August 2026. Novelty confidence is moderate because the packing argument is
elementary and could exist in unindexed folklore.

Human review should focus on the genus-two admissibility of the cone sphere,
the exact quotient for disjoint tangent supports, the normalization of the
one-dimensional Poincare constant, and the continuity/last-contact step. The
result proves eventual strictness for `1<a<2`, not the pre-contact equality
interval and not the anticipated `a>=2` regime.
