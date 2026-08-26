# Subquadratic p-elastic flow near nonzero curvature

Status: `candidate_partial_likely_valid`

This packet gives a rigorous conditional extension of the main convergence
mechanism in arXiv:2007.00582 from `p>=2` to every `1<p<2`.

The new result has three parts:

- local smooth well-posedness for nowhere-zero-curvature initial curves;
- an `H^4 -> L^2` Lojasiewicz-Simon inequality at every smooth critical curve
  whose curvature never vanishes;
- full smooth convergence whenever a global smooth flow remains in the
  nowhere-zero-curvature regime and has the same smooth sub-convergence input
  assumed by the source theorem.

The Hilbert realization is essential.  The source's `L^p/L^{p'}` proof uses
an embedding that holds for `p>=2` and fails for `p<2`.  In `H^4 -> L^2`, the
Hessian is strongly elliptic because its curvature-direction eigenvalue is
`(p-1)|k|^{p-2}>0`.

This is not a complete answer to the broad `p in [1,2)` problem.  It does not
prove global existence, prevent curvature zeros, or include `p=1`.  Those are
sharp obstructions recorded in the proof and attempt note.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet;
- `source_paper.pdf`: arXiv:2007.00582;
- `code/check_principal_symbol.py`: algebraic/numerical sanity check.
