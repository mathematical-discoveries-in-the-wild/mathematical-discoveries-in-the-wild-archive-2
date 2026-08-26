# Verification report

Verdict: candidate partial result, likely valid. No unrestricted-commutant
claim is made.

## Algebraic audit

1. With `e_alpha=2^(|alpha|/2)V^alpha h`, the vectors `e_alpha` form an
   orthonormal basis of mean-zero `L2`.
2. If `f=sum_beta a_beta e_beta`, direct substitution gives
   `T_f e_alpha=sum_beta a_beta e_(alpha beta)`. Thus `T_f` is a right
   free-semigroup multiplier; the word is appended, not prepended.
3. In chaos order `d`, every word is uniquely
   `beta=0^k gamma`, where `gamma` begins in `1` and has `d-1` ones
   (`gamma` is empty for `d=1`).
4. The resulting family `Gamma_d` is suffix-free. Hence the ranges of
   `R_gamma e_alpha=e_(alpha gamma)` are pairwise orthogonal.
5. Therefore
   `T_f=sum_gamma R_gamma phi_gamma(R_0)` and
   `||T_f x||^2=sum_gamma ||phi_gamma(R_0)x||^2`.

## Infinite-series audit

The isometry `R_0` is pure, with wandering space spanned by the vacuum and
words ending in `1`; its Wold model is multiplication by `z` on a
vector-valued Hardy space. The column operator above becomes pointwise
multiplication by `Phi=(phi_gamma)_gamma`. Boundary integration proves the
upper bound, normalized reproducing kernels prove the lower bound, and
finite coordinate projections justify the infinite orthogonal sum. Thus

`||T_f||=||Phi||_(H-infinity(D;ell2(Gamma_d)))`.

## Scaling audit

For the source coefficient `xi_(k1,...,kd)`, the binary word has length
`k1+...+kd+d-1`, so its normalized coefficient is

`2^(-(k1+...+kd+d-1)/2) xi_(k1,...,kd)`.

Substituting `w=z/sqrt(2)` into the vector Hardy norm gives exactly

`2^(-(d-1)/2) sup_(|w|<2^(-1/2))
 ||hat f(w,.)||_(H2(D_(2^(-1/2))^(d-1))).`

The formula gives `||T_(V_1 h)||=2^(-1/2)`, an elementary normalization
check, and reduces to the source's scalar norm formula for `d=1`.

## Numerical audit

`code/fixed_chaos_probe.py` uses a nontrivial finite order-three symbol. It checks
that the suffixes are suffix-free, independently computes the normalized
vector Hardy norm and the source mixed Hardy norm, and forms exact finite
Fock compression matrices. Output on 13 August 2026:

```
suffixes=['101', '1010', '11', '110']
suffix_free=True
predicted_vector_Hinf=0.700338611153
source_mixed_Hinf_H2=0.700338611153
depth= 0 compression=0.584026968555
depth= 4 compression=0.688239155679
depth= 8 compression=0.695470244971
```

All asserted compression norms were monotone and below the predicted norm.

## Literature and scope audit

The source paper proves the order-one scalar criterion and explicitly says
the comprehensive `L2` commutant description is open. Astashkin--Terekhin
(JMAA 457 (2018), Theorem 7) treats simultaneous boundedness in every
`Lp` for Haar chaoses of arbitrary fixed order, while its advertised exact
invertibility criterion is again for order one. Bounded exact-title,
fixed-chaos, commutant, and mixed-Hardy searches found no explicit
single-`L2` norm formula above. The abstract free-semigroup commutant model
is standard, so novelty is claimed only for this explicit Haar-chaos slice
and is pending specialist review.

The proof does not combine different chaos orders: terminal suffixes then
become comparable and Pythagoras fails. This is the precise obstruction to
promoting the packet as a full solution of the source problem.
