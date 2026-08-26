# Verification

## Claim audit

- The exact two questions were checked on source PDF page 42.
- Definitions 4.7 and 4.20 and Proposition 4.10 were checked on source PDF
  pages 18--19 and 24.
- The membership regimes quoted in the packet were checked on source PDF
  pages 33--34.
- The translate convention, word-counting dichotomy, root coefficient,
  central-support implication, and inclusion `delta_e in A(F_k) subset
  B_lambda(F_k)` were audited separately.
- Exact-question, formula-keyword, citation, and later radial-function
  searches through 11 August 2026 found no published resolution.

## Computational sanity check

`code/verify_identity.py` uses exact rational arithmetic. It tests every
reduced word of length at most six in ranks 2, 3, and 4 at parameters 1/3,
2/3, and 4/5. This is a check of the general proof, not evidence replacing
it.

## Artifact checks

- [x] Identity checker passes all cases.
- [x] Source question crop is RGB, legible, and visibly comes from page 42.
- [x] Source audit pages are rendered RGB and visually inspected.
- [x] `main.tex` compiles without errors, undefined references, or box warnings.
- [x] Final PDF metadata and text extraction are healthy (2 letter-size pages,
  4,405 extracted text characters).
- [x] Every final page is rendered RGB and inspected for layout defects.
- [x] SHA-256 hashes are recorded below.

## SHA-256

```text
b6c0f8c70152dfd80275718f4ce18296238ebdcde04a84935a5d0dc5ea533cfc  main.tex
dfb58e28cdd6040ed52c7a3ffbd0408d7e3ab0fcc16dbdda0f54face6b29b25c  README.md
d12d33d9141e5efbf8329b36685412b3bd2d87e64211480ab2cc2e48dd100ba9  solution_packet.pdf
67cfe284021aafaa24c9a164ec5507584e8e6a138c4e4ba3661c7e869201b034  source_paper.pdf
7848946722d1de17531ba0d988bb3a99bd0689f1359502f894dfe066755d6463  source_question_crop.png
084ab2780177614afba05970bab151eb4f9e943e03bd8b81f78204112e2af71b  code/crop_source.py
8b8722505b18328673724afc9b35d1b5521959e6e7fd5cc7117929ff382feed6  code/verify_identity.py
```

Verification completed at 2026-08-11T21:32:21Z.
