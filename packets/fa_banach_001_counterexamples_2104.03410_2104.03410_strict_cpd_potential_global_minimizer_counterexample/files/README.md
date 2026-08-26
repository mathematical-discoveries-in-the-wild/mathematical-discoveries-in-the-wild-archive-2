# Strictly positive averaged potential does not force global minimization

Result type: `counterexample`

Status: candidate full counterexample to the spherical global-minimizer
conjecture, likely valid pending expert review.

Source paper:

- Dmitriy Bilyk, Damir Ferizović, Alexey Glazyrin, Ryan W. Matzke, Josiah
  Park, and Oleksandr Vlasiuk, “Potential theory with multivariate kernels,”
  *Mathematische Zeitschrift* 301(3) (2022), 2907–2935,
  arXiv:2104.03410, DOI `10.1007/s00209-022-03000-z`.
- Conjecture location: source PDF page 15, immediately before Theorem 5.3;
  the converse question is repeated immediately after that theorem.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The conjecture is false already for continuous symmetric rotationally
invariant three-input kernels on every sphere `S^{d-1}`, `d >= 3`.  The
counterexample can be made stronger than the conjecture's hypothesis:

- the averaged pair kernel `U_K^sigma` is strictly conditionally positive
  definite;
- the uniform measure `sigma` is the unique minimizer of its pair energy;
- `sigma` is a strict local minimizer of the three-input energy in every
  direction;
- nevertheless, a Dirac mass has strictly lower three-input energy.

The construction starts with

`H_d=-uvt+(u^2+v^2+t^2)/d-2/d^2`,

where `u=<x,y>`, `v=<y,z>`, and `t=<z,x>`.  Its `sigma`-averaged pair kernel
vanishes, but its Dirac energy is negative.  Adding a sufficiently small
symmetric lift of the centered strictly positive definite pair kernel
`exp(<x,y>)` makes the averaged potential strict without changing the global
energy comparison.

## Files

- `main.tex`: self-contained construction and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width source crop.
- `verification.md`: proof audit and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

On August 11, 2026, the run indexes were searched by arXiv id, exact title,
the averaged-potential conjecture, and its local/global minimizer terms.
Exact-phrase and citation-oriented web searches found the source paper, its
2022 journal version, and related talks/follow-up work, but no later answer to
the conjecture or this null-potential construction.  Novelty confidence is
moderate pending specialist citation review.

## Scope and human review focus

This fully disproves the displayed equivalence/converse conjecture.  It does
not affect the source's proved necessary direction or its local-minimizer
theorem; in fact, the example sharply demonstrates that theorem by being
locally but not globally minimized at `sigma`.

Review should focus on the one-variable spherical averages in the cubic term,
the strict conditional positive definiteness of the centered exponential
kernel, and the numerical choice of the small lifting coefficient.
