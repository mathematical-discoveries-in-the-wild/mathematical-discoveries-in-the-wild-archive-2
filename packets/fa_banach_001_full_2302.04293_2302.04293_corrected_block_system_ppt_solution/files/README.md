# Full correction packet: block-system principal pivot solution

## Source

- Kenneth Beard and Aaron Welters, *Matrix monotonicity and concavity of the
  principal pivot transform*, arXiv:2302.04293v2.
- Target: Problem 7 and its claimed solution, Proposition 8, on page 6.
- Model: GPT5.6.

## Classification

- Status: `full_solution_with_source_correction_likely_valid`.
- Scope: complete solution of Problem 7 for arbitrary block matrices, plus a
  counterexample to Proposition 8 as written and its sharp repair.

## Result

For fixed `x1,y2`, put `b=y2-A21*x1` and `P=A22*A22^+`. Solutions exist if
and only if `(I-P)b=0`, equivalently `b` belongs to the range of `A22`. When
this holds, every solution is

```text
x2 = A22^+ b + z,
y1 = A11 x1 + A12 A22^+ b + A12 z,   z in ker(A22).
```

The source proposition omits the compatibility condition. Its hypotheses
hold for the zero `2 x 2` matrix, but with `x1=0,y2=1` its displayed formula
claims solutions even though the block system has none.

Under the source's range/kernel hypotheses, the repair is especially simple:
one must add `y2 in ran(A22)`. If this fails, the principal pivot transform
solves the system with `y2` replaced by its orthogonal projection
`A22*A22^+ y2`.

## Idea of Proof

The second block row is the single Moore--Penrose equation
`A22*x2=b`. Its range criterion and complete affine solution are standard
and immediate from the two orthogonal projections defined by the
pseudoinverse. Substitution into the first block row determines every
corresponding `y1`. This also exposes the exact step lost in the source proof:
applying `A22^+` is reversible only after imposing range compatibility.

## Files

- `main.tex`: self-contained corrected theorem and proof.
- `solution_packet.pdf`: compiled and visually inspected packet.
- `source_paper.pdf`: current arXiv v2 source paper.
- `figures/problem_and_claimed_solution_crop.png`: exact page-6 excerpt.
- `code/verify_block_solution.py`: deterministic finite-matrix checks.
- `code/crop_source.py`: source-crop helper.
- `verification_report.md`: audit record.
- `novelty.md`: bounded correction search.

