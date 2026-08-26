# Strip-growth obstructions for rank-one truncated Toeplitz symbols

Status: `partial_result_likely_valid`

Source: Ryan O'Loughlin, “Symbols of compact truncated Toeplitz operators,”
arXiv:2107.09115, *Journal of Mathematical Analysis and Applications* 507
(2022), 125819.

The source restates the long-standing conjecture that every bounded truncated
Toeplitz operator on `K_I^2` has a bounded symbol exactly when `I` is a
one-component inner function.  Equivalently, every compact truncated Toeplitz
operator has a symbol in `I C(T)` exactly in that case.

This packet proves a new sufficient obstruction for an individual boundary
rank-one operator.  If `I` has an angular derivative at `zeta` and tends to
zero along a sufficiently tangential sequence `z_n`, then
`k_zeta^I tensor k_zeta^I` cannot have a bounded symbol.  The mechanism is
endpoint rather than finite-power integrability: Sarason's criterion would
produce an analytic function with bounded real part, hence with only
logarithmic radial growth, while the reproducing kernel grows like
`1/|1-conj(zeta)z_n|`.

Two explicit applications are proved:

1. a Blaschke product with zeros
   `a_n=(1-exp(-sqrt(n))) exp(i/n)`;
2. the zero-free singular inner function associated with
   `sum_n exp(-sqrt(n)) delta_{exp(i/n)}`.

In both cases the boundary kernel at `1` belongs to `H^p` for **every** finite
`p>1`, yet the corresponding rank-one truncated Toeplitz operator has no
bounded symbol.  Thus these examples pass all previously known fixed-`p`
kernel-integrability tests.  Since the operators are rank one, they also have
no symbol in `I C(T)`, providing explicit witnesses for the compact
formulation of the conjecture.

The full conjecture remains open.  The result verifies its negative direction
for two highly tangential non-one-component examples but does not force such
a tangential small-value sequence for every non-one-component inner function.

Files:

- `solution_packet.pdf`: expert-facing proof packet.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: readable crop of Conjectures 3.1 and 3.2.
- `verification_report.md`: mathematical, literature, and artifact audit.

Human-review recommendation: verify the invocation of Sarason's rank-one
criterion and the Ahern--Clark/Cohn `H^p` kernel criterion; the remaining
estimates are elementary and written with their constants suppressed only by
two-sided asymptotic notation.
