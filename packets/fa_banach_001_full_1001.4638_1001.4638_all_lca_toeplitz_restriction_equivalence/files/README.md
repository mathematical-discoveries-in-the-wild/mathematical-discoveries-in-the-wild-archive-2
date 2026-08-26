# Full Solution Packet: The Toeplitz Restriction Theorem on All Second-Countable LCA Groups

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- V. S. Shulman, I. G. Todorov, and L. Turowska, “Closable Multipliers,”
  arXiv:1001.4638, published in *Integral Equations and Operator Theory* 69
  (2011), 29–62.
- Problem 2 is on page 33 of the source PDF and asks whether Theorem 7.5
  holds for all locally compact abelian groups.
- Section 7 has the standing assumption that the LCA group is second
  countable; this is also the standard-measure setting of the paper.
- Local source: `source_paper.pdf`.
- Evidence crops: `figures/open_problem_crop.png` and
  `figures/theorem_context_crop.png`.

## Claimed contribution

The packet proves Theorem 7.5 for every second-countable locally compact
abelian group. Thus Problem 2 has an affirmative answer in the source paper’s
standing category.

For a measurable `f : G -> C`, its Toeplitz multiplier `phi=Nf`, and arbitrary
measurable `U,V subset G`, the following are equivalent:

```text
(i)   (U x V) intersect E_f^* is marginally null;
(ii)  phi restricted to U x V is a local Schur multiplier;
(iii) phi restricted to U x V is weak-star closable.
```

The source proves this only for subgroups of Euclidean spaces or tori and
states that the group restriction enters solely through a Lebesgue
density-point argument in `(iii) => (i)`.

## New mechanism

A common nonnegative normalized `L^1(G)` approximate identity replaces
Euclidean density balls. After exhausting `U` and `V` by countably many
finite-measure pieces, one subsequence converges almost everywhere for every
indicator simultaneously. For any pair `(u,v)` in the resulting Cartesian
product of conull sets, two approximate-identity averages are both greater
than `1/2`. Their translated pieces must therefore overlap in positive Haar
measure, which gives

```text
P(1_{U_k} tensor 1_{V_l})(u-v) > 0.
```

This is exactly the nonvanishing assertion needed in the sole group-dependent
step of the source proof.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: page-33 crop of Problem 2.
- `figures/theorem_context_crop.png`: page-26 crop of Theorem 7.5.
- `verification.md`: proof-dependency and edge-case audit.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

Bounded searches on August 9, 2026 used arXiv and general web indexes with the
exact source title, theorem and problem labels, the phrases “w*-closable
multiplier” and “local Schur multiplier,” and close variants involving LCA
groups and approximate identities. They found the source and the authors’
later arXiv:1401.2620 on closable multipliers on group algebras. Inspection of
that later paper found different group-C*-algebra and group-von-Neumann-
algebra results, not the restricted-rectangle equivalence of Problem 2. No
later solution of this problem or this approximate-identity argument was
located. Novelty confidence is moderate pending a specialist citation search.

## Scope and human review focus

- The result covers the full standing category of Section 7: second-countable
  LCA groups. Non-second-countable groups lie outside the paper’s standard
  measure-space setup and are not claimed.
- Expert review should check the simultaneous almost-everywhere subsequence,
  the positive-overlap inequality, the orientation of the map `P`, and the
  source-proof audit that no other step uses Euclidean structure.

