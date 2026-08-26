# Exterior balls are subcritical for every distance weight

**Status:** candidate full counterexample, likely valid; human review recommended.

This packet answers Open Problem (3) of Ujjal Das, Yehuda Pinchover, and
Baptiste Devyver, *On existence of minimizers for weighted \(L^p\)-Hardy
inequalities on \(C^{1,\gamma}\)-domains with compact boundary*,
arXiv:2303.03527, printed page 32.

For every \(N\ge2\), \(1<p<\infty\), \(R>0\), and \(\alpha\in\mathbb R\), the
operator
\[
-\operatorname{div}\!\left(\delta^{-\alpha}|\nabla u|^{p-2}\nabla u\right)
\quad\text{on }\mathbb R^N\setminus\overline{B_R}
\]
is subcritical.  Besides the positive constant solution, radial flux
conservation produces an explicit positive nonconstant solution.  This rules
out criticality at both requested endpoints \(\alpha+p=1\) and
\(\alpha+p=N\), and in fact for every real \(\alpha\).

The proof has high mathematical confidence.  Novelty confidence is moderate:
after the current paper's first `\\end{document}`, its arXiv source archive
contains a discarded older document recording the special case
\((N,p,\alpha)=(2,2,0)\) and suggesting a generalization.  The published PDF
nevertheless asks the endpoint problem, and the discarded material does not
state or prove the all-\(N,p,\alpha\) theorem here.  The packet discloses this
fully for human assessment.

Files:

- `solution_packet.pdf`: review packet.
- `main.tex`: self-contained source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: real full-width crop of printed page 32.
- `code/verify_radial_flux.py`: algebraic floating-point regression check.
- `verification.md`: verification report.
- `novelty_search.md`: bounded novelty search and source-artifact disclosure.

Ledger:
`runs/fa_banach_001/ledger/results/2303.03527_exterior_ball_all_alpha_subcritical.json`.

