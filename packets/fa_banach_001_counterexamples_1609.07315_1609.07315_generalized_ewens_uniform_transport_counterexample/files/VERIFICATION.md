# Verification

## Construction

Let `n=64`, `eps=10^-200`, and use generalized Ewens weights

- `theta_1=1`,
- `theta_k=eps` for `2<=k<=63`,
- `theta_64=1/63!`.

All weights are strictly positive.  The identity has raw weight one.  Each of
the `63!` many 64-cycles has raw weight `1/63!`, so their aggregate raw mass is
one.  Every remaining permutation contains a cycle of length in `[2,63]` and
has raw weight at most `eps`; hence its aggregate mass `r` is bounded by
`64! eps < 10^-100 < 0.01`.

## Unique-coupling calculations

Write `mu` for this law and take `nu_1=delta_e`, `nu_2=mu`.  Then

- `H(nu_1|mu)=log(2+r)<log(2.01)<0.7`,
- `H(nu_2|mu)=0`,
- `W_{1,H} >= 64/(2+r)`,
- `W_{1,T} >= 63/(2+r)`,
- `tilde T_{2,H}=W_{1,H}^2` and
  `tilde T_{2,T}=W_{1,T}^2`, because the first marginal is a point mass,
- `widehat T_2 >= 64/(2+r)^2`, because every 64-cycle moves every coordinate.

## Source constants

For `S_64`, `ell=2` and `K_n=63`.  The part-(a) constants are `c=3` for
Hamming distance and `c=2` for transposition distance.  The invariant-law
constant in part (b) is `c^2=8(ell-1)^2+2=10`.

Using only `r<0.01`, the right side of every two-measure inequality is below
`63*0.7=44.1`, while the left-side lower bounds are:

| Source inequality | Metric/cost | Lower bound |
|---|---|---:|
| (7) | Hamming `W_1` | `>225` |
| (7) | transposition `W_1` | `>491` |
| (8) | Hamming weak cost | `>56` |
| (8) | transposition weak cost | `>122` |

For (9), the left side is
`widehat T_2/(2c^2) > 64/(20*2.01^2) > 0.79`, whereas the entropy side is
below `0.7`.

`code/verify_bounds.py` recomputes these estimates with 100-digit decimal
arithmetic and asserts every strict comparison.

## Hidden-hypothesis audit

The tempting proof by Theorem 1.3(b) is invalid: the opening sentence of
Theorem 1.3 assumes `mu in M_T` for the whole theorem, and the proof of part
(b) uses the product disintegration of such measures in its induction.  The
source itself says that generalized Ewens measures need not belong to `M`.

## Scope

The packet refutes the direct, parameter-uniform extension of all displayed
source inequalities.  Since every positive measure on a finite group admits
some finite transport--entropy constant, the broad question can still be
repaired by allowing constants depending on the weights or by imposing
regularity assumptions such as uniform control of the cycle weights.
