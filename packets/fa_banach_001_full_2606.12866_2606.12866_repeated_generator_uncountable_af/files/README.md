# Repeated generators force continuum many rapidly growing AF algebras

## Status

`candidate_full_solution_likely_valid`

This packet gives an affirmative answer to Problem 8.2 of Aguilar--Garcia--Knight--Marple--Spielberg, arXiv:2606.12866.

## Result

Let \(\mathbf n=(n_1,\ldots,n_k)\) and \(\mathbf g=(g_r)\) satisfy the source paper's rapidly-growing hypotheses. If two entries of \(\mathbf n\) are equal, then the ensemble \(\mathcal E(\mathbf n,\mathbf g)\) contains \(2^{\aleph_0}\) pairwise non-isomorphic AF algebras.

After permuting coordinates, isolate the repeated pair. On those two coordinates use the source paper's symmetric matrices
\[
\begin{pmatrix}p_r&\gamma_r-p_r\\ \gamma_r-p_r&p_r\end{pmatrix},
\qquad q_r=2p_r-\gamma_r,
\]
with parity-safe choices of \(q_r\) encoding continuum many inequivalent generalized integers. On every other coordinate use the scalar block \(\gamma_r\). The resulting direct limit is
\[
B_S\oplus U_3\oplus\cdots\oplus U_k,
\]
where the \(B_S\) are pairwise non-isomorphic simple AF algebras and the \(U_j\) are fixed simple UHF algebras. An isomorphism of two such finite direct sums must permute their minimal nonzero ideals, and cancellation of the common finite multiset of UHF summands forces the corresponding \(B_S\)'s to be isomorphic, a contradiction.

## Verification report

- The block matrix satisfies \(X_r\mathbf n=\gamma_r\mathbf n\) at every level, so every constructed chain belongs to the original ensemble.
- The parity-safe prime encoding works for both even and odd \(\gamma_r\) and gives continuum many generalized integers modulo the source equivalence relation.
- All sufficiently late \(2\times2\) blocks are strictly positive, hence each variable summand \(B_S\) is simple.
- Source Proposition 7.6 distinguishes the \(K_0\)-groups after one possible cross-equivalence class is discarded.
- The ideal-lattice step uses only that the minimal nonzero ideals of a finite direct sum of simple algebras are its summands.
- No computational experiment is used as proof.

The construction also repairs a minor parity omission in the printed proof of source Theorem 7.1: choosing \(q_r\) prime does not by itself ensure \(q_r\equiv\gamma_r\pmod 2\). The packet's sparse encoding enforces this condition explicitly.

## Novelty check

On 2026-08-09, bounded searches of the run registry, solution/attempt/proof-gap indexes, the locally parsed arXiv corpus, and web searches for the exact title, Problem 8.2 wording, repeated generators, and uncountably many AF algebras found the source paper but no later solution or matching theorem. Because the source is recent, novelty confidence remains provisional.

## Files

- `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: readable crop of Problem 8.2 on source PDF page 31.

## Human-review recommendation

Promote after checking the invocation of source Proposition 7.6 and the minimal-ideal cancellation paragraph. The result appears to be a full solution of Problem 8.2, not of the broader Problem 8.1 for generating vectors with no repetitions.
