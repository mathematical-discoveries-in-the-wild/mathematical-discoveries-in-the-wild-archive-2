# Counterexample packet: duplication defeats the many-polynomial Bezout estimate

Status: `candidate_counterexample_likely_valid`

Source: Emmanuel Fricain, Andreas Hartmann, William T. Ross, and Dan Timotin,
*An analytic approach to estimating the solutions of Bezout's polynomial
identity*, arXiv:2310.12734v3, Section 10.4, printed page 26.

## Result

The open problem's proposed estimate is false, even for degree-one
polynomials whose coefficient norms are all exactly one.

For any positive integer `m`, take `q=2m`, with `m` copies of `z` and `m`
copies of `1-z`.  The source separation parameter is `delta=m`.  In every
polynomial Bezout solution, evaluation at zero forces the constant terms of
the `m` coefficients paired with `1-z` to sum to one.  Hence at least one
solution polynomial has coefficient norm at least `1/m`.  A constant
depending only on the maximal degree would instead give the upper bound
`C/delta^2=C/m^2`, which is impossible once `m>C`.

The lower bound is exact: taking every solution polynomial equal to `1/m`
gives the identity.  Thus the optimal value for this family is

```text
1/m = q/(2 delta^2).
```

Consequently, any corrected estimate that retains the `delta^-2` form must
allow at least linear dependence on the number `q` of input polynomials.

## Files

- `main.tex`: self-contained source statement, theorem, proof, and scope audit.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/source_open_problem_page26.png`: complete source page containing
  the problem.
- `code/check_duplication_counterexample.py`: exact symbolic and numerical
  sanity checks; not used as proof.
- `verification.md`: proof, computation, literature, and visual QA record.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2310.12734_many_polynomial_bezout_delta_counterexample/code/check_duplication_counterexample.py
```

Human review should check only the source interpretation, the two evaluations
at `z=0,1`, and the quantifier contradiction `m>C`.

## Novelty status

On 2026-08-09, the run's cheap indexes and exact/core web searches were
checked, including the current arXiv record and author/citation search pages.
No later resolution or this duplication counterexample was found.  This is a
bounded novelty check, not a certification of priority.

Ledger:
`runs/fa_banach_001/ledger/results/2310.12734_many_polynomial_bezout_delta_counterexample.json`
