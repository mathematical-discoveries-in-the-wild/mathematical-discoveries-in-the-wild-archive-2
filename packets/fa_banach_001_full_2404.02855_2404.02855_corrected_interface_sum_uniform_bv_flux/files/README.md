# Uniform BV--flux bound for the corrected Brenier interface conjecture

Status: `candidate full solution, likely valid; human review requested`.

Source: Vincent Divol, Jonathan Niles-Weed, and Aram-Alexandre Pooladian,
*Tight Stability Bounds for Entropic Brenier Maps*, arXiv:2404.02855 and
IMRN 2025(7), rnaf078. The corrected conjecture is in Remark 6.12 of the
published normalization, reproduced in Chapter 6 of Pooladian's thesis.

## Result

If `0 <= rho <= M`, the source is supported in `B(0,R_x)`, and every target
atom lies in `B(0,R_y)`, then the revised interface coefficient satisfies

`Q(mu) <= 2 d omega_d M R_y R_x^(d-1) log(2)`.

The constant is independent of the number, weights, separation, and
Laguerre combinatorics of the target atoms. The proof identifies the ordered
interface sum with twice the weighted Laplacian mass of the polyhedral
Brenier potential and bounds that mass by boundary flux.

## Version audit

The arXiv-v1 formula contains `log(1 + mu_j/mu_i)` and is unbounded even for
two fixed atoms with masses `delta` and `1-delta`. The published
normalization absorbs the masses into the dual potential and replaces this
factor by `log(2)`. The packet proves the corrected conjecture, while
recording the elementary counterexample to the superseded v1 expression.

## Files

- `solution_packet.pdf`: rendered full proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: arXiv-v1 source paper.
- `source_revised_thesis.pdf`: later author source reproducing the corrected
  published statement.
- `source_metadata.json` and `source_metadata_arxiv.json`: version metadata.
- `figures/source_conjecture_revised.png`: exact corrected conjecture crop.
- `verification_report.md`: proof and literature audit.

## Novelty

Exact-formula, exact-phrase, and later-literature searches found no published
resolution. The argument uses standard convex-BV machinery, so novelty
confidence is moderate even though the application appears new.
