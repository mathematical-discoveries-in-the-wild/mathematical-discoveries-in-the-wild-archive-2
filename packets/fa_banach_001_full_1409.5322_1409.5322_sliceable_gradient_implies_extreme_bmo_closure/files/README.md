# Sliceable gradients and the extreme BMO closure

This packet answers the future-work request in Remark 6.4(3) of
arXiv:1409.5322 by giving two broad sufficient conditions on the gradient.

The first result is quantitative:

`dist_BMO2(M, closure(L_infinity)) <= 2 sqrt(2) L_Z s_infinity`.

Thus a sliceable fractional gradient puts the comparison martingale in the
required closure. The paper's higher-integrability example extends from
`0<theta<eta<=1` to every `eta>theta`; in particular it now covers the
quadratic endpoint `theta=1` under `Z in bmo(S_(2 eta))`, `eta>1`.

The second criterion is wider: it is enough that the future fractional
energy `integral_tau^T |Z_s|^(2 theta) ds` have uniformly bounded conditional
exponential moments at every rate. This directly yields every reverse Holder
exponent for the comparison stochastic exponential, without requiring
sliceability.

## Files

- `solution_packet.pdf`: final proof packet.
- `main.tex`: reproducible LaTeX source.
- `source_paper.pdf`: Geiss--Ylinen source paper.
- `supporting_yan_kazamaki_2005.pdf`: primary source for the closure
  inclusion.
- `supporting_schachermayer_1996.pdf`: primary source for the sliceability
  characterization and strictness example.
- `figures/`: rendered evidence pages used during verification.

The result should receive human review as a short full sufficient-condition
resolution with a quantitative strengthening.
