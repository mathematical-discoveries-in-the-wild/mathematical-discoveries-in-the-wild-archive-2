# Exponential semiaxes have an unavoidable square-root gap

Status: `candidate_full_counterexample_likely_valid`

Model: `GPT5.6`

Source: Aicke Hinrichs, David Krieg, Erich Novak, Joscha Prochno, and
Mario Ullrich, *Random sections of ellipsoids and the power of random
information*, arXiv:1901.06639v2, PDF page 8.

## Result

The source asks whether Gaussian random information is within a constant
factor of optimal information when the ellipsoid semiaxes decay
exponentially.  The answer is no for every such sequence.

If `0<a<1` and

```text
c_0 a^j <= sigma_j <= C_0 a^j,
```

then, for all `n>=22`,

```text
E[R_n(sigma)] >=
  [c_0 sqrt(1-a^2)/(4 sqrt(2))] sqrt(n+1) a^(n+1).
```

Since optimal information has radius `sigma_(n+1)`, the ratio is at least a
positive constant times `sqrt(n)`.  Thus the proposed comparison
`E[R_n(sigma)] asymp sigma_(n+1)` fails throughout the exponential class.

## Mechanism

Restrict the `n` Gaussian measurements to the first `n+1` coordinates.  The
kernel is a uniformly random line.  If its unit direction is represented as
`g/||g||`, the line section has radius

```text
a^(n+1) ||g|| /
  sqrt(sum_(r=0)^n a^(2r) g_(n+1-r)^2).
```

The numerator is typically of order `sqrt(n)`, while the geometrically
weighted denominator stays of constant order.  This line lies inside the full
infinite-dimensional kernel, so its radius is a valid lower bound.

## Files

- `main.tex`: source question, proof intuition, theorem, and complete proof.
- `solution_packet.pdf`: compiled review packet.
- `VERIFICATION.md`: proof, source, novelty, computation, and render audit.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: full-width crop from source PDF page 8.
- `code/check_random_line_scaling.py`: optional Monte Carlo sanity check; not
  used as proof.
- Run attempt note:
  `attempts/1901.06639_exponential_axes_random_line_counterexample_attempt.md`.

Human review should focus on the finite-coordinate kernel inclusion, the
uniform-sphere law of its null direction, and the two elementary probability
bounds producing the explicit constant.
