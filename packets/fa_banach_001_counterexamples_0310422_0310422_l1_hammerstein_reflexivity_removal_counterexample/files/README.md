# Counterexample packet: removing reflexivity in the Hammerstein problem

This packet gives a full negative answer to the strongest natural
removal-only interpretation of the question on pages 6--7 of
arXiv:math/0310422.

On real `ell_1`, let `R` be radial retraction onto the unit ball and set

`U(u)=(1-||u||_1,u_1,u_2,...)`, `F=U composed R`.

The map `F` is bounded, globally Lipschitz, weakly sequentially continuous by
the Schur property, and fixed-point-free.  Taking constant kernel `k=1`,
`h=0`, and `f(s,x)=F(x)` satisfies source conditions (4.2)--(4.6) with
`Omega=1` and growth ratio zero.  Every solution would be constant and hence
a fixed point of `F`, a contradiction.

Thus reflexivity cannot simply be deleted without a genuine replacement
compactness/condensing hypothesis.  The packet does not claim to characterize
all such replacement hypotheses and does not contradict source Theorem 4.1.

## Files

- `main.tex`: self-contained proof source.
- `solution_packet.pdf`: compiled expert-facing packet.
- `source_paper.pdf`: locally compiled archived arXiv source.
- `figures/question_lead_crop.png` and `question_page7_crop.png`: the compact
  page-spanning prompt; `question_page6_crop.png` retains the larger context
  containing conditions (4.5)--(4.6).
- `verification.md`: source, proof, novelty, and rendering checks.
- `tmp/`: compilation and rendered-page artifacts.

Status: candidate full counterexample to removal without replacement, likely
valid, pending expert review.

Ledger: `runs/fa_banach_001/ledger/results/0310422_l1_hammerstein_reflexivity_removal_counterexample.json`.
