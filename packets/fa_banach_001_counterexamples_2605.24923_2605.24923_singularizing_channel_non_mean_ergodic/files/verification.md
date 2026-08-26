# Verification report

Verdict: `candidate_counterexample_likely_valid`.

## Exact source direction

On PDF page 13, the source says that it is natural to seek analogues of its
strong Cesaro-convergence result for singularizing quantum channels
`Q_{mu,pi}`. It adds that Yosida--Kakutani is unavailable and that no
noteworthy quasi-compact singularizing examples were established.

The candidate gives a negative answer to the universal reading: not every
singularizing channel of the source's random-unitary Pettis-integral form has
strongly convergent Cesaro averages.

## Construction audit

Let `K` be an abelian group of cardinality `kappa`, where `2^K` carries an
atomless countably additive probability `mu`. Let

`H = ell_2(K) tensor ell_2(Z)`,

`pi(j,m) = S_j tensor U^m`,

where `S_j` translates the first coordinate and `U` is the bilateral shift.
On `G=K x Z`, put all measure on the slice `K x {1}`:

`nu(E) = mu({j : (j,1) in E})`.

Then `nu` is countably additive and the associated channel is exactly the
Pettis average of conjugations by `S_j tensor U`.

## Singularization audit

- Every vector of `H` has countable support in `K x Z`.
- For fixed vectors `x,v`, the coefficient
  `<v,(S_j tensor U)x>` can be nonzero only when `j` is a difference of first
  coordinates from two countable supports. This exceptional set is countable,
  so it is `mu`-null.
- A normal state has a countable spectral decomposition into vector states.
  Therefore the averaged output vanishes on every rank-one projection.
- A singular input state vanishes on compact operators before and after every
  unitary conjugation, so its averaged output also vanishes on compacts.
- The source's normal/singular decomposition handles an arbitrary state.
  Hence every channel output vanishes on the compact ideal and is singular.

## Cesaro audit

For `rho_0` supported at `e_0 tensor e_0`, set `sigma_n=Q^n rho_0` and let
`R_n=I tensor P_{e_n}`. Then

`sigma_n(R_m)=1` if `m=n`, and `0` otherwise.

For the observable

`D_N = sum_{n=1}^N R_n - sum_{n=N+1}^{2N} R_n`,

we have `||D_N||=1`, the `N`-th Cesaro mean evaluates it as `1`, and the
`2N`-th mean evaluates it as `0`. Their norm distance is therefore at least
`1` for every `N`. This rules out pointwise norm, hence SOT, convergence of
the channel averages.

The orbit states are pairwise norm-separated by `2`. A power-bounded
quasi-compact operator has relatively norm-compact orbits (equivalently, a
finite-dimensional peripheral part plus a decaying remainder). Thus the
channel is not quasi-compact.

## Computational sanity check

Command:

`conda run --no-capture-output -n sandbox python code/check_cesaro_gap.py`

The script uses exact rational arithmetic and verifies for `N=1,...,100` that
the diagonal witness values are `1` and `0` and that the corresponding scalar
weight vectors have `ell_1` distance `1`. This does not prove the
operator-algebraic claims; it checks only the exact arithmetic used in the
proof.

## Bounded novelty check

Performed 2026-08-09.

- Searched the run registry and solution/attempt/proof-gap indexes for arXiv
  `2605.24923`, `singularizing quantum channel`, `Cesaro`, `mean ergodic`, and
  `quasi-compact`.
- Searched indexed web/arXiv results for `singularizing quantum channels
  Cesaro averages quasi-compact`, the exact source title, `random unitary
  singularizing channel Cesaro averages nonconvergence`, and `quantum channel
  singular states mean ergodic non mean ergodic`.
- The search found the May 2026 source and general finite-dimensional quantum
  ergodicity literature, but no prior result matching this construction or
  answering the source's singularizing direction.

This is bounded evidence, not proof of novelty. Novelty confidence is moderate
to high because the source is recent and the exact searches returned no later
answer.

## Human-review recommendation

Review as a likely valid explicit counterexample. The main checks are:

1. the source's SOT convention for the channel space;
2. the extension of the singularization calculation from vector states to all
   normal states in the nonseparable Hilbert space;
3. the standard implication from power-bounded quasi-compactness to relative
   norm compactness of every orbit.
