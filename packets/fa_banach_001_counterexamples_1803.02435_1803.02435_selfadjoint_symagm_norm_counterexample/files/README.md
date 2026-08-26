# Self-adjoint symmetrized-AGM norm counterexample for arXiv:1803.02435

Status: candidate full counterexample to the literal operator/self-adjoint
formulation, likely valid, pending human review. The original Recht--Ré
positive-semidefinite weak-variance conjecture remains open.

For `n=k=3`, the packet gives three pairwise nonproportional invertible real
symmetric `2x2` matrices for which

`||E_wo,3|| = 581/6 + sqrt(829)`

is strictly larger than

`||E_wr,3|| = (3082 + sqrt(91205))/27`.

The norm ratio is approximately `1.00233216996281`; a rational certificate
shows the norm gap is larger than `164/675`.

## Contents

- `main.tex`: source statement, scope audit, theorem, exact proof, and boundary.
- `solution_packet.pdf`: compiled three-page review packet.
- `source_paper.pdf`: arXiv:1803.02435.
- `original_recht_re.pdf`: arXiv:1202.4184 scope evidence.
- `figures/`: source excerpts for the open statement and positivity context.
- `code/exact_verifier.py`: exact enumeration and eigenvalue verification.
- `VERIFICATION.md`: mathematical, novelty, and artifact checks.

Related attempt log:
`runs/fa_banach_001/attempts/1803.02435_symagm_norm_attempts.md`.
