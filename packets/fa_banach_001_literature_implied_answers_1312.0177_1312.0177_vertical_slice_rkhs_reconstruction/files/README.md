# Vertical-slice RKHS reconstruction

Status: literature-implied answer (complete answer to Question 5.6 of arXiv:1312.0177).

The source proves that the vertical slice \(\{(0,w_2):w_2\in\mathbb D\}\)
is a uniqueness set for \(\mathcal H(K_1^{\max})\), then asks for an
explicit reconstruction of \(g\) from \(g(0,w_2)\). Applying the classical
RKHS restriction theorem makes the restriction map unitary onto the RKHS
with restricted kernel. Its adjoint is the reconstruction operator:
\[
g=R^*(g|_{\{0\}\times\mathbb D}).
\]
The packet gives the cross-kernel evaluation formula, a convergent finite
Gram reconstruction using only trace values, and formulas for the canonical
colligation blocks \(A\) and \(B\).

The provenance label is conservative: Aronszajn's 1950 restriction theorem
is classical, while the direct identification with Question 5.6 and the
displayed reconstruction formulas were not found in the bounded search.

Files:

- solution_packet.pdf: review note and proof.
- source_paper.pdf: arXiv:1312.0177.
- figures/open_problem_crop.png: Question 5.6 on source page 36.
- main.tex: packet source.

The official AMS supporting PDF for Aronszajn (1950) could not be copied
because the environment blocked the download after its external-usage limit
was reached. The packet cites the DOI and is self-contained.

Ledger:
runs/fa_banach_001/ledger/results/1312.0177_vertical_slice_rkhs_reconstruction.json
