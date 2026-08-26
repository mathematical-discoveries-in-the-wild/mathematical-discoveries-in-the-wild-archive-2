# Dense-set weak-Baire norm counterexample

Source: A. Avilés, G. Plebanek, and J. Rodríguez, “A weak* separable
C(K)* space whose unit ball is not weak* separable,” arXiv:1112.5710,
Section 3.3, Question (B), PDF page 22.

Status: counterexample_likely_valid.

The packet gives a ZFC negative answer to the norm-dense-set formulation.
For a nonseparable real Hilbert space X = R direct-sum_2 Z, choose a Borel
function psi:R->[0,infinity) with dense graph and set

    A = {(t,z): ||z|| = psi(t)}.

Then A is norm dense and the norm on A is the restriction of the
weak-Baire function (t,z) -> sqrt(t^2+psi(t)^2), which depends on one dual
coordinate. The norm on all of X is not weak-Baire measurable: every real
sigma(X*)-measurable function depends on countably many dual coordinates,
and a nonzero vector orthogonal to their Riesz representatives is invisible
to all of them.

The result does not settle the source’s parenthetical variant requiring the
dense set to be a linear subspace. A focused upgrade attempt reduces that
case to a pathological dense-graph problem but finds neither a construction
nor an impossibility theorem.

Review files:

- solution_packet.pdf
- main.tex
- verification.md
- figures/open_problem_crop.png
- source_paper.pdf
- ../../../../attempts/1112.5710_dense_set_weak_baire_norm_counterexample.md

Ledger:
runs/fa_banach_001/ledger/results/1112.5710_dense_set_weak_baire_norm_counterexample.json.

