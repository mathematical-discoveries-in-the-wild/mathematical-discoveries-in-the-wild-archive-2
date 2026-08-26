# Verification audit

## 1. Exact source match

The attached source PDF states on page 3 that Cowen's example disproves the
sufficiency half of Deddens's conjecture and that necessity remains open. The
bar over `psi(D)` is explicitly said to mean complex conjugation, not closure.
The target is therefore exactly

```text
X T_phi = T_psi X, X != 0
implies conj(psi(D)) subset sigma_p(T_phi^*).
```

## 2. Kernel convention

For the standard Hardy kernel `K_a(w)=1/(1-conj(a)w)`, define
`k_zeta=K_conj(zeta)`. Then `zeta -> k_zeta` is H2-valued analytic, with
coefficient vector `(1,zeta,zeta^2,...)`, locally normally convergent in H2.
Also

```text
T_psi^* k_zeta = conj(psi(conj(zeta))) k_zeta.
```

The scalar on the right is analytic in `zeta`.

## 3. Nonzero eigenfield

Set `F(zeta)=X^*k_zeta`. If this were identically zero, `X^*` would vanish
on every reproducing kernel. Their linear span is dense in H2, so `X^*=0`,
contrary to the assumption `X!=0`.

## 4. Intertwining direction

Taking adjoints in `X T_phi=T_psi X` gives
`T_phi^* X^*=X^* T_psi^*`. Therefore

```text
T_phi^*F(zeta)=conj(psi(conj(zeta)))F(zeta).
```

This has the correct symbol and adjoint orientation.

## 5. Zero removal

At any zero `zeta_0` of the nonzero Banach-valued analytic field `F`, its
Taylor series has a first nonzero coefficient at some finite order `m`.
Locally factor `F(zeta)=(zeta-zeta_0)^mG(zeta)` with
`G(zeta_0)!=0`. Cancelling for punctured points and using continuity gives

```text
T_phi^*G(zeta_0)=conj(psi(conj(zeta_0)))G(zeta_0).
```

Thus each exceptional point supplies a genuine eigenvector, not only an
approximate eigenvector or a generalized eigenvector.

## 6. Final parameter conversion

For `a in D`, set `zeta=conj(a)`. The resulting eigenvalue is
`conj(psi(a))`, proving the whole conjugate-image inclusion.

## 7. Edge cases

The proof permits constant `phi` or `psi` and does not require univalence,
innerness, covering behavior, or image containment. Nonzero `X` is the only
condition needed to keep the eigenfield nontrivial.

## 8. Novelty search

Cheap-index searches found no duplicate. Bounded searches through 2026-08-13
used the exact open phrase, “Deddens conjecture” with necessity and analytic
Toeplitz keywords, the exact title, later citations, and the vector-valued
kernel identity. They found the source, later work citing its partial results,
and Shapiro's 2010 exposition repeating only the ordinary spectrum inclusion,
but no later resolution of the point-spectrum necessity statement. This
supports promotion but is not a priority claim.
