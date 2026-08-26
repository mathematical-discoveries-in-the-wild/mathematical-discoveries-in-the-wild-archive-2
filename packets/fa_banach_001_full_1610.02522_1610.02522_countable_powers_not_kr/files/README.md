# Neither countable power is a k_R-space

This packet gives a candidate full negative answer to Question 5.11 of
arXiv:1610.02522.

## Result

In ZFC, neither `(S_2)^omega` nor `(S_omega)^omega` is a `k_R`-space.

## Proof mechanism

Both `S_2` and `S_omega` contain a closed countably infinite discrete set
`D`.  Inside `D^omega`, the sequences whose support has size at most one
form a closed copy of the source paper's metrizable test space `P_0`.

It follows that `(S_omega)^omega` contains a closed copy of
`S_omega x P_0`, which the source proves is not `k_R`.  Since the power is
stratifiable and closed subspaces of stratifiable `k_R`-spaces are `k_R`,
the power cannot be `k_R`.

Likewise, `(S_2)^omega` contains a closed `S_2 x P_0`.  If the power were
`k_R`, that subspace would be `k_R`; its perfect quotient under the standard
map `S_2 -> S_omega` would make `S_omega x P_0` a `k_R`-space, again a
contradiction.

## Files

- `main.tex`: theorem, construction, complete proof, scope, and novelty audit.
- `solution_packet.pdf`: compiled expert-facing packet.
- `verification.md`: source, literature, proof, and render audits.
- `source_paper.pdf`: arXiv:1610.02522.
- `supporting/banakh_gabriyelyan_2016_closed_subspaces.pdf`: closed-heredity
  theorem for stratifiable `k_R`-spaces.
- `supporting/ceder_1961_countable_products_M3.pdf`: countable-product theorem
  for stratifiable (`M_3`) spaces.
- `supporting/arens_s2_paracomplex_2026.pdf`: proof that `S_2` is
  stratifiable.

Status: candidate full result, likely valid. Independent expert review is
requested, especially for the closed `P_0` embedding and the two inheritance
steps.
