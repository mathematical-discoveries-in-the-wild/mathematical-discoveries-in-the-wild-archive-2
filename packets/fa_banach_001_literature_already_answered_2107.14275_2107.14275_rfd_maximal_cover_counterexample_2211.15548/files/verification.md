# Verification

Verified on 2026-08-12.

## Source and mathematics

- Thompson's Question 1 was checked in the primary arXiv:2107.14275 PDF,
  p. 2.
- Hartz's explicit algebra and its two asserted properties were checked in
  the primary arXiv:2211.15548 PDF, Theorem 1.3 on pp. 4--5.
- The exact conclusion that the algebra is RFD while its maximal C*-algebra
  is not RFD was checked in Hartz's Corollary 1.4 on p. 6.
- The bridge was independently checked: if `C*_{max}(B)` were RFD, the
  Exel--Loring theorem applied to the maximal-cover extension of Hartz's
  Toeplitz representation would yield the point-SOT approximation forbidden
  by Theorem 1.3(b).
- The packet distinguishes the maximal C*-cover from the RFD C*-envelope.

## Packet QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- The final log contains no warnings, undefined references, overfull boxes,
  fatal errors, or compilation errors.
- `solution_packet.pdf` has 3 pages.
- All three pages were rendered at 150 dpi and visually inspected.
- No clipping, overlap, missing glyphs, unreadable evidence, or broken
  figures were found.

## SHA-256

- `solution_packet.pdf`:
  `8e0f3aa989ddbfddd30a20b4607d3b8bb7a4a6091c4570cb14103863f4c120e4`
- `source_paper.pdf`:
  `d2328339530b4a67d596c0cb51c7a9e9b2b9063986adecb4f03beeaa66f86ab2`
- `supporting_paper_hartz_2211.15548.pdf`:
  `15d137972e2fde4774ace03df9d9103adaa2bf97969832b5f91bc2be7abe4c42`
- `figures/open_question_crop.png`:
  `585fd47a95b959899ac969d82ae1b1356583f9812f3d2cc0b8edc02daba7985d`
- `figures/hartz_algebra_crop.png`:
  `0a2fc87604f87d4345621d7b312e96248b5b586a5c7a850916ea83f400442fce`
- `figures/hartz_theorem_crop.png`:
  `7691b65ef17a63b49ae8bd685dafb9c041f26e08231c8d010ef83f02e90c1385`
- `figures/hartz_counterexample_crop.png`:
  `5344317991ac20bd325f7113dbee7a2a8ad8a394dc3c10e951105b516dc58743`

