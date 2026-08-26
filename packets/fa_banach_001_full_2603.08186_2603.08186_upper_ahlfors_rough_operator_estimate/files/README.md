# Upper-Ahlfors rough-operator estimate

Status: `candidate_full_likely_valid`.

This packet gives a full positive answer to the open problem in
arXiv:2603.08186.  The pointwise estimate

```text
T_K^* f(x) <= C R_{1,mu}(g)(x)
```

requires only the upper Ahlfors bound `mu(B(x,r)) <= c_2 r^nu`, not a lower
Ahlfors bound or the source restriction `2^(1-nu)c_2/c_1 < 1`.

The key estimate keeps the annular measure through Holder and the
Poincare--Sobolev inequality:

```text
2^(-k nu) integral_{A_k} |f-f_{B_k}|
  <= C 2^(k(1-nu)) integral_{sigma B_k} g.
```

The scale sum is geometric for `nu>1`; upper Ahlfors regularity then turns
`d(x,y)^(1-nu)` into the modified Riesz kernel
`d(x,y)/mu(B(x,d(x,y)))`.

The human-facing artifact is `solution_packet.pdf`.  `source_paper.pdf` and
the exact source crops are included for audit.
