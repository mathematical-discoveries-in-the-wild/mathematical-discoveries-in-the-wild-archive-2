# Hilbert-valued weighted Sobolev closure

Status: `candidate_substantial_partial_likely_valid`

This packet addresses the two explicit “Interesting problems” at the end of
arXiv:math/0611038.

It proves:

1. an exact correction of the infinite-dimensional weighted `L^infinity`
   closure: coordinatewise scalar approximability must be supplemented by
   uniform decay of weighted coordinate tails;
2. a counterexample showing the coordinatewise-only assertion in the
   same-author companion paper is false in infinite dimension;
3. an exact Sobolev closure formula whenever the weighted primitive operator
   is bounded, with a checkable one-sided coordinate condition; and
4. the complete formula for all constant positive diagonal Hilbert weights:
   the closure is exactly the set of `f` for which `D_w f` is `C^1`.

The unrestricted “most general conditions” question remains open because
the source allows degenerate weights for which its displayed quantity is only
a seminorm and weights for which primitive boundedness can fail.

Files:

- `solution_packet.pdf` -- expert-facing proof packet
- `source_paper.pdf` -- arXiv:math/0611038
- `main.tex` -- packet source
- `verification.md` -- mathematical and artifact audit
- `tmp/` -- LaTeX and render QA artifacts

Attempt:
`runs/fa_banach_001/attempts/0611038_hilbert_weighted_sobolev_closure_attempt.md`

Ledger:
`runs/fa_banach_001/ledger/results/0611038_hilbert_weighted_sobolev_closure.json`
