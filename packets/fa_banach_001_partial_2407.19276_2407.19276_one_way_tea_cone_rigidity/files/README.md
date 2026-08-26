# One-way TEA preservers are scalar isometries

Status: `candidate_partial_likely_valid_full_TEA_branch`.

Source: Chi-Kwong Li, Ming-Cheng Tsai, Ya-Shu Wang, and Ngai-Ching
Wong, *Linear maps preserving ell_p-norm parallel vectors*,
arXiv:2407.19276, Problem 3.7 on page 15. The expanded final manuscript
retains the question as Problem 3.10.

## Result

Let `Lambda` be infinite and let `X` be either `c_0(Lambda)` or
`ell_infinity(Lambda)`, over the real or complex field. If a nonzero linear
map `T:X -> X` satisfies

```text
x,y form a TEA pair  =>  Tx,Ty form a TEA pair,
```

then there is a scalar `gamma>0` such that

```text
||Tx||_infinity = gamma ||x||_infinity   for every x in X.
```

Thus `T/gamma` is an isometric embedding and `T` is automatically bounded.
If `T` is bijective, it is a scalar multiple of a surjective isometry. This
fully answers the one-way TEA branch of the source problem, without assuming
boundedness or surjectivity.

The combined source problem also asks about parallel pairs. Its literal
`c_0` formulation is false because every nonzero rank-one map has parallel
range. The bijective/rank-greater-than-one parallel branch is not resolved in
this packet, so the durable result type is `partial`.

## Proof mechanism

A kernel lemma first shows that every nonzero TEA preserver is injective.
Pull back the target norm by setting `q(x)=||Tx||_infinity`. Then `q` is an
algebraic norm satisfying equality on every sup-norm TEA pair.

For each norming coordinate (in `c_0`) or norming point (in `C(beta Lambda)`),
the functions whose norm is attained there with positive real value form a
cone. The norm `q` is additive on this cone, so it extends to a real-linear
functional on the cone's real span. Comparing two cone extensions with phase
`1` and phase `-1` annihilates every tail functional. A third point forces
the extension to be a multiple of evaluation, and the multiplier is common
to all points. Hence `q=gamma||.||_infinity`.

All decompositions are exact. No finite-support approximation or continuity
of `T` is used.

## Packet contents

- `solution_packet.pdf`: five-page human-facing proof packet, visually checked.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: the exact Problem 3.7 passage.
- `verification_report.md`: proof and rendering audit.

The bounded novelty search through 2026-08-13 covered the final 2026 JMAA
manuscript, exact problem phrases, title/arXiv searches, author pages, the run
indexes, and close 2025--26 preserver papers. The final manuscript still
states the question, and no searched source contains this theorem. Novelty
confidence is moderate pending specialist review; mathematical confidence is
high.

Human review should focus on the real-linear extension of the cone-additive
norm and the two-point phase comparison. These are the only structurally new
steps.
