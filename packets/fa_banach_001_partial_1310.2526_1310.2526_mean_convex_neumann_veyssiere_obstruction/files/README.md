# Partial Counterexample: Mean-Convexity Does Not Control the Pure Neumann Gap

Status: candidate_substantial_partial_likely_valid_needs_human_review

Run: fa_banach_001  
Agent: agent_lane_07  
Target: Alexander V. Kolesnikov and Emanuel Milman,
*Brascamp-Lieb type inequalities on weighted Riemannian manifolds with
boundary*, arXiv:1310.2526.

## Exact target

The genuine signal is the remark after the generalized Veysseire theorem.
It asks whether analogues exist for the Dirichlet and generalized
mean-convex Neumann regimes corresponding to Cases (2) and (3) of the
preceding Brascamp--Lieb theorem.

The other queue signal merely says the authors do not know whom to credit for
a boundaryless weighted-Riemannian Brascamp--Lieb inequality; it is not an
open mathematical problem.

## Result

For every dimension n>=3 there are smooth bounded connected Euclidean
domains Omega_epsilon and a fixed Gaussian weight

    dmu = exp(-kappa |x|^2/2) dx

such that

    Ric_mu = kappa g,
    H_mu >= c > 0,
    lambda_1^N(Omega_epsilon,mu) -> 0.

The domains are two fixed lobes joined by a tube of radius epsilon. They can
be smoothed with a uniform positive ordinary mean-curvature lower bound.
Choosing kappa smaller than that bound divided by the common containing
radius preserves strict weighted mean-convexity. An odd function equal to
plus or minus one on the lobes has energy O(epsilon^(n-1)) and variance
bounded below.

Hence the pure Neumann Veysseire estimate

    lambda_1^N >= (average_mu 1/rho)^(-1)

is false under generalized mean-convexity alone, even for constant
rho=kappa. A valid Case-(3) analogue must retain a boundary-trace correction
or strengthen mean-convexity to nonnegative second fundamental form.

## Scope

This is a negative answer only to the pure Neumann spectral-gap reading.
It does not refute the boundary-corrected form suggested by the actual
Case-(3) Brascamp--Lieb inequality: the dumbbell test has nonconstant boundary
trace, so the boundary variance term is substantial. The Dirichlet analogue
also remains open.

## Files

- main.tex: theorem and proof.
- solution_packet.pdf: compiled proof packet.
- source_target_1310.2526.pdf: official target paper.
- source_veyssiere_1105.6080.pdf: official original Veysseire paper.
- VERIFICATION.md: geometry, curvature, Rayleigh, scope, and artifact checks.

## Novelty check

The cheap run indexes were searched for the arXiv id, title, Veysseire,
harmonic-mean curvature, mean-convex boundary, and dumbbell spectral-gap
phrases. Bounded primary-source searches found the target, Veysseire's
boundaryless theorem, and later boundary Brascamp--Lieb work, but no explicit
statement of this weighted mean-convex dumbbell obstruction. The result still
needs expert review, especially for how the source authors intended the word
“analogous” in the Case-(3) remark.
