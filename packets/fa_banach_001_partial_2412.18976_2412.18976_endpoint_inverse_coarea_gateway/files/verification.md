# Verification and review checklist

## Analytic audit

- The polar-coordinate factor is `s^(n-1)` and the adjugate chain-rule bound
  contributes `|f-y0|^(1-n)`.
- Integrating first on target spheres and then over `y0 in B` gives the
  Riesz-kernel bound `int_B |z-y0|^(1-n) dy0 <= C r`.
- Finite distortion implies `adj Df=0` a.e. on `{J_f=0}`.
- Multiplicity one on the good set and the area formula on countably many
  Lipschitz pieces give
  `int_{f^{-1}(B)} |adj Df| = int_B g`.
- The quoted `1`-Poincare characterization is the same mechanism used in the
  endpoint homeomorphism proof of Csörnyei--Hencl--Malý.
- On the good image, inverse differentiation on Lipschitz pieces gives
  `Dh=(Df)^{-1}`; the Poincare density vanishes off that image.
- In the radial proposition, finite distortion forces `rho'>0` a.e. wherever
  `rho>0`; change of variables and integration by parts make both radial and
  tangential inverse eigenvalues integrable.

## Deliberately unclaimed steps

- No claim that endpoint `(INV)` automatically implies strong `(INV+)`.
- No claim that a critical `W^{1,n-1}` trace automatically has Lusin `(N)`.
- No claim that the source's generalized-inverse construction is already
  well-defined under the endpoint hypotheses without the listed structural
  properties.
- No claim of classical a.e. differentiability before `W^{1,1}` regularity is
  obtained.

## Human review recommendation

Check the projection-linking hypothesis against the precise topological-fiber
definition, the null-set clause in radial coarea, the use of the
`1`-Poincare-to-`W^{1,1}` theorem for vector-valued maps, and whether recent
work proves the critical structural package under a different name.
