# Proof companion

Let `K=S^4`. Motakis constructs a separable complex Banach space `X`, a
Schauder basis `(d_gamma)`, and a map `kappa` from the basis indices into
`K` with these properties:

1. For every scalar Lipschitz function `f` on `K`, the diagonal rule
   `D_f d_gamma=f(kappa(gamma))d_gamma` extends to a bounded operator on
   `X`.
2. The rule `f -> [D_f]` extends to a Banach algebra isomorphism
   `Psi:C(K)->Cal(X)`.

On Lipschitz functions the lift itself is exactly multiplicative:
`D_f D_g=D_{fg}`.

Put `E=X direct-sum X`. Then `B(E)` and `K(E)` are the two-by-two matrices
over `B(X)` and `K(X)`, respectively. For a matrix-valued Lipschitz function
`F=(f_ij)`, put `J(F)=(D_fij)`. This is a unital algebra homomorphism. The
matrix amplification of `Psi^{-1}` gives an isomorphism

```text
Theta: Cal(E) -> M_2(C(K))
```

such that `Theta(q(J(F)))=F`, where `q` is the quotient map.

Write a point of `S^4` as `(z_0,z_1,t)` with `t` real and
`|z_0|^2+|z_1|^2+t^2=1`. Klaja and Ransford use

```text
a = 1/(1+it) [[z_0,0],[z_1,0]],
b = 1/(1+it) [[conj(z_0),conj(z_1)],[0,0]].
```

All entries are smooth, hence Lipschitz. They prove that

```text
c=I-2ab
```

is an invertible matrix function not homotopic to the identity. Therefore
`c` is not in `Exp(M_2(C(K)))`.

Define `S=J(a)` and `T=J(b)`. Multiplicativity gives

```text
I-2ST=J(c).
```

The inverse matrix function `c^{-1}` is smooth, so `J(c)` is invertible. If
`J(c)` were in `Exp(B(E))`, applying `q` and then `Theta` would put `c` in
`Exp(M_2(C(K)))`, a contradiction. Thus `I-2ST` is not in `Exp(B(E))`.

For the reversed product, direct multiplication gives

```text
I-2ba = diag(phi(t),1),
phi(t) = -((1-it)/(1+it))^2.
```

Let

```text
g(t)=i(pi-4 arctan(t)).
```

Since `(1-it)/(1+it)=exp(-2i arctan(t))`, one has `phi=e^g`. Both functions
are Lipschitz on `[-1,1]`. Hence

```text
I-2TS = J(diag(phi,1))
       = exp(J(diag(g,0))),
```

so `I-2TS` belongs to `Exp(B(E))`.

Finally, `(1/2)I-ST=(1/2)(I-2ST)` and similarly for `TS`. The nonzero scalar
`(1/2)I=exp(-(log 2)I)` lies in `Exp(B(E))`, so multiplication by it does not
change component membership. Therefore

```text
1/2 in epsilon(ST),
1/2 not in epsilon(TS).
```

This positively answers Question 4.2.
