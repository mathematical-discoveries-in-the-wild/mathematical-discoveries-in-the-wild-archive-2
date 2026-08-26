# Diskcyclic direct-sum counterexample

Source: arXiv:1507.01166, Bamerni--Kilicman--Noorani, *k-bitransitive and compound operators on Banach spaces*.

## Result

The final question has a negative answer. There is a diskcyclic operator
`T` such that its `k`-fold direct sum is not `k`-bitransitive for any
`k >= 2`.

Take a hypercyclic operator `R` for which `R direct-sum R` is not
hypercyclic (de la Rosa--Read) and put

    T = lambda (R direct-sum I_C), lambda > 1.

Then `(x,1)` is diskcyclic for `T` whenever `x` is hypercyclic for `R`.
If `T direct-sum T` were `2`-bitransitive, testing on input and output
sets whose added scalar coordinate is close to `1` would pin both
independent effective disk scalars close to `1`. This would force
topological transitivity of `R direct-sum R`, a contradiction.

## Files

- `main.tex`: complete proof packet
- `solution_packet.pdf`: compiled packet
- `verification_report.md`: proof and artifact audit
- `source_paper.pdf`: official arXiv source PDF
- `supporting_paper_de_la_rosa_read_2009.pdf`: primary theorem source
- `figures/open_problem_crop.png`: exact final question from page 10

Status: candidate full negative answer, likely valid; human review recommended.
