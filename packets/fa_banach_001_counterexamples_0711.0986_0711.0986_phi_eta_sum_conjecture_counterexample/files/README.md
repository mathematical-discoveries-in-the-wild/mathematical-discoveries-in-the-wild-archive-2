# Counterexample to the aggregate phi/eta comparison

Kontorovich (arXiv:0711.0986, published in *Statistics & Probability
Letters* 78 (2008), 2910--2915) records the conjecture

```text
(1/2) sum_{r=1}^{n-1} phi_r
    <= 1 + max_i sum_{j=i+1}^n bar_eta_{ij}.
```

This packet gives a finite-alphabet, full-support counterexample. It combines
`L=1024` independent delayed binary channels in a sequence of length `n=2L`.
Every nonzero eta row has sum exactly `1`, so the right side is `2`, whereas a
self-contained total-variation estimate gives

```text
(1/2) sum_r phi_r > 2.933.
```

Direct binomial evaluation gives the stronger numerical lower value `4.259`.

Files:

- `main.tex` — self-contained counterexample manuscript;
- `solution_packet.pdf` — compiled review packet;
- `verification.md` — definition, constant, and novelty audit;
- `code/check_counterexample.py` — analytic and exact-binomial checks;
- `source_paper.pdf` — official arXiv PDF;
- `figures/open_problem_page-02.png` — source page containing the conjecture.

Status: `counterexample_likely_valid`. Human review should prioritize the
finite-sequence convention for `phi_r` and the exact eta-matrix calculation.
