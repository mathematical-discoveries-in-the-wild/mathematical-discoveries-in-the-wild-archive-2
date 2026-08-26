# Balanced finite-cover Thomson--Brennan theorem

Status: `candidate_partial_solution_likely_valid`.

The packet proves the open Riemann-surface dichotomy from arXiv:2112.08504 for
balanced lifts of atomless measures through finite unbranched coverings of
Brennan-type planar domains. The class contains positive-genus bordered
surfaces, so it is strictly broader than the source paper's one-coordinate-chart
case.

The key is that `pi_* O_U` is a rank-`d` holomorphic vector bundle and every
holomorphic vector bundle over the noncompact planar base is trivial. The
balanced measure supplies a nondegenerate continuous fiber metric; on compact
support this is uniformly equivalent to `d` scalar `L2` norms. Density and
bounded point evaluations then pass exactly between cover and base, where
Brennan's theorem applies.

The result does not handle arbitrary measures along the fibers. Their
disintegrations yield possibly degenerate matrix weights, and coefficient
extraction can become unbounded. That is the isolated obstruction to this
proof route.

Files:

- `source_paper.pdf`: arXiv:2112.08504.
- `figures/open_problem_crop.png`: source Open Problem, PDF page 6.
- `main.tex` and `solution_packet.pdf`: theorem and proof.
- `verification_report.md`: proof and rendering audit.
- Ledger: `runs/fa_banach_001/ledger/results/2112.08504_balanced_finite_cover_thomson_brennan.json`.

