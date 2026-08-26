# Verification report

Verdict: candidate partial result, likely valid; no full solution claimed.

## Formal checks

1. Substituting `eta=-i*zeta` and `lambda=i*u` into the source R matrix gives
   weights `(a,-d,1)` exactly.
2. Direct multiplication of the displayed 4-by-4 matrices verifies both local
   Pauli-Z sign identities used in the proof.
3. The telescoping leaves `(-1)^N P` outside the auxiliary trace. On the
   `m`-particle sector, this is the scalar `(-1)^(N+m)`.
4. Fixed-particle configurations are connected by adjacent binary swaps. Each
   such swap and its reverse has a positive vertex realization, while the
   constant auxiliary arrow gives every state a positive diagonal entry.
   Hence each positive block is primitive.
5. Reversing the quantum word and complementing every bit gives a
   weight-preserving bijection between the `m` and `2N-m` blocks, including
   the auxiliary twist, so their Perron roots agree.

## Computational checks

`code/qtm_perron_probe.py` embeds the local R matrices without using Bethe
Ansatz formulas. At `(zeta,T,h,J)=(1.1,1,0.7,1)` the maximum residual in

`S t_q(0) S = (-1)^N P V`

was:

- `N=1`: `0`
- `N=2`: `2.23e-16`
- `N=3`: `4.45e-16`
- `N=4`: `5.56e-16`

The `N<=3` parameter grid found that each transformed sector has exactly one
entry sign, the central sector has the numerically largest Perron root, and
each tested QTM has a strict global modulus gap. These observations support
but do not prove the unproved cross-sector inequality.

`code/sector_intertwiner_lp.py` tests one possible upgrade. Its
inclusion-supported positive intertwiner LP is infeasible for `N=3`,
`m=2 -> 3`, so the packet does not rely on that route.

## Human-review recommendation

Check the tensor-leg order in the local transpose/spin-flip identity and the
telescoping of auxiliary `Z` factors. Then check that the positive
nearest-neighbor-swap path works at the periodic boundary as well as in the
interior. Do not infer the global conjecture without proving
`rho_N > rho_m` for every `m != N`.

