# Rank-one counterexamples to the graphon Perron converse

**Status:** candidate counterexample to the literal open problem, with a full
rank-one characterization; likely valid, pending human review.

**Source:** Benoit Bonnet, Nastassia Pouradier Duteil, and Mario Sigalotti,
*Consensus Formation in First-Order Graphon Models with Time-Varying
Topologies*, arXiv:2111.03900, open problem on printed page 25 (after Theorem
4.7 in the arXiv PDF).

## Result

On `I=[0,1]`, take the symmetric graphon

\[
a(i,j)=ij.
\]

Its degree is `d(i)=i/2`, and symmetry gives
`L^*1=L1=d-A1=0`. Thus `v=1` is a bounded, strictly positive adjoint-null
weight. Nevertheless, the topology is not a disjoint union of strongly
connected components in the sense of Definition 4.5. Every nonzero row has
full support, so any admissible closed component of positive measure must be
all of `I`; the single component then fails Definition 4.5(b) because
`inf d=0`.

More generally, for a full-support rank-one kernel
`a(i,j)=p(i)q(j)`, all positive adjoint-null weights are proportional to
`q/p`, while Definition 4.5 connectivity is equivalent to `ess inf p>0`.
This gives a complete characterization of the converse within the full-support
rank-one class.

## Scope caveat

The counterexample refutes the conclusion exactly as defined in Definition
4.5, where a uniform positive degree bound is part of “strongly connected.” It
does not refute the weaker conclusion obtained by retaining only qualitative
mutual reachability: `a(i,j)=ij` is qualitatively one component. If that weaker
notion was intended in the open problem, the result identifies a precise
statement correction rather than settling the intended question.

The source paper itself later gives a different symmetric graphon with
vanishing degree infimum in Section 5.4. Since every symmetric graphon has
`L^*1=0`, the obstruction is therefore latent in the source paper, although the
authors do not connect that example to the open problem. Priority for the bare
negative answer is correspondingly low; the durable contribution of this
packet is the explicit minimal example and the rank-one characterization.

## Packet contents

- `solution_packet.pdf` / `main.tex`: statement, proof, scope analysis,
  verification notes, and novelty bounds.
- `source_paper.pdf`: arXiv:2111.03900.
- `figures/open_problem_crop.png`: full-width source crop of the open problem.

## Verification and review focus

The proof is non-computational. Human review should focus on the interpretation
of “support” and `inf` in Definition 4.5 and on whether the open problem was
intended to retain its quantitative condition (b). For the continuous example
`a(i,j)=ij`, literal and essential infima agree, and each row with `i>0` has
topological and essential support equal to all of `I`.

## Novelty search

A bounded local-index, arXiv, and web search on 2026-08-09 used arXiv id
`2111.03900`, the exact open-problem phrase, the paper title with `Perron`, and
the terms `graphon positive stationary distribution strong connected
components`. It found the source and later papers citing it, but no separate
paper explicitly resolving this converse. The same-paper Section 5.4 example
substantially lowers originality confidence as explained above.

Ledger: `runs/fa_banach_001/ledger/results/2111.03900_graphon_perron_converse_rank_one_counterexample.json`.
