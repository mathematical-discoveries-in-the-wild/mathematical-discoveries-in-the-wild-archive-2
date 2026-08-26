# Verification record

Status: mathematical proof and final artifact QA complete.

## Proof checks

- `||y_n||=1` for every `n`, hence `d(0,A)=1`.
- `||e_n-y_n||<=c<1` and `(e_n)` is weakly null in `c0`.
- An unbounded-index sequence in `A` cannot weakly converge in `c0`, because
  every coordinate would have limit `c`.
- Therefore `A` is sequentially weakly closed and `I_A` is s.w.l.s.c.
- The Pasch–Hausdorff envelope of `I_A` is exactly `k d(.,A)`.
- The strict liminf inequality holds for every `k>0`.

## Novelty check

Cheap indexes, the full local source corpus, and exact-phrase/arXiv-focused
web searches found no later answer or matching `c0` construction. Novelty
confidence is moderate.

## Artifact QA

- Official source PDF: valid, 15 pages.
- Open-problem crop: rendered from PDF page 10 and visually checked for the
  complete question and readable full-width margins.
- LaTeX compiled to a three-page PDF with no warnings, overfull/underfull
  boxes, undefined references, or multiply defined labels.
- All three pages were rendered at 150 dpi and visually inspected. No
  clipping, overlap, unreadable evidence, or margin defects were found.
- `solution_packet.pdf` SHA-256:
  `6a438e0981e4ac4c8a884794a5da9b7bef5058078beacbc2453f77f8d608b01d`.
- `source_paper.pdf` SHA-256:
  `1084d15dec4f31801f8e42639c56739420709b879e0ec0c8d32543f5c8f12e3a`.
