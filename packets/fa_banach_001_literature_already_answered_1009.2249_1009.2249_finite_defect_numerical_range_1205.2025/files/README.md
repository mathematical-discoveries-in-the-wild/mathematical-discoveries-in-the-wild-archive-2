# Finite-defect numerical-range conjecture: affirmative later answer

Status: `literature_already_answered`

## Source

Benhida, Gorkin, and Timotin, arXiv:1009.2249, Conjecture 6.1. For a
contraction whose two defect indices equal `N<infinity`, the conjecture asks
whether the closed numerical ranges of all economical unitary
`N`-dilations wrap the closed numerical range of the contraction. This
implies that their intersection equals the original closed numerical range.

## Answer

Bercovici and Timotin, arXiv:1205.2025, Theorem 2.4, prove for every such
contraction:

- each support line of the original closed numerical range is a support line
  of the closed numerical range of some unitary `N`-dilation; and
- the intersection of the latter ranges is exactly the former.

The support-line assertion proves the full wrapping clause: for an open
half-plane containing the original compact range, take its parallel support
line. The theorem supplies a dilation range on the same supporting side,
which lies strictly inside the given half-plane.

## Packet contents

- `main.tex`, `solution_packet.pdf`: exact scope match and wrapping deduction.
- `source_problem_paper.pdf`: official arXiv:1009.2249 PDF.
- `source_answer_paper.pdf`: official arXiv:1205.2025 PDF.
- `figures/source_conjecture_crop.png`: Conjecture 6.1 on source PDF page 12.
- `figures/answer_theorem_crop.png`: Theorem 2.4 on answer PDF page 4.
- `VERIFICATION.md`: mathematical and rendering checks.
