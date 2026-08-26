# Factorial Toeplitz diagonals give a nonclosable polynomial core

Status: `counterexample likely valid`.

The open problem in Remark 2.2 of arXiv:2409.19113 asks whether a Toeplitz
matrix with analytic part in `H^p_m` can always be extended from vector
polynomials to an operator in the Sarason class.  The answer is no as stated.

For any admissible analytic part, set the negative diagonals to
`a_{-k}=k!I_m`.  Then `z^n e/n!` tends to zero in `H^p_m`, while its forced
matrix image tends to the nonzero constant `e`.  The polynomial operator is
not closable, so it has no closed extension at all.

Packet: `solution_packet.pdf`  
Source: `source_paper.pdf`  
Verification: `verification.md`  
Ledger: `runs/fa_banach_001/ledger/results/2409.19113_factorial_toeplitz_nonclosability.json`
