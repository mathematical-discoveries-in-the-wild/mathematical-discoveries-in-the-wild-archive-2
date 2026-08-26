# Both GW analysis algorithms can miss the out-of-span projection weight

Status: `candidate_counterexample_likely_valid`.

Source: R. Díaz Martín, I. V. Medri, and J. M. Murphy,
*Gromov-Wasserstein Barycenters: The Analysis Problem*, arXiv:2507.09865.

## Result

The source supplement asks whether, for a target outside a prescribed
Gromov--Wasserstein barycenter span, the weights returned by its fixed-point
and blow-up analysis algorithms coincide with a minimizer of

```text
J(lambda) = GW(Y_lambda,Y)^2.
```

The answer is no, already for two uniform four-point metric spaces. For the
explicit rational metrics in the packet, the target is outside every true
two-template barycenter. Both proposed analysis quadratic programs have the
unique zero-residual solution

```text
lambda_alg = (1/2,1/2),
```

whereas the exact projection onto the true GW barycenter geodesic has the
unique minimizer

```text
lambda_proj = (1/10,9/10).
```

At these weights the squared projection costs are respectively `1/100` and
`1/125`. Thus the algorithmic weight is wrong by `2/5` and has 25 percent
larger objective. Scaling all four metrics preserves the weights and makes
the additive objective gap arbitrarily large.

The same example is a genuine metric-space Karcher mean which is not a true
GW barycenter, so unconditional equivalence also fails. It does not
characterize additional hypotheses under which equivalence can be restored.

## Files

- `solution_packet.pdf`: review-ready counterexample and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: locally compiled arXiv:2507.09865 source (58 pages).
- `figures/open_problem_crop.png`: source supplement page 49, equation (63)
  and the exact out-of-span questions.
- `verification.md`: proof, exact-enumeration, and rendering checks.
- `novelty.md`: bounded duplicate and priority audit.
- `code/make_crops.py`: reproducible source-evidence crop.
- `code/verify_counterexample.py`: exact rational verification of every
  permutation comparison and the projection minimizer.

Human review should focus on the conditional-negative-definiteness reduction
from all couplings to permutations, and on the identification of the source
algorithms' two data-dependent alignments.
