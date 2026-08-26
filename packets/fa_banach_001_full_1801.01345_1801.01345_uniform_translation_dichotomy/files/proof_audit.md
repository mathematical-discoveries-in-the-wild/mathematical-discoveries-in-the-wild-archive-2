# Proof audit

**Verdict:** likely valid full dichotomy.  
**Exact scope:** all nonzero de Branges spaces with `sup_{t in R} ||U_t|| < infinity`; the conclusion is `PW_a` or the one-dimensional constant space.

Checks performed:

1. **Averaging bounds.** Since `U_t^{-1}=U_{-t}`, the uniform upper bound gives a uniform lower bound. Every interval average `A_T` therefore lies between `C^{-2}I` and `C^2I`; these inequalities pass to a weak-operator cluster point.
2. **Translation invariance of the limit.** Conjugating `A_T` by `U_s` translates `[-T,T]`. The symmetric difference has length `2|s|`, and the integrand is uniformly bounded, so the difference tends weakly to zero.
3. **De Branges axioms survive.** Conjugation commutes with real translations. For the zero-moving map, the exact identity is `U_t R_w=R_{w-t}U_t`, and `U_tF` vanishes at `w-t`; the old norm equality therefore holds pointwise under the average.
4. **Kernel-to-matrix step.** Two independent real rows `V(x_1),V(x_2)` define `M_t`. Kernel determinant invariance gives `det M_t=1` and shows every other row transforms by the same matrix. Uniqueness gives the group law, and explicit dependence on the two selected rows gives continuity.
5. **Generator classification.** For `X in sl(2,R)`, Cayley--Hamilton gives `X^2=-(det X)I`. The packet's symbolic script verifies representative elliptic, parabolic, and hyperbolic determinant kernels. The result is conjugacy-invariant up to the single positive kernel scalar.
6. **Positivity exclusion.** In the hyperbolic case the normalized off-diagonal entry is `sinh(ad)/(ad)>1`, so the two-point Gram determinant is negative. No global or asymptotic argument is needed.
7. **Edge case.** A constant kernel gives precisely the constant functions, realized by `H(z+i)`. This space genuinely meets the source's literal translation hypothesis, so the finite-dimensional caveat is necessary.
8. **Literature boundary.** Cheap indexes and bounded searches through 2026-08-13 found no exact resolution. Later translation/composition papers treat individual operators and do not state the full-group dichotomy.

Primary reviewer focus: the weak-operator cluster construction, the determinant argument defining `M_t`, and the distinction between the intended infinite-dimensional converse and the literal one-dimensional exception.
