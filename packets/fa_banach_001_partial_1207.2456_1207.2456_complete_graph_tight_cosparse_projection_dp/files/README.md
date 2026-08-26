# Exact Cosparse Projection for a Complete-Graph Tight Frame

Status: `candidate partial result - likely valid pending human review`

Source: Raja Giryes, Sangnam Nam, Michael Elad, Rémi Gribonval, and Mike E. Davies, *Greedy-Like Algorithms for the Cosparse Analysis Model*, arXiv:1207.2456.

## Source question

On PDF page 26, the source asks for which structured analysis operators an efficient optimal or near-optimal cosupport-selection procedure exists, and singles out tight-frame analysis operators for special attention. The exact source crop is in `figures/open_problem_crop.png`.

## Candidate result

Let `B` be an oriented edge-vertex incidence matrix of the complete graph `K_n`. For every input vector `z` and every target cosparsity, the nearest vector having that many zero entries in `Bx` can be computed exactly in polynomial time. After sorting `z`, equality classes may be taken as consecutive blocks. A dynamic program tracks the prefix length and the number of equal pairs contributed by each block.

The result upgrades to a full-rank redundant tight-frame operator:

`Omega = [B; 1^T]`, with `Omega^T Omega = n I`. Thus
`n^(-1/2) Omega` is Parseval, and the common nonzero scaling changes neither
the zero pattern nor any cosupport subspace.

If `F_l(z)` is the squared projection error for `B`, then the exact squared error for `Omega` is

`G_l(z) = min(F_l(z), F_{l-1}(z) + n * mean(z)^2)`

for `l>=1`. The second branch enforces the appended zero-sum coefficient by subtracting the global mean after the block projection. Thus the near-optimality constant is exactly `C_l=1` for every target level.

Disjoint unions of cliques are handled by local tables and a knapsack convolution over the zero-count budget. Componentwise DC completion gives a blockwise tight family; nonzero block scaling can normalize it to a global tight frame without changing cosupports.

## Why this addresses the paper

The source's greedy recovery theorems assume access to optimal or near-optimal projection oracles. For the complete-graph tight operator above, the dynamic program supplies those oracles exactly and efficiently at every cosparsity level. Consequently, the source's conditional AIHT/AHTP/ACoSaMP/ASP guarantees become implementable for this operator, subject to the same measurement-matrix and Omega-RIP hypotheses. This is a structured tight-frame subcase, not a general tight-frame theorem.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1207.2456_complete_graph_tight_cosparse_projection_dp/code/verify_complete_graph_projection.py
```

The verifier uses exact rational arithmetic and compares both algorithms with exhaustive enumeration of all set partitions. It checked every vector in `{-1,0,1}^n` for `1<=n<=6`, plus 80 deterministic random vectors in dimensions 7 and 8, at every admissible cosparsity: 1,172 vector instances and 35,318 optimum/projection comparisons, with no failure.

## Literature and novelty bounds

- Cheap run indexes were searched for `1207.2456`, `cosparse projection`, `complete graph`, `incidence`, `tight frame`, and related combinations; no duplicate packet was found.
- arXiv:1303.5305 proves strong NP-hardness for arbitrary operators and excludes an FPTAS unless `P=NP`, but explicitly leaves broader approximation algorithms and structured tractable cases open.
- Bounded arXiv/web searches through 2026-08-13 for complete-graph incidence, graph cosparsity, tight-frame cosparse projection, and dynamic-programming variants found graph-cosparsity background but no statement of this complete-graph/tight-completion dynamic program.

Novelty confidence is moderate, not definitive. The mathematical claim is self-contained and does not rely on novelty.

## Limitations and review focus

- This does not give a constant-factor approximation for arbitrary analysis operators.
- It does not prove new Omega-RIP inequalities; it discharges the projection-oracle assumption for a structured tight frame.
- The arithmetic-operation bound is polynomial; an implementation intended for large `n` would need state pruning and numerical engineering.
- Human review should focus on the fixed-block-size Monge uncrossing lemma and the union formula for the appended DC row.

Files:

- `main.tex`, `solution_packet.pdf`: formal packet.
- `source_paper.pdf`: arXiv:1207.2456.
- `supporting_paper_1303.5305.pdf`: general NP-hardness and approximation-status source.
- `code/verify_complete_graph_projection.py`: exact verifier and reference implementation.
