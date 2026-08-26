# Every integrable graphon has the unscaled sharp-interface limit

**Status:** candidate full solution (likely valid; specialist review requested)

Section 6.2 and the conclusion of arXiv:2408.00422v2 leave the epsilon-scaling of graphon Ginzburg--Landau energies open for unbounded \(L^p\) graphons. The packet proves that no extra scaling is needed: for every nonnegative \(W\in L^1((0,1)^2)\), the source functional with coefficients \(1\) and \(1/\epsilon\) Gamma-converges narrowly to the source graphon total variation. Since all of the paper's \(L^p\) graphons have \(p\geq1\) on a finite-measure domain, this covers the full stated class.

The proof replaces an unavailable global continuity assertion by a truncation argument proving lower semicontinuity of the graphon Dirichlet energy. It also gives a complete trichotomy for an arbitrary prefactor \(a_\epsilon\).

- Main packet: solution_packet.pdf
- Source paper: source_paper.pdf (arXiv:2408.00422v2)
- Source-question image: figures/open_problem_crop.png
- Proof audit: verification.md
- Ledger: runs/fa_banach_001/ledger/results/2408.00422_all_lp_graphons_unscaled_gamma_limit.json

The result does not cover signed kernels or nonintegrable fractional kernels; those are outside the source's \(L^p\), \(p\geq1\), graphon class.
