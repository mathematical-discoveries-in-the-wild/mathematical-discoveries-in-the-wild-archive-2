# Verification record

Date: 2026-08-17

## Source integrity

- `source_paper.pdf` (arXiv:2005.00902): 348,703 bytes;
  SHA-256 `131b9d19b83dfa105ee2504c3e9f53941379b85719bc630b5c3a63b298914fe0`.
- `supporting_paper_2511.13299.pdf` (arXiv:2511.13299): 1,027,424 bytes;
  SHA-256 `c16cd92ffbad949ca6603a1c38df5de2fa886adfeeabb206e93bc6538d6a75b8`.
- `source_question_crop.png`: direct 150-dpi crop of source PDF page 35;
  SHA-256 `bedca4e8de9fa69d86310bac6297417068d260ee17f90e040df4ad8b1fec10ac`.
- `literature_answer_crop.png`: direct 150-dpi crop of supporting PDF page 23;
  SHA-256 `28b2ee0117bd90da9ba152311e43e16463ad991a2ec32b8198aabb76b644841c`.

Both crops were visually inspected at original resolution and contain the
claimed text.

## Mathematical checks

1. The source question was compared against both the TeX source and PDF page
   35.
2. The later statement was compared against both the TeX source and PDF page
   23 of arXiv:2511.13299.
3. The explicit identities were checked in both directions against the
   definition of an `f`-algebra.
4. The quotient proof was checked for positive lifts, the order-ideal and
   two-sided-ideal properties of the kernel, noncommutative left/right
   multiplication, and the non-Archimedean case.
5. The four-term meet inequality follows from two applications of the Riesz
   decomposition property, valid in every vector lattice.

## PDF checks

- `latexmk` completed successfully with no warnings, overfull boxes,
  underfull boxes, undefined references, or errors after the final edit.
- `solution_packet.pdf`: 5 pages, 771,387 bytes;
  SHA-256 `b2f65633829c7f1a65a89e3e06a31e4f59aeec92eb32d155cf79119c412c1516`.
- `pdftotext -layout` recovered the disposition, source question, theorem,
  novelty limitation, and human-review note.
- All five rendered packet pages were visually inspected at 120 dpi; no
  clipping, overlap, missing glyphs, or unreadable figures were found.

Human mathematical review remains pending.
