# Minimal weak phase retrieval: cofactor characterization and null locus

Status: **candidate partial result, likely valid, pending human review**.

This packet contains three rigorous conclusions connected to Problems 9.1 and
9.2 of arXiv:2110.06868:

1. A finite necessary-and-sufficient cofactor characterization of weak phase
   retrieval by exactly `2n-2` real measurement vectors.
2. An explicit nonzero polynomial vanishing on every such frame. Consequently,
   the minimal weak-phase-retrievable locus is contained in a proper real
   algebraic hypersurface, is nowhere dense, and has Lebesgue measure zero.
3. An exact countercheck showing that the published six-vector `R^4` example
   cited before Problem 9.2 is not weak phase retrievable. The vectors
   `x=(2,1,0,1)` and `y=(0,-1,0,1)` have the same six measurement magnitudes
   but incompatible common-coordinate signs.

Problem 9.1 itself was already answered by Theorem 6 of arXiv:2301.03520; a
separate lightweight literature-status packet records that provenance. The
algebraic-nullity theorem here is a stronger adjacent result. Problems 9.2 and
9.3 remain open. In particular, disproving the published `R^4` example does not
prove that no other six-vector `R^4` example exists.

Files:

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:2110.06868.
- `supporting_paper_1612.08018.pdf`: source of the claimed `R^4` example.
- `code/verify_cofactor_theorem.py`: exact theorem/example sanity checks.
- `code/search_sign_frames_n5.py`: exhaustive exact sign-frame search.
- `verification.md`: commands, outputs, and proof/code boundary.
- `novelty.md`: bounded literature audit.

Human review should focus on the sufficiency direction of the cofactor theorem,
the explicit polynomial witness, and the direct multiplication for the `R^4`
countercheck.
