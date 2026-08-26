# Verification audit

## Counterexample audit

1. `R^2` with Lebesgue measure is doubling, supports a 2-Poincare
   inequality, and has the annular chain property at the origin.
2. The singleton direction space with its point mass and the ray
   `gamma(t)=(t,0)` is an allowed family of infinite curves from the origin.
3. The coordinate weight is Borel, is zero at every point of the ray, and is
   `exp(|x|)` elsewhere.  Thus the left side of the weak-polar inequality is
   zero for every integrable test function, so the inequality holds with
   constant one.
4. The ray is planar-Lebesgue-null, hence the negative power of the weight is
   `exp(-2|x|)` almost everywhere.  Polar integration gives
   `R_2=(3*pi/2)e^{-2}`.
5. The dyadic annulus `A_{2^j}` has area `3*pi*4^j`, so each summand of
   `mathcal R_2` is `1/(3*pi)` and the series diverges.
6. The shifted ray family has 2-modulus zero: its first unit segment has
   planar measure zero, and its indicator is an admissible density of zero
   `L^2` cost.  Thus property 4 of Theorem 1.3 fails despite finite `R_2`.

## Repair audit

Under positivity for line-almost every radial point, bounded truncations of
`indicator_A/h` converge in the weak-polar inequality to the unweighted
annular length.  Every infinite curve from the base point crosses a dyadic
annulus through radial distance `2^j`, contributing length at least `2^j`.
Holder's inequality then yields the exact annular summand bound; disjointness
allows summation.  The `p=1` endpoint follows from the essential-supremum
definition of `R_1`.  No doubling, Poincare, or annular-chain argument is
needed for the repaired numerical implication itself.

## Reproduction commands

From the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2203.01020_weak_polar_zero_weight_obstruction/code/verify_zero_weight_counterexample.py

cd runs/fa_banach_001/solutions/counterexamples/2203.01020_weak_polar_zero_weight_obstruction
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp main.tex
```

The script checks the closed-form integrals and annular terms; it is not a
substitute for the measure-theoretic proof.

## Final artifact audit

- Exact-formula sanity checks passed, including 1,000 dyadic summands.
- LaTeX compiled twice with no warnings, undefined references, overfull
  boxes, or underfull boxes.
- Both complete source crops and all five rendered letter-size pages were
  visually inspected.
- `solution_packet.pdf` SHA-256:
  `d9811ff2ed15f8b7684462e310aef7fb2dae90c11d9e3b68043ba4c9320474a9`.
