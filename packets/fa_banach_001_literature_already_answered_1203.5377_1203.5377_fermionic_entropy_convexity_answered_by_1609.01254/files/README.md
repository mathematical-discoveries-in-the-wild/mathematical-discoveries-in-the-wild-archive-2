# Literature status: fermionic entropy convexity

Status: `literature_already_answered` (full positive resolution of the
dimension-free Hessian/geodesic-convexity conjecture).

## Source question

Eric A. Carlen and Jan Maas, *An Analog of the 2-Wasserstein Metric in
Non-commutative Probability under which the Fermionic Fokker-Planck Equation
is Gradient Flow for the Entropy*, arXiv:1203.5377; Communications in
Mathematical Physics 331 (2014), 887-926.

Remark 5.6 on PDF page 24 proves, for Clifford dimensions `n=1,2`,

```text
Hess_rho S(nabla U,nabla U) >= ||nabla U||_rho^2,
```

and conjectures the same inequality for every `n`.

## Supporting answer

Eric A. Carlen and Jan Maas, *Gradient Flow and Entropy Inequalities for
Quantum Markov Semigroups with Detailed Balance*, arXiv:1609.01254; Journal
of Functional Analysis 273 (2017), 1810-1869.

The introduction on PDF page 2 explicitly says that the paper proves the sharp
geodesic-convexity result for the Fermi Ornstein-Uhlenbeck semigroup, thereby
solving the problem left open in the source paper. Theorem 8.6 on PDF page 34
proves geodesic `lambda_beta`-convexity in the metric associated with the Fermi
generator, where

```text
lambda_beta = min_j cosh(beta e_j / 2).
```

At infinite temperature (`beta=0`), `lambda_beta=1`, the invariant state is the
tracial state, and the supporting paper explains immediately before Theorem
8.6 that this metric is the source metric written with the same skew
derivations. In finite-dimensional Riemannian language, geodesic
1-convexity is exactly the Hessian bound conjectured in Remark 5.6.

## Scope

This fully resolves the source paper's all-dimensions Hessian conjecture. It
does not settle the separate question in Remark 5.7 concerning the sectional
curvature of the density manifold.

## Files

- `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: original question source, arXiv:1203.5377.
- `supporting_paper_1609.01254.pdf`: explicit later answer.
- Ledger: `runs/fa_banach_001/ledger/results/1203.5377_fermionic_entropy_convexity_answered_by_1609.01254.json`.

## Search evidence

The lane-0 cheap indexes were searched for the arXiv id and the terms
`Wasserstein metric`, `fermionic`, `Hessian`, `entropy convexity`, `Ricci`, and
`Clifford`; no prior packet was present. A local source search found the later
Carlen-Maas framework, and a bounded web/arXiv search located arXiv:1609.01254.
Its introduction explicitly identifies the old problem as solved, so this is
an already-known literature answer, not a new proof.
