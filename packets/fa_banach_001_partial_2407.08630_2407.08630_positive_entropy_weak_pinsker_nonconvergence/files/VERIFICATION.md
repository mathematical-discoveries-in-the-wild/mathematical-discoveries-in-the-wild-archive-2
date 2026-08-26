# Verification report

Verdict: `candidate partial result - likely valid`.

## Claim checked

Every ergodic invertible probability-preserving transformation of positive
Kolmogorov-Sinai entropy can occur, up to isomorphism, as `S` in Austin's
nonconvergent integral double averages, with `T` also isomorphic to `S` and
with the same bounded real observable in both factors.

## Audit

1. **Block permutation.** The positive integers are partitioned into finite
   even-length blocks, each much longer than all preceding indices. The
   permutation is the identity on alternating blocks and swaps adjacent
   indices on the other blocks. It is a bijection of `Z`, fixes zero, and the
   density of its fixed points along successive block endpoints tends
   alternately to one and zero.

2. **Bernoulli conjugacy.** For the two-sided Bernoulli shift
   `(sigma y)_n=y_{n+1}` and coordinate permutation `(C_p y)_n=y_{p(n)}`,
   `tau=C_p^{-1} sigma C_p` is conjugate to `sigma`. Since `p(0)=0`, direct
   substitution gives `(tau^i y)_0=y_{p(i)}`.

3. **Exact correlation.** For nonzero bounded centered `h` on the Bernoulli
   base and `f(y)=h(y_0)`, independence of distinct coordinates gives
   `integral f(sigma^i y)f(tau^i y)=||h||_2^2` if `p(i)=i`, and zero otherwise.
   Thus the Cesaro correlations are exactly the variance times the fixed-point
   densities; no approximation or limiting interchange is used.

4. **Weak Pinsker step.** Austin's weak Pinsker theorem gives, for every
   `epsilon>0`, an isomorphism from an ergodic system to `B x R`, with `B`
   Bernoulli and `h(R)<epsilon`. If the original entropy is finite and
   positive, choose `epsilon<h(S)`; entropy additivity then forces `h(B)>0`.
   If `h(S)=infinity`, the finite-entropy remainder forces `h(B)=infinity`.
   Hence `B` is nontrivial in both cases.

5. **Product and transfer.** Replacing `sigma` by its conjugate `tau` on the
   Bernoulli factor and leaving `R` unchanged gives `T_0=tau x R`, conjugate to
   `S_0=sigma x R`. The observable ignores the remainder, so the exact
   correlations persist. Transport through the weak-Pinsker isomorphism puts
   both transformations on the original probability space and preserves the
   integrals.

## Scope and possible failure points

- The proof applies to invertible standard probability-preserving systems,
  matching the automorphism setting of the cited weak Pinsker theorem and the
  source construction.
- Weak mixing is not needed once positive entropy and ergodicity are assumed.
- The argument provides divergence of the integrals, hence a fortiori rules
  out `L^2` convergence of the function-valued averages.
- It gives no information for zero-entropy weakly mixing systems. A subsequent
  lane-0 literature identification shows that Austin's universal affirmative
  question is false: Chacon's weakly mixing transformation is universal for
  weak disjointness and hence cannot occur in a divergent example. The present
  result remains a valid positive-entropy occurrence theorem.
- No computational evidence is used as proof.

## Novelty check

Bounded through 9 August 2026. Checked the run registry and solution/attempt
indexes; exact-phrase searches for Austin's concluding question; title and
citation searches for arXiv:2407.08630; and recent related arXiv records
2407.13741, 2410.11787, and 2411.02024. The searches found constructions for
Gaussian systems, Poisson suspensions, simple singular spectrum, and rank-one
base transformations, but no statement combining weak Pinsker with a
coordinate-permutation Bernoulli construction to settle all positive-entropy
systems. Because this is a bounded rather than exhaustive review, novelty
confidence is moderate.
