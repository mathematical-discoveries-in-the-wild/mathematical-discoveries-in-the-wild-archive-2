# Iterated angular–radial diagonal convergence

Status: `candidate full affirmative solution under the printed quantifiers;
semantic review important`.

Conjecture 1 of arXiv:2202.06119 states that for every `4/3 < p < 4` and
every `f in Lp(D)`, the rectangular Bessel–Fourier sums converge along “some
appropriate choice” of cutoffs. This packet proves that literal assertion.

The angular Fourier partial sums `P_M f` converge to `f` in `Lp(D)`. For each
fixed `M`, only finitely many angular coefficients remain, and classical
fixed-order Fourier–Bessel mean convergence implies
`S_{N,M} f -> P_M f` as `N -> infinity`. Choosing `N` after `M` and taking a
diagonal proves the claim.

Strengthenings:

- the sequence `M_k -> infinity` may be prescribed arbitrarily;
- `N_k` may exceed arbitrary lower bounds, including `A M_k + 1`;
- one path can be chosen uniformly on every norm-compact subset;
- one path can be chosen for every prescribed countable family.

Semantic caveat: the proof gives `for every f, there exists a path`, exactly
as printed. It does not give `there exists one path for every f`. The source's
discussion of uniform operator bounds suggests that this stronger order may
have been informally intended, and that problem remains open.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv:2202.06119 PDF.
- `figures/open_problem_crop.png`: genuine full-width crop of Conjecture 1 on PDF page 6.
- `VERIFIER_REPORT.md`: proof, novelty, scope, and rendering audit.
- Ledger: `runs/fa_banach_001/ledger/results/2202.06119_iterated_angular_radial_diagonal_convergence.json`.

