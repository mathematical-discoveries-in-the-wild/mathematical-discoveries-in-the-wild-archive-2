# A finite-gap reduction for the Haar-liminf problem

Status: `candidate_partial_likely_valid`

## Source question

Kahler and Szwarc, arXiv:2212.11229v3, Section 5, Question (ii), ask
whether every symmetric polynomial hypergroup satisfies
`liminf h(n) >= 2`. The current queue paper, Kahler and Obermaier,
arXiv:2603.17983, constructs `h(2) < 2` examples and gives partial answers
to two related questions, but it does not settle this liminf problem.

## Result

Let `D` be the Hermitian dual and `I` the convex hull of the support of the
orthogonalization measure. The packet proves:

- `P_n(x)^2 >= 2/h(n)-1` for every `x` in `D`;
- if `h(n)<2`, the `n` simple zeros of `P_n` occupy `n` different connected
  components of `I \ D`;
- if `I \ D` has only `G` components, then `h(n)>=2` for every `n>G`, hence
  `liminf h(n)>=2`;
- if `0` is in `D`, then `h(n)>=2` for every odd `n`; and
- a fixed Haar dip below 2 forces a uniform nonvanishing bound on `D`.

## Scope and obstruction

This is a genuine partial result. Polynomial hypergroups may have infinitely
disconnected, even discrete, duals. The proof gives no uniform bound on the
number of such gaps, and eight focused routes did not either exclude this
geometry or construct a fully product-positive recurrence with recurring
Haar dips. The unrestricted infinite-gap case remains open.

## Packet contents

- `main.tex`, `solution_packet.pdf`: exact statement, proof, refinements,
  scope, and the eight-route obstruction summary.
- `source_problem_paper.pdf`: arXiv:2212.11229v3.
- `source_target_paper.pdf`: arXiv:2603.17983.
- `figures/open_problem_crop.png`: exact source open-problem list.
- `figures/current_partial_crop.png`: current paper's `h(2)` theorem and
  partial-scope statement.
- `VERIFICATION.md`: mathematical and artifact checks.

Human review should concentrate on the identification of dual gaps and the
strict positivity in the two-zero orthogonality contradiction.
