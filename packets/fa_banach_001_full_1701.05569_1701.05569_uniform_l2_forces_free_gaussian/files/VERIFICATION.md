# Verification report

## Claim checked

For the stereographic scaling scheme of arXiv:1701.05569:

- unrestricted densities satisfying the source's uniform `L1/L2` bounds can
  have non-Gaussian limits;
- every translation-invariant limit under those same bounds is the free
  massive Gaussian.

## Adversarial mathematical audit

- Checked that the source defines the interacting sphere measures as
  normalized densities relative to smoothed Gaussian references and assumes a
  uniform positive `L1` lower bound and finite `L2` upper bound.
- Checked that the transpose of `I_k=U_alpha U_beta_k` puts both interacting
  and reference measures on the common space `D'(R^d)`.
- For the positive example, verified that
  `rho_k=1+epsilon cos(phi(I_k h))` is continuous and lies between
  `1-epsilon` and `1+epsilon`.  Its transported density depends only on the
  image coordinate `Phi(h)`, so no injectivity of the transport is needed.
- Checked bounded-continuous weighting: convergence of the transported
  Gaussian references implies convergence of the normalized cosine tilts.
- Checked non-Gaussianity on the one-dimensional marginal.  Its density
  relative to a nondegenerate normal law is `1+epsilon cos x`, which cannot be
  the exponential-quadratic ratio of two Gaussian densities.
- Re-derived the source's `L1`-to-`L2` inequality after transport.  Passing to
  weak limits is legitimate for bounded continuous cylinder functions and
  their squared absolute values.
- Extended the limiting expectation functional from bounded cylinder
  functions to `L2(gamma)`, applied Riesz representation, and used positivity
  plus normalization to obtain `nu=r gamma` with `r>=0`, `r in L2(gamma)`,
  and `int r dgamma=1`.
- Checked the free-reference convergence from the source's exact covariance
  identity and mollifier-error limit; the limit covariance is
  `(-Delta+m^2)^(-1)`.
- Proved strong mixing directly.  Translated cross-covariances of test
  functions tend to zero by Riemann--Lebesgue, hence correlations factor for
  cylinder exponentials.  Their span is dense in `L2(gamma)`.
- If `nu` is translation invariant, Radon--Nikodym uniqueness makes `r` fixed
  by every translation.  Mixing forces the fixed subspace to consist only of
  constants, and normalization gives `r=1`.
- Checked that the source proves Euclidean invariance for limits obtained from
  `O(d+1)`-invariant densities, including its bounded continuous
  self-interaction examples.  The negative theorem therefore covers the
  advertised Glimm--Jaffe class.

## Scope audit

The source's compactness proposition permits arbitrary densities satisfying
the norm bounds, while its Glimm--Jaffe theorem imposes invariant and
reflection-positive structure.  The packet states both answers and does not
claim the deliberately non-invariant cosine tilt is a Euclidean QFT measure.

## Literature audit

- Searched all cheap run indexes for arXiv:1701.05569, its title, the exact
  open-question wording, non-Gaussianity, and stereographic scaling.
- Inspected the full sources of arXiv:2311.04137 and arXiv:2502.07546.  They
  are closely related but use materially different hypotheses and do not
  explicitly resolve this source's scheme.
- No exact later answer was found.  Novelty is plausible but provisional.

## Packet/render QA

- The source PDF is the official 21-page arXiv PDF.
- The evidence crop contains the complete title, author, abstract, and exact
  open-problem sentence.
- The final packet was compiled twice with fatal-error checking, text
  extracted, and every rendered page visually inspected.

## Verdict

Candidate full resolution, likely valid.  Recommended verifier focus: common
transport notation, limiting `L2` domination, and the boundary between the
unrestricted compactness result and the invariant Glimm--Jaffe result.
