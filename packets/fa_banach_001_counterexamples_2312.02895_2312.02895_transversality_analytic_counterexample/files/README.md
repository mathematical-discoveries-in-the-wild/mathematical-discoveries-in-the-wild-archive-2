# Analytic counterexample to removing transversality

Status: `candidate_full_counterexample_likely_valid`  
Source: arXiv:2312.02895, Section 1.7 (published Section 2.7)  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

The transversality hypothesis in Theorem A cannot be removed, even for a
real-analytic boundary and with both factor manifolds two-dimensional.

On `M=N=R^2`, write `x=(r,q)` and `y=(s,t)` and take

```text
Sigma = {(x,y): s > r^2 t}.
```

Its indicator is an `S_p`-bounded Schur multiplier for every
`1<p<infinity`: after splitting into `t>0` and `t<0`, it is a pullback of the
triangular and reverse-triangular projections.  At the origin the `N`-normal
is nonzero, but all boundary sections meet there with tangent lines
`s=r^2 t`, so the zero-curvature condition and any single triangular
representation fail locally.

## Contents

- `solution_packet.pdf`: source question, theorem, complete proof, intuition,
  novelty scope, and review recommendation.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv v2 PDF of arXiv:2312.02895.
- `source_excerpt_transversality_page_11.pdf`: exact question page.
- `figures/open_problem_crop.png`: rendered crop of the open-problem passage.
- `verification.md`: mathematical and packet-QA record.

## Scope

This disproves the proposed extension of the equivalence in Theorem A and
also gives an analytic counterexample.  It does not address the paper's
separate global Fourier-multiplier questions on `SL_2(R)`.
