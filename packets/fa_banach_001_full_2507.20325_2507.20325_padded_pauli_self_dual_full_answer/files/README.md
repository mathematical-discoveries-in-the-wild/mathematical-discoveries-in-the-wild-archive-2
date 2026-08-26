# Padded Pauli self-dual free spectrahedra

Status: **candidate full affirmative answer pending human review**.

Evert and Passer ask in Remark 3.20 of arXiv:2507.20325v2 whether there is a
self-dual free spectrahedron `D_A` with coefficient size `d >= 3` and fewer
than `d^2-d+2` variables. The answer to the statement as written is yes for
every `d >= 3`: pad their self-dual `2 x 2` Pauli triple by a zero block.

At every matrix level the padded pencil is the direct sum of the Pauli pencil
and an identity block, so it defines exactly the same matrix convex set. The
packet gives the complete proof and clearly separates the unresolved natural
variant requiring an irreducible or size-minimal defining tuple.

- Source: Eric Evert and Benjamin Passer, *Matrix convex sets over the
  Euclidean ball and polar duals of real free spectrahedra*,
  arXiv:2507.20325v2, Remark 3.20.
- Claimed result: full answer to the literal existence question.
- Human-review focus: confirm that no implicit minimal-pencil convention is
  intended in Remark 3.20; none is stated in the paper's definitions or in the
  remark.
- Ledger:
  `runs/fa_banach_001/ledger/results/2507.20325_padded_pauli_self_dual_full_answer.json`.
