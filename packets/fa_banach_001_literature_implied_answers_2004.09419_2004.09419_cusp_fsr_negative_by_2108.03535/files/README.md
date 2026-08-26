# The cusp FSR question has a negative literature-implied answer

Status: `literature_implied_answer_negative`.

Question 5.4.1 of Earnest Akofor's *Metric Geometry of Finite Subset
Spaces* (arXiv:2004.09419, PDF page 131; printed page 122) asks whether the
cusp

```text
X = {(s, |s|^(1/2)) : -1 <= s <= 1}
```

admits Lipschitz retractions `X(n) -> X(n-1)`.

Theorem 5.1 of Leonid V. Kovalev's *Lipschitz clustering in metric spaces*
(arXiv:2108.03535v2, PDF page 10) gives a negative answer after a direct
identification. It says that if a metric space contains a bi-Lipschitz copy
of `[0,1]` and admits a Lipschitz retraction `X(4) -> X(3)`, then it is
uniformly locally quasiconvex. A branch of the cusp is bi-Lipschitz to an
interval, but symmetric points approaching the vertex have connecting-length
to ambient-distance ratio tending to infinity. Hence `X(4) -> X(3)` cannot
exist, and therefore the requested family cannot exist.

The supporting paper does not identify Akofor's cusp question explicitly;
the implication is agent-identified. No new theorem is claimed.

Files:

- `main.tex`: compact identification and hypothesis check.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:2004.09419.
- `supporting_paper_2108.03535.pdf`: arXiv:2108.03535v2.
- `tmp/`: build and render intermediates.
