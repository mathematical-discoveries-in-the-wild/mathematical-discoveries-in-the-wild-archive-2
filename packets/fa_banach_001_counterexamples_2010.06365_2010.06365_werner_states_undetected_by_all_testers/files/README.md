# Counterexample: Entangled Werner States Invisible to Every Tester

Status: `counterexample` (candidate; subject to human review)

Source: Maria Anastasia Jivulescu, Cecilia Lancien, and Ion Nechita,
*Multipartite Entanglement Detection Via Projective Tensor Norms*,
arXiv:2010.06365; *Annales Henri Poincare* 23 (2022), 3791--3838.

## Negative Answer

The source asks whether every entangled state is detected, without an index
permutation, by some tensor product of contractions from `S_1` to Hilbert
space followed by the output projective norm.

The answer is no.  For every `d >= 3`, the Werner states

```text
sigma_mu = mu (I+F)/(d(d+1)) + (1-mu)(I-F)/(d(d-1))
```

with `1/d <= mu < 1/2` are entangled, but every pair of testers `E,F`
satisfies

```text
||(E tensor F)(sigma_mu)||_pi <= 1.
```

The simplest explicit example is on `C^3 tensor C^3`:

```text
rho_* = (5 I - 3 F)/36 = sigma_{1/3}.
```

It has `Tr(F rho_*)=-1/3`, so it is entangled, while its supremum over all
tester criteria is exactly `1`.

## Sharp Strengthening

For every Werner state, the exact envelope over all tailored tester pairs is

```text
sup_{E,F} ||(E tensor F)(sigma_mu)||_pi
  = 1 + 2 max(0, 1/d-mu).
```

Thus the ordinary realignment tester is globally optimal on this family.

The proof averages every Hilbert-factorable witness to `a I+b F` and computes
the factorization norm exactly:

```text
gamma_2(T_{a,b})
  = max(|b|, |a+b/d| + (1-1/d)|b|).
```

The upper bound is an explicit scalar/traceless Hilbert-Schmidt
factorization.  The lower bound combines an off-diagonal matrix unit with a
nuclear-norm bound on the diagonal restriction `a J+b I`.

## Files

- `solution_packet.pdf`: rendered proof and verification report.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: source page 35 with the exact question.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `code/verify_werner_counterexample.py`: supplementary numerical checks.
- `verification.md`: proof, computation, and novelty audit.

## Novelty Status

A bounded local/arXiv/web search on August 11, 2026 found no prior negative
answer or computation of the all-tester Werner envelope.  The source's six
indexed citing works through 2025 were checked at title/abstract or full-text
citation context; none states this result.  Novelty is plausible, not
certified.
