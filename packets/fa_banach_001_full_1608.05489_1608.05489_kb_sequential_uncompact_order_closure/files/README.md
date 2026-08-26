# KB-Spaces and Monotone Stability of Sequentially Un-Compact Operators

Result type: `full`

Status: candidate full solution, likely valid pending human review.

Source paper:

- M. Kandić, M. A. A. Marabeh, and V. G. Troitsky, “Unbounded Norm
  Topology in Banach Lattices,” arXiv:1608.05489; published in
  *Journal of Mathematical Analysis and Applications* 451 (2017), 259–279.
- Local source PDF: `source_paper.pdf`.
- Open-question evidence: `figures/open_problem_crop.png`, page 30,
  Proposition 9.6 and the sentence immediately following it.

## Claimed contribution

The source proves that the following monotone-stability property forces a
Banach lattice `X` to be a KB-space: whenever sequentially un-compact
operators `T_n:c0 -> X` satisfy `T_n ↑ T`, the limit `T` is sequentially
un-compact. It then asks whether the converse holds.

This packet proves the converse and therefore obtains an exact
characterization. The key lemma is elementary but decisive: every positive
operator `S:c0 -> X` into a KB-space is compact. Indeed, the bounded increasing
partial sums `sum_{k<=N} S e_k` converge in norm, and their norm tails uniformly
control `S(I-P_N)` on the unit ball of `c0`. If `T_n ↑ T`, then `T-T_1` is
positive and hence compact, so `T=T_1+(T-T_1)` is sequentially un-compact.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: readable full-width crop of the source
  proposition and open-converse sentence.
- `verification.md`: independent line-by-line proof audit and novelty-search
  bounds.
- `tmp/`: LaTeX build and page-render intermediates.

## Novelty check

The bounded search was completed on 2026-08-09. It included the run’s four
cheap indexes; exact web searches for the question’s wording and the terms
`sequentially un-compact`, `order closed`, `c0`, and `KB-space`; and a local
full-text scan of all 43 ingested arXiv source papers that cite the exact title
of arXiv:1608.05489 (through the 2026 corpus). The search did find later
answers to two different questions in the source paper—arXiv:2304.04189 for
norm-closedness of un-compact operators and arXiv:2404.15641 for the band
lifting question—but no paper stating or proving the converse treated here.
Novelty confidence is moderate rather than definitive because the argument is
short and non-arXiv literature was not exhaustively citation-indexed.

## Human review focus

The central check is the tail estimate
`||S(I-P_N)|| <= ||s-s_N||` for a positive `S:c0 -> X`. The packet proves it
first for finitely supported vectors and then passes to arbitrary vectors by
norm density and closedness of the positive cone. No order completeness of
`X` and no unjustified infinite sum inside `c0` is used.
