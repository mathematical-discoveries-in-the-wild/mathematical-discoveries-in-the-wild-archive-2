# arXiv:1102.4394 — full one-dimensional endpoint result

Status: `candidate full resolution, proved`

Frank and Loss state that their arbitrary-domain Hardy--Lieb--Thirring
inequality should remain valid in dimension one at the endpoint
`gamma=1/2`.  This packet proves the statement.

The proof decomposes the domain into intervals.  Finite intervals are split at
their midpoint; the Dirichlet halves are controlled by the known critical
half-line endpoint theorem.  Removing the midpoint condition adds at most one
eigenvalue, and the source paper's own `q=2` pointwise Hardy--Sobolev estimate
controls its square root by twice the `L1` mass of the negative potential.

The resulting universal constant is

```
L_{1,1/2} = C_{1/2,0} + 2 <= 3.185,
```

where `C_{1/2,0}` is the Ekholm--Frank half-line constant.

- Proof packet: `solution_packet.pdf`
- Original source PDF: `source_paper.pdf`
- Supporting half-line theorem: `supporting_halfline_paper.pdf`
- Open-question evidence: `figures/open_problem_crop.png`
- Supporting-theorem evidence: `figures/halfline_theorem_crop.png`
- Verification: `verification_report.md`
- Attempt and stress-test record:
  `runs/fa_banach_001/attempts/1102.4394_one_dimensional_endpoint_hlt_upgrade.md`
- Ledger:
  `runs/fa_banach_001/ledger/results/1102.4394_one_dimensional_endpoint_hardy_lieb_thirring.json`
