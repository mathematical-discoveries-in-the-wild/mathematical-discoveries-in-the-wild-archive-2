# Verification report

## Verdict

Likely valid full solution to Conjecture 1 in arXiv:2407.13457, strengthened
to arbitrary symmetrized Dirichlet laws. Human review is recommended before
dissemination.

## Claim audited

For every `n>=2`, `p>0`, probability vector `(theta_A)`, and cone measure on
the `l_p` sphere, the weighted sum of conditional block entropies dominates
`theta_** Ent(f)`, where `theta_**` is the minimum total weight of blocks
covering a given pair. The proof actually allows arbitrary positive Dirichlet
parameters before the coordinatewise power map.

## Adversarial checks

1. **Exact probabilistic representation.** If `X` has cone measure, then
   `Z_i=|X_i|^p` has the symmetric Dirichlet law with parameter `1/p`, and the
   coordinate signs are independent fair signs independent of `Z`. The map
   `(Z,epsilon) -> X` is an almost-sure coordinatewise bijection.

2. **Block conditionals are preserved.** Given the complementary coordinates,
   the remaining signs stay independent and the remaining magnitudes have the
   scaled conditional Dirichlet law. Because the power/sign map is
   coordinatewise bijective off the null boundary, it preserves every
   complementary-coordinate sigma-field and hence every conditional entropy.

3. **Dirichlet Brascamp-Lieb coefficient condition.** With
   `c_A=theta_A/(1-theta_**)` and observables depending on `A^c`, Proposition
   14 of arXiv:0907.2858 requires, for each pair `{i,j}`, the sum over blocks
   whose complements meet the pair. This sum is exactly
   `(1-sum_{A superset {i,j}} theta_A)/(1-theta_**) <= 1`.
   The possible empty complement at `A=[n]` merely gives a constant
   Brascamp-Lieb factor and requires no extension of Proposition 14.

4. **Entropy duality normalization.** The Brascamp-Lieb exponents `c_A`
   produce `sum theta_A Ent(E_A h) <= (1-theta_**) Ent(h)`. Subtracting this
   from the weighted conditional entropy chain rule (the weights sum to one)
   gives the desired Dirichlet factorization with no lost constant.

5. **The `theta_**=1` endpoint.** In this case every positive-weight block
   contains every pair, hence every coordinate, so `theta_[n]=1`; the target
   inequality is the entropy identity. No division by zero is used.

6. **Sign constant comparison.** Ordinary product Shearer gives `theta_*`.
   Choosing an index attaining the singleton minimum and pairing it with any
   other index proves `theta_** <= theta_*`, so the sign estimate is at least
   as strong as needed.

7. **Joint block chain rule.** Conditional on `(Z_Ac,epsilon_Ac)`, applying
   the entropy chain rule first to `Z_A` and then to `epsilon_A` yields exactly
   the two terms called `M_A` and `S_A`; no independence between `Z_A` and
   `Z_Ac` is assumed.

8. **Convexity direction.** Conditional entropy is convex in the nonnegative
   function: its second variation is
   `E[u^2/h]-(E u)^2/E h >= 0`. Therefore entropy after averaging the
   complementary signs is no larger than the average of the magnitude
   entropies before that averaging. This is precisely the direction needed to
   bound the Dirichlet term by `M_A`.

9. **Boundary-singular regimes.** The supporting Dirichlet theorem holds for
   every positive parameter. Thus `p>1`, where `1/p<1` and the density blows
   up at the simplex boundary, causes no problem. Boundary coordinates are
   nevertheless zero with probability zero. The proof also covers `0<p<1`.

10. **Integrability extension.** The formal proof for bounded positive
    functions extends by standard truncation to nonnegative `L log L`
    functions. Conditional expectation preserves the required Orlicz
    integrability by Jensen.

11. **Scope.** The packet proves exactly the conjectured lower bound and a
    stronger class of measures. It deliberately does not claim universal
    optimality of `theta_**`.

## Independent executable QA

`code/verify_quadrature.py` uses 90-point normalized Gauss-Jacobi rules for
the Dirichlet stick-breaking and conditional Beta laws. It checks the
three-coordinate pair-block inequality for three genuinely sign-dependent
positive functions and five parameters `alpha=0.2,0.5,1,2,5`. All 15 cases
passed; the minimum computed slack was `3.714465e-02`. This is a smoke test,
not a proof.

The four-page packet compiled to its final PDF with no LaTeX, reference,
overfull, or underfull warnings. Every final rendered page and the source crop
were inspected at readable resolution; there is no clipping, overlap, malformed
formula, or unreadable evidence image.

## Literature and novelty check

The run's four cheap indexes had no entry for arXiv:2407.13457. Targeted arXiv
and exact-phrase searches through 13 August 2026 used `Conjecture 1`,
`symmetrized Dirichlet`, `cone measure`, `l_p sphere`, and entropy
factorization. They found the source, its 2026 JFA publication, and the cited
2011 Brascamp-Lieb paper, but no later primary-source resolution. The
publisher's 2026 full-text record still presents the statement as Conjecture
1. Novelty is provisional.

## Recommended verifier focus

Check the coefficient set in the application of Proposition 14 and the
convexity comparison from the averaged-sign magnitude entropy to `M_A`. Once
those two one-line steps are confirmed, the rest is exact chain-rule algebra.
