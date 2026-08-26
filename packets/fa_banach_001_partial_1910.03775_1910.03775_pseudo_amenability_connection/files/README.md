# Pseudo-amenability and approximate semi-amenability

Status: **candidate partial result — likely valid, pending human review**.

Source: F. Ghahramani and R. J. Loy, *Approximate semi-amenability of
Banach algebras*, arXiv:1910.03775. Question 2 on PDF page 24 asks for the
connection between approximate semi-amenability and pseudo-amenability.

This packet proves:

1. Every pseudo-amenable Banach algebra is approximately semi-amenable.
2. If an approximately semi-amenable Banach algebra has a central
   approximate identity, even an unbounded one, then it is pseudo-amenable.
3. Hence the two notions are equivalent for every commutative Banach
   algebra.

The unrestricted noncommutative converse remains open in this packet. Its
specific obstruction is the absence of a central localizer for converting
the source's two unitized tensors into one approximate diagonal in
`A tensor_pi A`.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: exact source-question crop.
- `code/crop_open_problem.py`: reproducible crop script.
- `verification.md`: analytic checks, build audit, novelty scope, and
  limitations.

Human-review focus: the localization argument in Theorem 4.2, especially
the order of choosing two potentially unbounded central approximate-identity
elements and then the tensor index.
