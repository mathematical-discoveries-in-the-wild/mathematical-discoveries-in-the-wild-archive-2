# Relative Schur weak--strong classification

Status: `candidate_strong_partial_likely_valid`

Source: Karsten Kruse, *Extension of vector-valued functions and weak-strong
principles for differentiable functions of finite order*, arXiv:1910.01952,
Question 6.9(i), printed page 21.

## Result

Let `E` be a Banach space and let `G subset E*` determine boundedness. For
every fixed integer `k >= 1`, the following are equivalent:

1. every bounded `sigma(E,G)`-null sequence is norm null;
2. every `E`-valued map on an open subset of any Banach domain whose
   `G`-scalarizations are `C^k` is itself `C^k`;
3. the same implication holds just for real-variable curves.

Failure is witnessed by a smooth disjoint-bump construction at an
accumulation point. The same relative Schur condition therefore classifies
all positive finite orders.

For `G=E*`, this reduces to the ordinary Schur property. That special case is
already in Bachir--Lancien (2003), so it is not claimed as new. The candidate
advance is the exact arbitrary-`G` pair classification matching the source
theorem.

The distinction is sharp:

- `(ell_1, ell_infinity)` satisfies the principle, giving an
  infinite-dimensional non-semi-Montel affirmative example in the full-dual
  Banach setting;
- `(ell_1, c_0)` fails it, although `c_0` determines boundedness of `ell_1`.

Thus the property genuinely depends on `(E,G)`.

## Files

- `main.tex`: self-contained theorem, proof, bump converse, scope, and
  novelty audit.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv source paper.
- `supporting_bachir_lancien_2003.pdf`: closest primary literature result.
- `figures/open_problem_crop.png`: source Question 6.9.
- `verification.md`: proof and render audit.
- `tmp/`: compilation and page-render intermediates.

## Scope

This is complete for each Banach pair `(E,G)` but remains a partial answer to
the source: it does not classify general locally convex targets, determine
which Banach spaces work for every admissible `G`, or address Questions
6.9(ii)--(iv).
