# Zero-state tangent obstruction for the bi-approximately-unital conjecture

This packet gives a sharp conditional reduction, not a full solution, to the conjecture following Lemma 4.4 of arXiv:1802.04424.

For a bi-approximately unital Lp-operator algebra, the dual real-positive cone splits into two kinds of weak-star limits of positive multiples of states:

1. finite-coefficient limits, which are nonnegative multiples of restrictions of states on the multiplier unitization and are automatically nonnegative on the support idempotent;
2. unbounded-coefficient limits, precisely the weak-star tangent cone of the state space at the zero restriction.

The algebra has a real-positive cai if and only if every functional in the second class is nonnegative on the support idempotent. Equivalently, a counterexample must consist of states `omega_i`, scalars `t_i -> infinity`, and a weak-star limit `t_i omega_i -> f` with `Re f**(e) < 0`.

The packet also gives an explicit construction showing why the tempting uniform-boundedness shortcut is invalid: every nonunital approximately unital algebra admits state nets `omega_i` and `t_i -> infinity` with `t_i omega_i -> 0` weak-star. For convex state spaces, the limit can be any prescribed state.

Files:

- `source_paper.pdf`: official published source paper.
- `figures/open_problem_crop.png`: Lemma 4.4 and the exact conjecture.
- `main.tex`: conditional reduction and obstruction proof.
- `solution_packet.pdf`: compiled packet.
- `verification_report.md`: adversarial proof audit.

Status: conditional reduction / sharp obstruction; the original conjecture remains open in this packet.
