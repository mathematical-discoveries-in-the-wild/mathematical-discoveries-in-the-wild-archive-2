# Finite support of projected Plancherel weak limits

Status: candidate substantial partial result, likely valid.

Source: Radoslaw Adamczak, *Random non-Abelian G-circulant matrices.
Spectrum of random convolution operators on large finite groups*,
arXiv:1712.04772, Section 7, Question (I), page 25.

For a finite group `G`, let

`mu_G = sum_{chi in Irr(G)} chi(1)^2 / |G| delta_{chi(1)}`

be the projected Plancherel measure on the one-point compactification of the
positive integers. The source asks which weak limits of such measures can
occur and specifically whether examples more complicated than finite mixtures
exist.

The packet proves that every such weak limit has finite support. The mechanism
is:

1. The commuting probability satisfies
   `cp(G) = integral d^(-2) d mu_G(d)`.
2. A limit other than `delta_infinity` therefore gives a uniform positive
   lower bound on `cp(G)`.
3. P. M. Neumann's structure theorem makes all such groups uniformly
   finite-by-abelian up to uniformly bounded index.
4. Clifford theory then gives a uniform bound on the number of distinct
   irreducible character degrees. The key point is that, for a fixed
   multiplier on a finite abelian group, all irreducible projective
   representations have the same degree.
5. A weak limit of probability measures with uniformly bounded support
   cardinality again has finite support.

This completely rules out infinite-support limits. It does not characterize
which finitely supported measures occur, so the full source question remains
open.

Files:

- `main.tex` and `solution_packet.pdf`: theorem, proof, example, and scope.
- `source_paper.pdf`: source paper compiled from the repository's ingested
  arXiv TeX after the official PDF download path was unavailable.
- `figures/open_problem_crop.png`: real rendered crop of Section 7,
  Question (I).
- `verification.md`: mathematical and rendering checks.

Human-review focus: verify the Clifford-theory degree-count lemma, especially
the passage from an invariant constituent over the finite normal subgroup to
projective representations of an abelian quotient.
