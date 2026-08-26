# Verification

## Source

- `source_paper.pdf` is arXiv:2507.13121v2 (16 pages).
- Printed page 16 contains Question 7.4; the exact crop is
  `figures/question_7_4_crop.png`.
- The source defines `B_0=1` and
  `B_n=product_{k=1}^n (lambda_k-z)/(1-conj(lambda_k)z)`.
- Its completeness theorem says the cumulative family is dense in the disk
  algebra exactly for a non-Blaschke sequence.  Removing a finite prefix
  preserves the non-Blaschke condition.

## Algebraic checks

1. If `S_N` is the partial-sum projection of a putative basis
   `(B_n)_{n>=0}`, then
   `ker S_N = closure span{B_n:n>=N}`.
2. Write `B_{N+k}=B_N C_k`, where `C_k` is formed from the tail zeros.  Tail
   completeness and the fact that multiplication by a finite Blaschke product
   is an isometry on `A(D)` give
   `ker S_N=B_N A(D)`.
3. The quotient `A(D)/B_N A(D)` has dimension `N`, with coordinates the
   derivatives through the multiplicities of the zeros of `B_N`.  Hence
   `S_N f` is the unique element of `E_N=span(B_0,...,B_{N-1})` having the
   same confluent jets as `f`.

## Repeated-node check

For each fixed `N`, split every zero of multiplicity `m` into `m` distinct
nearby points inside the disk.  Apply the standard invertible
divided-difference change of coordinates to the value map on those nodes.
As the nodes coalesce:

- the transformed value map `A(D)->C^N` converges in operator norm to the jet
  map, by Cauchy estimates on a compact neighborhood of the finitely many
  interior nodes;
- its restriction to `E_N` converges to the invertible Hermite jet map;
- inversion is continuous in finite dimensions.

Therefore the associated Lagrange projection onto `E_N` converges in operator
norm to `S_N`.  Choosing it within `1/N` of `S_N` preserves strong convergence
to the identity and contradicts Ivanov–Shekhtman Theorem 4.

## Edge cases

- If the question is read literally with indices `n>=1`, all basis candidates
  vanish at `lambda_1`; their closed span is a proper ideal.  The main proof
  treats the stronger intended family including `B_0=1`.
- Repetitions are allowed and are exactly why the confluence step is included.
- No claim of a new 2026 theorem is made: the negative answer is classified as
  literature-implied because the obstruction theorem is from 2001.

