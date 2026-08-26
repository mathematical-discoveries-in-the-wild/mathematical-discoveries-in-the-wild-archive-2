# RFD sub-semidual quotients are subduals

This packet gives a substantial partial answer to Open Problems 3 and 3' on
page 34 of arXiv:1511.07105.

For every discrete group, the finite-dimensional part of any sub-semidual is
automatically conjugation-closed.  The determinant character occurs in a
positive tensor power, compact-semigroup recurrence supplies its inverse, and
exterior-power duality then supplies the conjugate representation.  If the
associated quotient `C*_S(G)` is residually finite-dimensional, its defining
kernel is an intersection of this conjugation-stable family of finite-dimensional
kernels.  Inversion therefore descends to the quotient, proving that all of
`S` is a subdual.

This also answers the locally compact Eberlein version under the corresponding
RFD hypothesis and gives the RFD-associated subclass of Open Problem 2.

Status: `candidate_partial_likely_valid`, pending human review.  The packet
explicitly explains why the tempting unrestricted compact-quantum-group
antipode argument is circular on an arbitrary exotic completion.

Files:

- `main.tex`: complete proof, antipode audit, upgrade history, scope, and
  literature-search record.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: source arXiv paper.
- `supporting_paper_woronowicz_compact_quantum_groups.pdf`: primary supporting
  compact-quantum-group reference.
- `figures/open_problem_crop.png`: readable source excerpt containing Problems
  3 and 3'.
- `VERIFICATION.md`: proof, build, visual-QA, and hash record.
