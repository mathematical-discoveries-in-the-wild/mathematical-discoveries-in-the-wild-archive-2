# Verification Report

## Verdict

`literature_implied_answer (partial subcase), exact and likely valid`

## Mathematical audit

| Component | Verdict | Check |
| --- | --- | --- |
| Karlin--Rinott criterion | source-verified | Royen arXiv:2410.04143, PDF page 2, explicitly states that `|Z|` is MTP2 iff a diagonal sign matrix makes `Sigma^{-1}` an M-matrix, citing Karlin--Rinott (1981). |
| Cdf closure | valid | Lower-orthant indicator kernels are MTP2; products and marginalization preserve MTP2. |
| Stronger max/min inequality | valid | This is exactly the lattice inequality for the MTP2 cdf `F`. |
| Passage to sum/min | valid | `s+t >= s join t` and `F` is coordinatewise increasing. |
| Geometric parallelotope identity | valid | Bijectivity of `A` gives `P_A(s)+P_A(t)=P_A(s+t)` and intersection equals `P_A(s meet t)`. |
| Two-dimensional automatic condition | valid | A sign flip changes the sign of the unique off-diagonal precision entry; positive definiteness is preserved. |

## Provenance and scope audit

- The source target is arXiv:2407.15684, Conjectures 2 and 4 on PDF page 2.
- Cheap run indexes contained no exact prior packet for this paper or conjecture.
- Bounded OpenAlex/arXiv searches found no later exact resolution of the full conjecture.
- Karlin--Rinott's MTP2 theorem is old literature; Royen arXiv:2410.04143 supplies a directly inspectable modern restatement and does not mention Tehranchi's conjecture.
- The implication is therefore agent-identified and classified under `literature_implied_answers`, not as a new partial theorem.
- The full sign-frustrated/non-lattice case remains open in this investigation.

## Computational audit

The scripts are stored under
`runs/fa_banach_001/attempts/evidence/2407.15684_strong_gci/`.

- `search_2d.py`: exact polygon intersections/Minkowski hulls plus deterministic polar Gaussian quadrature. Rotated rectangle and diamond optimizations reached only equality to about `2e-13`; 20,000 random polygon pairs found no negative gap.
- `search_boxes.py`: bivariate optimization and random 3/4-variable box searches. The sum/min conjecture had no robust negative gap. The stronger max/min inequality failed in dimension 3 with estimated ratio `0.9554169`, confirming the MTP2 route cannot be global.
- `search_3d_polytopes.py`: 800 random centrally symmetric 3-polytopes on a common 65,536-point Sobol Gaussian sample; minimum observed ratio `1.09225`.

These computations are stress tests only and are not used in the proof.

## PDF QA

- `solution_packet.pdf` compiled to five US-letter pages with no LaTeX warnings, undefined references, or overfull/underfull boxes.
- All five final pages were rendered at 150 dpi and visually inspected. The theorem statements, formulas, full-page source evidence, captions, margins, references, and page numbers are legible and unclipped.
- SHA-256: `a01d5ad738047be69b22e73efc230f4799a2a7e7c608071c4935904283b61c10`.
