# Endpoint Ritt square functions need not be weak type (1,1)

Status: `candidate_full_counterexample_likely_valid`

Source: Jennifer Hults and Karin Reinhold-Larsson, *Square functions and
variational estimates for Ritt operators on L1*, arXiv:2507.07256v2,
Ergodic Theory and Dynamical Systems (2026), DOI
`10.1017/etds.2026.10293`.  Open Question 1 on PDF page 3 asks whether the
generalized square function `Q_{alpha,s,r}` is weak type `(1,1)` on the
endpoint `sr=alpha+1` for general Ritt operators on `L1`.

## Result

The answer is no.  On the Rademacher product probability space, let `D_m` be
the dyadic martingale differences and set

```text
delta_m=10^(-6m), lambda_m=1-delta_m,
T=E_0+sum_{m>=1} lambda_m D_m.
```

Bounded-variation formulas for martingale multipliers prove

```text
sup_n ||T^n|| <= 3,
sup_n n||T^n-T^(n+1)|| < 2/e,
```

so `T` is Ritt on `L1`.

For every `1<=s<2`, take `r=1` and `alpha=s-1`.  These parameters satisfy the
endpoint identity.  Disjoint time blocks around `n=1/delta_m` isolate the
`m`th martingale difference and give, for
`f_N=r_1+...+r_N`,

```text
Q_{s-1,s,1}^T f_N >= N^(1/s)/32 everywhere,
||f_N||_1 <= sqrt(N).
```

This contradicts weak type `(1,1)` because `1/s>1/2`.

## Scope and verification

The packet gives a full negative answer to the universal general-Ritt
question, and the same fixed operator refutes an entire endpoint interval
`1<=s<2`.  It does not settle the boundary `s=2` or subclasses of positive
contractions and convolution operators.

Eight focused audits cover operator-norm convergence, power boundedness, the
Ritt estimate, block localization, interference, the weak-type contradiction,
parameter scope, and novelty.  The numerical checker validates the scalar
bounds and finite identities but is not part of the proof.

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2507.07256_endpoint_ritt_square_weak11_counterexample/code/verify_counterexample.py
```

Human review should begin with the martingale multiplier summation-by-parts
formula and the past/future interference estimates on the lacunary blocks.

## Novelty status

Bounded searches through 2026-08-13 covered the exact question/title/DOI,
Ritt endpoint weak-type and martingale-multiplier variants, the local corpus,
the current ETDS paper, and adjacent Ritt square-function sources.  The
February 2026 accepted revision still asks the question, and no later answer
or matching construction was found.  Novelty is plausible, not certified;
priority is not claimed.

## Files

- `main.tex`: full proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: current arXiv source paper.
- `figures/open_question_crop.png`: full-width rendering of source PDF page 3.
- `code/verify_counterexample.py`: high-precision scalar checks.
- `VERIFIER_REPORT.md`: explicit verification record.
- `tmp/`: build and rendered-page intermediates.

