# Exact atomic singular-inner polynomial classification

**Status:** candidate substantial partial result, likely valid  
**Source:** Alexandru Aleman and Frej Dahlin, *Generalized de Branges--Rovnyak spaces*, arXiv:2405.07016, Question 1 on page 25  
**Agent:** `agent_lane_04` (`GPT5.6`)  
**Date:** 2026-08-13

For
\[
S_a(z)=\exp\!\left(-a\frac{1+z}{1-z}\right),\qquad
b_{N,a}(z)=z^NS_a(z),
\]
the packet proves, for every integer `m >= 1`,
\[
\mathcal H(K_{b_{N,a}}^m)\cap\mathbb C[z]
=\{p:\deg p\le m(N-1)\}.
\]
Thus the infinite-dimensional borderline space for `b=zS_a` contains only constants. The proof uses an exact positive-kernel decomposition and a compactly supported Laplace-transform model after the Cayley map. It does not resolve whether some other extreme symbol contains all polynomials.

Contents:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:2405.07016v3.
- `figures/open_problem_crop.png`: full-width evidence crop of Question 1.
- `proof_audit.md`: explicit verifier report and scope check.
- `code/exponent_audit.py`: mechanical check of the exponent maximum used in the pole argument.
- `code/coefficient_probe.py` and `code/extreme_outer_probe.py`: exploratory finite-section diagnostics only; neither is proof evidence.

The ledger entry is `runs/fa_banach_001/ledger/results/2405.07016_atomic_singular_inner_polynomial_classification.json`.
