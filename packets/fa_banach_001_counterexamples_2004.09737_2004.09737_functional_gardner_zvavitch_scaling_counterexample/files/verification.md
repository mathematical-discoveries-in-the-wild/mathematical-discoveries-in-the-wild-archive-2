# Verification record

## Verdict

`counterexample_likely_valid`, pending expert review.

The construction contradicts the exact conclusion of Roysdon--Xing Conjecture 6.2 while satisfying its displayed pointwise hypothesis in the one-dimensional p = 1 case.

## Exact checks

- For p = 1 and t = 1/2, all lambda dependence disappears and the premise becomes
  `h((x+y)/2) >= sqrt(f(x)g(y))`.
- With `f_M=M exp(-x^2)`, `g_M=M^{-1} exp(-x^2)`, and `h=exp(-x^2)`, reciprocal amplitudes cancel on the right.
- The exponent gap is exactly `(x-y)^2/4`, so the premise holds for all real x and y.
- For standard Gaussian measure, `A = integral exp(-x^2) d gamma_1 = 1/sqrt(3)`.
- The proposed conclusion reduces exactly to `1 >= (M+M^{-1})/(2C)`, which fails whenever M is sufficiently large.
- The functions are smooth, positive, even, strictly log-concave, Lebesgue-integrable, Gaussian-integrable, centered by barycenter, and maximized at the origin.

## Computational check

Run:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/2004.09737_functional_gardner_zvavitch_scaling_counterexample/code/verify_counterexample.py

The script performs exact SymPy reductions and checks explicit violating parameters for several values of C. The proof does not depend on numerical computation.

## Bounded novelty check

Searches performed on 2026-08-09:

- exact phrase `Functional L_p-Gardner-Zvavitch conjecture`;
- exact title and arXiv:2004.09737, including citation-oriented searches;
- `functional Gardner-Zvavitch counterexample` and close variants;
- the same Conjecture 6.2 reproduced in the corresponding 2020 dissertation;
- later papers and announcements on functional or Gaussian Gardner--Zvavitch inequalities.

The searches found the source statement, its dissertation duplicate, and later work on normalized or geometric variants, but no matching counterexample to Conjecture 6.2 as written. Novelty is plausible, not certified.

## Scope and reviewer priorities

1. Confirm that "centered" in Conjecture 6.2 carries no unstated amplitude normalization. Both standard centering meanings are satisfied by the example.
2. Confirm the p = 1 specialization of the displayed premise and conclusion.
3. Keep the scope exact: this disproves only the unnormalized functional conjecture. It does not disprove equal-height, probability-normalized, sup-normalized, or geometric Gardner--Zvavitch statements.
