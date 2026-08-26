# Closed graph versus property (Q): two positive regimes

Status: `candidate_substantial_partial_likely_valid`

This packet addresses the question at the end of Example 6.2 of
arXiv:1203.1101: can a maximally monotone operator with norm x weak-star
closed graph differ from its Cesari reconstruction `hat(A)`?

It proves two rigorous positive subcases:

1. Every multifunction on any Banach space whose graph is nonempty, convex,
   and norm x weak-star closed satisfies `hat(A)=A`. This removes the
   reflexivity assumption from the source's convex-graph example, and does
   not need monotonicity.
2. If `A` is maximally monotone and `dom(A)` has nonempty relative interior
   in its closed affine hull, then `hat(A)=A`. Graph closedness is a
   conclusion rather than an assumption.

The full empty-relative-interior, nonconvex-graph case remains open in this
packet. Eight upgrade routes were recorded in the attempt file. Three
explicit counterexample templates fail because their unbounded cancellation
also forces the missing pair into the norm x weak-star graph closure.

Files:

- `solution_packet.pdf` — expert-facing proof packet
- `source_paper.pdf` — arXiv:1203.1101
- `main.tex` — packet source
- `verification.md` — mathematical and artifact audit
- `tmp/` — LaTeX and render QA artifacts

Attempt:
`runs/fa_banach_001/attempts/1203.1101_closed_graph_vs_property_q_attempt.md`

Ledger:
`runs/fa_banach_001/ledger/results/1203.1101_closed_graph_property_q_relative_interior.json`
