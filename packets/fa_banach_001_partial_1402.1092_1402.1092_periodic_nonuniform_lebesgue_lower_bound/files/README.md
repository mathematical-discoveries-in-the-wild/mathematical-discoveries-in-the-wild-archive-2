# arXiv:1402.1092 — periodic nonuniform sampling lower bound

Status: substantial partial resolution; high validity confidence and moderate
novelty confidence.

The source's Conjecture 80 asks whether every complete interpolating sequence
for PW_pi^2 has a pointwise logarithmic lower bound for each individual
truncation kernel, rather than only for the maximum of earlier truncations.

This packet proves the conjecture for every periodic nonuniform lattice

    t_(qm+r) = qm + alpha_r,
    0 = alpha_0 < alpha_1 < ... < alpha_(q-1) < q.

After splitting the frequency interval into q equal cells, a Vandermonde
matrix gives the biorthogonal Fourier functions explicitly. Every symmetric
truncation kernel then has a common scalar Dirichlet core whose coefficient
equals q on the diagonal, plus a uniformly bounded collection of endpoint
terms. The local L1 norm is therefore bounded below by c log(N+1), uniformly
in the evaluation frequency.

The alternating family

    t_(2m) = 2m,
    t_(2m+1) = 2m + a,  0 < a < 2,

is an immediate genuinely non-equidistant corollary.

- Proof packet: solution_packet.pdf
- Locally compiled source paper: source_paper.pdf
- Open-conjecture crop: figures/open_problem_crop.png
- Optional checker: code/verify_periodic_kernel.py
- Attempt audit: runs/fa_banach_001/attempts/1402.1092_periodic_nonuniform_lebesgue_lower_bound.md
- Ledger: runs/fa_banach_001/ledger/results/1402.1092_periodic_nonuniform_lebesgue_lower_bound.json

The full conjecture for arbitrary aperiodic complete interpolating sequences
remains open. The cached source uses an unavailable publisher class, so the
local source PDF was compiled from the original TeX with a documented
substitute article class; automatic theorem numbering therefore differs from
the original label.

