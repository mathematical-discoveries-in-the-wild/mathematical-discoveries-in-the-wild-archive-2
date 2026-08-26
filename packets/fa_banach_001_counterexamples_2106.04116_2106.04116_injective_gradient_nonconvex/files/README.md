# Counterexample to the convexity conjecture

This packet refutes Conjecture 1 of arXiv:2106.04116.

On the one-dimensional inner-product space, take

\[
F(x)=-\sqrt{1+x^2}.
\]

The function is globally 1-Lipschitz and strictly concave. Its Clarke
subdifferential is the singleton containing its ordinary derivative, and that
derivative is injective. Thus subdifferentials at two points intersect only
when the points coincide, making the conjectured segment identity automatic.

Artifacts:

- `solution_packet.pdf`: compiled counterexample packet.
- `main.tex`: editable source.
- `source_paper.pdf`: source paper.
- `figures/problem_crop.png`: exact conjecture excerpt from source page 26.
- `novelty_search.md`: bounded novelty search.
- `verification_report.md`: mathematical and rendering checks.

Status: candidate full counterexample, likely valid; priority is not asserted.
