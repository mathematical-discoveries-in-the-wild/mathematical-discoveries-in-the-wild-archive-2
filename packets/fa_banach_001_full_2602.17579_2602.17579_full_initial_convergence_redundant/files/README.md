# All initial-data convergence assumptions in Theorem 5.6 are redundant

Status: `full_solution_likely_valid_with_strengthening`

Source: Bastian Hilder, Patrick van Meurs, and Upanshu Sharma,
*Non-equilibrium functional inequalities for finite Markov chains*,
arXiv:2602.17579.

## Result

Remark 5.7 conjectures that convergence of the full microscopic initial data
`mu_0^epsilon` can be removed from Theorem 5.6. This packet proves that
conjecture and a stronger statement: the theorem remains true after deleting
the entire convergence bullet, including convergence of both coarse initial
marginals.

There are two elementary replacements for the two uses of convergence:

- The stationary laws `rho^epsilon` converge on the finite state space to a
  strictly positive law. Hence their minimum coordinate is uniformly positive,
  and for every probability law `mu`, without any convergence,
  `H(mu | rho^epsilon) <= log(1/min rho^epsilon)`.
- Uniform positivity of the coarse initial laws and bounded inter-cluster exit
  rates give the direct differential inequalities
  `d/dt hat_mu_t(y) >= -R hat_mu_t(y)` and
  `d/dt eta_t(y) >= -R eta_t(y)`. Thus both stay above
  `c_0 exp(-RT)` on every fixed time interval, without convergence to an
  averaged initial law.

These are exactly the two uniform bounds for which the convergence assumptions
are used in the source and in the proof of the cited 2024 coarse-graining
theorem. The rest of the source proof is unchanged.

## Scope

This completely resolves the explicit conjecture in Remark 5.7 and strengthens
Theorem 5.6 by removing all three initial-data convergence requirements. It
retains the theorem's uniform strict positivity of the coarse initial data and
the `O(epsilon)` initial coarse relative-entropy assumption. Removing strict
positivity at time zero is a separate endpoint issue.

## Files and verification

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:2602.17579.
- `supporting_paper_2201.10256.pdf`: Hilder--Sharma's cited coarse-graining
  theorem and stationary-law convergence lemma.
- `figures/open_problem_crop.png`: Remark 5.7 on source PDF page 25.
- `figures/supporting_usage_crop.png`: the exact use of microscopic initial
  convergence in the cited proof, PDF page 21.

## Novelty check

Before promotion, the run indexes were searched for the source arXiv id,
title, theorem, and initial-data convergence phrases. A bounded arXiv/web
search on 2026-08-13 used the exact conjecture sentence, source title, arXiv id,
and variants of “remove initial-data convergence” and “coarse-graining Markov
chains.” It found the source and the cited arXiv:2201.10256 paper, but no later
answer or strengthening.

## Human-review recommendation

Review as a short, likely valid full solution with strengthening. The key
checks are positivity of the limiting stationary law, the elementary entropy
bound, and cancellation of the fast within-cluster generator when deriving the
coarse marginal differential inequality.

