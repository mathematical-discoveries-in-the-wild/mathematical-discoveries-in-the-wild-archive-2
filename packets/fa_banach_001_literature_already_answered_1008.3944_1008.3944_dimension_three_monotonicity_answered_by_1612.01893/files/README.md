# Literature status: three-dimensional random-simplex monotonicity

- Source question: Luis Rademacher, *On the monotonicity of the expected
  volume of a random simplex*, arXiv:1008.3944.
- Later answer: Stefan Kunis, Benjamin Reichenwallner, and Matthias Reitzner,
  *Monotonicity of the Sample Range of 3-D Data: Moments of Volumes of Random
  Tetrahedra*, arXiv:1612.01893.
- Status: `literature_already_answered`.
- Agent: `agent_lane_18`; model: `GPT5.6`; date: 2026-08-11.

Rademacher's Discussion asks: “(3-D case) For Meckes's strong conjecture,
find an easy argument to disprove it for d=3.” The later paper proves its
Theorem 1: in R^3 expected volume of the four-point sample range is not
monotone under inclusion. Its decisive Proposition 1 shows that, for a
unit-volume tetrahedron T and the centroid c of a facet,

```text
E |conv(X1,X2,X3,c)| < 13/720 - pi^2/15015
                      = E |conv(X1,X2,X3,X4)|.
```

Rademacher's boundary-point characterization then produces an infinitesimal
enlargement of T for which expected random-tetrahedron volume decreases. This
is a direct negative answer to the source question, so no new-proof attack is
appropriate.

Files:

- `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: reconstructed source paper arXiv:1008.3944.
- `supporting_paper_1612.01893.pdf`: later answering paper.
- `main.tex`: source for the status note.

