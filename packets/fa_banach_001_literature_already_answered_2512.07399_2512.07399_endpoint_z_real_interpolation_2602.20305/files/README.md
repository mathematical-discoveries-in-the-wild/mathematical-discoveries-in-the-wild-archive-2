# Endpoint real interpolation of tent spaces

Status: `literature_already_answered (affirmative)`

## Original question

In Section 4, page 40 of the current PDF of arXiv:2512.07399, immediately
before Lemma 4.3, Auscher--Bechtel--Haardt discuss the endpoint omitted from
their Proposition 4.4: after defining their tent spaces only for
`0 < p < infinity`, can `Z^{infinity,q,r}_beta` also be characterized by real
interpolation of tent spaces?  The source package used by the queue described
this as future work.

## Decisive later answer

Luca Haardt, *A coherent theory of tent spaces and homogeneous
Triebel--Lizorkin spaces*, arXiv:2602.20305v2, introduces the endpoint
`T^{infinity,q,r}_beta` using a Carleson-box norm.  Proposition 3.31, page 51,
proves for every `0 < p <= infinity`, `0 < q,q_0,q_1,r <= infinity`, distinct
`beta_0,beta_1`, and `0 < theta < 1` that

```text
(T^{p,q_0,r}_{beta_0}, T^{p,q_1,r}_{beta_1})_{theta,q}
    = Z^{p,q,r}_{(1-theta)beta_0+theta beta_1}.
```

Taking `p = infinity` is exactly the missing endpoint characterization.  The
current PDF of the source paper now also points readers directly to this
proposition.

## Files

- `source_paper.pdf`: current arXiv PDF for 2512.07399.
- `supporting_paper_2602.20305.pdf`: decisive later paper, version 2.
- `solution_packet.pdf`: compact theorem-level identification note.
- Ledger: `runs/fa_banach_001/ledger/results/2512.07399_endpoint_z_real_interpolation_2602.20305.json`.
