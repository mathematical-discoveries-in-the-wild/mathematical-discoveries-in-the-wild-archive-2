# Holevo--Utkin sharp zero-sum norm conjecture: literature answer

Run: `fa_banach_001`

Agent: `agent_lane_14`

Status: `literature_already_answered`

## Original question

On PDF page 2 of Holevo--Utkin, *A conjecture on a tight norm inequality in
the finite-dimensional $\ell_p$* (arXiv:2603.24017), inequalities (1)--(4)
conjecture the exact extremal ratio between the $\ell_{2\alpha}$ and
$\ell_2$ (quasi-)norms on the zero-sum hyperplane.  The proposed constant is
the better of the values supplied by the two-level vectors
`(1,-1,0,...,0)` and `(d-1,-1,...,-1)`.

## Exact answer

Haonan Zhang, *Proof of the Holevo--Utkin conjecture on sharp $\ell_p$ norms
for zero-sum vectors* (arXiv:2605.05243v2), explicitly cites the source,
restates the target as Conjecture 1 on PDF pages 1--2, and proves in Theorem 2
on PDF page 2 that Conjecture 1 holds for every remaining dimension `d >= 4`.
Together with the source's proof for `d = 3`, this resolves all dimensions in
the source conjecture.  The exponent substitution is `p = 2 alpha` below 2
and `q = 2 alpha` above 2; `alpha = 1` is equality of the same norm.

The supporting author expressly knew that the paper was proving the exact
Holevo--Utkin conjecture.  This is an already-known literature resolution,
not a new result of the run.

## Remaining scope

No exponent or dimension covered by the original conjecture remains open.

## Files

- `main.tex`: compact identification note.
- `solution_packet.pdf`: rendered status packet.
- `source_paper.pdf`: arXiv:2603.24017.
- `supporting_paper_2605.05243.pdf`: exact answer paper.

