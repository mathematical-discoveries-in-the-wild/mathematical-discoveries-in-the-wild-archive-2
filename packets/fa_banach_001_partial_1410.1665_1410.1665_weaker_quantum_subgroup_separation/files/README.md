# Weaker compact-quantum-subgroup separation condition

Status: `partial_result_likely_valid`

Source: Volker Runde and Ami Viselter, *On positive definiteness over
locally compact quantum groups*, arXiv:1410.1665, Remark 6.8 on PDF page 19.

## Result

Remark 6.8 asks whether the compact-subgroup separation theorem remains valid
under the weaker hypothesis that a state `mu` does not factor through the
subgroup quotient `Phi:C_0^u(G)->C^u(H)`.

The answer is affirmative in either of two broad regimes:

- `H` is coamenable, for an arbitrary locally compact ambient quantum group
  `G`;
- `G` is compact, for an arbitrary compact quantum subgroup `H`.

No structural condition (6.2) from the source theorem is needed in these
regimes. In particular, the answer is affirmative for every finite quantum
group pair and every classical compact subgroup.

## Mechanism

Failure of all desired positive-definite separators forces

```text
mu * theta = theta = theta * mu,
```

where `theta=h_H^u o Phi` is the subgroup Haar idempotent. If `H` is
coamenable, faithful universal Haar averaging forces `mu` to vanish on
`ker Phi`. If `G` is compact, `mu` agrees with the counit on the polynomial
coinvariant algebra, and Takeuchi correspondence identifies the polynomial
kernel as its augmentation ideal times `Pol(G)`.

## Remaining case

The noncompact ambient/noncoamenable subgroup case remains open. There Haar
averaging detects only the reduced image, while factorization is a universal
C*-algebra statement. Four focused upgrade attempts and the isolated
obstruction are recorded in
`runs/fa_banach_001/attempts/1410.1665_weaker_quantum_subgroup_separation.md`.

## Files

- `main.tex`, `solution_packet.pdf`: theorem and proof.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop.png`: exact Remark 6.8 evidence.
- `verification_report.md`: proof and artifact audit.

Ledger:
`runs/fa_banach_001/ledger/results/1410.1665_weaker_quantum_subgroup_separation.json`.
