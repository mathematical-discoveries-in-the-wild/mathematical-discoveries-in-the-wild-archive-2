# Sharp Rider gap for split compact metabelian groups

Status: `candidate_partial_solution_likely_valid`

Model: `GPT5.6`

Agent: `agent_lane_02`

Source target: arXiv:1110.6683, Theorem 2.3 and Remark 2.4, physical PDF page 4.

## Result

For every compact semidirect product `G = A ⋊ H` with `A` and `H` compact
abelian, every finite-spectrum central convolution idempotent has `L1` norm

```text
0, 1, or at least (1 + sqrt(2))/2.
```

The constant is sharp already for the nonabelian dihedral group `D_16`.

The proof gives an exact, norm-preserving transference. Each little-group
irreducible of `A ⋊ H` determines a finite rectangle in the character group of
the abelian direct product `A × H`; these rectangles partition the abelian
dual. A sum of minimal central idempotents therefore becomes, pointwise, an
abelian idempotent trigonometric polynomial. Saeki's sharp abelian theorem
then applies.

## Scope

This is a substantial partial answer, not a solution of the source problem
for arbitrary compact groups. The splitting and abelian complement are used
in the character-rectangle identity.

## Review files

- `solution_packet.pdf`: full statement and proof
- `source_paper.pdf`: exact arXiv source compiled from the stored v4 source
- `figures/open_problem_crop.png`: real rendered crop of source PDF page 4
- `code/verifier.py`: finite sanity checks and the exact sharpness example
- `VERIFIER_REPORT.md`: verification scope, result, and reviewer priorities

## Build

From this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

## Verification

From the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1110.6683_sharp_rider_gap_split_metabelian/code/verifier.py
```

Human review should focus on the little-group completeness argument and the
restriction-fiber character sum. Once those are checked, the transference and
Saeki reduction are exact.
