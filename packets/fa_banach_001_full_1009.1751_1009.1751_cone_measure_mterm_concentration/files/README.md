# Sharp cone-measure concentration for positive best m-term error

**Status:** candidate full answer, likely valid, pending expert review.

**Source:** Jan Vybíral, *Average best m-term approximation*,
arXiv:1009.1751, Remark 1(i), source PDF page 16.

Writing `k=m+1`, the packet proves that for every finite `p>0`, throughout
the nontrivial upper-tail range,

`mu_p{n^{1/p} x_k^*>t}=exp(-Theta_p(k t^p))`.

The range begins at the natural scale
`t asymp [log(en/k)]^{1/p}` and extends to a constant multiple of
`(n/k)^{1/p}`.  It also proves a constant-factor high-probability window around
`[log(en/k)/n]^{1/p}`.  Since `sigma_m(x)_infinity=x^*_{m+1}`, this is the
concentration statement requested after Theorem 7 and strictly strengthens
the mean estimate there.  For `p=infinity`, an exact binomial formula is given.

## Contents

- `solution_packet.pdf`: theorem, proof, verification, and novelty scope.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source Remark 1(i).
- `code/check_concentration_scaling.py`: Monte Carlo regression check.
- `verification.md`: symbolic and computational checks.
- `tmp/`: build and rendering intermediates.

## Human-review recommendation

Check the two normalizations in the lower-tail construction: the Gamma sum is
bounded above, while the selected Gamma coordinates are bounded both below
and above.  Also verify that the deterministic range
`k t^p <= b_p^p n` is exactly what allows the selected coordinates to remain
above threshold after normalization.

