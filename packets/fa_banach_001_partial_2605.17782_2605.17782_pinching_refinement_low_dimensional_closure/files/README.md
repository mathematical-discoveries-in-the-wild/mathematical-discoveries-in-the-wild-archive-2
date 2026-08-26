# Low-dimensional, rank-one, and first higher-cycle closures

Status: **candidate partial result — likely valid, pending human review**.

Source: Trung Hoa Dinh, *On the Failure of the Upper Bound in the Refined BMV Conjecture and a Pinching Correction*, arXiv:2605.17782 (2026), Conjecture 5.1 on PDF page 7.

The source asks whether

\[
\mathcal A_{n,m}(A,B)\geq
\mathcal A_{n,m}(A,E_A(B))
=\operatorname{Tr}(A^nE_A(B)^m)
\]

for all positive semidefinite matrices and all nonnegative integers \(n,m\). The source proves the case \(m=2\).

This packet proves four overlapping closures:

- every positive semidefinite \(2\times2\) pair, for all \(n,m\);
- every rank-one \(A\), in arbitrary finite dimension, for all \(n,m\);
- arbitrary finite dimension for \(n=0\) or \(n=1\), for all \(m\);
- any pair that is phase-balanced: in an eigenbasis of \(A\), a diagonal unitary gauges \(B\) to an entrywise nonnegative matrix.
- arbitrary finite dimension at the first higher-cycle corner \((n,m)=(2,3)\).

The full higher-dimensional conjecture remains open. The new \((2,3)\) proof controls its signed three-cycle contribution through a correlation-matrix squared-norm estimate, but no analogous estimate is yet proved for all exponents.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source evidence for Conjecture 5.1.
- `code/check_pinching_subcases.py`: independent numerical sanity checks.
- `verification.md`: commands, tested scope, and limitations.

Human-review focus: check the path-deletion argument for repeated eigenspaces, the normalization of the cyclic weak-composition formula, and the correlation normalization in the \((2,3)\) theorem. The numerical checks are not used as proof.
