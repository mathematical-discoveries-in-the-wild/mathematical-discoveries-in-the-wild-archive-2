# Antisymmetric pseudo-p-Laplacian eigenfunction

This packet gives a counterexample to the literal open classification in
Remark 3.8, page 9, of arXiv:2006.07948.

For every `1 < p < infinity`, minimize the anisotropic Dirichlet Rayleigh
quotient on the closed space of functions on the square satisfying
`u(x,y) = -u(y,x)`.  Compactness gives a nonzero minimizer.  Invariance under
the signed coordinate swap and averaging of arbitrary variations show that
the minimizer is a genuine weak eigenfunction of the full pseudo-p-Laplacian.
No nonzero separated product of one-dimensional p-sines can have this
antisymmetry.  The proof extends to every cube in dimension at least two and
to boxes with two equal side lengths.

Status: `candidate_counterexample_likely_valid`, pending human review.

Files:

- `main.tex`: complete variational proof, direct symmetry argument, and cube
  upgrade.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_question_crop.png`: readable source excerpt.
- `VERIFICATION.md`: proof, build, visual-QA, and hash record.
