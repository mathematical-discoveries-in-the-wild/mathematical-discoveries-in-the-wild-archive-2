# arXiv:2304.14250 — maximal-operator obstruction below one

Status: `candidate_counterexample_likely_valid`

The source says that extending its discrete Rubio de Francia extrapolation
theorem from `p>1` to `0<p<1` is open, but it defines the target `A_p` class
only above one. This packet treats the necessary direct interpretation: an
extension retaining the main `A_{p0}` hypothesis must at least imply the
unweighted `ell^p` estimate.

That implication is false. The discrete Hardy--Littlewood maximal operator
satisfies the weighted strong-type hypothesis for every fixed `p0>1` and all
discrete `A_{p0}` weights. For the point mass `e_1`, however,
`M e_1(n) >= 1/n`, which is not in `ell^p` for any `p<=1`.

Files:

- `main.tex`: scoped counterexample and family-of-pairs formulation.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: locally compiled archived source.
- `figures/open_problem_page.png`: source abstract containing the signal.
- `verification.md`: proof, scope, literature, and artifact audit.
