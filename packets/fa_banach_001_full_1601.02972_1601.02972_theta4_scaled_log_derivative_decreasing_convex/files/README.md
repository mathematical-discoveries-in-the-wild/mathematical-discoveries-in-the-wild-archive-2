# 1601.02972 — scaled logarithmic derivative of theta_4

Status: candidate full result, likely valid, human review needed.

Model: GPT5.6.

Source: Markus Faulhuber and Stefan Steinerberger, *Optimal Gabor frame
bounds for separable lattices and estimates for Jacobi theta functions*,
arXiv:1601.02972, source PDF page 3.

## Result

For

    theta_4(s) = sum_{k in Z} (-1)^k exp(-pi k^2 s),  s > 0,

the function

    H(s) = s^2 theta_4'(s) / theta_4(s)

is strictly decreasing and strictly convex on `(0,infinity)`.  This proves the
precise stronger behavior that the source says appears true but its arguments
cannot establish.

The proof splits at `s=1`.  For `s>=1`, Jacobi's product writes `H` as a
positive sum of rescaled copies of

    phi(x) = x^2 / (exp(x)-1),  x >= pi.

A direct two-derivative calculation shows that `phi` is strictly decreasing
and strictly convex there.  For `0<s<=1`, the imaginary transformation and
the product for `theta_2` give

    H(s) = pi/4 - s/2 + 2 pi sum_{n>=1} n sum_{j>=0}
           [exp(-C_{n,j}/s) - 3 exp(-D_{n,j}/s)],

where `C_{n,j}=2 pi n(2j+1)` and `D_{n,j}=2 pi n(2j+2)`.  Every bracket is
strictly increasing and strictly convex.  The derivative of the entire
correction is less than `0.32`, so the `-s/2` term forces strict decrease;
positive curvature of all brackets gives strict convexity.

## Files

- `main.tex`: theorem, proof intuition, and complete proof.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: readable crop of source PDF page 3.
- `code/crop_source.py`: reproducible source-crop script.
- `code/verify_numerics.py`: independent high-precision numerical smoke test.

## Human review recommendation

Review as a likely valid full solution.  The highest-value checks are the
small-parameter modular expansion, the factor `3` in its paired exponentials,
and the uniform derivative estimate for the correction term.

