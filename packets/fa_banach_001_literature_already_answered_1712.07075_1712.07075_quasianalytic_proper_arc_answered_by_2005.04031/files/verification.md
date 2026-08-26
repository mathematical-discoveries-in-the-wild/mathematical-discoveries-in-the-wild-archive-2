# Verification record

Verified on 2026-08-17 for `fa_banach_001`, lane 9.

## Source matching

- arXiv:1712.07075, PDF page 3, asks for existence of a contraction `T`
  satisfying `pi(T)=sigma(T)` with this common set not equal to the unit
  circle.
- arXiv:2005.04031, Corollary 9.7 on PDF page 27, explicitly gives a
  quasianalytic contraction `R` with spectrum the closed upper semicircle,
  unitary asymptote supported there, and quasianalytic spectral set equal to
  that spectrum.
- The later result matches every quantifier of the source existence question.
  Its lack of an estimate for `||R^{-1}||` belongs only to the broader
  Kérchy–Szalai quantitative question.

## Artifact QA

- Both arXiv PDFs were downloaded directly and identified as valid PDFs.
- `latexmk` completed successfully; the final log contains no warnings,
  undefined references, overfull boxes, or errors.
- Poppler reports a two-page, unencrypted letter-size packet.
- Poppler text extraction recovered all headings, equations, claims, and
  references.
- Both pages were rendered at 144 dpi and visually inspected after the final
  heading-spacing edit.  No clipping, overlap, illegible text, or malformed
  symbols were observed.

## SHA-256

- `source_paper.pdf`: `a04dd721cdb892605272039d729e989b75eec83e14f0d75939f14327c294358a`
- `supporting_paper_2005.04031.pdf`: `b975c2370eba97a9ecf12d543623f308368d9461714b6fbd48a6d9ecc10acaa1`
- `solution_packet.pdf`: `76cea7cf44e69629808a70acb6b8854baf878ba0f396689e8e452a2d77b66eb6`
- `main.tex`: `18549dbf570528d03281d5d9e5f7edc79b51129ee13a4ec2600127e16d92cf09`
- `README.md`: `fcfc6c494fea833b7bb856b4514ebff58309533ec3c3b0b36a9ac2de65832cc7`
