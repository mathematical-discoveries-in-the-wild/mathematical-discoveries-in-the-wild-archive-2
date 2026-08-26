# Bounded nilpotency step forces non-degeneracy

**Status:** candidate full solution, likely valid; human review needed.

**Source:** Terhi Moisala and Enrico Pasqualetto, *Direct limits of infinite-dimensional Carnot groups*, arXiv:2101.03979, Problem P3 on source PDF page 3 (published in *Mathematica Scandinavica* 128 (2022), 160--200).

The packet gives an affirmative answer to P3. For every nilpotency bound `s`, it proves a conjugation estimate uniform over the dimension, group law, and homogeneous left-invariant metric:

`N(g^{-1} h g) <= C_s (1+N(g))^s N(h)^(1/s)` when `N(h)<=1`.

The proof uses a bounded nilpotent collection lemma for homogeneous layers and optimized asymmetric dilation of commutators. Because the constant depends only on `s`, the estimate survives the varying groups and metrics of an arbitrary direct system. It yields continuity of every right translation for the infimum pseudometric. The source paper's bounded-class and generating-first-layer lemmas then give Cauchy-continuity of inversion and dilation continuity, hence full CMSG non-degeneracy.

Consequently every bounded-step direct system in P3 is non-degenerate. Its CMSG direct limit exists; for a countable system the limit is again an infinite-dimensional Carnot group by the source theorem.

## Contents

- `solution_packet.pdf`: expert-facing theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: P3 on source PDF page 3.
- `tmp/`: LaTeX and visual-QA intermediates.

## Verification and novelty

Eight focused attempts checked counterexample routes, the uniform layer/commutator mechanism, classes two and three, infinite-dimensional filtration passage, noninjective bonding maps, and the source's conditions (C1)--(C3). Exact-title, arXiv-id, quoted-P3, bounded-step, and non-degeneracy searches through 12 August 2026 found no later answer. Standard literature has the same `1/s` conjugation exponent for a fixed Carnot group, but with a constant depending on that group and metric; the uniformity needed here was not located.

## Human-review recommendation

First verify the bounded-word homogeneous-layer collection lemma and its claim that the constant depends only on the nilpotency class. Then check the one-line infimum-pseudometric passage, especially the replacement of a near-minimizing pair by `a^{-1}b`. Those are the only non-source ingredients carrying the full conclusion.
