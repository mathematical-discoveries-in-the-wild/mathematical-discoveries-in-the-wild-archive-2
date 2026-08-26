# Uniform vertical Cheeger bounds for the proposed Gabor counterexamples

Status: `candidate_sharp_partial_likely_valid`.

For the source pair

```text
f_± = Gaussian ± i gamma T_d Gaussian,   d=1/a,
```

the packet proves that choosing `gamma <= exp(-pi d^2/2)` makes the Cheeger
ratio of every vertical half-plane cut uniformly positive, independently of
the separation `d`.  This rigorously rules out the visually obvious
two-bump cut as the cause of whole-plane instability.

The proof identifies the vertical marginal with a quantity uniformly
comparable to an extremely unbalanced two-Gaussian mixture and proves a
uniform one-dimensional hazard bound for that mixture.

This is a sharp partial upgrade, not a full answer.  The whole-plane
local-Lipschitz estimate requires control of arbitrary weighted cuts (or the
full analytic Poincare constant).  The STFT weight has an isolated periodic
zero comb and is not log-concave, so vertical-cut control alone does not imply
the required global isoperimetric inequality.

See `solution_packet.pdf` for the complete proof and scope boundary.  Eight
focused upgrade attempts are recorded in the corresponding attempt note.
