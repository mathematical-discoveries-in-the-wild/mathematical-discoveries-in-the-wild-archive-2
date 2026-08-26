# Verification record

## Statement audited

For the Bloch and star-little Bloch spaces defined in arXiv:2208.02147 on the
unit polydisk,

```text
omega_0(z)=omega(z)=rho(z,0)
            =(sum_j arctanh(|z_j|)^2)^(1/2).
```

## Checks

1. **Metric duality.** From
   `H_w(u,u)=sum_j |u_j|^2/(1-|w_j|^2)^2`, direct finite-dimensional duality
   gives

   ```text
   Q_f(w)^2=sum_j (1-|w_j|^2)^2 |partial_j f(w)|^2.
   ```

2. **Product distance.** For any path from `0` to `z`, Minkowski's integral
   inequality bounds its length below by the Euclidean norm of the coordinate
   disk distances.  The synchronized radial path
   `gamma_j(t)=phase(z_j)*tanh(t*arctanh(|z_j|))` attains the bound.
3. **Extremal phase.** Taking `eta_j=conj(z_j)/|z_j|` makes
   `eta_j z_j=|z_j|`, so every summand of the target value is positive real;
   there is no cancellation.
4. **Bloch bound.** The elementary inequality

   ```text
   |1-s^2 eta^2 w^2| >= 1-s^2|w|^2 >= s(1-|w|^2)
   ```

   proves `beta_{F_s}<=1` for every `0<s<=1`.
5. **Little-star membership.** For `s<1`, `F_s` extends holomorphically to a
   neighborhood of the closed polydisk.  Its derivatives are bounded, while
   every factor `1-|w_j|^2` tends to zero at the distinguished boundary;
   hence `Q_{F_s}(w)->0` there.
6. **Zero target.** At `z=0`, all three quantities vanish; the coefficient
   normalization is only used when the displayed Euclidean norm is nonzero.
7. **Operator consequences.** The exact norm formula is a direct substitution
   into Theorem 3.3 of the source.  The compactness reformulation follows from
   equivalence of `l1` and `l2` norms in the fixed dimension `n`.

## Novelty check

- Cheap run indexes: no hit for arXiv:2208.02147 or this extremal formula.
- Exact-title and arXiv-id searches: only the source paper.
- Focused arXiv searches for point-evaluation norms and the terms `omega`,
  `Poincare`, `polydisk`, and `arctanh`: no answer located.
- The older generalized-Bloch composition literature found by search concerns
  essential norms, not this point-evaluation extremal.

This was a bounded novelty search, not exhaustive bibliographic certification.

## Review risk

Low mathematical risk: the proof is an explicit extremal plus a two-line
product-distance computation.  The main bibliographic risk is that the
identity may be folklore or recorded under different notation outside the
bounded search.

