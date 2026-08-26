# Sharp spectral multipliers beyond Métivier groups (arXiv:2412.07920)

Status: `literature_already_answered`

Source paper: Lars Niedorf, *Spectral multipliers on Métivier groups*,
arXiv:2412.07920.

Supporting answer: Lars Niedorf, *Spectral multipliers on two-step stratified
Lie groups with degenerate group structure*, arXiv:2501.16262.

## Identification

Immediately after its main theorem, arXiv:2412.07920 asks whether
`p`-specific multiplier estimates with the sharp regularity threshold

```text
s > d |1/p - 1/2|
```

hold beyond Métivier groups.  The paper identifies favorable weighted
Plancherel estimates as the obstruction when the alternating form has a
nontrivial radical.

The later arXiv:2501.16262 explicitly cites arXiv:2412.07920, restates the
question, and proves such estimates for a class in which the matrices `J_mu`
may have nontrivial kernels.  Its Theorem 1.1 covers two-step groups satisfying
Assumptions A and B and a dimensional condition.  The paper explicitly says
that this theorem is completely new in the non-Métivier case.

## Concrete affirmative cases

The supporting paper verifies its assumptions for:

- central products of copies of the free two-step group `N_{3,2}`; for at
  least two copies, the multiplier part gives a nonempty interval `p > 1`;
- Heisenberg--Reiter groups `H_{N,d_2}` satisfying the stated dimensional
  condition, again with a nontrivial multiplier range when the strict form of
  that condition holds.

These groups are genuinely non-Métivier because `J_mu` has a nonzero kernel
for every nonzero `mu` in the examples under discussion.  Thus the existential
content of “beyond Métivier” is answered affirmatively in later literature.

## Scope

This is not a theorem for every two-step stratified Lie group.  The later
paper requires structural Assumptions A and B and a high-dimensional
inequality.  It also says that the relevant Plancherel estimates are not known
in arbitrary two-step groups.  Accordingly, this packet records a decisive
scoped affirmative answer, not a solution of the unrestricted general
problem.

## Search evidence

The cheap run indexes were searched for `2412.07920`, the exact title,
`Métivier`, `spectral multiplier`, and the sharp-threshold phrase; no prior
packet or attempt for the source paper was found.  A bounded primary-source
search located arXiv:2501.16262.  Its introduction cites arXiv:2412.07920 as
the Métivier result, poses the beyond-nondegenerate question, and announces
the non-Métivier theorem.

## Files

- `source_paper.pdf`: arXiv:2412.07920v2.
- `supporting_paper_2501.16262.pdf`: arXiv:2501.16262v2.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.

Ledger:
`runs/fa_banach_001/ledger/results/2412.07920_beyond_metivier_answered_by_2501.16262.json`.
