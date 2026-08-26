# Coordinate-power middle fibers contain a full analytic ball

Result type: `full`

Status: candidate full resolution of the highlighted coordinate-square fiber
question, likely valid pending expert review.

Source paper:

- Verónica Dimant and Joaquín Singer, “A look into homomorphisms between
  uniform algebras over a Hilbert space,” *Studia Mathematica* 265(1) (2022),
  57–75, arXiv:2102.06771, DOI `10.4064/sm210219-10-6`.
- Open-question location: end of Section 2, source PDF page 9.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The fiber highlighted by Dimant–Singer is on the large-ball side of their
middle-fiber alternatives.  More strongly, for every integer `m >= 2`, if

`g_m(x) = (x_n^m)_n`,

then the fiber over `g_m` in the vector-valued spectrum contains an analytic
copy of the full open unit ball of `H^infinity(B_l2,l2)`.

The construction uses the fixed holomorphic defect
`phi_m(x)=x_1...x_m`.  The multinomial inequality

`||g_m(x)||^2 + |phi_m(x)|^2 <= ||x||^(2m)`

provides enough norm room to append an arbitrarily chosen bounded holomorphic
map in coordinates escaping to infinity.  A free-ultrafilter limit of the
resulting composition homomorphisms stays in the fiber.  Quadratic and cubic
diagonal test polynomials recover every coordinate of the parameter and prove
injectivity.

## Files

- `main.tex`: self-contained proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width source crop.
- `verification.md`: proof audit and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

On August 11, 2026, the run registry, solution, attempt, and proof-gap indexes
were searched by arXiv id, exact title, the exact coordinate-square example,
and middle-fiber terminology.  Targeted web searches found the arXiv source
and its 2022 journal publication, but no later paper answering this example.
This was a bounded search, so novelty confidence is moderate pending a
specialist citation review.

## Scope and human review focus

This is a full answer to the natural example explicitly singled out on source
PDF page 9, and it proves the stronger coordinate-power family.  It does not
settle the paper's broader question whether some other middle fiber can have a
third behavior besides being a singleton or containing an analytic ball.

Review should focus on the weak-star ultrafilter analyticity step (the same
mechanism used in the source paper) and the quadratic/cubic separation
argument.
