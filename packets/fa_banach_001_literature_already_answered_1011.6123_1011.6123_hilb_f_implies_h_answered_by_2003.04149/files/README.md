# The Hilbert-space Frobenius-to-H* question was answered affirmatively

Status: `literature_already_answered` (the `Hilb` branch only)

Abramsky--Heunen, arXiv:1011.6123, ask whether (A), (C), (M), and (F)
force (H), both in `Hilb` and in arbitrary monoidal dagger categories.  In
`Hilb`, they show that this is equivalent to asking whether a nontrivial
radical special Frobenius algebra exists.

Poinsot, arXiv:2003.04149, answers the `Hilb` branch.  Theorem 33 states that
a commutative Hilbertian Frobenius semigroup is semisimple exactly when
`mu mu*` is injective.  Specialness gives `mu mu* = I`, hence semisimplicity
and therefore (H).  Corollary 32 equivalently rules out a nonzero radical
example, and Proposition 39 proves a stronger Frobenius/H*-equivalence.

This packet does **not** claim to settle the general monoidal dagger-category
branch.

Files:

- `solution_packet.pdf` -- compact literature-status note
- `source_paper.pdf` -- official arXiv:1011.6123 PDF
- `supporting_paper_2003.04149.pdf` -- decisive later paper
- `main.tex` -- status-note source

Ledger:

- `runs/fa_banach_001/ledger/results/1011.6123_hilb_f_implies_h_answered_by_2003.04149.json`
