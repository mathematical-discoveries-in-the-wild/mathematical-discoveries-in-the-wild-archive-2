# Periodic fractional Strichartz wave-packet counterexample

Status: `full_counterexample_pending_human_review`

Appendix B of arXiv:1506.04181 asks whether, for `0<alpha<1`, the unit-time
periodic estimate

`||exp(-it|D|^alpha)u||_L4 <= C ||u||_H^gamma`

can hold at `gamma_0=(1-alpha)/4`. It cannot. A packet of
`M~N^(1-alpha/2)` consecutive modes centered at a large frequency `N`
remains coherent on a moving spatial tube for all `0<=t<=1`. Its spacetime
`L4` norm is at least `c M^(3/4)`, whereas its `H^gamma` norm is comparable to
`N^gamma M^(1/2)`. Hence every such estimate requires
`gamma>=1/4-alpha/8`. The source proves the matching upper estimate, so this
exponent is sharp.

## Files

- `main.tex`, `solution_packet.pdf`: full proof, consequences, and scope.
- `source_paper.pdf`: arXiv:1506.04181.
- `figures/open_question_crop.png`: source Appendix B question.
- `verify_wavepacket.py`: exact exponent and finite phase sanity checks.
- `references.md`, `verification_report.md`: search and QA records.

## Human review

- [ ] A human expert has independently checked the proof, interpretation, and
  novelty status.
