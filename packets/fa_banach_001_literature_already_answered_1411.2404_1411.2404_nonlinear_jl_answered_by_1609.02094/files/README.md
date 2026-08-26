# Nonlinear Johnson--Lindenstrauss optimality after arXiv:1411.2404

Status: `literature_already_answered (principal nonlinear question)`

The discussion section of Kasper Green Larsen and Jelani Nelson,
*The Johnson--Lindenstrauss lemma is optimal for linear dimensionality
reduction* (arXiv:1411.2404), identifies the obvious next problem: prove the
matching lower bound when the embedding is allowed to be nonlinear.

The same authors subsequently solved this principal problem in *Optimality of
the Johnson--Lindenstrauss Lemma* (arXiv:1609.02094). Theorem 2 constructs an
`n`-point subset of `R^d` for which **every map** satisfying the JL distance
guarantee has target dimension

```text
m = Omega(epsilon^(-2) log(epsilon^2 n)).
```

In the near-full parameter range emphasized in its abstract, this becomes
`Omega(epsilon^(-2) log n)`, matching the JL upper bound. Thus the linearity
restriction highlighted in arXiv:1411.2404 is genuinely removed. The later
paper also records Alon--Klartag's refinement of the lower-bound range.

This packet is a provenance record, not a new mathematical result. The exact
all-parameter optimal dimension has subtleties reflected by
`log(2+epsilon^2 n)`; the classification here concerns the source paper's
principal nonlinear-optimality question rather than every literal parameter
formulation in its discussion.

Files:

- `solution_packet.pdf`: compact literature-status note.
- `source_paper.pdf`: arXiv:1411.2404.
- `supporting_paper_1609.02094.pdf`: decisive later paper.

Official records:

- https://arxiv.org/abs/1411.2404
- https://arxiv.org/abs/1609.02094

