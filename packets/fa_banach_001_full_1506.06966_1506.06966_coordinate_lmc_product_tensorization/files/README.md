# Candidate Full Result: Product Tensorization Resolves the Coordinate-LMC Dimension Conjecture

Status: **candidate full solution (likely valid; human review requested)**

Model: GPT5.6

Source: Thomas Bonis, *Rates in the Central Limit Theorem and diffusion
approximation via Stein's Method*, arXiv:1506.06966v6 (2018), Proposition 12
and the conjecture immediately following it on PDF pages 16--17.

## Claimed Contribution

Under the only sign convention consistent with the Gaussian example and with
the proof of Proposition 12, the conjectured complexity is correct. There are
constants depending only on the common strong-convexity and coordinate
Lipschitz constants such that the random-coordinate Rademacher scheme reaches

\[
  W_2(\nu_n,\mu)\leq\epsilon
\]

with

\[
  h\asymp \frac{\epsilon^2}{d},
  \qquad
  n=O\!\left(\epsilon^{-2}d^2\log\frac d\epsilon\right).
\]

Each step evaluates one scalar partial derivative, so this is also the
arithmetic complexity asserted in the source conjecture.

## Sign Convention in the Source

Equation (11) in Proposition 12 prints

\[
 (\partial_i u(y)-\partial_i u(x))(y_i-x_i)
 \leq -\rho (y_i-x_i)^2.
\]

This is a typographical sign error. It fails for the Gaussian example claimed
in the same proposition, is incompatible with an integrable density when
combined with the other hypotheses, and is replaced throughout the source's
proof by

\[
 (\partial_i u(y)-\partial_i u(x))(y_i-x_i)
 \geq \rho (y_i-x_i)^2.
\]

The packet proves the intended, nonvacuous conjecture with this corrected
strong-convexity sign and flags this interpretation prominently for review.

## Proof Intuition

The apparently multidimensional hypothesis is much stronger than it looks.
For all `x,y`, the source assumes

\[
 |\partial_i u(y)-\partial_i u(x)|\leq L|y_i-x_i|.
\]

Taking `x_i=y_i` shows that `partial_i u` is independent of every coordinate
except `x_i`. Hence

\[
 u(x)=c+\sum_{i=1}^d u_i(x_i),
 \qquad
 \mu=\bigotimes_{i=1}^d\mu_i.
\]

The source already proves an `O(sqrt(h))` stationary-bias estimate in
dimension one. Apply that estimate to every coordinate and tensorize the
quadratic transport cost to obtain `O(sqrt(d h))`, exactly the dimension
dependence conjectured by the source. The source's synchronous-coordinate
coupling contracts at rate `exp(-c h n/d)`. Choosing
`h` proportional to `epsilon^2/d` and burning in for
`O((d/h) log(d/epsilon))` steps finishes the proof.

## Verification Summary

- The separation implication follows directly by setting `x_i=y_i`.
- The product invariant law is preserved by every individual coordinate
  kernel, hence by their random-scan average.
- The exact identity
  `W2(product pi_i, product mu_i)^2 = sum_i W2(pi_i,mu_i)^2`
  follows from the additive quadratic cost.
- The random-scan kernel is a strict `W2` contraction for
  `h < 2 rho/L^2`, giving uniqueness and the claimed burn-in.
- The dimension-one bias input is the source's proved estimate in the proof of
  Proposition 12, specialized to `d=1`; its constant is uniform because all
  coordinates share the same `rho,L`.
- No numerical evidence is used as proof.

See [verification.md](verification.md) for the adversarial step check.

## Bounded Novelty Check

Searches performed on 2026-08-09 included the exact source title and arXiv id,
the quoted complexity conjecture, `random coordinate Langevin Monte Carlo`,
`Rademacher coordinate Langevin`, and close product/tensorization variants.
The later paper Ding--Li--Lu--Wright, *Random Coordinate Langevin Monte Carlo*
(arXiv:2010.01405; COLT 2021), studies a related coordinate algorithm with
Gaussian increments and more general potentials. The bounded search did not
locate an explicit resolution of Bonis's exact Rademacher-noise conjecture or
the simple product implication of its stated coordinatewise hypothesis. This
does not prove novelty; novelty confidence is moderate.

Primary links:

- Source: https://arxiv.org/abs/1506.06966
- Related later work: https://arxiv.org/abs/2010.01405

## Packet Contents

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv source PDF.
- `figures/open_problem_crop_page16.png` and
  `figures/open_problem_crop_page17.png`: complete two-page source evidence.
- `verification.md`: adversarial verification report.

## Human Review Recommendation

Send to a probability/MCMC reviewer. The main checks are:

1. confirm that the sign correction is indeed the intended reading of
   Proposition 12;
2. confirm that the dimension-one stationary-bias constant in the source is
   uniform over the coordinate potentials under common `rho,L`;
3. check whether the same tensorization observation already appears in later
   coordinate-LMC literature under the exact Rademacher scheme.

