# Power partial Toeplitz overlap classification

Status: `candidate full classification; likely valid`.

Question IV of arXiv:2407.10609 asks for a characterization of
operator-valued Toeplitz operators that are power partial isometries. The
source writes every nonzero partially isometric Toeplitz operator as
`T = M_Gamma M_Psi^*` with inner factors satisfying its explicit product
condition. Define the overlap `C = M_Psi^* M_Gamma = T_{Psi^* Gamma}`. Then

`T^m = M_Gamma C^(m-1) M_Psi^*`.

Because the outer multipliers are isometries, `T^m` is a partial isometry
exactly when `C^(m-1)` is. Thus `T` is power partial isometric exactly when
`C` has the complete Halmos--Wallen form: a direct sum of a unitary,
unilateral shifts, backward shifts, and truncated shifts, with arbitrary
multiplicities.

The packet also proves:

- constant symbols reduce exactly to power partial isometries on the
  coefficient space;
- for analytic `Phi`, `M_Phi` is power partial isometric exactly when
  `Phi(zeta)^{*m} Phi(zeta)^m` is a constant projection for every `m`;
- `Phi(z)=z_1 A` with
  `A=2^(-1/2)[[1,1],[0,0]]` is a nonconstant partially isometric Toeplitz
  symbol whose square is not a partial isometry.

Files:

- `solution_packet.pdf`: review-ready full proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: current arXiv:2407.10609 PDF.
- `figures/open_problem_crop.png`: genuine crop of Question IV on PDF page 35.
- `sanity_check.py`: exact symbolic verification of the counterexample.
- `VERIFIER_REPORT.md`: proof, novelty, scope, and rendering audit.
- Ledger: `runs/fa_banach_001/ledger/results/2407.10609_power_partial_toeplitz_overlap_classification.json`.
