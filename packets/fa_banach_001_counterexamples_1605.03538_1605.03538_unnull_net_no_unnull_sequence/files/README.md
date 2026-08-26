# An un-null net with no un-null sequence of its terms

This packet gives a negative answer to Question 2.14 on page 5 of
arXiv:1605.03538.

Let `Gamma=omega_1` and let `X=ell_infinity^c(Gamma)` be the Banach lattice
of bounded, countably supported functions.  Direct the countable subsets
`C` of `Gamma` by inclusion, put `gamma_C=min(Gamma minus C)`, and set
`x_C=e_{gamma_C}`.  Every fixed un-test vector has countable support, which
the net eventually escapes.  Hence `x_C` is un-null.  For any proposed
sequence `(C_n)`, however, the indicator of
`{gamma_{C_n}: n in N}` is a single element of `X_+` whose truncation with
every `x_{C_n}` has norm one.  Thus no sequence of terms is un-null.

Status: `candidate_counterexample_likely_valid`, pending human review.

Files:

- `main.tex`: complete counterexample and literature boundary.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: readable source excerpt.
- `code/verify_incidence.py`: finite checks of the incidence identities.
- `VERIFICATION.md`: proof, build, visual-QA, and hash record.
