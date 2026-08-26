# Uniform Roe exactness versus nuclearity: answered by Sako

- **Source:** G. Arzhantseva, E. Guentner, and J. Spakula, *Coarse
  non-amenability and coarse embeddings*, arXiv:1101.1993.
- **Answering paper:** Hiroki Sako, *Finite-dimensional approximation
  properties for uniform Roe algebras*, arXiv:1212.5900, Theorem 1.1.
- **Status:** `literature_already_answered` (Section 5.2 general question).
- **Model:** `GPT5.6`.

Section 5.2 of the source asks whether exactness of `C_u^*(X)` forces
nuclearity for every bounded-geometry metric space `X`.  Sako's Theorem 1.1
proves the stronger five-way equivalence

`Property A <=> nuclearity <=> exactness <=> local reflexivity <=> ONL`.

Thus the answer is affirmative.  It also implies immediately that the source's
specific non-Property-A box space has nonexact uniform Roe algebra (a fact the
source already records by a box-space argument).

Scope limitation: this does not settle the separate Section 5.1 question
whether the maximal-to-reduced map is an isomorphism for that box space.  The
run's focused work on that question is retained in
`attempts/1101.1993_maximal_uniform_roe_isomorphism_attempt.md`.

Files:

- `solution_packet.pdf` -- compact source/answer status note.
- `source_paper.pdf` -- arXiv:1101.1993.
- `supporting_paper_1212.5900.pdf` -- Sako's answering paper.
- `supporting_paper_1504.05615.pdf` -- later primary status evidence for the
  distinct maximal-versus-reduced question.
- Ledger:
  `ledger/results/1101.1993_uniform_roe_exactness_answered_by_1212.5900.json`.
