# Counterexample packet: eventual norm continuity does not suffice

status: `candidate_counterexample_likely_valid`

source_arxiv: `1912.13057`

source_result: Remark 3.3 following Theorem 3.1 in Glück--Mugnolo,
*Eventual Domination for Linear Evolution Equations*.

scope: full negative answer to the first explicit question in Remark 3.3;
the separate question about deleting the smoothing assumption on the
dominating semigroup remains open in this packet.

## Result

The implication `(i) => (iii)` in source Theorem 3.1 becomes false when
analyticity is weakened to eventual norm continuity, even if every other
hypothesis is retained and both semigroups become rank-one, compact, and
uniformly strongly positive after finite time.

On `E=L2(0,1)`, let `u=1`, let `P f=(integral f)1`, and let `F=ker P`.  Conjugate
the nilpotent left-shift semigroup on `L2(0,1)` to `F`, calling the result
`W(t)`.  Define

```
T_A(t) = P + W(t)(I-P),
T_B(t) = P + W(2t)(I-P).
```

These are distinct real `C0`-semigroups, but both equal `P` for `t>=1`.
Consequently `T_B(t)f=T_A(t)f=Pf>=0` for every positive `f` and every `t>=1`,
so source assertion (i) holds.  Both generators nevertheless have spectrum
exactly `{0}`, with `0` a simple resolvent pole, and hence have equal spectral
bounds.  Assertion (iii), the strict inequality `s(B)>s(A)`, fails.

The nonempty-spectrum condition is not evaded: the nilpotent shift generator
has empty spectrum, but the common one-dimensional fixed component adds the
simple eigenvalue `0`.  At time `1` both semigroups map all of `E` into
`span{1} subset E_u=L-infinity`, and the common tail `P` is uniformly strongly
positive with respect to `u`.  The construction therefore satisfies all
source assumptions except analyticity, replaced exactly by eventual norm
continuity.

## Why the construction works

Analyticity enters the published proof only after eventual domination and
equal spectral bounds force equality of the two semigroup orbits on a tail.
Analytic unique continuation then forces equality at all positive times.
Eventually norm-continuous semigroups need not be injective and can erase a
whole complementary subspace in finite time.  Two different prehistories can
therefore have the same tail.

## Evidence

- `source_paper.pdf`: exact arXiv source PDF.
- `figures/open_question_crop.png`: source PDF page 9, Remark 3.3.
- `main.tex`: self-contained formal proof and theorem-hypothesis crosswalk.
- `VERIFICATION.md`: algebra, spectrum, order, quantifier, literature, build,
  and visual checks.
- `solution_packet.pdf`: compiled review packet.

## Deep-upgrade and literature audit

The second question in source Remark 3.3 was also investigated.  The later
Arora--Glück paper arXiv:2204.00146 proves a useful near-result: its Proposition
4.2 removes smoothing of the dominating semigroup once one assumes a
time-independent lower bound `T_B(t)f >= c_f u` on every sufficiently late
orbit.  That is stronger than individual eventual strong positivity, where
the order constant may depend on `t`, so it does not answer the source
question.  Strong convergence in `E` alone does not upgrade to convergence in
the gauge norm of `E_u`; this is the exact obstruction.  No rigorous proof or
counterexample for that second question emerged from the additional attack.

A bounded novelty search on 11 August 2026 covered the run indexes, the local
full-source corpus, the exact source wording, the exact arXiv id/title, close
phrases involving eventual norm continuity, nilpotent shift semigroups,
eventual equality, spectral bounds, and the later arXiv:2204.00146 refinement.
No prior answer to the first question or matching construction was found.
The construction is elementary, so novelty confidence is medium; mathematical
validity confidence is high pending human review.

## Human review recommendation

Check the real unitary identification of `L2(0,1)` with the mean-zero
subspace, the all-complex-parameters resolvent formula for the nilpotent shift
generator, the direct-sum pole calculation, and the exact match with every
hypothesis of source Theorem 3.1 after replacing analyticity by eventual norm
continuity.

