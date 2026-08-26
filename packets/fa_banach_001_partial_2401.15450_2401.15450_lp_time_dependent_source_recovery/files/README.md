# Frame characterizations for time-dependent source recovery

Promoted partial result for the future-work program in arXiv:2401.15450.

After choosing standard natural norms, the spatial condition has an exact
answer. For every `1 <= p <= infinity`:

- in discrete time, universal stable recovery
  `ell^p(N_0;ell^2) -> ell^p(N_0;H)` of arbitrary time-dependent sources is
  possible if and only if the sampling Bessel family is a frame;
- for bounded continuous generators, universal stable recovery
  `W^{1,p}(0,T;ell^2) -> L^p(0,T;H)` of arbitrary time-dependent forcing is
  possible if and only if the family is a frame.

Both directions are explicit. If `C` is the analysis operator and `L C=I`,
then the recovery maps are

```text
(R_discrete y)_n = L y_{n+1} - A L y_n,
R_continuous(y) = L y' - A L y.
```

Necessity follows from a one-pulse discrete trajectory and an exponential
continuous trajectory.

## Files

- `main.tex`: self-contained statements and proofs.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: page-22 future-work statement.
- `figures/continuous_future_crop.png`: page-23 continuous-time continuation.

The result is partial relative to the source's open-ended program: it does not
classify constant-source observability for arbitrary unbounded semigroup
generators.
