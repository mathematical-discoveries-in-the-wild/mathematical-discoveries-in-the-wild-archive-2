# Verification report

Verdict: `likely valid; candidate full solution`.

This report is independent of numerical experimentation.  Every estimate
needed by the construction is checked symbolically below.

## 1. Finite-prefix condition numbers

For a normalized conditional Schauder basis `(u_j)`, the synthesis maps
`S_N e_j = u_j` satisfy `||S_N|| >= 1` and `||S_N^{-1}|| >= 1`.  If the products
`kappa_N = ||S_N|| ||S_N^{-1}||` were uniformly bounded, both factors would be
uniformly bounded.  The resulting two-sided `ell_2` estimates on every finite
linear combination would make `(u_j)` a Riesz basis.  Thus a subsequence of
`kappa_N` tends to infinity.

## 2. Global basis geometry

Every partial-sum projection within a copied finite prefix has norm at most
the original Schauder basis constant `K`.  A global partial sum keeps all
earlier orthogonal blocks and applies one such projection in the current
block.  Its norm is therefore at most `max(1,K)`.  Hence the concatenation is a
normalized Schauder basis.

If it had uniform Riesz bounds, restriction to each block would uniformly
bound both `||S_m||` and `||S_m^{-1}||`, contradicting
`kappa_m -> infinity`.  Thus it is a bounded non-Riesz basis in exactly the
sense used by the source paper.

## 3. Group estimate and strong continuity

With `delta_m = 2^(-m)/(kappa_m N_m)`, one has

```text
kappa_m max_j |exp(i delta_m j t)-1|
    <= kappa_m delta_m N_m |t|
    = 2^(-m)|t|.
```

After factoring out the common scalar phase, this gives
`||T_m(t)|| <= 1 + 2^(-m)|t|`.  Therefore the orthogonal direct sum exists for
every real `t` and satisfies `||T(t)|| <= 1+|t|/2`.  The group law holds in
each block.  Continuity on finitely supported block vectors and the uniform
local norm bound extend strong continuity to the whole Hilbert sum.

## 4. Generator

Let `A_m` be the finite-dimensional diagonalizable block operator and define
`A = direct_sum A_m` on the square-summability domain.  For `x` in this domain,
the block identities

```text
T_m(t)x_m - x_m = integral_0^t T_m(s) A_m x_m ds
```

assemble into the corresponding Bochner integral in the Hilbert sum, proving
that `x` lies in the group generator domain and that the generator equals `A`.
Conversely, applying each bounded block projection to a generator difference
quotient gives the reverse domain inclusion.  Finally,
`A v_{m,1} = i beta_{m,1} v_{m,1}` with `beta_{m,1} >= 4^m` and
`||v_{m,1}||=1`, so the generator is unbounded.

No logical dependency remains conditional.  The only external input is the
classical existence of a normalized conditional Schauder basis in a Hilbert
space, for which the source itself supplies Babenko's explicit example and
bibliographic reference.
