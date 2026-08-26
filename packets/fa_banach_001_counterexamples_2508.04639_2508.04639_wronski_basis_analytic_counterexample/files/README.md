# Counterexample packet for arXiv:2508.04639

This packet gives a full counterexample to Conjecture 8 under the source
paper's own finite-basis and regular-ODE conventions.

## Result

Take the Hilbert function space

\[
H=\operatorname{span}\{1,x^2\},\qquad
\langle a+bx^2,c+dx^2\rangle=ac+bd.
\]

Then `{1,x^2}` is an analytic orthonormal basis, but it cannot be the
fundamental solution system of a regular second-order linear homogeneous ODE
on all of `R`. Substitution in
`p_2 y'' + p_1 y' + p_0 y = 0` forces `p_0=0` and then `p_2(0)=0`, contradicting
the source's requirement that the leading coefficient never vanish.

The same obstruction appears in the proposed Wronskian quotient:
`W(1,x^2)=2x`, so the resulting equation is singular at zero.

## Files

- `solution_packet.pdf`: review-ready packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: official arXiv PDF, v4.
- `figures/open_problem_crop.png`: full-width crop of Conjecture 8.
- `verification.md`: exact verification checklist and scope notes.

Status: `candidate_counterexample_likely_valid`, pending human review.
