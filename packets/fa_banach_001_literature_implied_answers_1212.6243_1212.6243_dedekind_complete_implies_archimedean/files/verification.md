# Verification

## Statement audit

The source defines Dedekind completeness by existence of a supremum for every
upper-bounded subset. Proposition 18 assumes that `Y` is both a Dedekind
complete lattice and Archimedean, then asks immediately afterward whether the
Archimedean assumption is necessary. The packet keeps every other hypothesis
and proves that this one follows from Dedekind completeness.

## Proof audit

Let `n y <= x` for all `n >= 1`.

1. Monotonicity of positive parts in a vector lattice gives
   `(n y)^+ <= x^+`, and positive homogeneity gives `(n y)^+ = n y^+`.
2. Therefore `{n y^+}` is upper bounded; its supremum `s` exists.
3. Since `y^+ >= 0`, the sequence is increasing, so deleting its first term
   does not change its supremum.
4. Translation is an order isomorphism, hence commutes with every existing
   supremum. Therefore
   `s = sup_n (n+1)y^+ = y^+ + sup_n n y^+ = y^+ + s`.
5. Cancellation gives `y^+=0`, equivalently `y<=0`, exactly the source's
   definition of Archimedeanness.

No numerical or computer-assisted step is involved.

## Scope audit

The packet answers only the local necessity question following Proposition
18. It does not claim a new resolution of the headline Riesz--Kantorovich
supremum problem, nor does it remove Dedekind completeness.

