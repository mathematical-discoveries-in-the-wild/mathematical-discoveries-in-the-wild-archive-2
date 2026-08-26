# 2601.14397 — degree-two structured determinantal counterexample

Status: candidate full counterexample, likely valid; human review requested.

Model: GPT5.6.

Source: Radomił Baran and Hugo J. Woerdeman, *Symmetric Schur-class functions on the bidisk and Schur-class functions on the symmetrized bidisk*, arXiv:2601.14397v1 (2026), Theorem 2.2 and the open question on source PDF page 4.

## Result

The packet gives an exact rational symmetric polynomial of bidegree `(2,2)` that is zero-free on the closed bidisk but has no Theorem 2.2 representation with `2 x 2` blocks and a contractive structured matrix. This negatively answers the source question already at `n=2`.

The proof has two finite parts:

- an exact degree-two Schur–Cohn certificate for closed-bidisk stability;
- an exhaustive `2+2` spectral-partition classification followed by exact semidefinite dual certificates excluding a common contraction metric in every class.

The checker uses exact SymPy rational arithmetic; numerical experiments are not part of the proof.

## Files

- `main.tex`: complete expert-facing counterexample proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: full-width crop of the source question on PDF page 4.
- `code/verify_counterexample.py`: exact reusable checker.
- `verification_report.md`: verification record and reviewer focus.

## Reviewer focus

Please check:

1. the Schur–Cohn slice argument and the zero-count continuation from the side boundary to the whole bidisk;
2. the claim that coefficient comparison gives exactly the three canonical simultaneous-similarity classes, with complementary partitions obtained by interchanging `B,C`;
3. the trace-duality identity excluding a common contraction metric.

## Novelty bound

Bounded arXiv searches through 11 August 2026 used the exact source title/phrase and the core terms `symmetric stable polynomial`, `bidisk`, `structured determinantal representation`, `Kummert`, and `n x n`. No later resolution or matching counterexample was found. The source is from January 2026, so this is a short search window and the novelty claim remains provisional.
