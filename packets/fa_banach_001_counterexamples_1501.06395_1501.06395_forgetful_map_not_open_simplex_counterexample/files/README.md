# The multiplicative forgetful map is not open

**Status:** candidate full counterexample, likely valid, pending expert review.

**Source:** Isaac Goldbring and Thomas Sinclair, *Omitting types in operator
systems*, arXiv:1501.06395, Question 6.7 on printed page 17.

## Result

For every `n >= 3`, the forgetful map

\[
G:\mathcal X_n\longrightarrow\mathcal{OS}_n
\]

is neither weak-open nor strong-open. In particular, Question 6.7 has a
negative answer under either topology introduced in the source paper.

Let `E_0=C^n`. For `0<epsilon<1`, define the unital function space
`S_epsilon` in `C^(n+1)` by

\[
J_\epsilon(z_1,\ldots,z_n)=
\left(z_1,\ldots,z_n,
\frac{1+\epsilon}{2}(z_1+z_2)-\epsilon z_3\right).
\]

The underlying operator spaces converge strongly to `E_0`, uniformly at all
matrix levels:

\[
\|J_\epsilon\|_{cb}\leq 1+2\epsilon,
\qquad \|J_\epsilon^{-1}\|_{cb}\leq1.
\]

Nevertheless, no representatives of these forgotten classes converge to
`E_0` in `X_n`. Near-multiplicativity would make the images of the `n`
coordinate projections have vanishing cross ternary products. Hamana's
ternary envelope transfers those products to `C^(n+1)`. At the extra
simplex vertex, two limiting coordinate functions have modulus `1/2`, so one
cross ternary product has limiting modulus `1/8`, a contradiction.

## Packet contents

- `solution_packet.pdf` / `main.tex`: complete construction and proof.
- `source_paper.pdf`: arXiv:1501.06395.
- `supporting_paper_hamana_1999.pdf`: the ternary-envelope reference.
- `figures/open_problem_crop.png`: source crop of Question 6.7.

## Verification and review focus

The proof is symbolic. Human review should focus on the universal-property
passage from an arbitrary C*-cover to the ternary envelope and on the final
open-map sequential argument. The matrix-norm estimate and the `1/8`
obstruction are explicit.

The construction does not decide openness for `n=1,2`; this is unnecessary
for the universally quantified source question.

## Novelty search

A bounded search on 2026-08-09 covered the run indexes, the exact wording of
Question 6.7, the paper title and arXiv id, later papers citing the source, and
searches combining `forgetful map`, `X_n`, `OS_n`, and `Kirchberg embedding
problem`. No later explicit answer or this simplex construction was found.
Priority remains subject to specialist review.

Ledger: `runs/fa_banach_001/ledger/results/1501.06395_forgetful_map_not_open_simplex_counterexample.json`.
