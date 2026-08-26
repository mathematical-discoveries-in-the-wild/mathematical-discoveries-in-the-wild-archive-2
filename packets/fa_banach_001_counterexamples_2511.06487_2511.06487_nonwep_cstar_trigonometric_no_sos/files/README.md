# Non-WEP C*-coefficients refute the trigonometric factorization extension

Status: **candidate counterexample / likely valid**.  This gives a complete
negative answer to the broad concluding question in arXiv:2511.06487: the
paper's results do not both extend to arbitrary C*-algebra coefficients.

For every unital C*-algebra `A` without the weak expectation property, there
is a finite two-variable trigonometric polynomial `p in A[F_2]` such that:

- every spatial unitary evaluation of `p` is strictly positive; but
- `p` is not a finite sum of hermitian squares in `A[F_2]`.

The construction chooses `x` with
`||x||_min < ||x||_max` in `A tensor C[F_2]` and sets
`p=lambda*1-x^*x` for a scalar `lambda` strictly between the squared norms.
Spatial evaluations see the minimal tensor product; sums of squares must be
positive in the maximal tensor product.

The packet also records that validity of the trigonometric extension forces
WEP, and that standard noninjective von Neumann algebras give examples under
the same spatial evaluation convention.

- Review packet: `solution_packet.pdf`
- LaTeX source: `main.tex`
- Source paper: `source_paper.pdf`
- Decisive WEP reference: `supporting_paper_1107.0418.pdf`
- Source crop: `figures/open_problem_crop.png`
- WEP theorem crop: `figures/wep_theorem_crop.png`
- Verification: `verification_report.md`
- Attempt history: `../../../attempts/2511.06487_cstar_coefficients_wep_obstruction.md`
- Ledger: `../../../ledger/results/2511.06487_nonwep_cstar_trigonometric_no_sos.json`

Human-review focus: verify the intended spatial/minimal evaluation semantics,
the algebraic approximation preserving the min/max norm gap, and the simple
maximal-positivity obstruction to every finite sum of squares.

