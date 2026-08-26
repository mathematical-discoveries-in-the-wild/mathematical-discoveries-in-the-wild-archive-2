# Verification Report

Candidate: arXiv:1803.09212, exact SD-tuple classification

## Claim checked

For every positive tuple `(a_1,...,a_d)`,

`(a_1,...,a_d) is an SD-tuple iff sum_i 1/a_i <= 1`.

Consequently `U(d)=d`, and the reciprocal `l2` classification suggested
after equation (2.27) is false for every `d>=2`.

## Verdict

`likely valid` (full resolution of the precise SD-tuple question)

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Source scope | valid | Definition 2.5 asks for all simplex dimensions; the discussion after (2.27) explicitly proposes the reciprocal `l2` characterization and leaves `sqrt(d) <= U(d) <= d`. |
| Polytope representation | valid | At a fixed level, `Wmin(conv{v_s})` consists exactly of sums `sum_s v_s F_s` for a POVM `(F_s)`. Scalar non-vertex points can be split into vertex effects. |
| Product vertices | valid | The vertices of a Cartesian product of diamonds are precisely products of signed coordinate vertices. Their POVM therefore has one signed coordinate outcome per block. |
| Coordinate marginal | valid | The `j`th coordinate identity in block `i` is `P_j^(i)=a_i(H_{j,+}^(i)-H_{j,-}^(i))`. No other product vertices contribute to that coordinate. |
| Positive domination | valid | `E_j=H_{j,+}+H_{j,-}` is positive and `E_j-a_i^{-1}P_j=2H_{j,-}>=0`. Summing signs and all other indices gives a joint POVM for the `E^(i)`. |
| Trace witness | valid | `tr(P_j E_j)>=t_i` for rank-one `P_j`; marginal expansion produces `sum_J tr((sum_i P_{j_i})G_J)`, bounded by the maximum norm times `tr(I_p)=p`. Commutativity is not used. |
| MUB construction | valid | Character orthogonality proves each quadratic basis is orthonormal. The elementary odd-prime quadratic Gauss sum proves cross-basis overlap modulus `p^{-1/2}`. The standard basis has the same overlap. |
| Projection-sum norm | valid | `sum_i P_{j_i}=UU*` and its nonzero eigenvalues equal those of the `d x d` Gram matrix `U*U`. Gershgorin gives norm at most `1+(d-1)/sqrt(p)`. |
| Matrix-convex input | valid | Every PVM block lies in `Wmin_p(Delta_p)` using its projections as effects and zero at the zero vertex. Maximal matrix convex sets commute with Cartesian products, so the conjoined tuple lies in `Wmax_p(Delta_p^d)`. |
| Limit over primes | valid | The SD definition holds for every `n`; arbitrarily large odd primes with `p+1>=d` exist. Hence `sum_i a_i^{-1}<=1+(d-1)/sqrt(p)` for unbounded `p`, yielding the reciprocal `l1` condition. |
| Converse | valid by source | Corollary 2.25 of arXiv:1803.09212 proves `sum_i a_i^{-1}<=1` is sufficient. |
| Uniform constant and counterexample | valid | For a uniform scale `C`, the exact condition is `d/C<=1`; hence `U(d)=d`. At `a_i=sqrt(d)`, the reciprocal `l2` sum is one but the reciprocal `l1` sum is `sqrt(d)>1`. |

## Computational verification

`code/verify_sd_tuple_mub.py` independently constructs the explicit bases,
checks orthonormality and mutual unbiasedness, enumerates or samples
transversals, and compares every projection-sum norm with the Gershgorin
bound.  The suite covered:

- exhaustive `(p,d)=(3,2)`: 9 transversals;
- exhaustive `(p,d)=(5,3)`: 125 transversals;
- exhaustive `(p,d)=(7,4)`: 2,401 transversals;
- exhaustive `(p,d)=(11,5)`: 161,051 transversals; and
- 5,000 sampled transversals for `(p,d)=(17,7)`.

All tests passed.  The largest orthogonality or unbiasedness error was below
`6e-16`.  The numerical test is a sanity check, not a substitute for the
analytic Gauss-sum and Gershgorin arguments.

## Counterexample and loophole search

- Fixed qubit/binary constructions were checked conceptually first; Clifford
  observables recover reciprocal `l2` behavior and cannot exploit the
  all-simplex-dimensions quantifier.
- The signs in the diamond are not silently discarded.  They are explicitly
  summed, and positivity makes the unsigned marginal dominate the required
  signed difference.
- The proof does not assume pairwise joint measurability; it uses the full
  joint POVM inherited from a single product-polytope representation.
- The asymptotic argument has a finite certificate: if the reciprocal sum is
  `s>1`, any odd prime with `(d-1)/sqrt(p)<s-1` contradicts containment at
  simplex dimension and matrix level `p`.
- The result deliberately does not claim to solve all of Problem 2.3.

## External dependency

Only the sufficient direction is imported: Corollary 2.25 of the source.
The new necessary direction is self-contained apart from standard finite
polytope matrix-convex terminology, character orthogonality, the existence of
arbitrarily large primes, and Gershgorin's theorem.

## Gaps and scope limitations

No proof gap was found in the exact SD-tuple theorem.  The source's broad
arbitrary-product containment problem remains open.  The novelty search is
bounded, so originality is plausible rather than certified.

## Confidence

Score: 99/100

Residual uncertainty concerns literature novelty and expert confirmation of
the conventional identity `Wmax(K x L)=Wmax(K) x Wmax(L)` in the exact
notation of the source.  That identity also follows directly from the scalar
state-space definition used there.

## Human review recommendation

`send to human`

Primary review focus: the signed coarse-graining lemma and the placement of
the conjoined PVM tuple in `Wmax_p(Delta_p^d)`.
