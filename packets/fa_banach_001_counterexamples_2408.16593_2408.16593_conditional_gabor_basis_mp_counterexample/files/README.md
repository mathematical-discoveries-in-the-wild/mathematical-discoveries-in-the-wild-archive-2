# Conditional Gabor basis counterexample in every M^p, 1<p<2

This packet gives a candidate full negative answer to Question 5.1 of
arXiv:2408.16593.

For every `1<p<2`, choose `0<delta<1-1/p` and take the endpoint-power window
from Heil--Powell Example 5.11. Its critical lattice Gabor system is a
conditional Schauder basis of `L2`, its unique dual is `gamma=1/g` on
`(0,1)`, and both windows belong to `M^p`. The new regularity calculation is

`gamma_hat(n) ~ C_delta |n|^(delta-1)`, with `C_delta>0`,

so `gamma in M^r` exactly when `r(1-delta)>1` for `1<r<=2`. The basis is not
Riesz and therefore fails unconditional convergence for some `f in M^2`.

## Files

- `main.tex` / `solution_packet.pdf`: complete proof and provenance.
- `verification.md`: adversarial audit.
- `code/check_endpoint_asymptotic.py`: finite numerical sanity check only.
- `source_paper.pdf`: arXiv:2408.16593.
- `supporting_paper_heil_powell_2006.pdf`: source of the conditional basis.
- `figures/`: crops of the open question and the decisive prior results.

## Status

`counterexample_likely_valid`; human harmonic-analysis review recommended.

