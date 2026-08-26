# Verification Report

Candidate: arXiv:2412.15490, Remark 3, exact value of the best weighted
Sobolev constant (C_{2\alpha,6}).

## Claim checked

For every \(\alpha>0\),
\[
C_{2\alpha,6}=\sqrt3(\pi/2)^{2/3},
\]
the sharp Euclidean (D^{1,2}(\mathbb R^3)\to L^6(\mathbb R^3)) constant.

## Verdict

**likely valid**

No normalization conflict or missing analytic step was found. The proof uses
one substantial external theorem: Kleiner's sharp Euclidean isoperimetric
inequality for smooth three-dimensional Cartan--Hadamard manifolds.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Cone coordinates | valid | With (a=\alpha+1\), \,\(\rho=r^a/a\) and \(\varphi=a\theta\) turn the punctured weighted space into the flat cone of angle (2\pi a\) times \(\mathbb R\). |
| Weighted measure | valid | \(\rho\,d\rho\,d\varphi\,dz=r^{2\alpha+1}dr\,d\theta\,dy=|x|^{2\alpha}dx_1dx_2dy\). |
| Dirichlet energy | valid | The radial, angular, and vertical terms become respectively (v_\rho^2\), \(\rho^{-2}v_\varphi^2\), and (v_z^2\), with no residual factor. |
| Cone angle sign | valid | Since \(\alpha>0\), the total angle is (2\pi(\alpha+1)>2\pi\); this is the nonpositively curved (angle-excess) direction required by the smoothing. |
| Smooth completion | valid | A smooth nondecreasing slope from (1) to (a\) gives a convex warping function (h\); the surface curvature is \(-h''/h\le0\), and its linear exterior is exactly a cone exterior after a radial translation. |
| Axis cutoff | valid | The logarithmic cutoff has \(\int |\nabla\chi_\varepsilon|^2=O(1/|\log\varepsilon|)\) on bounded cylinders; bounded compactly supported functions therefore lose neither energy nor (L^6) mass in the limit. |
| Cartan--Hadamard bound | valid, external | Kleiner proves sharp Euclidean isoperimetry in dimension 3. Coarea and Schwarz rearrangement give the Euclidean sharp (p=2) Sobolev inequality. |
| Matching upper bound | valid | Truncated Euclidean near-extremizers fit in arbitrarily large flat balls placed sufficiently far from the cone axis. |
| Explicit constant | valid | For (U(x)=(1+|x|^2)^{-1/2}), \(\int U^6=\pi^2/4\) and \(\int|\nabla U|^2=3\pi^2/4\), hence the quotient is \(\sqrt3(\pi/2)^{2/3}\). |
| Extension to the source space | valid | The source space is the completion under precisely the energy plus weighted (L^6) norm, so the inequality and infimum identification extend from the dense smooth class. |

## Adversarial points checked

- The cone is not silently treated as smooth at its axis; the cutoff and
  compact-exterior completion are explicit.
- The smoothing does not need to agree with the cone all the way to its
  original vertex. Its eventual linear profile (h(s)=a(s-c)) is exactly
  isometric to the cone exterior via \(\rho=s-c\).
- The lower bound is not inferred from the source paper's sector
  rearrangement. It comes from sharp three-dimensional Cartan--Hadamard
  isoperimetry after the exact global cone transformation.
- The upper-bound sequence does not cross the cone seam or singular axis.
  Its support is placed in a genuinely Euclidean ball.

## External dependency

B. Kleiner, *An isoperimetric comparison theorem*, Invent. Math. 108
(1992), 37--47, DOI 10.1007/BF02100598. The standard implication from sharp
isoperimetry to the sharp Sobolev inequality is also recorded explicitly in
Muratori--Soave, arXiv:2103.08240.

## Novelty check

Bounded web/arXiv searches on 9 August 2026 covered:

- arXiv:2412.15490 and the exact title;
- the exact phrase “exact value of (C_{2\alpha,6})”;
- `weighted Sobolev best constant`, `Grushin sharp Sobolev constant`, and
  `flat cone Sobolev constant`;
- the source authors and the 2026 journal record.

No later exact answer or the cone identification used here was found. This is
not a comprehensive priority search.

## Confidence

Score: **91/100**

The coordinate calculation and approximation argument are explicit. The main
remaining review risk is whether a specialist wants a more formal statement
of the standard coarea implication or of the density at the singular axis.

## Human review recommendation

**send to human**

Verify the three coordinate identities, the convex-warping completion lemma,
and the passage through logarithmic cutoffs. Also perform a broader
literature-priority search around Sobolev inequalities on Euclidean cones.

