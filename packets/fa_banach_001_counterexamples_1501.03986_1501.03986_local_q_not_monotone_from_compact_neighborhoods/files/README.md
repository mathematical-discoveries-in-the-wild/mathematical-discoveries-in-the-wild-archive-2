# Negative answer to Open Question 8 on local behavior of Q_X

Status: `counterexample`

Let `X` be the closed unit disk and `z_0=0`.  Form a connected compact
neighborhood `N` by adjoining a nonrectifiable Jordan arc to the boundary of
the smaller disk `closed_D(0,1/4)`, with no other intersection.

- Straight-line integration gives the exact ambient value `Q_X(0)=1`.
- Source Lemma 10.4 gives functions on the infinite-length arc with derivative
  norm at most 3, endpoint derivatives zero, and arbitrarily large endpoint
  oscillation.
- Constant extension across the smaller disk preserves continuous
  differentiability because the derivative at the attachment point is zero.
  After scaling, these functions show `Q_N(0)=infinity`.

Thus the implication in Open Question 8 of arXiv:1501.03986 is false, even
when the ambient set is convex.

Files:

- `source_paper.pdf`: arXiv:1501.03986.
- `figures/open_question_8.png`: source question on PDF page 31.
- `main.tex`, `solution_packet.pdf`: complete counterexample proof.
- `verification.md`: mathematical and rendering checks.
