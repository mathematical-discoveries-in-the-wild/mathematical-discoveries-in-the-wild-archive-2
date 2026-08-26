# A positivity-preserver with a non-hyperbolic inverse

This packet gives a negative answer to Problem 2 on page 3 of arXiv:0801.1749.

Let `D=d/dx` and

`U = (99/100) cosh(D) + (1/100) exp(D^2/2)`.

This is averaging over a probability measure consisting of 99 percent equal
mass at `-1,+1` and one percent standard Gaussian mass, so it preserves every
strictly positive polynomial.  The Gaussian component makes every finite
moment Hankel form strictly positive definite.  Nevertheless, direct formal
series inversion gives

`U^{-1}(x^6) = x^6 - 15 x^4 + (747/10) x^2 - 3027/50`.

The corresponding cubic in `x^2`, after multiplication by 50, has
discriminant `-668917845000`, so the output has nonreal zeros although `x^6`
is hyperbolic.

Status: `candidate_counterexample_likely_valid`, pending human review.

Files:

- `main.tex`: complete proof and full-support Gaussian upgrade.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: readable source excerpt.
- `code/verify_counterexample.py`: exact symbolic coefficient and
  discriminant check.
- `VERIFICATION.md`: proof, build, visual-QA, and hash record.
