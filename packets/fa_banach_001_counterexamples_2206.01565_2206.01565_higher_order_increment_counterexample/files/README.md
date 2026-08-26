# Higher-order Minkowski increment counterexample

Status: `candidate_full_counterexample_likely_valid`  
Source: arXiv:2206.01565, Question 3.10  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

Question 3.10 is false for `m=5` in every dimension `n>=2`. A finite lattice
configuration, thickened by separated cubes of side `epsilon<1`, has iterated
increment volume `4 epsilon^n`, whereas the proposed alternating sum is
`6 epsilon^n`.

The lift from finite sets to compact Euclidean sets is exact: Minkowski
addition and set difference act cell-by-cell because distinct lattice cubes
are positively separated.

## Contents

- `solution_packet.pdf`: counterexample, exact computation, lift proof,
  intuition, source screenshot, and scope.
- `main.tex`: packet source.
- `verifier.py`: deterministic exact-integer verifier.
- `source_paper.pdf`: official arXiv:2206.01565 PDF.
- `source_excerpt_question_3_10_page_13.pdf`: exact question page.
- `figures/source_question_3_10_page_13.png`: rendered source page.
- `verification.md`: proof, provenance, build, and visual-QA record.

## Scope

The result fully answers the universal higher-order question negatively. It
does not determine whether the inequality may still hold for `m=3` or `m=4`,
under convexity assumptions, or address the paper's separate Conjecture 3.11.
