# Vague mass escape destroys transport-cost lower semicontinuity

Status: `counterexample_likely_valid`  
Agent: `agent_lane_02`  
Model: `GPT5.6`  
Date: 2026-08-11

## Result

The open question on page 10 of Gozlan--Herry--Peccati,
*Transport inequalities for random point measures* (arXiv:2002.04923), has a
negative answer as stated.

Even for the ordinary bounded continuous transport cost

\[
  \rho(x,y)=1\wedge |x-y|,\qquad
  c(x,p)=\int_{\mathbb R}\rho(x,y)\,p(dy),
\]

the map \(\mathcal T_c:\mathcal M_0(\mathbb R)^2\to[0,\infty]\) is not lower
semicontinuous for the vague topology.  Indeed,
\(\nu_{1,n}=\delta_0\) and \(\nu_{2,n}=\delta_n\) converge vaguely to
\(\delta_0\) and \(0\), respectively.  The approximating costs equal \(1\),
whereas the limiting cost is \(+\infty\), since the limiting measures have
different total masses and hence no coupling.

The example satisfies more than the question asks: \(c\) is bounded and
jointly continuous, and it is linear (thus convex) in its probability-measure
argument.

## Packet contents

- `solution_packet.pdf`: review-ready statement, proof, verification, and
  novelty audit.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: the arXiv source paper.
- `figures/open_problem_crop.png`: page-10 source evidence.
- `verification_report.md`: independent hypothesis-by-hypothesis proof audit.

## Novelty check

On 2026-08-11 we searched the run registry and solution/attempt/proof-gap
indexes, the exact paper title and question phrase, and combinations of
“generalized transport cost,” “vague topology,” “locally finite measures,”
“mass escape,” and “lower semicontinuity,” including arXiv-focused searches.
No later paper explicitly answering this exact question was found.  The search
did find the original arXiv/JFA paper and general literature on vague
convergence, but not this counterexample.  Novelty is therefore plausible, not
certified exhaustive.

## Human review recommendation

High-confidence short counterexample.  The key review point is only that the
paper's convention assigns \(+\infty\) when total masses differ; this is stated
immediately after its definition of \(\mathcal T_c\).
