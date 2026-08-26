# Maximality conjecture for groups with a compact open subgroup

Status: `candidate partial result; likely valid; human review requested`

Source: Nico Spronk, *Operator space structure on Feichtinger's Segal algebra*, arXiv:math/0607299v2, conjecture on source p. 17.

## Result

Let `G` be a locally compact group that has a compact open subgroup. Then the canonical operator space structure on Feichtinger's Segal algebra `S_0(G)` is (completely isomorphic to) the maximal operator space structure if and only if `G` has an open abelian subgroup.

This proves the source conjecture for the full compact-open class, and therefore for every totally disconnected locally compact group. It also gives the hereditary obstruction: if `S_0(G)` is maximal, then every compact subgroup of `G` is virtually abelian.

## Mechanism

If `K` is compact open, source Theorem 3.3 makes restriction `S_0(G) -> S_0(K)` a complete surjection. Maximality passes to operator-space quotients, and source Corollary 2.5(ii) identifies `S_0(K)` with `A(K)`. Hence `A(K)` would be maximal. Combining the maximal tensor identity with source Theorem 3.1 gives

```text
A(K) tensor_gamma A(K) ~= A(K x K).
```

Losert's theorem forces `K` to have an open abelian subgroup, which is open in `G`. Conversely, if `G` also has an open abelian subgroup `A`, then `A intersect K` is compact, abelian, and open in `G`; the source already proves maximality in that situation.

## Files

- `main.tex`, `solution_packet.pdf`: formal theorem and proof.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: source conjecture and its stated known case.
- `verification.md`: proof dependency and artifact audit.

Human-review focus: confirm that source “complete surjection” identifies the target completely isomorphically with an operator quotient, and that the natural tensor maps in the maximal-space identity and Losert theorem agree. Both points are made explicit in the proof.
