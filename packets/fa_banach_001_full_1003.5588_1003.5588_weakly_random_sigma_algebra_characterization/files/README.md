# Full solution packet for arXiv:1003.5588, Question 1

Status: `candidate_full_solution_likely_valid`

This packet gives a necessary-and-sufficient characterization of the weakly
random sub-sigma-algebras from Szegedy's Question 1.  Under the paper's
standing separability assumption, `B` is weakly random exactly when the
conditional rank-one tensor map

`(f,g) -> E(f(x) conjugate(g(y)) | B)`

maps the two `L_infinity` unit balls into a relatively compact subset of
`L1(B)`.  Equivalently, the conditional expectations of all measurable
rectangle indicators form an `L1`-precompact family.

The forward implication uses Arzela--Ascoli on the weakly compact unit ball
of `L_infinity(B)` inside `L2(B)`.  The reverse implication is a finite-net
argument.  The packet also proves the rectangle-only formulation and gives
finite and atomless sanity examples.

Files:

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: arXiv:1003.5588.
- `figures/open_problem_crop.png`: exact source definition and Question 1.
- `code/make_crop.py`: reproducible source crop.
- `code/verify_finite_models.py`: finite conditional-expectation checks.
- `verification.md`: compilation, rendering, search, and proof audit.

