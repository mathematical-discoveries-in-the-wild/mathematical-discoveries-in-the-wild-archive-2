# Partial Result: Multi-center A1 mixtures at the Rubio endpoint

- **Source:** Amenta–Lorist–Veraar, *Rescaled extrapolation for vector-valued functions*, arXiv:1703.06044.
- **Target:** the scalar strong endpoint `p=q'`; principally the outstanding `q=2`, `w in A1` Rubio de Francia square-function conjecture.
- **Status:** `candidate_partial_likely_valid`.
- **Model:** `GPT5.6`.

## Result

The strong `L2(w)` endpoint class proved in arXiv:2308.01442 for even radially decreasing `A1` weights is closed under arbitrary positive mixtures with a uniform `A1` characteristic. Therefore the endpoint holds uniformly for genuinely nonradial multi-center/multiscale weights such as

```text
w(x) = sum_j c_j (1 + |x-a_j|/r_j)^(-alpha),  0<alpha<1,
```

whenever the sum is finite almost everywhere and locally integrable. The constant depends only on `alpha`, not on the number, positions, scales, or coefficients of the kernels.

The packet also proves a focused full-problem reduction: every `A1` weight of bounded characteristic is comparable to a positive mixture of Coifman–Rochberg weights `(M 1_E)^delta`. Thus proving the endpoint uniformly for that special family would settle the full `q=2` conjecture.

## Proof idea

After squaring, the weighted endpoint inequality is linear in the weight. Tonelli therefore integrates any uniform family of endpoint estimates. Sublinearity of the maximal operator simultaneously preserves the `A1` constant. The reduction uses reverse Hölder on the dyadic level sets `{w>2^k}` and a convergent geometric series.

## Scope

This does **not** prove the conjecture for every `A1` weight. The unresolved step is the endpoint estimate for general `(M 1_E)^delta`; these weights are not shown to belong to the radial mixture cone. Endpoint cases `p=q'<2` also remain open.

## Files

- `main.tex` — proof packet, explicit kernel class, and conditional reduction.
- `solution_packet.pdf` — rendered packet.
- `source_paper.pdf` — arXiv:1703.06044.
- `supporting_paper_2308.01442.pdf` — decisive 2023 radial/Walsh endpoint paper.
