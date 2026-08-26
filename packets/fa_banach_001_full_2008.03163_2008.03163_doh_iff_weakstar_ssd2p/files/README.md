# DOH is exactly dual to weak-star SSD2P

Result type: full

Status: candidate full solution, likely valid pending expert review.

Source:

- Andre Ostrak, “On the duality of the symmetric strong diameter 2 property
  in Lipschitz spaces,” arXiv:2008.03163; RACSAM 115 (2021), Paper 66.
- Open question: converse of Proposition 2.1, stated in the abstract and at
  the start of Sections 2 and 3.

## Claimed contribution

The packet proves the open converse in full:

> For every real Banach space X, X is decomposably octahedral if and only if
> X* has the weak-star symmetric strong diameter-2 property.

For finitely many slice directions, the constraints `||f_i +/- g|| <= 1`
form the unit ball of an equivalent norm on `(X*)^(n+1)`. Hahn--Banach
computes each nonnegative support functional as a minimum over a finite
decomposition in `X**`. The principle of local reflexivity transfers that
decomposition to `X`, fixes the slice directions and the prescribed sum,
and allows the defining DOH inequality to be applied. Finite-dimensional
separation then yields all `2n+1` required inequalities simultaneously.

## Files

- `main.tex`: expert-facing proof source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: official arXiv source paper.
- `supporting_paper_2404.11430.pdf`: later paper explicitly recording the
  converse as open in 2024.
- `code/verify_finite_model.py`: finite-dimensional linear-programming
  checks of the support formula and separation step.
- `verification.md`: proof audit, test output, hashes, and visual QA.
- `tmp/`: LaTeX and rendered-QA intermediates.

## Novelty check

On August 9, 2026, exact-title, arXiv-id, exact-phrase, and core-term
searches found no proof or counterexample. ArXiv:2404.11430 explicitly says
the converse remains open, as does later dissertation/expository material
indexed in 2026. No later work found by the bounded search announces the
equivalence proved here. Novelty confidence is moderate-to-high pending
specialist review.

## Human review focus

- The Hahn--Banach identification in Lemma 1, especially the adjoint
  equations and the factor `2` in `2 sum r_i = c Jy`.
- The use of local reflexivity to fix `Jx_i` and `Jy` exactly while sending
  the finite family `r_i` into `X` with distortion tending to one.
- The strong-separation orientation and why the separating coefficients are
  nonnegative.
- The strict slice inequalities obtained by choosing `rho` smaller than all
  slice widths and the requested SSD2P tolerance.

