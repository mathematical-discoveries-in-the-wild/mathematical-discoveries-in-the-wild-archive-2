# Attempt record

Target: Remark (2) after the source's corollary, asking whether convergence to the Gibbs mode holds for every initial condition in `ell^2` without truncation.

1. **Coefficientwise limit.** The spectral expansion makes every fixed non-Gibbs coefficient tend to zero. This alone is insufficient for a conditional Schauder basis, so a direct dominated-convergence argument was rejected.

2. **General semigroup stability theorems.** The spectral bound is zero and zero is an accumulation point; standard exponential-stability criteria do not apply. Compactness of `A` also makes `exp(tA)=I+compact`, which predicts the failure of operator-norm convergence.

3. **Abel summation for monotone basis multipliers.** The source orders `nu_2<nu_3<...<0` with `nu_k -> 0`. Thus, for fixed `t`, the multipliers `exp(t nu_k)` increase to one and have total variation exactly one after adjoining the zero Gibbs coefficient. Abel summation against the uniformly bounded partial-sum projections gives a bound independent of `t`. Density of finite basis spans then proves strong convergence for all `ell^2` data.

4. **Quantitative and sharpness audit.** Truncating the multiplier at index `N` has total variation at most `2 exp(t nu_N)`, yielding a head–tail estimate. Conversely, the eigenvector test gives operator norm at least `sup_k exp(t nu_k)=1` for every `t`; hence no uniform decay rate can be asserted. This delineates exactly what the full answer does and does not provide.

5. **Later-literature audit.** Exact-title, exact-question, author, citation, and related master-equation searches through 2026-08-12 found the published source and a 2023 grand-canonical paper in a different weighted self-adjoint sequence space, but no later statement resolving this exact nonnormal ordinary-`ell^2` question.
