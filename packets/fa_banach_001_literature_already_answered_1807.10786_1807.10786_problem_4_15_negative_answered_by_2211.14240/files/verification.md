# Verification record

## Exact mathematical match

- Target page 16 states Problem 4.15 for arbitrary Banach Lipschitz operator
  ideals and the disjunctive premise `I^min` or `I^max` of composition type.
- Supporting Proposition 2.13 shows that
  `Lip_0 o A^min o Lip_0` is not of composition type for every Banach linear
  operator ideal `A`.
- Supporting Proposition 2.16 shows that for every closed `A`, the minimal
  kernel of `Lip_0 o A o Lip_0` equals `OF o Lip_0`, hence is of composition
  type.
- Taking the closed minimal ideal `A=OF` makes the same ideal satisfy the
  premise via its minimal kernel and fail the conclusion.
- Supporting page 11 explicitly cites `[30, Problem 4.15]` and says this gives
  a negative answer. Its reference [30] is Turco--Villafañe, the target paper.

## Provenance

- Archived target source SHA-256:
  `ddf6fcca4645442c3487f8dd7e678abe2df0c00444058b4ce0767bbdb0dbb4de`.
- Archived supporting source SHA-256:
  `f408d5ac1772f0078269f5e1a1c000ec48ce3b666a2422c0b710fcdd19bc4045`.
- `source_paper.pdf` SHA-256:
  `b08afddfaec0a49cb19bf0f3d36ba6c758e09a9b61a553111ec92cc723e9833f`.
- `supporting_paper_2211.14240.pdf` SHA-256:
  `d0cdea4965fd387df03f71722183e18d737289e59beaecc8945fcf603bfe005e`.

The supporting PDF is the same file already bundled and checked in the run's
`2211.14240_minimal_ideal_no_other_examples_structural_classes` packet.

## Evidence crops

- `source_problem_crop.png` SHA-256:
  `e762e3ad4f4889c5febfde49f3772e662a9a0720ab46bafba5601aaf893bbf24`.
- `supporting_noncomposition_crop.png` SHA-256:
  `6d39b14b48436819696531948bb6f01f2ea6b5335a29850c416e8495f8058739`.
- `supporting_answer_crop.png` SHA-256:
  `8de7c1b81a13335749462e693ab67ad052a61a62c174bcc813444a7ed6a59d2f`.

All crops were rendered at 180 dpi and visually inspected.

## Final packet QA

- Final packet: 3 US-letter pages.
- `tmp/main.log` contains no LaTeX warnings, overfull or underfull boxes, or
  unresolved-reference messages.
- Ghostscript `nullpage` validation and full text extraction both succeeded.
- All three rendered pages were visually inspected at original detail; no
  clipping, collisions, stray blank pages, or unreadable evidence crops were
  found.
- Final `solution_packet.pdf` SHA-256:
  `c172d66a71a6f2e4007761eb3e02a52e6a8a420cb1b1cfe2349fa9a04de9e020`.
