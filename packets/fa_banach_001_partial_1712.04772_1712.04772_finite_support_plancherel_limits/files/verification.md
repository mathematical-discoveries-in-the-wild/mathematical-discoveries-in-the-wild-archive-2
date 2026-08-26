# Verification report

Verdict: candidate partial result, likely valid.

## Mathematical checks

1. For every finite group `G`, the identity
   `cp(G)=k(G)/|G|=sum_chi 1/|G|`
   agrees exactly with
   `integral d^(-2) d mu_G(d)`.
2. The test function `d -> d^(-2)`, extended by value zero at infinity, is
   continuous on the one-point compactification. Thus weak convergence of the
   projected Plancherel measures transfers directly to convergence of
   commuting probabilities.
3. P. M. Neumann's theorem was checked in the formulation quoted as Theorem
   1.2 of Matthew Tointon's arXiv:1707.05565: a uniform positive lower bound on
   commuting probability gives a normal subgroup of bounded index and a
   bounded normal subgroup whose quotient is abelian.
4. The Clifford-theory lemma was checked in two stages. For the
   finite-by-abelian subgroup, an irreducible constituent over the finite
   normal subgroup determines one character degree because irreducible
   projective representations of an abelian group with fixed multiplier all
   have the same degree. Passing to the ambient bounded-index group introduces
   only boundedly many orbit-size and projective-multiplicity factors.
5. The final topological step uses disjoint neighborhoods of hypothetical
   `D+1` support points and the Portmanteau theorem. It works equally when one
   support point is infinity.
6. Extraspecial groups provide a consistency check: their limits can mix a
   finite atom with infinity, but still have finite support, so the theorem
   does not accidentally assert a false finite-versus-infinity dichotomy.

No computational experiment is used as proof.

## Novelty check

The run's registry, solution, attempt, and proof-gap indexes were searched for
the source arXiv id, projected Plancherel measures, weak limits, character
degrees, and commuting probability. The local parsed-source corpus and bounded
primary-source web searches were also checked. The search found the source
question, P. M. Neumann's structure theorem as quoted by Tointon, and Sean
Eberhard's work on scalar commuting-probability limits, but no explicit result
stating finite support for all projected-Plancherel weak limits. Novelty is
therefore plausible rather than certified.

## Artifact checks

- The source question crop was rendered from page 25 of `source_paper.pdf` and
  visually inspected for completeness and readability.
- The final packet PDF was compiled with all intermediates under `tmp/`.
- Every final PDF page was rendered to PNG and visually inspected for clipping,
  overlap, broken formulas, and unreadable evidence.
