# The proposed weak Schatten endpoint is false in dimension one

Status: `literature_implied_answer (dimension-one counterexample; d>=2 open)`

Frank and Sabin, *The Stein--Tomas inequality in trace ideals*,
arXiv:1609.08388, Remark 5 on PDF page 6, propose the endpoint paraboloid
estimate in weak `S^{d+1}`.  In dimension one it reads

```text
|| conjugate(W) T_S W ||_{S^{2,infinity}}
    <= C ||W||_{L_t^4 L_x^2}^2.
```

Bez, Hong, Lee, Nakamura, and Sawano, arXiv:1708.05588, formulate the dual
orthonormal estimate as Conjecture 1.3 and disprove it for `d=1` in Theorem
5.3 (PDF pages 27--28).  Lorentz--Schatten duality therefore disproves the
source weak trace-ideal endpoint in dimension one.  This operator-side
identification is the reason for the `literature_implied_answers` provenance
rather than a new counterexample packet.

The result is not an all-dimensional answer.  Feng, Song, and Wu,
arXiv:2507.14974, Conjecture 1.6 and the following paragraph on PDF page 6,
state explicitly that the endpoint remains open for every `d>=2`.

Files:

- `source_paper.pdf`: arXiv:1609.08388.
- `supporting_paper_1708.05588.pdf`: the dimension-one counterexample,
  Theorem 5.3.
- `supporting_status_2507.14974.pdf`: current-status confirmation,
  Conjecture 1.6.
- `figures/`: rendered evidence pages from all three papers.
- `main.tex` and `solution_packet.pdf`: compact identification note.
- Upgrade-attempt record:
  `runs/fa_banach_001/attempts/1609.08388_weak_schatten_endpoint_upgrade_attempts.md`.
- Ledger:
  `runs/fa_banach_001/ledger/results/1609.08388_d1_weak_schatten_counterexample_open_dge2.json`.

Human-review recommendation: verify the operator/density trace pairing and
the Lorentz ideal duality `S^{2,1}* = S^{2,infinity}`; then compare source
Remark 5 with supporting Theorem 5.3.  The dimensional limitation must remain
prominent.

