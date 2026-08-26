# Diagonal sampled second-order Riesz transform is unbounded

Status: `counterexample_likely_valid`

Source: R. Bañuelos and D. Kim, *Discrete analogues of second-order Riesz
transforms*, arXiv:2504.18739v2.

## Result

Conjecture 1.4, equation (1.24), includes the claim that the sampled diagonal
operator

```text
R_dis^(jj) f(n) = sum_m c_d m_j^2 / |m|^(d+2) f(n-m)
```

has the same finite `ell^p` norm as the classical diagonal second-order Riesz
transform. Under the literal definition (1.16)--(1.17), this is false.

For every `d>=2`, every diagonal index `j`, and every `1<p<=infinity`, the
displayed convolution operator is unbounded on `ell^p(Z^d)`. Large box
indicators and disjoint dyadic cones give an output lower bound proportional
to `log N` on a fixed fraction of the input box. At `p=2`, the discrete norm
is therefore infinite, whereas the source records the classical norm as
`gamma(2)=1`.

This fully refutes the universally quantified conjecture as stated. It does
not settle its off-diagonal or trace-free-difference clauses, whose kernels
retain cancellation.

## Source diagnosis

The source's all-index kernel factorization separates two coordinate factors;
that separation is invalid when `j=k` because both derivatives occupy the
same coordinate. The next page also displays a strictly positive integral as
its own negative and declares it zero. The counterexample is independent of
this diagnosis.

## Files

- `solution_packet.pdf`: self-contained counterexample and source audit.
- `source_paper.pdf`: current official arXiv v2 PDF (37 pages).
- `figures/source_definition.png`: equations (1.16)--(1.17).
- `figures/source_conjecture.png`: Conjecture 1.4, including (1.24).
- `figures/source_proof_flaw.png`: the source's page-21 sign failure.
- `code/verify_box_lower_bound.py`: numerical sanity check only.
- `code/make_source_crops.py`: reproducible source crop generator.
- Attempt audit:
  `runs/fa_banach_001/attempts/2504.18739_diagonal_discrete_riesz_unbounded_counterexample.md`.
- Ledger:
  `runs/fa_banach_001/ledger/results/2504.18739_diagonal_discrete_riesz_unbounded.json`.

## Novelty and review

The four cheap run indexes and bounded exact/nearby searches found no prior
answer, correction, or erratum. Expert review should first confirm that the
paper intends the diagonal formula literally, without an unstated local
compensation. Under the displayed definition, the box proof is elementary.

Final packet verification: 5 letter-size pages, 611634 bytes; every page was
rendered at 144 dpi and visually inspected with no clipping, overlap, or
illegible source evidence. SHA-256:
`252548002c9b5360f2fa807ef2acc9968465f9aff24352326230d78c6a77e50d`.
