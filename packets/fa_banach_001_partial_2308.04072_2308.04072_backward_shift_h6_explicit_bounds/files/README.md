# Partial result: explicit two-sided bounds on the backward shift in H^6

Status: partial result, likely valid, subject to human review.

Source: arXiv:2308.04072, Oleksiy Karlovych and Eugene Shargorodsky,
*Bounded compact and dual compact approximation properties of Hardy spaces:
new results and open problems*.

Open Problem 5.4 asks for the exact norm of the backward shift

```text
Bf(z) = (f(z)-f(0))/z
```

on `H^p` for finite `p`. The source passage is in
`figures/open_problem_crop.png`, and the source PDF is included.

## Result

The packet proves the rigorous bracket

```text
(6229716996096 / 1533633162625)^(1/6)
    <= ||B||_{H^6}
    <= 2^(1/3) phi^(1/6),
```

or numerically

```text
1.2631583709 <= ||B||_{H^6} <= 1.3651318687.
```

The lower bound is an exact mixed-moment calculation for

```text
I(z) = (32/35 + z)/(1 + (32/35)z),
f(z) = I(z) - 11/28.
```

The upper bound interpolates the May 2026 exact `H^4` norm
`phi^(1/4)` with the exact `H^infinity` norm `2`. The packet also records the
resulting piecewise interpolation upper bound for every finite exponent.

## Scope

This does not determine the exact `H^6` norm. Eight focused upgrade routes
are documented in `main.tex` and in the attempt note. The strongest exactness
route—a degree-six harmonic/SOS majorant tangent to the affine-inner
candidate—fails because the candidate circle occurs with odd multiplicity.

The literature check found exact results at `p=1,2,4,infinity`, but no exact
`p=6` result. A forthcoming 2026 estimates paper announced by the `H^4`
authors was not yet findable, so novelty confidence for the explicit lower
bound is moderate.

## Files

- `main.tex`: theorem, proof, literature status, and upgrade attempts.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original open-problem paper.
- `supporting_paper_2605.10469.pdf`: exact `H^4` supporting theorem.
- `figures/open_problem_crop.png`: source evidence.
- `code/verify_h6_bound.py`: exact symbolic verifier.

## Human review

Check the mixed-moment polynomial, rational substitution, and the standard
Hardy-space interpolation step including the `H^infinity` endpoint.
