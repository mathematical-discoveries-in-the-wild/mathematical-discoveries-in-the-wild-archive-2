# Greedy K-functional near-attainment with logarithmic loss

Status: `candidate_partial_result_likely_valid`  
Source: arXiv:2310.17309v2, equation (4.3) on PDF page 19  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

Under the source paper's Bernstein hypothesis, let
`alpha=1/sigma-1/p` and `q=min(sigma,2)`. For the dyadic greedy rank
`N=2^n`, the packet proves

```text
K(f,N^(-alpha); L^p(S),V_{sigma,p})
 <= ||f-G_N f||_p + N^(-alpha)||G_N f||_{V_{sigma,p}}
 <= C(1+log N)^(1/q) K(f,N^(-alpha); L^p(S),V_{sigma,p}).
```

The desired uniform constant remains open. The proof combines the source's
two endpoint embeddings with a finite-coordinate truncation estimate and
carefully decomposes the fixed greedy projection of `f` across an arbitrary
K-functional competitor.

## Contents

- `solution_packet.pdf`: statement, full proof, intuition, exact source crop,
  verification, limitations, and reference.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv source PDF.
- `source_excerpt_open_problem_page_19.pdf`: exact full source page.
- `source_excerpt_exact_question.pdf`: cropped vector excerpt.
- `figures/open_problem_crop.png`: required readable source screenshot.
- `code/finite_tree_search.py`: exploratory exact finite-tree search; not part
  of the proof.
- `verification.md`: proof, provenance, computation, and PDF-QA record.

## Scope

This is a pointwise near-attainment theorem, not a solution of the source's
uniform-equivalence question. Eight focused upgrade routes were examined; the
remaining obstruction is removal of the coefficient-endpoint loss.
