# Problem statement

Let `(X,||.||)` be an infinite-dimensional Fréchet space and let
`V={V_n}` be nested linear subspaces satisfying

```text
closure(V_n) subset V_{n+1},
X = closure(union_n V_n).
```

Write

```text
rho_n(x) = dist(x,V_n),
d_{n,V} = sup {rho_n(v): v in V_{n+1}},
d_V = inf_n d_{n,V},
```

and

```text
R(V) = inf { sup_{t in R_+} ||t v|| :
             v in (union_n V_n) minus {0} }.
```

Aksoy and Lewicki prove in Lemma 2.22 that `d_V>0` implies `R(V)>0`.
Remark 2.23 says, exactly:

> By [12], Prop. 3.4 and Cor. 3.8 and Lemma 2.22 if all n, V_n are
> finite-dimensional, then d_V > 0 if and only if R(V) > 0. We do not know if
> this is satisfied for arbitrary V.

The packet answers this negatively. It constructs a standard F-norm on
`C^infinity[0,1]` and closed infinite-dimensional steps for which
`R(V)=1` but `d_V=0`.
