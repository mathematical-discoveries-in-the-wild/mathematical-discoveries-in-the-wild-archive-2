# Candidate full solution: Hadamard module for every finite p

Status: **candidate full solution; likely valid, pending human review**.

This packet answers the open question following Example 5.2 of Calin,
Cartwright, Coffman, Delfín, Girard, Goldrick, Nerella and Wu,
“C*-like modules and matrix p-operator norms” (arXiv:2505.19471; published in
*Annals of Functional Analysis*).

## Result

For the paper's Hadamard-diagonal algebra

\[
A_p=\{H\operatorname{diag}(\lambda_1,\lambda_2)H:\lambda_1,\lambda_2\in
\mathbb C\}\subset M_2^p(\mathbb C),
\]

the row–column module
\((M^p_{1,2}(A_p),M^p_{2,1}(A_p))\) is C*-like exactly when \(p=2\).

- For \(1<p<2\), the exact column used in Example 5.2 violates the first
  norm-recovery axiom.
- For \(2<p<\infty\), its adjoint row violates the second axiom, by
  \(p\)-\(p'\) adjoint duality.

The proof is analytic and covers complex coefficients. Its central equality
case reduces possible norming functionals to
\(e_1,e_2,2^{-1/p'}(1,i),2^{-1/p'}(1,-i)\); strict Clarkson inequalities and
a positive second variation exclude all four.

## Files

- `main.tex`: self-contained theorem, proof intuition, proof, novelty bounds,
  and reviewer focus.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source PDF.
- `figures/open_problem_crop.png`: real full-width crop of the question on
  source PDF p. 18.
- `verification_report.md`: line-by-line proof audit and artifact checks.
- `code/check_identities.py`: numerical/symbolic sanity checks; not proof.
- `code/crop_source_question.py`: reproducible crop helper.

## Novelty check

On 2026-08-11, the four cheap run indexes were searched for the arXiv id,
exact title, C*-likeness, Example 5.2, and the Hadamard/simultaneously
diagonalizable formulation; there was no duplicate. Exact-title and
exact-question web searches found the source and its published Springer
version, whose p. 18 still says the question is open, but no separate answer.
This was bounded rather than exhaustive, so novelty confidence is moderate.

## Recommended human review

Check especially the smooth equality case leading to the four projective
directions, the exceptional-phase second variation, and the adjoint transfer
from \(p'<2\) to \(p>2\).
