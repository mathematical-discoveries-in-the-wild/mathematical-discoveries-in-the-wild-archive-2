# Verifier report

Verdict: `candidate_partial_solution_likely_valid`

Model: `GPT5.6`

Date: 2026-08-11

## What was checked

The proof was audited in four layers.

1. The little-group character formula was derived directly from restriction
   to the compact abelian normal subgroup and finite-index induction.
2. Pontryagin-dual restriction fibers were checked to have the same cardinality
   as the representation degree, giving the exact rectangle identity.
3. The rectangle identity and partition property were checked numerically for
   all cyclic actions `C_m -> Aut(C_n)` with `2 <= n <= 14`, `2 <= m <= 6`.
   The final run covered 147 actions and 3,160 little-group blocks.
4. The sharp nonabelian example on `D_16` was checked symbolically, and every
   central idempotent of `D_{2n}` was exhaustively enumerated for `3 <= n <= 30`.

## Command

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1110.6683_sharp_rider_gap_split_metabelian/code/verifier.py
```

Expected final line:

```text
PASS: all packet sanity checks completed.
```

## Proof versus computation

The computations are sanity checks only. The theorem rests on the formal
rectangle lemma in `main.tex`, plus Saeki's 1968 sharp abelian idempotent-norm
theorem. No finite search is used to infer the compact result.

## Main human-review focus

- Confirm that every irreducible of `A ⋊ H` is the induced representation
  indexed by an `H`-orbit in `A^` and a character of its stabilizer.
- Confirm that restriction `H^ -> H_gamma^` is surjective and that each fiber
  has `[H:H_gamma]` elements.
- Confirm that rectangles for distinct irreducibles are disjoint. This is the
  step that makes an arbitrary sum of primitive central idempotents an abelian
  idempotent rather than merely a trigonometric polynomial with multiplicity.

No gap was found in this audit. Novelty confidence is moderate because a 1979
paper of Hauenschild treats the structural classification of central
idempotents for groups with abelian normal subgroups of finite index, although
the inspected text does not state the sharp norm transference proved here.
