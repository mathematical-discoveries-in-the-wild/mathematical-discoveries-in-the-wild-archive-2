# Sharpness of the Benamou--Brenier atom bound

Source: Bredies, Carioni, Fanzon, and Romero, *On the extremal points of the
ball of the Benamou--Brenier energy*, arXiv:1907.11589.

Status: candidate full solution; complete proof in `main.tex` and
`solution_packet.pdf`.

The source proves that a dynamic inverse problem with data space `H` has a
minimizer representable by at most `dim(H)` normalized trajectory atoms, then
asks whether this upper bound is optimal.  This packet proves universal
sharpness: for every `D >= 1` and every `alpha,beta > 0`, there is a one-time
sampling problem with `H=R^D`, a weak-star continuous observation operator,
and squared fidelity whose unique minimizer has atomic complexity exactly `D`.

The construction uses `D` pairwise disjoint continuous measurement channels.
The unique minimizer is stationary mass one at one point in each channel.  A
single trajectory atom activates at most one channel at the sampling time, so
at least `D` atoms are necessary; `D` constant trajectories attain the bound.

Files:

- `solution_packet.pdf` — expert-facing full proof packet.
- `main.tex` — LaTeX source.
- `source_paper.pdf` — official source paper.
- `figures/source_question_crop.png` — exact source corollary and open remark.
- `verification.md` — proof and novelty audit.
