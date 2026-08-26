# Every amenable action admits a 1-approximating sequence

**Status:** candidate full solution, likely valid; human review required.

This packet addresses the conjecture following Definition 1.3 of Adrián M.
González-Pérez, *Crossed-Product Extensions of Lp-Bounds for Amenable Actions*,
arXiv:1611.08486, J. Funct. Anal. 274 (2018), 2846–2883.

The proof converts the positive `L2` approximants supplied by amenability into
equal-Haar-volume indicator fields.  It quantizes each squared approximant
into level sets, puts the levels in disjoint right translates lying in the
kernel of the modular homomorphism, and adds one bounded correction layer so
that every fibre has exactly the same measure.  The correction contributes
vanishing relative boundary.  If the group itself is amenable, ordinary
Følner sets already solve the problem for every action.

The modular step is what removes an apparent unimodularity restriction: for a
nonamenable group, the kernel of the modular homomorphism is necessarily
noncompact, so it supplies arbitrarily many disjoint Haar-preserving right
slots.

Reviewers should focus on:

1. the exact-volume measurable selection in the nonatomic case;
2. the quantized layer-cake inequality and normalization;
3. the modular-kernel dichotomy;
4. compatibility with the source paper's net/sequence convention.

Files:

- `solution_packet.pdf`: complete proof and verification report;
- `source_paper.pdf`: original arXiv paper;
- `figures/open_problem_crop.png`: page 9 definition and conjecture;
- `code/verify_quantized_layers.py`: finite surrogate checks (not part of the proof).

Ledger record:
`ledger/results/1611.08486_amenable_actions_admit_one_approximating_sequences.json`.
