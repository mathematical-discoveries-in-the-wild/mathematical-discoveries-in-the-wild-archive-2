# The exact idempotent gap between two notions of Banach pure infiniteness

**Status:** candidate substantial partial result, likely valid; human review
requested.

Bardadyn--Kwaśniewski--McKee ask for the relationship, without an
approximate-unit hypothesis, between their algebraic infinite-idempotent
notion of pure infiniteness and the sequential sandwich-approximation notion
of Cortiñas--Montero--Rodríguez.

This packet proves an exact characterization for complex topologically simple
Banach algebras:

`algebraically purely infinite`

if and only if

`sequentially purely infinite + contains a nonzero idempotent`.

In particular, the source's bounded two-sided approximate unit of idempotents
can be replaced by one nonzero idempotent.  More strongly, algebraic pure
infiniteness always implies sequential pure infiniteness, with no approximate
identity assumption.

The proof uses proper infiniteness of a unital corner to encode every finite
sum through one sandwich, and an invertible perturbation in a single nonzero
corner for the reverse implication.  The unrestricted equivalence is reduced
to the existence of a nonzero idempotent in every sequentially purely infinite
Banach algebra.

Files:

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original arXiv source paper.
- `figures/source_assumption_crop.png`: source Proposition 6.3.
- `figures/open_problem_crop.png`: source Remark 6.4.
- `code/crop_open_question.py`: reproducible source-page crops.
- `tmp/`: LaTeX intermediates and rendered-page QA files.

Novelty confidence is moderate.  The component corner results are in the
cited papers, but bounded index and exact-phrase searches did not locate this
combination.  Expert review should focus on the finite-sum compression using
proper infiniteness and on the CMR corner result used in the reverse direction.
