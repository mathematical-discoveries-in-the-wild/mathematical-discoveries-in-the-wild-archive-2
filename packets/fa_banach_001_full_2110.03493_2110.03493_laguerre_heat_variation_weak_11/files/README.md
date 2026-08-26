# Weak (1,1) variation for the Laguerre heat semigroup

Status: `candidate_full_likely_valid` (analytic proof; exact symbolic audit of
the only polynomial-degree calculation).

This packet answers the endpoint question stated on page 9 of Jorge J.
Betancor and Marta de León-Contreras, *Variation inequalities for Riesz
transforms and Poisson semigroups associated with Laguerre polynomial
expansions*, arXiv:2110.03493v2.

For every `rho > 2` and `alpha in (0,infinity)^n`, the rho-variation of the
Laguerre heat semigroup is of weak type `(1,1)` for the Laguerre probability
measure.  The proof uses the local/global decomposition already built in the
source paper:

1. The source's global Sasso estimate already controls the total time
   variation of the global heat kernel by a positive weak-`(1,1)` operator.
2. On the local region, write `r = exp(-t/2)`.  The derivative of a scalar
   Mehler component has a cubic numerator, while derivatives of its spatial
   gradients have polynomial numerators of degrees at most five and four.
   Their total variations are therefore controlled by their suprema, giving
   the vector-valued Calderón--Zygmund size and smoothness estimates.
3. Strong `L2` variation for symmetric diffusion semigroups supplies the local
   `L2` input.  The source's measure-transfer lemma and vector-valued
   Calderón--Zygmund argument then give local weak `(1,1)`.

The script `code/verify_derivative_degrees.py` symbolically verifies the three
polynomial numerators and their degree bounds.  It is an audit aid only; the
proof is analytic.

Human review should focus on the passage from bounded critical-point count to
total variation, the local supremum estimates, and the reuse of the source's
global weak-`(1,1)` kernel operator.  The packet deliberately claims only the
parameter range asked in the source.

