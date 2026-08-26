# Proof: geometric block-polar factorization

## General setting

Let `K` be a bounded Borel star body in `R^m`, containing the origin in its
interior, and let

\[
\rho_K(x)=\inf\{t>0:x\in tK\}
\]

be its gauge. For `n>=1` and `0<q<=infinity`, define

\[
\mathcal B_q^{(n)}(K)=
\left\{(x_1,\ldots,x_n)\in(\mathbb R^m)^n:
 \|(\rho_K(x_1),\ldots,\rho_K(x_n))\|_{\ell_q^n}\le1\right\}.
\]

Convexity is not needed, so this includes quasi-norm balls with exponents below
one.

## Theorem

For any two such star bodies `K,L`,

\[
\frac{\operatorname{vol}_{mn}(\mathcal B_q^{(n)}(K))}
 {\operatorname{vol}_{mn}(\mathcal B_q^{(n)}(L))}
=\left(\frac{\operatorname{vol}_m(K)}
 {\operatorname{vol}_m(L)}\right)^n.
\]

This also holds for `q=infinity`.

## Proof intuition

The distribution of the gauge radius under Lebesgue measure is universal up
to the scalar `vol(K)`: a shell at radius `r` has infinitesimal volume
`m vol(K) r^{m-1} dr`. The outer `l_q` constraint sees only the `n` radii and
not the angular variables. Thus the radial region and its weighted measure are
the same for all inner bodies, while every block contributes exactly one
factor of the inner body's volume.

## Proof

Homothety gives, for every `r>=0`,

\[
\operatorname{vol}_m\{x:\rho_K(x)\le r\}
=\operatorname{vol}_m(rK)=r^m\operatorname{vol}_m(K).
\]

Consequently the pushforward of Lebesgue measure by `rho_K` is

\[
(\rho_K)_\#(dx)=m\operatorname{vol}_m(K)r^{m-1}\,dr.
\]

Equivalently, for every nonnegative Borel function `f`,

\[
\int_{\mathbb R^m}f(\rho_K(x))\,dx
=m\operatorname{vol}_m(K)\int_0^\infty f(r)r^{m-1}\,dr.
\]

Applying this identity in each block and using Tonelli's theorem yields, for
every nonnegative Borel `F` on `[0,infinity)^n`,

\[
\int_{(\mathbb R^m)^n}F(\rho_K(x_1),\ldots,\rho_K(x_n))\,dx_1\cdots dx_n
=(m\operatorname{vol}_m(K))^n
 \int_{[0,\infty)^n}F(r)\prod_{j=1}^n r_j^{m-1}\,dr.
\]

Choose `F` to be the indicator of

\[
R_{q,n}=\{r\in[0,\infty)^n:\|r\|_{\ell_q^n}\le1\}.
\]

Then

\[
\operatorname{vol}_{mn}(\mathcal B_q^{(n)}(K))
=(m\operatorname{vol}_m(K))^n I_{m,n,q},
\qquad
I_{m,n,q}=\int_{R_{q,n}}\prod_{j=1}^n r_j^{m-1}\,dr.
\]

The finite constant `I_{m,n,q}` depends on `m,n,q` but not on `K`. Repeating
the identity with `L` and dividing proves the theorem. For `q=infinity`, the
same proof applies with `R_{infinity,n}=[0,1]^n`. QED.

## Application to the source question

Set `K=B_p^m` and `L=B_q^m`. Their gauges are the `l_p^m` and `l_q^m`
(quasi-)norms. Therefore

\[
\mathcal B_q^{(n)}(B_p^m)=B_{p,q}^{m,n},
\qquad
\mathcal B_q^{(n)}(B_q^m)=B_q^{mn}.
\]

The general theorem becomes exactly

\[
\operatorname{vol}(B_{p,q}^{m,n})
=\operatorname{vol}(B_q^{mn})
\left(\frac{\operatorname{vol}(B_p^m)}
{\operatorname{vol}(B_q^m)}\right)^n.
\]

This is the requested geometric interpretation: the two bodies have the same
block-radius base `R_{q,n}`; only the `n` angular shell factors change. It also
proves the formula without evaluating a beta or gamma integral.

## Direct geometric transport interpretation

For a centrally symmetric star body `K`, let `S_K={theta:rho_K(theta)=1}` and
let `mu_K` be normalized cone measure on `S_K`. The shell identity is the
measure disintegration

\[
dx=m\operatorname{vol}(K)r^{m-1}\,dr\,d\mu_K(\theta),
\qquad x=r\theta.
\]

For `m>=2`, the standard probability spaces `(S_L,mu_L)` and `(S_K,mu_K)` are
nonatomic, so choose a measure-preserving bijection `phi:S_L->S_K` modulo null
sets. (For the one-dimensional symmetric case, match the two endpoints.)
Extend it homogeneously by

\[
T(r\theta)=r\phi(\theta).
\]

Then `rho_K(Tx)=rho_L(x)`, while the cone disintegrations show that `T` scales
Lebesgue volume by `vol(K)/vol(L)`. Consequently the block map `T^n` carries
`mathcal B_q^{(n)}(L)` onto `mathcal B_q^{(n)}(K)` modulo null sets, preserves
the entire vector of block radii, and scales volume by
`(vol(K)/vol(L))^n`. This is a literal geometric transport realizing the
factorization, not only a cancellation of formulas.
