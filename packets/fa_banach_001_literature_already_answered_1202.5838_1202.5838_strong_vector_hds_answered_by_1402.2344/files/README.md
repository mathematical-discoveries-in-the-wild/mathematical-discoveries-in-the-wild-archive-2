# Literature answer: the strong vector-valued Hopf--Dunford--Schwartz inequality

- **Source:** S. Charpentier and L. Deleaval, *On a vector-valued
  Hopf-Dunford-Schwartz lemma*, arXiv:1202.5838.
- **Answering paper:** Quanhua Xu, *H-infinity functional calculus and maximal
  inequalities for semigroups of contractions on vector-valued Lp-spaces*,
  arXiv:1402.2344, Theorem 1 and Corollary 3.
- **Status:** `literature_already_answered` (Conjecture part (2) only).
- **Model:** `GPT5.6`.

The source conjecture on PDF page 5 has a weak endpoint part and a strong
`Lp(lq)` part.  Its part (2) asks for the coordinatewise ergodic maximal
operator to be bounded on `Lp(lq)` for every `1<p,q<infinity`.

Xu explicitly cites Charpentier--Deleaval, says that their missing strong
range question is answered affirmatively, and proves a stronger Banach-lattice
statement.  Theorem 1 on PDF page 2 gives the maximal ergodic inequality on
`Lp(X;E)` for every UMD Banach lattice `E`; choosing `E=lq` yields exactly the
source's strong conclusion for every `1<p,q<infinity`.  Corollary 3 matches
the source hypothesis of contractions across the full `Lp` scale.

Scope limitation: this does **not** answer Conjecture part (1), the weak
`L1(lq)` endpoint.  Xu restates that endpoint as Problem 10 on PDF page 9 and
says it is open even for `E=lq`.  The run's focused endpoint work is retained
in
`attempts/1202.5838_vector_hds_weak_endpoint_upgrade_attempt.md`.

Files:

- `solution_packet.pdf` -- compact source/answer identification note.
- `source_paper.pdf` -- arXiv:1202.5838.
- `supporting_paper_1402.2344.pdf` -- explicit answering paper.
- Ledger: `ledger/results/1202.5838_strong_vector_hds_answered_by_1402.2344.json`.

