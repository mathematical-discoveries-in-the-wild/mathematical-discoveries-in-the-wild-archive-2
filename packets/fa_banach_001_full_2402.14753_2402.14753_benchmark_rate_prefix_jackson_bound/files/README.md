# 2402.14753 benchmark-rate prefix Jackson bound

Candidate full affirmative solution packet for the tighter-Jackson-bound open
question in Petrov--Torr--Bibi, arXiv:2402.14753.

## Result

For every `m>=1`, a finite fixed classical attention head of hidden dimension
`3(m+1)` approximates every geodesically `L`-Lipschitz map
`f:S^m -> R^(m+1)` uniformly to accuracy `epsilon` with

`N = O_m((L/epsilon)^m)`

prefix positions.  The same prefix works element-wise for every fixed input
sequence length.  This replaces the source exponent `10+14m+4m^2` by the
intrinsic exponent `m`, matching the trained-network benchmark stated in the
question.

## Files

- `solution_packet.pdf`: compiled candidate proof.
- `main.tex`: proof source.
- `source_paper.pdf`: locally compiled source paper.
- `figures/open_question_crop.png`: exact source question from PDF page 9.
- `code/check_softmax_net_bound.py`: numerical sanity check for `m=1`.
- `verification.md`: build, render, and mathematical verification record.

The numerical script is a sanity check only; the proof is analytic and
self-contained in `main.tex`.
