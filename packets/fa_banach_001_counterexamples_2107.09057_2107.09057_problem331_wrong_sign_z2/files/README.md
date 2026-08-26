# Problem 3.31 wrong-sign counterexample

This packet gives a full counterexample to Problem 3.31 of arXiv:2107.09057
exactly as printed.

- `solution_packet.pdf`: expert-facing proof and corrected formulation.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: official source PDF.
- `figures/problem331_crop.png`: readable source passage from PDF page 15.
- `supporting_papers/1408.1165.pdf`: the finite-group bi-shift
  classification used to enumerate all minimizer lines for `Z_2`.
- `verification_report.md`: proof and visual checks.
- `novelty.md`: bounded search record.

The printed premise is automatically true for every normalized 2-box because
it points in the same direction as the sharp uncertainty lower bound.  The
likely intended hypothesis is the reversed near-minimum inequality
`H(x)+H(Fx) <= 2 log(delta)+epsilon`.
