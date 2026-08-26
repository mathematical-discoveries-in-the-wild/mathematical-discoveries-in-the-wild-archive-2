# Random unitary pencil conjecture: literature answer

Status: `literature_already_answered`

## Source question

Michael T. Jury and George Roman, *Determinants of Random Unitary Pencils*,
arXiv:2506.04400v1 (2025), Conjecture (1.9) on PDF page 3 (restated as the
unnumbered conjecture at the start of Section 3).

For matrix tuples \(\mathcal X=(X_1,\ldots,X_g)\) and
\(\mathcal Y=(Y_1,\ldots,Y_g)\) with outer spectral radii below one, the
conjecture asks whether

\[
\lim_{d\to\infty}\int_{U(d)^g}
\det L_{\mathcal X}(\mathcal U)\,
\overline{\det L_{\mathcal Y}(\mathcal U)}\,d\mathcal U
=
\det\!\left(I-\sum_{j=1}^gX_j\otimes\overline{Y_j}\right)^{-1}.
\]

## Supporting answer

Michael T. Jury, Lodewyk J. van Rensburg, and George Roman,
*Free versions of the strong Szegő limit theorem*, arXiv:2607.25980v1
(2026), Theorem 1.6 on PDF page 4, proves exactly this formula under exactly
the equivalent spectral-radius hypotheses. The sentence immediately before
the theorem explicitly says that it “fully proves the conjecture left open”
in the source paper. Theorem 6.2 on PDF page 25 is a stronger quotient-of-
determinants result, and the paper identifies Theorem 1.6 as its case
\(C=D=0\).

This is therefore an explicit same-authors-plus-coauthor answer, not an
agent-derived implication and not a new result of this run. No part of
Conjecture (1.9) remains open within its stated scope.

## Evidence and files

- `source_paper.pdf`: arXiv:2506.04400v1, 49 pages.
- `supporting_paper_2607.25980.pdf`: arXiv:2607.25980v1, 31 pages.
- Search evidence: exact-title, arXiv-id, author, “random unitary pencil,” and
  “outer spectral radius” searches; the decisive evidence is the explicit
  cross-reference and Theorem 1.6 in arXiv:2607.25980.
- `solution_packet.pdf`: 2 letter-size pages, compiled without warnings and
  visually checked page by page; SHA-256
  `6c63a0c34df5074cacacfd9acad1f912e10288ff50b2ab70d8d5fb5014100a9c`.
- Ledger:
  `runs/fa_banach_001/ledger/results/2506.04400_random_unitary_pencil_conjecture_answered_by_2607.25980.json`.
