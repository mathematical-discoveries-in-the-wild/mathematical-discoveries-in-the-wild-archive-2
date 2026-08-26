# 1910.00720 — periodic tridiagonal two-matrix conjecture answered

Status: literature_already_answered (full conjecture, affirmative).

Model: GPT5.6.

Source: Benjamín A. Itzá-Ortiz and Rubén A. Martínez-Avendaño,
*The numerical range of a class of periodic tridiagonal operators*,
arXiv:1910.00720; *Linear and Multilinear Algebra* 69 (2021), 786–806,
DOI 10.1080/03081087.2019.1706438. Conjecture 3.7 is on source PDF page 19.

Supporting answer: Benjamín A. Itzá-Ortiz, Rubén A. Martínez-Avendaño, and
Hiroshi Nakazato, *The numerical range of some periodic tridiagonal operators
is the convex hull of the numerical ranges of two finite matrices*,
arXiv:2103.01866; *Linear and Multilinear Algebra* 69 (2021), 2830–2849,
DOI 10.1080/03081087.2021.1957760. Theorem 2.3 is on supporting PDF page 7;
Example 2.4 gives the exact specialization on pages 11–12.

## Identification

The source conjectures that the closure of the numerical range of the
`(n+1)`-periodic tridiagonal operator with lower-diagonal period word `0^n 1`
is the convex hull of the numerical ranges of `B_n+J_n` and `B_n-J_n`.

The supporting paper explicitly identifies itself as a proof. Its Theorem 2.3
proves a more general palindromic two-matrix formula, and Example 2.4 applies
it to the source operator and concludes that it proves Conjecture 3.7. Thus the
source formula holds for every `n`.

## Files

- `main.tex`: compact theorem correspondence.
- `solution_packet.pdf`: rendered literature-status packet.
- `source_paper.pdf`: locally rebuilt arXiv:1910.00720 PDF.
- `supporting_paper_2103.01866.pdf`: locally rebuilt answer PDF.
- `verification.md`: build, hash, and visual-inspection record.

