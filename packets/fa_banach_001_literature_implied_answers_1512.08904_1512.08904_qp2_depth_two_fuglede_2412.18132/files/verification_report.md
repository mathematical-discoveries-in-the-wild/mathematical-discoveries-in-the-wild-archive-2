# Verification report

Status: `likely valid literature-implied partial answer`

## Source checks

- The original sentence appears in arXiv:1512.08904v1, Section 6.4, printed
  and PDF page 23.
- Zhou's complete finite theorem appears as Theorem 1 of
  arXiv:2412.18132v4, PDF page 26.
- Zhou's general-depth results appear as Lemmas 11, 13, and 14 on PDF pages
  11–12.
- Both PDFs are stored locally in the packet.

## Mathematical checks

- Tiling reduction checked in both directions by restriction to cosets of
  `Z_p^2` and reduction modulo `p^m Z_p^2`.
- Annihilator identity checked: `(p^m Z_p^2)^perp = p^(-m) Z_p^2` for the
  standard character with kernel `Z_p`.
- Spectrum construction checked sector-by-sector: outer frequency cosets are
  orthogonal on each ball; within a sector the Gram matrix is the finite
  Fourier Gram matrix of `A`.
- Converse completeness checked by the orthogonal decomposition of
  `L^2(Omega_A)` into character sectors of `p^m Z_p^2`, each of dimension
  `|A|` in the cell coordinate.
- The modulo-four obstruction example has 8 graph points, tiles `Z_8^2` with
  the vertical subgroup, and has the stated 5-point image; cardinality 5 does
  not divide 16, so that image cannot tile.
- The subgroup-complement claim follows from Fourier duality for the quotient
  `G/H`; the reverse claim follows because a subgroup spectrum forces one
  representative in every coset of its annihilator.

## Scope audit

The packet claims only depth at most two, the cited extremal cardinalities,
and the subgroup-complement class. It explicitly leaves all arbitrary subsets
of `(Z/p^m Z)^2`, `m>=3`, open. It does not represent Zhou as knowingly
answering the 2015 `Q_p^2` question.

## Artifact checks

- LaTeX compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Build log checked for undefined references, overfull boxes, and fatal errors.
- Every rendered page was visually inspected at readable resolution.

Reviewer focus: the converse half of the spectral finite-quotient reduction.
