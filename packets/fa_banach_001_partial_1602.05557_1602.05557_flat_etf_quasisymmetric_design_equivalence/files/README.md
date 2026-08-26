# Flat ETF / quasi-symmetric design equivalence

Status: `candidate_partial_likely_valid`.

The source target is Problem 2 of Matthew Fickus, Dustin Mixon, and John
Jasper, *Equiangular tight frames from hyperovals*, arXiv:1602.05557.  For an
even integer `q`, it asks for `q(q^2+q-1)` balanced `+/-1` vectors in
`R^(q(q+1))` that form an ETF and have pairwise inner products of absolute
value `q`.  The first open case in the paper is `q=6`.

This packet proves that the problem is exactly equivalent to the existence of
a quasi-symmetric design with explicit parameters.  For `q=6`, the required
object is a quasi-symmetric `2-(41,21,63)` design with 246 blocks, replication
126, and block intersections 9 and 12.  Its block graph would be
`SRG(246,140,85,72)` with eigenvalues `140,17,-4`.

The equivalence is constructive in both directions: normalize one ETF row and
take negative supports, or sign the incidence matrix of the design and add an
all-ones row.  This is a structural partial result, not a solution of the
remaining existence problem.

Verification:

```bash
conda run --no-capture-output -n sandbox python code/verify_parameters.py
```

Files:

- `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1602.05557.
- `supporting_paper_1402.3521.pdf`: two-distance tight-frame/SRG reference.
- `supporting_paper_2102.05576.pdf`: later quasi-symmetric restriction paper.
- `figures/problem_2_q6_crop.png`: exact source question and first open case.
- `code/verify_parameters.py`: exact integer/rational parameter audit.
- `verification.md`: proof and artifact audit.

Ledger:
`runs/fa_banach_001/ledger/results/1602.05557_flat_etf_quasisymmetric_design_equivalence.json`.
