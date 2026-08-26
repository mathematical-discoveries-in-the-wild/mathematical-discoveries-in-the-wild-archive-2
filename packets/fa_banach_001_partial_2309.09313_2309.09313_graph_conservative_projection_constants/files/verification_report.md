# Verification report

## Mathematical checks

The proof was checked by two complementary methods.

1. Exact rational arithmetic constructs every displayed candidate
   projection and verifies idempotence, the conservative range condition,
   and the claimed `ell_infinity` row norm.
2. Independent linear programs optimize over *all* projections, rather
   than over the displayed candidates. For a cycle this optimizes all
   rank-one-defect projections. For complete and complete bipartite graphs
   it optimizes all left inverses of a gradient basis.

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2309.09313_graph_conservative_projection_constants/code/verify_projection_constants.py
```

Output:

```text
verification passed
exact rational assertions: 190
independent LP optimum assertions: 46
weighted-cycle instances: 36
complete-graph exact instances: 7 (n=2,...,8)
complete-graph independent LP instances: 4 (n=2,...,5)
complete-bipartite exact instances: 7
complete-bipartite independent LP instances: 6
```

The exact cases include the geodesic weighted-cycle endpoint where one edge
has half the perimeter. The block tests combine cycle, clique, and biclique
projection matrices and verify that both idempotence and the maximum-block
norm survive direct summation.

## Proof audit

- Extension norm equals relative projection norm because gradient and
  integration are inverse isometries between `Lip_0` and `CVF`.
- Every projection onto the weighted-cycle hyperplane has the form
  `I-u tensor phi`; the row-norm optimization includes real and complex
  choices of `u`.
- The complete-graph lower bound uses averaging over all vertex
  permutations and an elementary uniqueness classification of equivariant
  potential maps.
- The biclique lower bound uses averaging over row/column permutations and
  the direct decomposition into additive matrices plus zero-row/zero-column
  matrices.
- Block gluing is exact because edges partition by blocks and every cycle
  belongs to one block.

## PDF QA

The source main.tex compiled with latexmk to a five-page A4 PDF with no TeX
warnings, undefined references, overfull boxes, or underfull boxes. All five
pages were rendered at 150 dpi and visually inspected. The title, status
box, source-question image, formulas, page breaks, and bibliography are
fully visible with no clipping or overlap.

Final SHA-256:

    029ca723791734e4ff40c3ae6da2a5c0980a0753d758adb2c05ca0939df750ea
