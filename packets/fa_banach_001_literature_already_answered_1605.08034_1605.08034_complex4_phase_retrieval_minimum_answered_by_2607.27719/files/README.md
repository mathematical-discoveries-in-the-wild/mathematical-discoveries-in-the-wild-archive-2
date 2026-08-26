# 1605.08034 — the complex four-dimensional minimum is exactly eleven

Status: literature_already_answered (full exact answer in complex dimension four).

Model: GPT5.6.

Source: Yang Wang and Zhiqiang Xu, *Generalized phase retrieval: measurement number, matrix recovery and beyond*, arXiv:1605.08034, source PDF page 5.

Supporting lower bound: Meng Huang, *Phase Retrieval in C^4 Requires Exactly Eleven Measurements*, arXiv:2607.27719v1, Theorem 1.2 and Corollary 1.3 on supporting PDF page 4, with proof on pages 10–14.

Supporting upper bound: Cynthia Vinzant, *A small frame and a certificate of its injectivity*, arXiv:1502.04656, supporting PDF pages 1–2.

## Identification

The source says that the smallest number of standard rank-one intensity measurements was unknown even in `C^4`. Its own lower bound and Vinzant’s construction left the value at ten or eleven.

Huang proved on 30 July 2026 that no ten-vector family has the phase-retrieval property in `C^4`. Combined with Vinzant’s explicit eleven-vector injective frame, the exact minimum is eleven.

## Scope

This settles standard rank-one phase retrieval in complex dimension four. It does not determine the source’s separate generalized-measurement, fusion-frame, low-rank recovery, or higher-dimensional minima.

## Files

- `main.tex`: complete literature-status derivation and scope boundary.
- `solution_packet.pdf`: rendered status packet.
- `source_paper.pdf`: official source PDF.
- `supporting_paper_2607.27719.pdf`: official exact lower-bound PDF.
- `supporting_paper_1502.04656.pdf`: official eleven-vector construction PDF.
