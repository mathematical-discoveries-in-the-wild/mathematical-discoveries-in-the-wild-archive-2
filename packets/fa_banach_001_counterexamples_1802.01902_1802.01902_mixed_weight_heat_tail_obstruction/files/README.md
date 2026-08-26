# Mixed-weight heat-tail obstruction

Status: `candidate_counterexample_likely_valid`  
Model: `GPT5.6`  
Agent: `agent_lane_11`  
Date: 2026-08-09

## Source and exact target

José Bonet, Wolfgang Lusky, and Jari Taskinen, *Schauder bases and the
decay rate of the heat equation*, arXiv:1802.01902, Question `3 degrees` on
page 14 (equation (4.19)).

The question asks whether the paper's arbitrary tail-decay conclusion can hold
in dimension `N>1` for

```text
w(x) = exp(|x_1|) product_{j=2}^N (1+|x_j|)^2,
```

where the weight is fast only in the first coordinate.  The source screenshot
is `figures/open_problem_crop.png`; the original PDF is `source_paper.pdf`.

## Claimed contribution

The answer is **no**.  More strongly, if

```text
X = L^1_w(R^N)
```

and `E` is any closed finite-codimensional subspace of `X`, then

```text
|| exp(t Delta)|_E ||_{X -> L^infinity}
    >= c_E t^(-N/2-1)
```

for all sufficiently large `t`, with `c_E>0`.  A Schauder tail is
finite-codimensional, so it cannot obey a uniform `O(t^-m)` estimate for any
integer `m>N/2+1`, let alone for every positive integer `m`.

## Proof intuition

A finite-codimensional subspace cannot remove every vector from a family of
`d+1` disjoint bumps, where `d` is its codimension.  Put those bumps a distance
comparable to `sqrt(t)` apart in the second coordinate.  Normalizing a bump in
the mixed weighted norm costs only order `t`, because the transverse weight is
quadratic.  At the center of whichever surviving bump has largest normalized
coefficient, the heat kernel contributes order `t^-N/2`; Gaussian decay makes
the other centers too far away to cancel it.  The resulting lower bound is
`t^-N/2 * t^-1`.

## Verification report

Verdict: `likely valid` (confidence 96/100).

| Step | Status | Verifier note |
| --- | --- | --- |
| Finite-codimension intersection | valid | `d+1` disjoint unit vectors span a space meeting a codimension-`d` subspace nontrivially. |
| Weighted bump normalization | valid | Translation only in `x_2` gives `a_{j,t} <= C j^2 t`; all other weight factors remain bounded on the fixed bump support. |
| Cancellation control | valid | Choosing the largest `|c_j|/a_{j,t}` and a sufficiently large fixed separation gives a uniform Gaussian diagonal-dominance estimate. |
| Operator lower bound | valid | The chosen vector has weighted norm one and lies in `E`, giving `c_E t^(-N/2-1)`. |
| Application to Schauder tails | valid | Every closed basis tail has finite codimension.  Taking an integer `m>N/2+1` contradicts the lower bound as `t` tends to infinity. |

No computational lemma or external theorem is used.  The main human-review
focus should be the normalization inequality `max_j |c_j|/a_{j,t} >=
1/sum_j a_{j,t}` and the Gaussian off-diagonal estimate; both are written in
full in the packet.

## Novelty check

A bounded web/arXiv search on 2026-08-09 used the exact title, arXiv id,
authors, the displayed mixed weight, and phrases `fast growing in one
coordinate` and `Schauder basis heat equation`.  It found:

- arXiv:1802.01902 and author-hosted copies containing the question;
- a later author-hosted manuscript proving a stronger result for weights fast
  in **all** coordinate directions.

No later paper or manuscript answering the displayed mixed-weight question was
found.  The later fast-weight theorem does not apply here because the
quadratic transverse factors fail the source's all-orders growth condition.
Novelty is therefore plausible but not certified by an exhaustive
bibliographic review.

## Human-review recommendation

Send to a functional analyst/PDE reviewer.  If the essential lower-bound
argument is confirmed, this is a complete negative answer to Question
`3 degrees`, not merely a counterexample to one proposed construction.

