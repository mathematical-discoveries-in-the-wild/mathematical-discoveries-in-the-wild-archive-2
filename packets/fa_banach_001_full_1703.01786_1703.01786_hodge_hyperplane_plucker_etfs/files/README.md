# Hodge-hyperplane Plucker ETFs

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source:

- John I. Haas, Jameson Cahill, Janet Tremain, and Peter G. Casazza,
  *Constructions of biangular tight frames and their relationships with
  equiangular tight frames*, arXiv:1703.01786v2.
- Exact target: Question 6.3 on PDF page 17.
- Source evidence: `figures/open_question_crop.png`.

## Claimed contribution

Every real unit-norm `(n,t)` ETF `{u_j}` with `t >= 3` produces a Plucker ETF.
Take the hyperplane projections

```text
Q_j = I_t - u_j u_j^T.
```

They form a tight `(n,t-1,t)` fusion frame. The Hodge isometry identifies the
Plucker vector of `u_j^perp` with `*u_j` up to sign, so the lifted Plucker
vectors are again an `(n,t)` ETF. Regular simplex ETFs give the infinite
family

```text
(n,m,l,t) = (t+1,t,t-1,t),  t >= 3.
```

The first member is an explicit tetrahedral `(4,3)` ETF lifted from a tight
`(4,2,3)` fusion frame, already different from the source's
`(16,6,2,4)` example.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_question_crop.png`: source definition and exact question.
- `code/verify_hyperplane_family.py`: numerical checks for `3 <= t <= 12`.
- `verification.md`: build, numerical, visual, and novelty checks.

## Novelty guardrail

On 2026-08-11, the run indexes and bounded arXiv-facing searches for the exact
identifier, `Plucker ETF`, `Plücker ETF`, Plucker-embedding/ETF combinations,
and Hodge-star/hyperplane variants found the source and general frame
literature but no later answer or this construction. This is not a priority
claim; specialist review remains appropriate.

## Human review focus

- Confirm that the source's lifted-Plucker orientation convention can only
  change each vector by a sign. The proof is designed to be insensitive to it.
- Confirm that Definition 6.2 requires only a tight fusion frame, not a BTFF.
- Check the fixed signed-permutation convention between maximal minors and
  Hodge-star coordinates; it is an ambient orthogonal map and cannot affect
  the ETF property.
