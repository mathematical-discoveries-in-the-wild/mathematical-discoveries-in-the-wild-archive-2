# Central area drifts obstruct intrinsic Young-regime lift uniqueness

This packet gives a candidate negative answer to the intrinsic-uniqueness
reading of the “Sewing with Rectangular Increments” question in
arXiv:2406.16857.

For every `1/2 < rho <= 2/3`, the zero surface in `R^3` has a one-parameter
family of distinct full rectangular `rho`-Hölder multiplicative double-group
functionals with the same path components and the same levels through two.
The perturbation is

`R_Q^lambda = exp_*(lambda Leb(Q) Omega) = 1 + lambda Leb(Q) Omega`,

where `Omega` is the nonzero degree-three Jacobi cycle

`[e1,e2 wedge e3] + [e2,e3 wedge e1] + [e3,e1 wedge e2]`.

Its boundary vanishes by Jacobi, products involving it vanish by the Peiffer
identity, and Lebesgue area is additive under both rectangle concatenations.
The drift satisfies both the paper's stated surface estimate and the sharper
mixed rectangular estimate discussed in its appendix.

The conclusion is scoped: rectangular regularity alone does not force an
intrinsically unique lift from the underlying surface. A theorem that selects
the paper's canonical Young-integral lift by an additional normalization,
smooth-approximation rule, or naturality/locality axiom is not ruled out.

Files:

- `solution_packet.pdf`: self-contained counterexample note.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: the exact source question on PDF page 56.
- `code/verify_counterexample.py`: exact degree-three boundary and norm checks,
  exact rational additivity checks, and finite mixed-regularity tests.
- `verification.md`: audit record and human-review boundary.

