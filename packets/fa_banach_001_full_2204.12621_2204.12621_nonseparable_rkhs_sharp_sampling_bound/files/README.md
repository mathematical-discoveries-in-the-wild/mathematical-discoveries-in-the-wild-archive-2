# Sharp sampling bound for nonseparable RKHSs

Status: **full proof candidate**.

Remark 13 of Dolbeault--Krieg--Ullrich, arXiv:2204.12621, predicts that
their sharp sampling-number theorem should remain true without RKHS
separability after adding `tr_0(K)/m` under the square root. This packet proves
that prediction: for a universal integer `C`,

```text
g_{C m}(B_H)^2 <= (tr_0(K) + sum_{k>=m} d_k(B_H)^2) / m.
```

The proof combines the source's infinite-vector Kadison--Singer
subsampling with the nonseparable spectral/null decomposition of
Moeller--Ullrich, arXiv:2009.11940. The key new observation is that, under a
three-component leverage density, the null-space sampling Gram matrix is
almost surely diagonal and remains uniformly controlled after the source's
subsampling step.

Contents:

- `solution_packet.pdf`: theorem, proof intuition, full proof, audits, and
  provenance.
- `source_paper.pdf`: Dolbeault--Krieg--Ullrich, arXiv:2204.12621.
- `supporting_paper_2009.11940.pdf`: Moeller--Ullrich,
  arXiv:2009.11940.

The packet makes a mathematical full-proof claim, not a certified priority
claim. Exact-phrase, symbol, and later-arXiv searches performed on 9 August
2026 found no matching theorem.

Ledger:
`runs/fa_banach_001/ledger/results/2204.12621_nonseparable_rkhs_sharp_sampling_bound.json`.
