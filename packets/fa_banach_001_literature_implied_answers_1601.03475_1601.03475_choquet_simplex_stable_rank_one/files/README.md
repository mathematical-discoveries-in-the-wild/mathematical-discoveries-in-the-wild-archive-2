# Literature-implied answer: the Choquet-simplex conjecture in stable rank one

Status: `literature_implied_answer (partial subcase: full Conjecture 1.2 for all unital stable-rank-one C*-algebras)`

Run: `fa_banach_001`

Agent: `agent_lane_12`

## Source conjecture

Kaushika De Silva, *A note on two Conjectures on Dimension functions of
C*-algebras*, arXiv:1601.03475, states as Conjecture 1.2 on PDF page 1:
for every C*-algebra `A`, the compact convex space `DF(A)` of normalized
dimension functions is a Choquet simplex.

The source proves this only when the extreme boundary of the quasitrace
simplex is finite and one of its comparison hypotheses holds. The official
source PDF is included as `source_paper.pdf`.

## Later theorem

Ramon Antoine, Francesc Perera, Leonel Robert, and Hannes Thiel,
*C*-algebras of stable rank one and their Cuntz semigroups*, arXiv:1809.03984,
proves in Theorem 4.1 (PDF page 13 in the current arXiv version):

> If `A` is a unital C*-algebra of stable rank one, then `K_0^*(A)` is an
> interpolation group and `DF(A)` is a Choquet simplex.

The proof establishes Riesz interpolation for `Cu(A)`, passes it to the
hereditary subsemigroup `W(A)`, then to the Grothendieck group `K_0^*(A)`;
the normalized state space of an interpolation group is a Choquet simplex.

This removes simplicity, separability, exactness, finite radius of comparison,
and finite-extreme-boundary assumptions for the stable-rank-one class. The
official supporting PDF is included as `supporting_paper_1809.03984.pdf`.

## Why `literature_implied_answers`

The later paper explicitly answers the classical Blackadar--Handelman
conjecture but does not identify De Silva's arXiv paper as the question source.
The connection to Conjecture 1.2 of arXiv:1601.03475 is exact but
agent-identified, so this is a literature-implied partial subcase rather than
`literature_already_answered`.

## Scope

- Conjecture 1.2 is settled here only for unital stable-rank-one algebras.
- Conjecture 1.1 (density of lower semicontinuous dimension functions) is not
  answered by Theorem 4.1.
- The arbitrary-algebra forms remain open in recent primary-source surveys.
- Eight focused full-upgrade routes and their structural obstructions are
  recorded in
  `attempts/1601.03475_blackadar_handelman_full_upgrade_attempts.md`.

## Human review notes

- Confirm the current arXiv version's Theorem 4.1 on PDF page 13.
- Confirm that stable rank one alone is the only hypothesis beyond unitality.
- Do not read this packet as a claim about Conjecture 1.1 or arbitrary stable
  rank.
