# Partial packet: chordal-deletion and joined-obstruction bounds

- Source: M. Bakonyi and T. Constantinescu, *Research Problem: The Completion
  Number of a Graph*, arXiv:math/0312390.
- Extracted target: find a graph-theoretic characterization of graphs with a
  given completion number.
- Packet status: `partial_result_likely_valid`.
- Model: `GPT5.6`.

## Result

Let `cn(G)` be the source's completion number. Define:

- `cvd(G)`: the minimum number of vertices whose deletion makes `G` chordal;
- `j(G)`: the maximum number of pairwise completely joined, vertex-disjoint
  induced nonchordal subgraphs of `G`.

Then

```text
j(G) <= cn(G) <= cvd(G).
```

The upper bound completes the chordal principal block positively and restores
the deleted rows/columns, one possible negative eigenvalue per restored
vertex. The lower bound places independent non-PSD-completion obstructions on
the completely joined blocks and sets all specified cross-block entries to
zero, forcing an additive block-diagonal negative index in every completion.

Consequently, whenever `j(G)=cvd(G)`, the completion number is determined. In
particular, every nonchordal graph that becomes chordal after one vertex
deletion has completion number `1`. This generalizes the source's chordless-
cycle calculation. The joined-obstruction lower bound also recovers the sharp
lower bound for the source's joined-four-cycle examples.

## Scope

This is not a full classification. For example, the theorem only gives
`1 <= cn(K_{m,n}) <= min(m-1,n-1)` for `m,n >= 2`. The missing lower-bound
mechanism must handle nonchordal obstructions whose unspecified cross-block
entries can couple in a completion.

## Evidence and verification

- `source_paper.pdf` is the official arXiv PDF.
- `figures/open_problem_crop.png` shows the definition and research question
  on printed page 3.
- `main.tex` gives the theorem and proof.
- `code/check_graph_families.py` checks the one-vertex cycle class and records
  the join-of-two-cycles obstruction that invalidates a tempting stronger
  corollary.
- `verification.md` records the proof audit.
- `attempts/0312390_completion_number_full_upgrade.md` records eight upgrade
  attempts.

## Novelty check

The run indexes and local arXiv source corpus had no exact duplicate or later
use of this invariant. An OpenAlex exact-record query on 2026-08-11 reported
zero citations to the source. Exact web searches were noisy because
“completion number” also names unrelated Hamiltonian and line-graph
invariants; no direct later answer was found. Novelty confidence is moderate.

## Human review focus

Check the extension of the component obstruction matrices to a partial
positive matrix on all of `G`, and the use of a fully specified zero cross
block to make negative inertia additive.
