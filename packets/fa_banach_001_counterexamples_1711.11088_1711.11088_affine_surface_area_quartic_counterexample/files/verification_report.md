# Verification Report

Candidate: arXiv:1711.11088, conjecture following Corollary 1 on extending the affine isoperimetric inequality from 2-homogeneous to general convex functions.

## Claim checked

The conjecture is false in every dimension. A quartic perturbation of the Gaussian potential makes the conjectured normalized ratio increase from its equality value.

## Verdict

candidate_counterexample_likely_valid_human_review_needed

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Official arXiv PDF page 7 states the inequality and then conjectures it for general convex functions. |
| Candidate regularity | valid | psi_epsilon=|x|^2/2+epsilon*x_1^4 is smooth, even, and has Hessian diag(1+12 epsilon x_1^2,1,...,1). |
| Strong convexity | valid | Every Hessian eigenvalue is at least one for epsilon at least zero. |
| Integrability | valid | exp(-psi_epsilon) is bounded by exp(-|x|^2/2). |
| Hessian determinant | valid | The determinant is exactly 1+12 epsilon x_1^2. |
| Equality base point | valid | At epsilon=0, both A(0) and Z(0) equal (2 pi)^(n/2), and all normalization exponents cancel to give R(0)=1. |
| Derivative of mass | valid | Z'(0)/Z(0)=-E[G_1^4]=-3. |
| Derivative of affine area | valid | Differentiating the determinant factor contributes 12 E[G_1^2]/(n+2) and differentiating the density contributes -E[G_1^4], giving 12/(n+2)-3. |
| Normalized derivative | valid | The derivative of log R at zero from the right is 12/(n+2)-3+3n/(n+2)=6/(n+2)>0. |
| Strict counterexamples | valid | Right differentiability and positive derivative imply R(epsilon)>1 throughout some interval (0,epsilon_n). |
| Minimum normalization | valid | psi_epsilon(0)=min psi_epsilon=0; additive constants do not explain the quartic failure. |
| All dimensions | valid | The calculation applies separately to every integer n at least 1. |
| Scope | valid | The result targets the new functional integral det(Hess psi)^(1/(n+2)) exp(-psi) and not the distinct weighted functional (16). |

## Differentiation audit

Let alpha=1/(n+2). On 0<=epsilon<=epsilon_0, the derivative of the affine-area integrand is

    exp(-|x|^2/2-epsilon*x_1^4)
      * [12 alpha x_1^2 (1+12 epsilon x_1^2)^(alpha-1)
         -x_1^4 (1+12 epsilon x_1^2)^alpha].

Because 0<alpha<=1/3, its absolute value is bounded by a fixed polynomial in x_1 times exp(-|x|^2/2). The mass derivative is dominated by x_1^4 exp(-|x|^2/2). Both dominators are integrable, so differentiation under the integral is valid by dominated convergence.

## Adversarial stress tests

- The conclusion is not based on a floating-point computation; the sign is the exact rational number 6/(n+2).
- No singularity occurs at the base point: determinant and density factors are smooth for nonnegative epsilon.
- The first-order sign is for the fully normalized ratio, including the variation of the mass on the right-hand side.
- A positive derivative at an equality point suffices: by the definition of one-sided derivative, (R(epsilon)-1)/epsilon is positive for all sufficiently small positive epsilon.
- The candidate is centered and even, so translation or barycenter corrections cannot restore the stated inequality.
- The literal additive-constant obstruction was independently checked: psi_a=|x|^2/2+a gives ratio exp(-2a/(n+2)). The quartic proof is retained because it survives the natural condition min psi=0.

## Deep upgrade audit

The initial one-dimensional observation was upgraded twice. First, the perturbation calculation was carried out for arbitrary dimension, producing the exact positive derivative 6/(n+2). Second, the example was required to be even, smooth, strongly convex, centered, and normalized by min psi=0, eliminating the most obvious objections to the literal additive-constant counterexample.

## Novelty check

On 2026-08-11, the exact arXiv id/title and conjecture wording, the Hessian-determinant affine surface area, Gaussian extremizers, floating functions, Ulam floating functions, weighted floating functions, and functional affine isoperimetric inequalities were checked against the run registry, solution, attempt, and proof-gap indexes and by bounded web/arXiv search. The searches found the source and related inequalities for different functional affine surface areas, but no answer or counterexample to this exact conjecture. This is a bounded check, not a guarantee of novelty.

## Artifact verification

- source_paper.pdf is the official 24-page arXiv PDF.
- figures/open_problem_crop.png is rendered from source PDF page 7 and includes the full corollary and conjecture.
- The proof is exact and does not depend on numerical quadrature.

Confidence: 99/100.

Recommended action: specialist review by an analyst working in log-concave functional inequalities or affine convex geometry.
