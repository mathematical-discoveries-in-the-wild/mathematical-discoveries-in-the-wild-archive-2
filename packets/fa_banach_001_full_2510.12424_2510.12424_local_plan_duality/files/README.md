# Local-plan duality on infinite metric-measure spaces

Status: `candidate_full_solution_likely_valid`

Source: Luigi Ambrosio, Toni Ikonen, Danka Lučić, and Enrico Pasqualetto,
*Metric Sobolev spaces II: dual energies and divergence measures*,
arXiv:2510.12424 (2025), Remark 5.13 on PDF page 59.

## Result

The future-work extension in Remark 5.13 can be completed.  A local plan is a
positive Borel measure on open-ended locally rectifiable curves whose
arclength occupation measure has density in `L^q(m)` and whose integrated
finite-endpoint boundary is locally finite.  If `B_q^loc(mu)` is the infimum of
the barycenter norm over local plans with boundary `-mu`, then

```text
B_q^loc(mu) = D_q(mu) = F_p(mu)
```

for every boundedly-finite signed measure `mu`, every metric measure space in
the source's sense, and conjugate exponents `p in [1,infinity)`,
`q in (1,infinity]`.  Whenever the common value is finite, the local-plan
infimum is attained by a plan concentrated on injective curves, with exact
mass and boundary identities.

The endpoint characterization explicitly includes transport to or from
infinity.  If the optimal plan is split into curves with two finite ends,
only a finite left end, and only a finite right end, then its finite starts are
`mu^+` and its finite ends are `mu^-`.  For finite `mu`, the difference of the
one-ended masses is exactly `mu^+(X)-mu^-(X)`.

## Proof mechanism

The source's derivation/current correspondence localizes isometrically by
bounded-support cutoffs.  A `D_q`-minimizer exists and is acyclic by Theorem
5.9.  Its locally normal current therefore has mass `|b|m`, boundary `-mu`,
and is acyclic.  The local superposition theorem of Ambrosio--Renzi--Vitillaro
(arXiv:2503.18157, Theorem 1.4) represents it by injective open-ended curves
with exact mass and boundary variation.  This gives an optimal local plan
with barycenter exactly `|b|`.  Conversely, integrating any admissible local
plan gives a locally normal current, hence a derivation with norm bounded by
the plan barycenter.

## Files

- `main.tex`, `solution_packet.pdf`: full statement and proof.
- `source_paper.pdf`: official arXiv source paper.
- `supporting_paper_2503.18157.pdf`: decisive local-superposition theorem.
- `figures/open_problem_crop.png`: source screenshot of Remark 5.13.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `code/verify_examples.py`: exact sign and integrability sanity checks.
- `verification.md`: proof, source, build, and novelty audit.

## Review recommendation

High-priority expert review.  The key points to check are the cutoff proof of
the local derivation/current isometry and the definition of the integrated
finite-endpoint boundary.  Once those are accepted, both inequalities and
attainment follow directly from the two cited source theorems.
