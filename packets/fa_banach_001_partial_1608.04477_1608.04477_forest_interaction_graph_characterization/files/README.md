# Fixed-cost compatibility, balanced binary costs, and the forest boundary

Status: partial_result_likely_valid_strengthened (human review requested)

Source question: S. Bartz, H. H. Bauschke, and X. Wang, *A class of multi-marginal c-cyclically monotone sets with explicit c-splitting potentials*, arXiv:1608.04477, p. 12. The paper asks for which pair-sum costs global multi-marginal cyclical monotonicity forces cyclical monotonicity of every two-marginal projection.

New strengthened results:

1. **Exact fixed-cost equivalence.** A fixed family of pair costs has the projection property for every set Gamma if and only if, for every family of finitely supported one-marginals, there is one joint coupling whose marginal on every edge is pairwise optimal. A finite rationalization lemma proves the equivalence without assuming a false multi-marginal Birkhoff theorem.

2. **Complete binary classification.** For Xi={0,1}, define the cross difference

   Delta_e = c_e(0,0)+c_e(1,1)-c_e(0,1)-c_e(1,0).

   Ignore edges with Delta_e=0 and sign every remaining edge by sign(Delta_e). The projection property holds for every Gamma if and only if this signed graph is balanced—equivalently, every cycle has positive sign product, or vertexwise 0/1 relabelings make all cross differences positive. If it is unbalanced, a two-point complementary set Gamma={a,1-a} is a counterexample.

3. **Consistent-supermodularity sufficient class.** If node orders can be chosen so every pair cost is supermodular, a common quantile coupling is simultaneously optimal on all edges; hence the projection property holds.

4. **Costs-independent graph boundary.** Uniformly over arbitrary marginal sets and arbitrary edge costs, the projection property holds exactly when the interaction graph is a forest. The forest proof isolates an edge by componentwise permutations. Every cyclic graph has a binary two-point cut-weight counterexample.

Scope: The fixed-cost compatibility theorem is an exact reformulation, and the binary theorem is a full intrinsic resolution for two-point spaces. The packet does not yet give an intrinsic normal-form classification for arbitrary finite or infinite pair costs, nor does it solve the source paper's second set-by-set classification question.

Novelty bound: Bounded exact and close-variant searches through 2026-08-09 found adjacent work on tree-structured optimal transport, extremal dependence, pairwise countermonotonicity, and balanced signed graphs, but no statement of the fixed-cost cyclical-monotonicity equivalence or binary iff-balance theorem. Novelty confidence is moderate pending expert review.

Files:

- main.tex / solution_packet.pdf: full statements and proofs.
- code/verify_binary_n3.py: exhaustive LP sanity check for all triangle sign patterns and all subsets of the three-bit cube.
- source_paper.pdf: original arXiv paper.
- figures/open_problem_crop.png: source question on p. 12.
