# Verification

- Source PDF: official arXiv PDF for 2410.10731, 16 pages.
- Source question: Section 6, printed page 15.
- Source input: Proposition 3.5, its displayed Bernstein upper bound.
- Lower bound: independently checked on the one-row and one-column
  coordinate subspaces, including infinite target exponents.
- Algebra: `code/check_exponents.py` checks the exact alignment criterion on
  a rational grid.
- Scope: no assertion is made in the crossed regions.
- Packet: compiled with `latexmk`; text extraction and page renders checked.
- Status: candidate substantial partial result, subject to expert review.
