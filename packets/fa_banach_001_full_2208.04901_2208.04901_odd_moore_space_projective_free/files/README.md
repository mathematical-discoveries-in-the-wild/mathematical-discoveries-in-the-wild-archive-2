# Odd Moore spaces answer the Hermiteness question

Status: candidate full solution; likely valid.

For every odd integer m at least 3, the Moore space

X_m = M(Z/m,4) = S^4 union_degree-m e^5

has H^5(X_m;Z)=Z/m, while every finite-rank complex vector bundle on X_m is
trivial. Consequently C(X_m) is projective free, and therefore Hermite. This
gives a full affirmative answer to the unnumbered Section 2 question in
arXiv:2208.04901.

The proof also gives a sharp dichotomy in this family: for even m, there is
a nontrivial stably trivial rank-two bundle on X_m, so C(X_m) is not
Hermite.

Files:

- main.tex and solution_packet.pdf: theorem, Puppe-sequence proof, parity
  sharpening, and novelty scope.
- source_paper.pdf: official arXiv PDF.
- figures/open_problem_crop.png: the source question on printed page 9.
- verification.md: proof-audit report.

Ledger:
runs/fa_banach_001/ledger/results/2208.04901_odd_moore_space_projective_free.json.
