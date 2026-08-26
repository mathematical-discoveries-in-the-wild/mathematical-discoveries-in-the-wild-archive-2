# Double-cone Sobolev interpolation question answered by arXiv:0812.1146

Status: **literature already answered**.

The Appendix of Nadine Badr's arXiv:0705.2216 asks whether the spaces
`H_p^1(X)` on the Euclidean double cone interpolate for all
`1<=p<=infinity`.

Pascal Auscher and Nadine Badr, *Sobolev spaces on multiple cones*,
arXiv:0812.1146, explicitly revisits the same space and gives a negative,
sharp answer.  Theorem 3.2 states that if
`1/p=(1-theta)/p_0+theta/p_1`, then

```text
(H_{p_0}^1(X),H_{p_1}^1(X))_{theta,p}=H_p^1(X)       if p != n,
                                         =hat H_n^1(X) if p = n,
```

where `hat H_n^1(X)` is a strict dense subspace of `H_n^1(X)` characterized
by the Hardy condition `f_a/|x| in L^n(X)`.  Thus the family fails to be an
interpolation scale exactly at its critical exponent.

The original question is on printed page 23 of `source_paper.pdf`.  The exact
answer is Theorem 3.2 on printed page 5 of `supporting_0812.1146.pdf`; the
strictness example follows immediately below it.

Contents:

- `main.tex` / `solution_packet.pdf`: compact identification and scope note.
- `source_paper.pdf`: arXiv:0705.2216.
- `supporting_0812.1146.pdf`: the exact later answer, arXiv:0812.1146.

This packet records a literature resolution, not a new result of the run.
