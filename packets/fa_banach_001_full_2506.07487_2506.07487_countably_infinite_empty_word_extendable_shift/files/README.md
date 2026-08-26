# Countably infinite empty-word set with a continuously extendable shift

status: `full` (candidate full solution, likely valid; human review requested)

source: Rodrigo Bissacot, Iván Diaz-Granados, and Thiago Raszeja,
*Extendable Shift Maps and Weighted Endomorphisms on Generalized Countable
Markov Shifts*, arXiv:2506.07487.

packet: `runs/fa_banach_001/solutions/full/2506.07487_countably_infinite_empty_word_extendable_shift/`

ledger: `runs/fa_banach_001/ledger/results/2506.07487_countably_infinite_empty_word_extendable_shift.json`

## Result

The source asks for examples of generalized countable Markov shifts `X_A`
whose shift extends continuously to all of `X_A` and whose empty-stem set
`E_A` is infinite. The packet constructs an irreducible, column-finite
zero-one matrix for which `X_A` is compact,

```text
E_A = {(e,{o})} union {(e,{o,b_j}) : j>=1},
```

and the shift extends continuously by fixing every point of `E_A`. Thus
`E_A` is countably infinite and carries the identity dynamics.

The alphabet consists of a hub `o`, binary-tree markers `b_j`, and a ray
`v_{j,1},v_{j,2},...` attached to every marker. Every column contains `o`.
The ray columns converge to `{o,b_j}`, while columns whose marker index tends
to infinity converge to `{o}`. The parent edges force the same column limit
after one shift, which is the mechanism behind continuity.

## Verification

- The packet proves irreducibility, column-finiteness, compactness, the exact
  classification of all column accumulation points, and sequential continuity
  at every empty configuration (the configuration space is metrizable).
- `code/verify_construction.py` checks finite windows of the column formula,
  bounded column sizes, parent paths to the hub, and predicted stabilization.
  It is a sanity check, not a substitute for the proof.
- A bounded current search using the exact title, `infinite E_A`, `empty-word
  configurations`, and continuous extensions found no later construction.
  A November 2025 author talk still presents the finite periodic-renewal
  examples. Novelty confidence is moderate, subject to expert review.

## Files

- `solution_packet.pdf`: self-contained theorem and proof.
- `source_paper.pdf`: arXiv:2506.07487.
- `figures/open_problem_crop.png`: source page 35 question.
- `code/verify_construction.py`: finite-window sanity checker.
- `verification.md`: verifier-focused audit.

