# Verification

## Mathematical checks

- Every admissible seminorm has null space exactly `V_0`, so quotient reduction
  is a lattice isomorphism.
- The reverse pointwise order on seminorms becomes forward inclusion of unit
  balls; meet is intersection and join is closed convex hull of the union.
- The constructed bodies contain `rU` and lie in `U`, hence their gauges obey
  `p <= q <= r^{-1}p < epsilon^{-1}p` for every chosen `epsilon < r`.
- Hahn--Banach gives a norming functional; a nonzero kernel direction exists
  exactly when dimension is at least two.
- The cap-localization estimate is quantitative and survives closure, removing
  finite-dimensional compactness assumptions.
- The cap sets `{z_3}` and `[z_0,z_2]` have exact distance `h`; the uniform cap
  gap makes the left modular expression meet the exposed hyperplane only at
  `z_0`.
- The right modular expression meets the same hyperplane in `[z_0,z_2]`, so
  `z_1` is an explicit witness of inequality.
- In dimension zero the lattice is a singleton; in dimension one it is a chain
  of scalar multiples of the reference norm.

## Literature checks

Bounded searches used the exact conjectural phrase, the paper title,
`normal subobject lattice`, `seminorm lattice modular`, and the quotient
dimension condition. They found the source and adjacent lattice literature but
no later resolution or matching proof. Novelty confidence is moderate and
human/author review is required.

## Artifact checks

- Exact arXiv TeX source compiled locally to a 25-page source PDF.
- Solution-packet compilation: passed with `latexmk`; four-page PDF produced.
- Page rendering: passed with Ghostscript `png16m` at 144 dpi.
- Visual inspection: all four rendered pages inspected; the source footnote,
  theorem, proof, and references are legible with no clipping or overlap.
- Human mathematical review: pending.

SHA-256:

- `source_paper.pdf`:
  `39685241f1b24ddb03bc0b6a514b3fc498410f07aa4ac67d2d2720cf7102cbc8`
- `figures/open_problem_crop.png`:
  `b99459b216bcf07d4fba3d889ecbd03c4904059501e2d5f3abe1fe04b2158374`
- `solution_packet.pdf`:
  `1919d2b815c256ef382dd4f1c8e4d4b43f7910fabc7c39c8aeb80d1a906bfa43`
