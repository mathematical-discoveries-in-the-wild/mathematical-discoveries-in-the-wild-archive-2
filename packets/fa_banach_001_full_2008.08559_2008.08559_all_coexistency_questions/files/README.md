# All-dimensional coexistency criteria

Status: **candidate full solution; likely valid; expert review recommended**.

Source: G. P. Gehér and P. Šemrl, *Coexistency on Hilbert space effect algebras and a characterisation of its symmetry transformations*, arXiv:2008.08559v2, Questions 6.2--6.4.

The packet proves three dimension-free statements:

1. Equality of the coexistent rank-one effects of `A` and `B` implies that both are scalar, or `B=A`, or `B=I-A`. This affirmatively extends source Corollary 2.11 to arbitrary Hilbert spaces.
2. An effect has no strictly smaller coexistency neighborhood exactly when both `0` and `1` belong to its spectrum. This affirmatively extends source Lemma 6.1 without separability.
3. `A^sim subset B^sim` holds exactly when the positive-part trace support functional `h_A(T)` is at most `h_B(T)` for every finite-rank self-adjoint test operator `T`.

Main mechanisms: inverse strength forms plus real-polynomial unique factorization; endpoint-eigenspace mixing; joint spectral localization; and WOT Hahn--Banach separation of the Minkowski sums `[0,A]+[0,I-A]`.

Novelty confidence is moderate: the run indexes and local parsed arXiv corpus revealed no exact answer, but a fresh external-network search was unavailable.

Files:

- `solution_packet.pdf`: review packet
- `source_paper.pdf`: locally compiled arXiv source
- `figures/open_problem_crop.png`: source page 27 with all three questions
- `code/check_identities.py`: symbolic and finite-dimensional diagnostic checks
- `main.tex`: packet source

Ledger: `runs/fa_banach_001/ledger/results/2008.08559_all_coexistency_questions.json`.
