# Full solution packet for arXiv:2003.05382, Problem 2.17

Status: `candidate_full_solution_likely_valid`

This packet gives an explicit canonical Boolean-product operator model for
arbitrary (not necessarily positive) selfadjoint marginal laws.  It computes
the spectral-maximum CDF exactly: below the distinguished Boolean-product
value zero it is an endpoint test, while at and above zero it is the familiar
Boolean formula `FG/(F+G-FG)`.

The model also produces the two requested additional extreme-value types.
The Boolean transforms of the classical Gumbel and reverse-Weibull limits are
respectively the logistic law and the bounded reciprocal-power law
`1/(1+(-x)^alpha)` on `x<=0`.  Along with the known Dagum family, this realizes
all three classical extreme-value types as limits of normalized maxima of
positive Boolean-independent operators.

Files:

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: arXiv:2003.05382.
- `supporting_paper_1711.06227.pdf`: the Boolean projection calculation used
  in the proof.
- `figures/problem_2_17_crop.png`: exact source problem.
- `code/make_crop.py`: reproducible crop.
- `code/verify_formulas.py`: algebraic and finite-dimensional checks.
- `verification.md`: compilation, rendering, and mathematical audit.

