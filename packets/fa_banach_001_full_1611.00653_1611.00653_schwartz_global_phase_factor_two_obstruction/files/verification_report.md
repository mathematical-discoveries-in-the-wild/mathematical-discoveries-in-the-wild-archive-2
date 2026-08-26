# Verification report

Target: the final displayed Schwartz-class variational question in Section
7.2 of arXiv:1611.00653.

1. **Polar energy identity.** For `u=rho exp(i omega)`, direct
   differentiation gives
   `|grad u|^2=|grad rho|^2+rho^2|grad omega|^2`.
2. **Jacobian bound.** Expanding
   `J(rho^2,omega)=2 rho det(grad rho,grad omega)` and applying determinant
   Cauchy--Schwarz followed by `2ab<=a^2+b^2` gives the pointwise energy
   majorant.
3. **Integrability.** Schwartz membership gives `rho in L^2` and finite
   energy. The polar identity gives `grad rho` and `rho grad omega` in `L^2`.
   Hence the Jacobian is `L^1` and
   `V=(rho^2 omega_y,-rho^2 omega_x)` is `L^1` by Hölder.
4. **Zero total Jacobian.** Distributionally `div V=J`. Testing with radial
   cutoffs `chi_R`, with `|grad chi_R|<=C/R`, gives
   `integral chi_R J -> 0`. Dominated convergence gives `integral J=0`.
5. **Factor two.** Zero signed integral implies
   `integral J_+ = (1/2) integral |J|`. Therefore
   `integral_E J <= (1/2) integral |grad u|^2` for every measurable `E`.
6. **Contradiction.** The requested strict inequality for any
   `0<delta<=1` contradicts the factor-two estimate. Since the source asks
   for every positive `delta`, no qualifying `E` exists.

No numerical or computer-assisted step is used. The only regularity assumed
is the classical/weak differentiability needed to state the source's
Jacobian and polar energy; smooth admissible functions are covered directly.
