# Uniformly distributed Steiner directions can fail to converge

Status: `literature_already_answered (two deterministic questions)`.

## Source questions

Volcic, *Random symmetrizations of measurable sets*, arXiv:0902.0462,
asks on PDF pages 12--13 whether there is a uniformly distributed sequence of
directions and a bounded Caccioppoli, convex, compact, summable, or
finite-measure set whose iterated Steiner symmetrals fail to converge to the
centered ball in the appropriate metric. The paper conjectures more strongly
that density alone of the directions suffices for convergence.

## Explicit later counterexample

Bianchi, Burchard, Gronchi, and Volcic, *Convergence in shape of Steiner
symmetrizations*, arXiv:1206.2041, answer the existence question affirmatively
and refute the stronger conjecture.

Example 2.1 (PDF pages 3--4) constructs a compact convex planar body `K` and
directions

\[
u_m=(\cos\beta_m,\sin\beta_m),\qquad
\beta_m=\sum_{k=1}^m\alpha_k,
\]

for which the successive Steiner symmetrals do not converge. In Section 5
(PDF page 9), the authors choose, for example,
`alpha_m = theta m^{-sigma}` with `1/2 < sigma < 1`. They explicitly state
that the resulting direction sequence is uniformly distributed on the circle
while the symmetrals of the compact set from Example 2.1 do not converge.

Thus the 2009 existence question has answer **yes**, already for a planar
compact convex body and Hausdorff convergence. Uniform distribution implies
density, so the same example makes the density-only convergence conjecture
**false**. Other probabilistic and unbounded-set questions in the source paper
are outside this packet.

This is a later-literature resolution, not a new result.

## Files

- `solution_packet.pdf`: compact literature-status note.
- `source_paper.pdf`: arXiv:0902.0462.
- `supporting_paper_1206.2041.pdf`: the decisive later paper.
- Ledger: `runs/fa_banach_001/ledger/results/0902.0462_uniformly_distributed_steiner_counterexample.json`.
