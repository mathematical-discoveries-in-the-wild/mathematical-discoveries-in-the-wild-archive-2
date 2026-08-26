# 0810.1433 — polyhedral-cylinder d.c. extension

Status: `candidate partial result; likely valid; pending human review`

Source: Libor Veselý and Luděk Zajíček, *On extensions of d.c. functions and
convex functions*, arXiv:0810.1433, Remark 2.4(a).

The source asks whether its power-type-2 renorming assumption can be omitted
or essentially weakened. This packet removes all renorming assumptions for
finite-codimensional polyhedral cylinders

`C = T^{-1}(K)`,

where `T:X->E` is onto a finite-dimensional space and `K` is a closed convex
polyhedron. If a d.c. map `F:C->Y` and one of its controls are Lipschitz on
bounded parts of `C`, then `F` extends d.c. to all of `X`.

The key is a globally Lipschitz d.c. retraction

`R(x)=x+S(pi_K(Tx)-Tx)`,

where `S` is a linear right inverse of `T` and `pi_K` is Euclidean projection
onto `K`. The latter is finite piecewise affine, hence d.c. with a global
Lipschitz control. The source's composition lemma then applies on bounded
balls.

This is a scoped partial result: it does not remove the renorming hypothesis
for arbitrary convex domains and it strengthens the local control assumption.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source proof step and Remark 2.4(a), page 7.
- `verification.md`: proof, build, visual, and novelty audit.
