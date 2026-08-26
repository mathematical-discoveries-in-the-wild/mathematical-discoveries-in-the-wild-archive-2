# Verification notes

## Claim audit

- The theorem covers every `1 <= q <= 2 <= p <= infinity`.
- Problem 7.7 excludes `p=q'`; the proof also includes that line and recovers
  the source theorem there.
- The endpoint `p=q=2` has `r=infinity` and reduces to bounded symbols on the
  operator Hilbert space `S_2`.

## Exponent audit

Let

```text
delta_1 = 1/2 - 1/p,
delta_2 = 1/q - 1/2,
delta   = delta_1 + delta_2 = 1/q - 1/p = 1/r.
```

The first Maurey weights have exponent `s_p=2/delta_1`; the residual endpoint
weights have exponent `s_q=2/delta_2`.  Holder gives

```text
1/(2r) = delta/2 = 1/s_p + 1/s_q.
```

On the dual line `q=p'`, this gives `2r=2p/(p-2)`, exactly Xu's exponent.
For `(p,q)=(infinity,2)` it gives `2r=4`; for `(2,1)` it again gives `4`.
For `(infinity,1)` it gives `2r=2`, the Pisier--Shlyakhtenko/Xu corner.

## Dependency audit

1. Junge--Parcet Lemma 4.1(iii): cb `L_p -> L_q` maps are completely
   `(q,1)`-summing with controlled norm.
2. Junge--Parcet Theorem A(i)/(iii): factorization at any intermediate
   exponent; here the intermediate exponent is exactly `2`.
3. Equivariant extraction: after Maurey factorization, the squared
   `S_2^m[S_2^n]` norm is averaged over two diagonal tori.  Its Hilbertian
   Fubini identity produces `E_diag(d_1^2)` and `E_diag(d_2^2)` exactly.
   Xu's `S_2`-amplification criterion then yields a cb residual map.
4. Xu Corollary 7.2 (`LGOH` in the arXiv source): cb maps from `S_s` to `OH`
   satisfy the geometric two-state domination used on matrix units.
5. Standard complete Holder multiplication and homogeneity of `S_2=OH`.

No numerical computation is used as proof.

## Stress tests

- Rank-one symbols: Oikhberg's exact formula for `x -> A x B` gives precisely
  the exponent `2r`, so the proposed exponent cannot be weakened within this
  factorization form.
- Constant `n x n` blocks have factorization size `n^(1/r)`, matching the
  Schatten inclusion scale.
- Adjoint symmetry sends `(p,q)` to `(q',p')` and preserves `r`.
- Finite-compression passage uses reflexivity of `ell_{2r}` (`2r>=2`) and
  coordinatewise convergence after balanced rescaling of the two factors.

## Literature bounds

Searched on 2026-08-11:

- run registry and deterministic source indexes for arXiv:0505306 and the
  exact mixed Schur-multiplier wording;
- exact web/arXiv phrases involving `completely bounded Schur multipliers`,
  `S_p`, `S_q`, `factor through S_2`, and `operator Hilbert space`;
- OpenAlex's 33 indexed citing works for Xu's paper.

Relevant results found: Junge--Parcet (arXiv:0901.1928), Oikhberg (2010), and
Caspers--Wildschut (arXiv:1902.07949, same-exponent multipliers).  No explicit
full answer to Problem 7.7 was found.

## Recommendation

Send to an operator-space specialist for line-by-line review, prioritizing the
squared Hilbert--Schmidt torus average and the extension of the residual map
from its coordinate range in `OH`.  If that lemma is confirmed, the rest is a
short chain of the cited theorems and Holder arithmetic.
