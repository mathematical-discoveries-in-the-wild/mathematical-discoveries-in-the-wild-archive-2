# Setwise smoothness of an RKHS automatically gives a continuous embedding

This packet answers the open question after Proposition 4 of arXiv:1604.05251.

## Result

For an open set `Ω ⊂ R^d`, every RKHS setwise contained in `C^m(Ω)` is continuously contained there. The same holds for `C^m_0(Ω)`, and for both finite `m` and `m=∞`.

The proof is by the Fréchet-space closed graph theorem: RKHS-norm convergence implies pointwise convergence, while convergence in either smooth target also implies pointwise convergence, so the canonical inclusion has closed graph.

## Files

- `main.tex`: complete proof and audit.
- `solution_packet.pdf`: compiled packet.
- `figures/open_problem_crop.png`: exact source passage.
- `verification.md`: compilation and visual-verification record.

