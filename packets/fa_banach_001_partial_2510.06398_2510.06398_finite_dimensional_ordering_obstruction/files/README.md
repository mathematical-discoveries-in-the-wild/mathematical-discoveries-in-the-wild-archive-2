# A finite-dimensional obstruction program for Schauder reorderings

Status: **candidate partial result; likely valid; human review requested**

Source: Miguel Berasategui, *Quasi-greedy Markushevich bases, duality and
norming subspaces*, arXiv:2510.06398v1. The target question appears on PDF
page 2: must every quasi-greedy Markushevich basis in a Banach space have a
Schauder reordering?

## Result

For a finite basis `B=(e_i)_(i=1)^d`, let

```text
beta(B) = min over permutations sigma of
          max_(1 <= m <= d) ||P_{ {sigma(1),...,sigma(m)} }||.
```

Suppose there are normalized finite-dimensional bases `B_j` with uniformly
bounded coordinate functionals, a common quasi-greedy constant `K`, and
`beta(B_j) -> infinity`. Then the union of the `B_j` in the Banach space

```text
X = (direct sum_j E_j)_ell_2
```

is a `K`-quasi-greedy Markushevich basis with no Schauder reordering.

The mechanism is exact. A global greedy set cuts each block in a greedy set,
so the `ell_2` norm preserves the common quasi-greedy estimate. Conversely,
every global ordering induces an ordering on each finite block. At the global
time when a bad induced block prefix has appeared, the global prefix
projection restricts to that bad block projection. Its norm is therefore at
least `beta(B_j)`, and the global partial-sum norms are unbounded.

Thus a positive answer to the source question would force a dimension-free
ordering theorem: for every fixed quasi-greedy constant and uniform
coordinate-functional bound, all finite-dimensional bases in that class must
have uniformly bounded best-ordering constants.

## Scope

This does **not** solve the source problem. The missing step is an explicit
family of finite-dimensional Banach bases with the stated uniform bounds and
diverging `beta`. The packet proves the reduction, not the existence of those
blocks. It also does not prove the converse implication from a finite
dimension-free ordering theorem to a Schauder reordering of every infinite
basis.

A later paper, Albiac--Ansorena--Berasategui (arXiv:2510.13693), constructs a
counterexample in a nonlocally convex quasi-Banach space and explicitly says
that the Banach-space restriction remains open. Its construction therefore
does not supply the blocks required here.

A bounded literature check on 2026-08-09 searched the run registry and arXiv
for combinations of `finite-dimensional`, `quasi-greedy`, `permutation`,
`Schauder reordering`, `basis constant`, and `direct sum`. No exact statement
of this reduction was found. Novelty is plausible but not certified; the
block-sum argument may be folklore.

## Files

- `main.tex`, `solution_packet.pdf`: complete theorem and proof packet.
- `verification.md`: adversarial verifier report.
- `source_paper.pdf`: local copy of arXiv:2510.06398v1.
- `figures/open_problem_crop.png`: source evidence from PDF page 2.
- `tmp/`: LaTeX build and rendered visual-QA intermediates.

No computational code is used: the result is an abstract operator-norm
argument.

## Human review recommendation

Review as a likely valid finite-dimensional reduction, not as an answer to the
open problem. Focus on the blockwise greedy-set observation, the restriction
of a global prefix projection to one block, and whether this reduction is
already known informally in the greedy-basis literature.

Ledger:
`runs/fa_banach_001/ledger/results/2510.06398_finite_dimensional_ordering_obstruction.json`.
