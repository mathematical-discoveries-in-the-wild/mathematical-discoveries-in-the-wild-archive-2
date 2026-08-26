# Block-projection counterexample for weighted Sobolev interpolation

Run: `fa_banach_001`

Agent: `agent_lane_14`

Status: `candidate_full_result_and_counterexample_likely_valid_human_review_needed`

## Source question

On PDF page 47, Section 8.3 of Cwikel--Einav, *Interpolation of
weighted Sobolev spaces* (arXiv:1807.10790), the authors ask whether one can
have

```text
mathcal W^p(U,theta,r_w)
  proper subset of
[W^{1,p}(U,w_0),W^{1,p}(U,w_1)]_theta.
```

## Candidate full answer and stronger counterexample

The packet constructs positive compact-bounded measurable weights on the full
line. Their quotient is locally Lipschitz. For `p=2` and `theta=1/2`, it proves

```text
mathcal W^2(R,1/2,r)
  proper subset of
[W^{1,2}(R,w_0),W^{1,2}(R,w_1)]_{1/2}
  proper subset of
W^{1,2}(R,sqrt(w_0 w_1)).
```

The first strictness exactly answers the source question. The second gives a
counterexample to the unrestricted Stein--Weiss-type identity.

The mechanism is a reflection-symmetric block system with a single projection
bounded on both endpoints. Endpoint block norms stay uniformly comparable to
one, while geometric-mean block norms decay exponentially. A `1/n` coefficient
witness belongs to both endpoints but fails the auxiliary logarithmic-gradient
condition. A `1/sqrt(n)` witness belongs to the geometric-mean Sobolev space
but, by the common projection, not even to the endpoint algebraic sum.

## Files

- `main.tex`: complete expert-facing construction and proof.
- `solution_packet.pdf`: six-page rendered review packet.
- `source_paper.pdf`: local copy of arXiv:1807.10790.
- `figures/open_problem_crop.png`: real source screenshot from PDF page 47.
- `code/verify_blocks.py`: deterministic formula and series checks.
- `verification.md`: proof and rendering audit.
- `novelty_search.md`: bounded novelty-search record.

## Human-review focus

Check the uniform boundedness of the common core-average projection, the
identification of its two endpoint ranges, and the use of Theorem 1.21 of the
source paper to obtain the full auxiliary-space inclusion on `U=R`. The two
witness divergences then follow from explicit series estimates.

