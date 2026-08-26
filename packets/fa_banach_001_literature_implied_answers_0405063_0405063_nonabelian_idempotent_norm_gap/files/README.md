# Nonabelian idempotent norm gap (arXiv:math/0405063)

Status: `literature_implied_answer (full question)`.

## Question

Ilie and Spronk, *Completely bounded homomorphisms of the Fourier algebras*,
arXiv:math/0405063, note immediately after Theorem 2.1 (journal page 488;
PDF page 9) that for an abelian locally compact group every nonzero idempotent
`u` in `B(G)` has either

\[
\|u\|_{B(G)}=1
\quad\text{or}\quad
\|u\|_{B(G)}\geq \frac{1+\sqrt2}{2},
\]

and ask whether a similar result holds for nonabelian groups.

## Identification

Mudge and Pham, *Idempotents with small norms*, arXiv:1510.03535,
Theorem 2.2 (PDF page 3), prove for every locally compact group `G` that a
nonzero idempotent `u = 1_S` in `M_cb A(G)` with

\[
\|u\|_{cb}<\frac{1+\sqrt2}{2}
\]

has `S` equal to an open coset. Their introduction (PDF page 2) also records
the contractive inclusion

\[
B(G)\subseteq M_{cb}A(G),\qquad \|u\|_{cb}\leq\|u\|_{B(G)}.
\]

Hence an idempotent in `B(G)` of norm below the threshold is an open-coset
indicator and therefore has `B(G)`-norm exactly one. This proves the requested
nonabelian dichotomy. Since abelian groups are included, the constant remains
sharp for the class of all locally compact groups.

This is an agent-identified implication of the later theorem, not a new proof.
Mudge and Pham cite Ilie--Spronk for the norm-one characterization, but do not
label their Theorem 2.2 as an answer to the exact sentence on journal page 488.

## Files

- `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: Ilie--Spronk source paper.
- `supporting_paper_1510.03535.pdf`: decisive Mudge--Pham paper.
- Ledger: `runs/fa_banach_001/ledger/results/0405063_nonabelian_idempotent_norm_gap.json`.

