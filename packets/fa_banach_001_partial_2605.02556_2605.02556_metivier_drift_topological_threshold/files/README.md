# The topological-dimension threshold for Métivier sub-Laplacians with drift

This packet removes the extra `+1` from Theorem 1.2 of arXiv:2605.02556.
For every Métivier group, it proves the spectral-multiplier theorem under the
sharp-form hypothesis

`s > d |1/p-1/2|`.

The new input is a drift-cap estimate for the character-weighted volume of a
Carnot--Carathéodory propagation ball.  It replaces the source's coarse
full-annulus bound and fits directly into the abstract theorem of
Martini--Ottazzi--Vallarino (arXiv:1705.04752).

Status: candidate partial result of high mathematical confidence.  It fully
closes the gap for the Métivier class, but the source phrases its question for
arbitrary two-step stratified groups; that broader problem remains open.

Files:

- `main.tex`: theorem, cap lemma, proof, parameter audit, and scope.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_question_crop.png`: source question on PDF page 3.
- `figures/source_dplus1_theorem_crop.png`: source's near-optimal theorem.
- `code/verify_thresholds.py`: exact exponent and parameter sanity checks.
- `VERIFICATION.md`: proof, build, visual-QA, novelty, and hash record.
