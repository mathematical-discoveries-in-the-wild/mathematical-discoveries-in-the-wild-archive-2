# Negative-index Lagrangian Fredholm pairs exist

Run: `fa_banach_001`  
Agent: `agent_lane_03`  
Model: `GPT5.6`  
Status: `literature_already_answered (affirmative construction)`

## Original question

Bernhelm Booß-Bavnbek and Chaofeng Zhu, *The Maslov index in weak
symplectic functional analysis*, arXiv:1301.7248, Section 2.3.1, PDF page 14,
ask whether a weak symplectic Hilbert space can contain a Fredholm pair of
Lagrangian subspaces with negative index.

## Later answer

The same authors answer the question in *The Maslov index in symplectic
Banach spaces*, arXiv:1406.0569, Example 1.2.11, PDF pages 29-30. For every
`n in N` they construct a weak symplectic Hilbert space and Lagrangians
`lambda_+`, `lambda_-` forming a Fredholm pair with index `-n`.

The supporting paper explicitly announces the example as showing that
negative index really occurs, so this is an exact literature answer rather
than an agent-inferred implication.

## Files

- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: original arXiv:1301.7248 paper.
- `supporting_paper_1406.0569.pdf`: later explicit construction.
- `tmp/`: build and rendering intermediates.

