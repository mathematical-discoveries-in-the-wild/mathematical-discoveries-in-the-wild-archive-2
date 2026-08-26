# Verification

Status: candidate_substantial_partial_likely_valid_needs_human_review

## Source checks

- The accreditation sentence near the Brascamp--Lieb discussion is not an
  open problem.
- The remark after Theorem 4.1 is genuine and asks about Dirichlet and
  mean-convex Neumann Veysseire analogues.
- The source's locally convex proof uses the sign of the full second
  fundamental form, not merely its trace.

## Geometry checks

- For a rotational tube (s,r(s)theta), the outward mean curvature is
  -r''/(1+r'^2)^(3/2)+(n-2)/(r sqrt(1+r'^2)).
- The central radius-epsilon cylinder has mean curvature
  (n-2)/epsilon>0, requiring n>=3.
- While the radius is small, a bounded convex transition is dominated by the
  rotational curvature. A concave increasing transition has both terms
  nonnegative. Strict inequalities permit smoothing and attachment to fixed
  spherical lobes.
- The resulting family lies in a fixed ball, has two fixed positive-volume
  lobes, and has H>=h_0>0 uniformly.

## Weighted-curvature checks

- For V=kappa|x|^2/2 in Euclidean space,
  Ric_mu=Hess V=kappa g.
- Since |<x,nu>|<=R, choosing kappa=h_0/(2R) gives
  H_mu=H-kappa<x,nu>>=h_0/2.
- The harmonic mean of constant rho=kappa is exactly kappa.

## Spectral checks

- The domain and Gaussian weight are reflection-symmetric.
- The lobe-sign test is odd and has weighted mean zero.
- Its weighted L_2 norm is bounded below by the fixed lobe volumes.
- Its gradient is supported in a fixed-length radius-epsilon cylinder, so
  its Dirichlet energy is O(epsilon^(n-1)).
- The weighted Neumann Rayleigh quotient therefore tends to zero, contradicting
  any lower bound lambda_1^N>=kappa.

## Scope checks

- The packet does not claim to refute a Case-(3) inequality containing the
  source's boundary-trace variance term.
- It does not claim a Dirichlet counterexample.
- It explicitly restricts the geometric construction to dimensions n>=3.

## Artifact checks

- Both official source PDFs open as valid PDFs.
- main.tex compiled without errors.
- solution_packet.pdf was rendered page by page and visually inspected.
