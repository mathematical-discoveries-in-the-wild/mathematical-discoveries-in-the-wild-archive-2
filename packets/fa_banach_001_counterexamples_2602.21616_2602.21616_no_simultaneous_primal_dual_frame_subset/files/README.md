# 2602.21616 — no simultaneous primal/dual frame subset

Status: candidate full counterexample, likely valid; human review requested.

Model: GPT5.6.

Source: Pu-Ting Yu, *Every semi-normalized unconditional Schauder frame in
Hilbert spaces contains a frame*, arXiv:2602.21616v3 (2026), Remark 3.4(b) on
source PDF page 12.

## Result

The source asks whether every unconditional Schauder-frame pair `(x_n,y_n)`
has a subset `J` for which both the normalized primal sequence
`(x_n/||x_n||)_{n in J}` and the paired rescaled coefficient sequence
`(||x_n|| y_n)_{n in J}` are frames.

The packet gives a full negative answer in `H = l2`. In block `k`, repeat the
unit vector `e_k` exactly `k` times and attach coefficient vector `e_k/k` to
each copy. The `k` copies reconstruct the `k`th coordinate, and the
reconstruction converges unconditionally. If a subset selects `r_k` copies,
then its two frame quadratic forms have diagonal weights `r_k` and `r_k/k^2`.
The first sequence's upper frame bound forces `sup_k r_k < infinity`, whereas
the second sequence's lower frame bound would force `inf_k r_k/k^2 > 0`.
This is impossible.

The construction is normalized on the primal side and has no zero coefficient
vectors.

## Files

- `main.tex`: source question, proof intuition, and complete counterexample.
- `solution_packet.pdf`: rendered human-review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: readable crop of Remark 3.4(b), PDF page 12.
- `code/crop_source.py`: reproducible source-crop script.
- `verification_report.md`: adversarial quantifier and frame-bound audit.

## Reviewer focus

Please check the unconditional-net argument and that the source's associated
coefficient-functionals convention is exactly the orientation used in the
packet. The frame obstruction itself follows immediately by testing both
diagonal quadratic forms on the basis vectors.

## Novelty bound

The four run indexes and targeted searches through 11 August 2026 for the
exact Remark 3.4(b) wording and the simultaneous primal/coefficient frame
subset problem found the source paper but no later resolution. Since the
source is from 2026, the novelty claim is provisional.
