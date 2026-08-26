# Locally Length Baire-Envelope Theorem

Status: `candidate_partial_result_likely_valid`

Source: Oleksandr V. Maslyuchenko and Ziemowit M. Wójcicki,
*Classification of Lipschitz derivatives in terms of semicontinuity and the
Baire limit functions*, arXiv:2509.20849, Introduction and Theorem 7.1
(source PDF pp. 2 and 16).

## Claimed contributions

The packet advances the inverse problem for triples
`(lip f, Lip f, LLip f)` in three directions.

1. If a metric domain is asymptotically `C`-quasiconvex at `x`, then
   `LLip f(x) <= C (lip f)^vee(x)` for every continuous map into any metric
   space.  Consequently, on every locally length domain,
   `(lip f)^vee = (Lip f)^vee = LLip f`.  This extends source Theorem 7.1
   beyond locally convex normed domains.
2. On `[-1,1]`, the triple `u=v=w=1_{0}` satisfies every order,
   generalized-semicontinuity, and upper-Baire-envelope constraint proved in
   the source but is not realizable.  Thus those necessary conditions are not
   sufficient for the inverse problem.
3. On the compact connected double arc
   `X_alpha={(t,+/-t^alpha):0<=t<=1}`, `alpha>1`, the vertical coordinate map
   has both pointwise Baire envelopes zero at the origin while its local
   Lipschitz derivative is one.  Hence the source identity fails sharply on
   general metric subspaces.

This is a substantial partial answer, not a classification of all realizable
triples.

## Packet contents

- `solution_packet.pdf`: proof and review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/inverse_question_crop.png`: rendered source question.
- `figures/source_theorem_crop.png`: rendered source Theorem 7.1.
- `code/verify_double_arc.py`: independent numerical check of the double arc.
- `code/verification_output.txt`: saved PASS output.
- `VERIFIER_REPORT.md`: adversarial step-by-step review.
- `main.tex`: packet source; build intermediates and rendered pages are under
  `tmp/`.

## Reproduce the verification

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2509.20849_locally_length_baire_envelope/code/verify_double_arc.py \
  --suite
```

## Human-review focus

Check the metric-codomain scalarization, the local length-space neighborhood
argument, and the generalized semicontinuity of the singleton indicator.  The
bounded novelty search through 2026-08-13 found no prior statement of these
results; novelty remains plausible rather than certified.
