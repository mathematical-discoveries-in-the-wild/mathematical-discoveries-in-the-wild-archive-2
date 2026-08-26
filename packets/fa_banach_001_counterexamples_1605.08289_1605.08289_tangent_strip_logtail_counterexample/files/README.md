# Tangent-strip logarithmic counterexample

Status: `candidate_counterexample_likely_valid` / full negative answer to
Question 34 of arXiv:1605.08289 for every finite integer `p >= 0`.

For the unit disc `D` and the internally tangent disc
`D'_r = { |z-(1-r)| < r }`, the map `w=(1-z)^(-1)` identifies
`Omega = D \ closure(D'_r)` with a vertical strip.  An analytic cutoff that
distinguishes the strip's two ends, multiplied by `w^(-p)/Log(2-iw)`, gives an
explicit `F_p in A^p(Omega)`.  Its `p`-th derivative has a one-sided
`1/log(1/t)` trace on the outer circle, so its outer Cauchy projection diverges
like `log log(1/(1-rho))`.  Any `A^p` Laurent decomposition would make that
projection the `p`-th derivative of an `A(D)` function, a contradiction.

Files:

- `solution_packet.pdf`: complete proof and verification notes.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv:1605.08289 PDF.
- `figures/open_problem_crop.png`: full-width crop of PDF page 13 containing
  Question 34.
- `code/check_asymptotics.py`: optional numerical sanity check; not used by
  the proof.
- `verification.md`: review checklist and commands.

Important scope note: the source's later literal subquestion with
`F in A(D)` cannot hold, because its outer-circle Cauchy transform equals
`F` inside `D`.  The packet answers the substantive preceding question for
`F in A^p(Omega)`; for `p>0` it applies the Cauchy obstruction after `p`
derivatives.

Human review priority: the `T = w^2 d/dw` endpoint induction and the uniform
bounded-error estimate producing the log-log divergence.
