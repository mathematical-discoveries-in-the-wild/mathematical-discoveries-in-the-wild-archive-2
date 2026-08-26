# Hardy deficit is not a norm in dimension n >= 3

Status: **candidate counterexample / likely valid** to the explicit norm
subquestion on page 5 of arXiv:1909.12587.  The parent question about existence
of Hardy--Moser--Trudinger extremals remains open.

For every integer `n >= 3`, the functional

`H(u) = int_B |grad u|^n - (2(n-1)/n)^n int_B |u|^n/(1-|x|^2)^n`

is nonconvex on `C_c^infinity(B^n)`.  Consequently `H(u)^(1/n)` cannot be a
norm.  The proof uses a smooth logarithmic boundary layer whose one-dimensional
Hardy quotient tends to `1/4`, below `((n-1)/n)^n`.

The packet also proves the structure-preserving extension: on every bounded
smooth convex domain, the sharp distance-to-boundary Hardy deficit is
nonconvex and its `n`th root is not a norm for `n >= 3`.

- Review packet: `solution_packet.pdf`
- LaTeX source: `main.tex`
- Source paper: `source_paper.pdf`
- Exact source crop: `figures/open_problem_crop.png`
- Verification: `verification_report.md`
- Attempt history: `../../../attempts/1909.12587_hardy_deficit_nonconvexity.md`
- Ledger: `../../../ledger/results/1909.12587_hardy_deficit_not_a_norm.json`

Human-review focus: check the compact-support localization of the base
function, the radial second-variation coefficients, and the Fermi-coordinate
tangential-error estimate in the domain corollary.

