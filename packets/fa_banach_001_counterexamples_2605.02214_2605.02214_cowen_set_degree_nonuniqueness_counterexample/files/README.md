# Full counterexample packet: Cowen-set degree nonuniqueness

This packet gives a full negative answer to Problem 4.2 of arXiv:2605.02214.
For `Phi_m(z)=z^m I_n` and `B_k(z)=z^k I_n` with `k>m`, one has
`B_k in E(Phi_m)`, but the Toeplitz self-commutator has rank `mn` while
`deg(det B_k)=kn`.

The packet strengthens this to an exact theorem.  For
`D=diag(z^(m_1),...,z^(m_n))`, the finite Blaschke--Potapov products in
`E(D)` have determinant degrees exactly

`sum_j m_j, sum_j m_j+1, sum_j m_j+2, ...`.

Hence the commutator rank is the minimum possible degree for this family, not
the degree of every Cowen-set product.  This does not refute the paper's
central existential conjecture: `B=D` realizes the minimum.

## Files

- `main.tex`: self-contained proof source.
- `solution_packet.pdf`: compiled expert-facing packet.
- `source_paper.pdf`: locally compiled arXiv source paper.
- `figures/open_problem_crop.png`: exact source statement from page 11.
- `verification.md`: mathematical, source, and rendering checks.
- `tmp/`: compilation and page-rendering artifacts.

Status: candidate full counterexample, likely valid, pending expert review.

Ledger: `runs/fa_banach_001/ledger/results/2605.02214_cowen_set_degree_nonuniqueness_counterexample.json`.
