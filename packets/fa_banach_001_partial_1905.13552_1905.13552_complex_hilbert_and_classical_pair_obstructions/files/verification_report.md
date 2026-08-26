# Verification report

Verdict: `partial_result_likely_valid`

## Mathematical checks

1. The source definition of `L_{o,p}` fixes the point and permits the modulus
   to depend on that point.  Each construction uses one fixed point and a
   sequence of norm-one operators, so it disproves exactly this local
   property, not merely uniform property `(P2)`.
2. The John ellipsoid of the real four-dimensional body `B_Z` is unique.
   Circle invariance of `B_Z` therefore makes the ellipsoid circle invariant,
   hence Hermitian and the image of the complex Euclidean ball under a
   complex-linear map.
3. John's contact decomposition makes the contact points span the underlying
   real four-dimensional space.  They cannot all lie in one complex line, so
   two complex-independent contacts exist.
4. In the Hilbert construction, equality in
   `||R A_n Qz|| <= ||A_n Qz|| <= ||Qz|| <= 1` first forces `z` into the
   selected Hilbert plane and then onto the fixed contact line.  The other
   contact vector has positive distance from that phase orbit.
5. For `p<=q`, the diagonal operator has norm one, almost norms at `e_1`, and
   every exact norming point has second coordinate of modulus one.
6. For `q<p`, the identity embedding norm is
   `2^(1/q-1/p)` and its maximizers have equal coordinate moduli.  This remains
   true for `p=infinity` with both moduli one.
7. On that maximizer torus, the derivative of
   `||A_t z||_q^q` at zero is `2 q a^q cos(relative phase)`.  Coordinates are
   bounded away from zero, so the derivative convergence is uniform even for
   `q=1`.
8. Comparing an exact maximizer with the equal-phase test vector forces every
   cluster point to have equal phases.  Compactness upgrades this sequential
   statement to uniform separation of all norming points from the fixed
   opposite-phase vector for sufficiently small `t`.

## Upgrade attempts and obstruction audit

- Attempt 1 tested the finite-dimensional norming-set characterization and
  classical diagonal operators.
- Attempt 2 traced the cited universal theorem arXiv:1810.00684 and all eight
  OpenAlex citations.  Its theorem is explicitly real and already uses a
  fixed point, so the real part of Question 3 is settled but the complex part
  is not.
- Attempt 3 found the John-ellipsoid/Hilbert-domain construction and upgraded
  it from dimension two to arbitrary complex Hilbert domains by orthogonal
  projection.
- Attempt 4 handled every complex classical pair.  The hard `p>q` region was
  upgraded from numerical phase evidence to the exact compactness and
  first-variation lemma in the packet.
- Attempt 5 pursued a universal maximal-determinant contact map between
  arbitrary complex two-dimensional balls.  At nonsmooth contact faces there
  is no proved contractive perturbation that fixes one contact and shrinks the
  other; the needed separation lemma remains unproved.
- Attempt 6 checked quotient and Dvoretzky reductions.  Approximate lifts vary
  with the approximation index, while the `L_{o,p}` modulus depends on the
  fixed lift, so the uniform `(P2)` quotient argument does not transfer.
- The remaining probability of a full universal proof was assessed as low
  after these two structural obstructions; no additional credible line was
  left to justify more iterations on this target.

## Novelty and literature bounds

- Exact-question and exact-property searches were run through 2026-08-13.
- Searches included `L_{o,p}`, `property (P2)`, `operatorwise`, `complex Banach
  spaces`, the source title/authors, arXiv:1810.00684, and its complete
  OpenAlex citing-work list.
- The 2022 expert overview reports the universal nonexistence theorem only for
  real Banach spaces.
- No located paper states a complex universal answer, the Hilbert-domain
  theorem, or the all-`ell_p^2`/`ell_q^2` theorem.  Novelty is provisional
  pending expert bibliographic review.

## Artifact checks

- The source PDF opens and has nine pages.
- The source page containing Question 3 is readable in
  `figures/open_question_crop.png`.
- LaTeX compilation and warning scan are recorded after packet build.
- Every final packet page is rendered and visually inspected before promotion.
