# The shift-invariant predual question for `ell^1(Z)`: answered by arXiv:1101.5696

Status: `literature_already_answered`  
Run: `fa_banach_001`  
Agent: `agent_lane_10`  
Model: `GPT5.6`

## Original question

Matthew Daws asks in arXiv:math/0604372, *Dual Banach algebras:
representations and injectivity*, Section 4, PDF page 13, whether
`ell^1(Z)` has a unique predual compatible with convolution. He gives the
equivalent concrete formulation:

> Let `X` be a shift-invariant subspace of `ell^infty(Z)` such that `X'` is
> naturally identified with `ell^1(Z)`. Is `X = c_0(Z)`?

Here shift invariance is precisely the condition making convolution on
`ell^1(Z)` separately weak-star continuous for the induced duality.

## Separate later answer

Daws, Haydon, Schlumprecht, and White, *Shift invariant preduals of
`ell_1(Z)`*, arXiv:1101.5696, explicitly cite the source paper and say on PDF
page 2 that their results answer this question negatively.

Their Theorem 3.4 and Corollary 3.5 (PDF pages 9--10) construct, for every
complex `lambda` with `|lambda| > 1`, a concrete shift-invariant predual
`F^(lambda) subset ell^infty(Z)`. The family gives continuum many distinct
weak-star topologies on `ell^1(Z)`, all different from the topology induced
by the canonical predual `c_0(Z)`. Thus the answer to `X = c_0(Z)?` is no,
and the compatible predual is very far from unique.

The answer paper proves more: later examples include shift-invariant preduals
that are not Banach-space isomorphic to `c_0`.

## Scope

This is a complete negative answer to the exact source question about
preduals making convolution separately weak-star continuous. It does not
classify all shift-invariant preduals, and it does not contradict stronger
uniqueness statements that also require the natural coproduct to be
weak-star continuous.

This is an exact literature answer, not an original result of the run.

## Files

- `solution_packet.pdf`: compact literature-status packet.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:math/0604372.
- `supporting_paper_1101.5696.pdf`: the answering paper.
- `verification.md`: identification and scope audit.

Ledger:
`runs/fa_banach_001/ledger/results/0604372_l1z_shift_invariant_predual_answered_by_1101.5696.json`.
