# Solution

Let `X=C^infinity[0,1]` over the real or complex scalars. Put

```text
p_j(f)=max_{0<=k<=j} ||f^(k)||_infinity,
||f||_F=sum_{j=0}^infinity 2^(-j-1) p_j(f)/(1+p_j(f)).
```

This is a complete translation-invariant F-norm inducing the ordinary
`C^infinity` topology. Define, for `n>=1`,

```text
V_n={f in X : f^(k)(0)=0 for every k>=n}.
```

Each `V_n` is closed, since it is an intersection of kernels of continuous
jet functionals. It is properly contained in `V_{n+1}`, as witnessed by
`x^n`, and it is infinite-dimensional (for example, it contains all smooth
functions supported away from zero). The union contains every polynomial.

To verify density in the full Fréchet topology, fix `f`, `m`, and `epsilon`.
Approximate `f^(m)` uniformly by a polynomial `q`. Integrate `q` exactly `m`
times and choose the integration constants to match
`f(0),...,f^(m-1)(0)`. The resulting polynomial `P` has `P^(m)=q`; repeated
integration bounds every lower derivative of `f-P` by the same uniform error.
Thus `p_m(f-P)<epsilon`. (For `m=0`, this is Weierstrass approximation.)

For every nonzero `f`, all `p_j(f)>=p_0(f)>0`. Hence

```text
lim_{t to infinity} ||t f||_F=sum_{j=0}^infinity 2^(-j-1)=1.
```

The F-norm never exceeds one, so `sup_{t>=0}||t f||_F=1`. Consequently
`R(V)=1`.

It remains to estimate `d_{n,V}`. Fix `f in V_{n+1}` and set
`a=f^(n)(0)`. Choose a smooth cutoff `chi` on `[0,infinity)` which is one
near zero and vanishes on `[1,infinity)`. For `0<delta<=1`, put

```text
h_delta(x)=a x^n/n! chi(x/delta).
```

Near zero this is exactly `a x^n/n!`, so `g_delta=f-h_delta` belongs to
`V_n`. For each `k<n`, the Leibniz rule gives

```text
||h_delta^(k)||_infinity <= C_{n,k,chi}|a| delta^(n-k).
```

Therefore `p_j(h_delta)` tends to zero for every `j<n`. For the remaining
seminorms, simply use `p/(1+p)<=1`. It follows that

```text
rho_n(f) <= limsup_{delta to 0} ||h_delta||_F
           <= sum_{j=n}^infinity 2^(-j-1)=2^(-n).
```

This holds for every `f in V_{n+1}`, so `d_{n,V}<=2^(-n)`, and hence
`d_V=0`. Thus `R(V)>0` does not imply `d_V>0` for arbitrary `V`.
