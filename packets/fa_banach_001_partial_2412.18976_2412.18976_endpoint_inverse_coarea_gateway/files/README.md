# Critical radial-coarea gateway for generalized inverses

Result type: `partial`

Status: candidate substantial reduction, likely valid pending specialist
review. The full `p=n-1` conjecture remains open.

Source paper:

- A. Doležalová, S. Hencl, and J. Onninen, “$(INV)$ condition and regularity
  of the inverse,” arXiv:2412.18976.
- Open-question location: Theorem 1.2 and the paragraph immediately following
  it, source PDF page 3.
- `source_paper.pdf` is reconstructed from the cached October 23, 2025 arXiv
  source.
- `figures/open_problem_crop.png` is the exact source crop.

## Claimed contribution

The packet proves a critical radial-coarea gateway theorem.  Let
`m=n-1`.  If an endpoint generalized inverse has the three structural
properties used implicitly by the topological part of the supercritical
argument—multiplicity one on `{J_f>0}`, projection-linking for inverse images
of target segments, and the critical radial coarea inequality—then

`int_B |h-h_B| <= C r int_{f^{-1}(B)} |adj Df| = C r int_B g`

for an `L^1` density `g`.  The `1`-Poincare characterization gives
`h in W^{1,1}_loc`, and its weak derivative is zero off the good image and
equals `(Df)^{-1}` on it.  Thus `h` has finite distortion.

This replaces the source's false-at-the-endpoint Morrey diameter estimate by
the Csörnyei--Hencl--Malý coarea mechanism.  It also identifies the sharp
remaining obstruction: critical surface Lusin `(N)` and the resulting
topological linking/selection facts.  A second proposition proves the full
endpoint conclusion for every radial cavitation or collapsed-core map of
finite distortion.

## Files

- `main.tex`: statements, proofs, exact source context, and limitations.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source reconstruction.
- `figures/open_problem_crop.png`: exact crop of the theorem and conjecture.
- `verification.md`: proof audit and review checklist.
- `tmp/`: build and visual-QA files.

## Scope

The packet does **not** prove that an arbitrary endpoint finite-distortion
`(INV)` map automatically satisfies strong `(INV+)`, projection-linking, or
critical radial coarea.  Critical Sobolev surface maps can fail Lusin `(N)`,
and the source's proofs of all three structural facts use the missing
supercritical surface control.  No priority claim is made; expert review is
recommended.
