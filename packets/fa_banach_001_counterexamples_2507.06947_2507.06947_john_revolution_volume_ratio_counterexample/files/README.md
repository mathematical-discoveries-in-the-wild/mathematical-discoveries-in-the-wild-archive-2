# Counterexample to Conjecture 5.10 of arXiv:2507.06947

Status: candidate full counterexample, likely valid, subject to human review.

For every `1 <= s < d` with `s` not dividing `d`, the packet constructs a
centrally symmetric polytope `K` in John position such that, for
`F = span(e_1,...,e_s)` and `E = B^d`,

    K cap F = sqrt(d/s) [-1,1]^s.

The unit ball is the largest-volume ellipsoid in `K`, hence in particular a
solution of the source paper's fixed-axis ellipsoid-of-revolution problem.
The resulting section ratio attains the source's larger Brascamp--Lieb bound
and strictly exceeds the conjectured cube constant whenever `s` does not
divide `d`.

The smallest example is `(d,s)=(3,2)`: `area(K cap F)=6`, whereas Conjecture
5.10 predicts at most `4 sqrt(2)` before division by the common disk area.

Files:

- `solution_packet.pdf`: expert-facing proof packet.
- `source_paper.pdf`: locally compiled arXiv source, with Conjecture 5.10 on
  printed/PDF page 19.
- `figures/open_problem_crop.png`: real source-page crop.
- `code/verify_counterexample.py`: algebra and volume sanity checker.
- `verification.md`: verifier report and review focus.

Ledger:
`runs/fa_banach_001/ledger/results/2507.06947_john_revolution_volume_ratio_counterexample.json`.

