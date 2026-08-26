# Fock-space power boundedness for compact and zero-free weights

Source target: arXiv:2201.09249, Section 6.2.2, PDF page 29. The source says
that power boundedness for a bounded weighted composition operator
`W_{u,phi}` on a Fock space with `phi(z)=az+b` and `|a|<1` is apparently
unsolved.

This packet proves a substantial partial classification for every
`1 <= p < infinity`:

- For an arbitrary bounded **compact** `W_{u,phi}`, power boundedness is
  equivalent to `|u(b/(1-a))| <= 1`; zeros of `u` are allowed.
- For every bounded **zero-free** weight, this criterion remains exact unless
  the operator is noncompact and `a` is a nonzero real number.
- In that exceptional real boundary case, the sharp criterion is
  `|u(b/(1-a))| <= |a|^(1/p)`.

Thus the only untreated class is noncompact with a weight that has zeros.
The proof closes the published gap by reducing to a Gaussian strip measure:
its Fock-Carleson mass is comparable to `|a|^{-n}`, so the nth power norm is
comparable to

`(|u(b/(1-a))| |a|^{-1/p})^n`.

The packet includes the exact source page, the two closest supporting papers,
eight focused upgrade attempts, and an explicit noncompact zero-bearing
example explaining the residual obstruction.

Status: substantial partial result, likely valid, pending human review.
