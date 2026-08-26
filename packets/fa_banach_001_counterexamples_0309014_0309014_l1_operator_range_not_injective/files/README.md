# An operator range in ell_1 that is not an injective operator range

Status: **candidate full counterexample; likely valid; human review
recommended**

Source: H. P. Rosenthal and V. G. Troitsky, *Strictly semi-transitive operator
algebras*, arXiv:math/0309014; Remark 4.4 on PDF page 13.

## Full negative answer

Take a bounded quotient `Q:ell_1 ->> ell_2` and the bounded injection

`J:ell_2 -> ell_1`, `J(x)_k=2^(-k)x_k`.

Then `Y=J(ell_2)=Range(JQ)` is an order-one operator range in `ell_1`.
It is not an injective operator range of any finite order.

Indeed, if `Y=Range(S)` for a bounded injection `S:N->ell_1`, with `N` a
closed subspace of `(ell_1)^m`, then `U=J^(-1)S:N->ell_2` is a linear
bijection.  Its graph is closed, so the closed graph and open mapping theorems
make `N` isomorphic to `ell_2`.  This is impossible: `N` has the Schur property
and `ell_2` does not.

The packet also proves a general quotient--embedding obstruction explaining
the construction.  The distinction from the unrestricted notion of operator
range is essential: arbitrary Banach domains can always be quotiented by the
kernel, whereas the source permits only closed subspaces of finite powers of
the ambient space.

## Files

- `main.tex`, `solution_packet.pdf`: full counterexample and general criterion.
- `source_paper.pdf`: arXiv:math/0309014.
- `figures/open_question_crop.png`: exact Remark 4.4 source passage.
- `verification.md`: line-by-line proof, definition, and scope audit.

The paper's separate question on simultaneous smallness for merely transitive
algebras remains unresolved; its eight-route investigation is retained in
`runs/fa_banach_001/attempts/0309014_general_transitive_simultaneous_smallness_attempt.md`.
