# Verification report

Verdict: `literature_answer_verified_in_canonical_iid_model`

## Source audit

The current source is arXiv:1102.0300v4. Remark 1.4 explicitly conjectures
that the `2 exp(-n^c)` singularity term in equation (1.5) can be improved to
`2 exp(-cn)`. The source also discusses exponent one in epsilon as optimal.

## Resolving-paper audit

The current resolving source is arXiv:2203.06141v3. Its Theorem 1.1 proves

`P(sigma_min(A) <= epsilon n^(-1/2)) <= C epsilon + exp(-cn)`

for symmetric matrices with i.i.d. mean-zero, variance-one subgaussian entries
on and above the diagonal. The paper explicitly says that this proves
Vershynin's conjecture.

## Implication audit

At `epsilon=0`, the event is exactly singularity and the theorem gives the
conjectured exponential-in-n bound. The theorem additionally obtains optimal
linear epsilon dependence.

## Scope audit

The 2011 theorem allowed arbitrary independent diagonal entries satisfying a
size condition, whereas the 2023 resolving theorem assumes an i.i.d. diagonal.
The packet claims a full answer only for the canonical i.i.d. symmetric model.
It also distinguishes the still stronger optimal-base Bernoulli conjecture
`(1/2+o(1))^n`.

## Render audit

Clean. The final packet compiles to three pages (418,582 bytes), with no
LaTeX warnings, undefined references, overfull boxes, or underfull boxes.
All three rendered pages were inspected at full readable resolution: text and
both evidence crops are sharp, margins are intact, and there is no clipping,
overlap, or other layout defect.

Final packet SHA-256:
`cd12275e5773d197cdacc496432a03421fb5c213ef1b3f59af88e4d2cbe221ba`.

## Human verifier focus

1. Confirm the interpretation of `(A_ij)_{i<=j}` as entries on and above the
   diagonal in Theorem 1.1 of the resolving paper.
2. Preserve the arbitrary-diagonal and optimal-base scope qualifications.
