# A c0 counterexample for Pasch–Hausdorff envelopes

Status: **claimed full counterexample; likely valid; pending human review**.

This packet answers the open question in Section 2 of Tang–Zhang–Guo,
arXiv:2110.05257, negatively.

Fix `0<c<1` in `c0` and let

```text
y_n = e_n + c(e_1+...+e_{n-1}),   A={y_n},   f=I_A.
```

The set `A` is sequentially weakly closed: a subsequence with indices tending
to infinity would converge coordinatewise to the constant vector `(c,c,...)`,
which is not in `c0`. Hence `f` is proper, bounded below, and sequentially
weakly lower semicontinuous. For every `k>0`, however,

```text
f_k(x)=k d(x,A),
d(0,A)=1,
d(e_n,A)<=c,
e_n -> 0 weakly.
```

Thus `liminf f_k(e_n)<=kc<k=f_k(0)`, so the envelope is not sequentially
weakly lower semicontinuous.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: real full-width crop of the question.
- `verification.md`: artifact and proof checks.

Primary review focus: sequential weak closedness of `A`.

