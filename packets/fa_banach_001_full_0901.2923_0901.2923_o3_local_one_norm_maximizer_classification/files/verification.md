# Verification report

## Claim checked

The entrywise one-norm on O(3) has exactly 192 local maximizers. They are all
equivalent under signed row and column permutations to the displayed matrix
U-star, and all are global maximizers of norm 5.

Verdict: candidate full solution; likely valid.

## Step audit

1. The source's Theorem 3.3 gives the local-maximizer criterion
   S U-transpose positive definite and its Lemma 3.1 excludes zero entries.
2. If P=S U-transpose is positive definite, then S=P U and
   S S-transpose=P-squared. Uniqueness of the positive square root forces
   U=(S S-transpose)^(-1/2) S.
3. Conversely, a nonsingular sign matrix whose polar factor has the same
   signs satisfies the source positivity criterion.
4. Signed row and column permutations commute with the polar construction.
5. After normalizing the first row and column of a 3 by 3 sign matrix, its
   determinant is four times the determinant of a 2 by 2 binary tail.
6. Exactly six binary tails have determinant plus or minus one. They reduce
   to two row/column-permutation types, and an explicit cyclic column
   permutation plus one row sign change joins the two types.
7. Exact multiplication verifies the canonical polar factor is orthogonal,
   has the canonical signs, and has positive test matrix with eigenvalues
   1, 2, 2.
8. Undoing normalization gives 6 times 2^(3+3-1)=192 sign matrices.
   Distinct sign matrices yield distinct local maximizers.
9. The source's sharp O(3) bound is 5, and the representative has norm 5;
   hence every classified local maximum is global.

## Independent checks

- Exhaustive enumeration of all 512 sign matrices found exactly 192
  nonsingular matrices and one signed-permutation orbit.
- Symbolic arithmetic verified orthogonality, the sign pattern, the positive
  matrix, its eigenvalues, and norm 5.
- Computation is confirmatory only; the packet contains an exact proof.
- The reproducible packet-local check is code/verify_sign_orbits.py.

## Upgrade-attempt log

- Route 1 followed the source's two SO(3) sign cases.
- Route 2 replaced Euler--Rodrigues calculations by the unique polar factor
  of each sign matrix.
- Deep upgrade classified the entire O(3) problem, not only the displayed
  SO(3) cases, and obtained the exact count 192.
- General-dimension upgrade gives a finite polar codebook for every N.
- A p-norm upgrade was assessed but not claimed: for p different from 1 the
  gradient varies with entry magnitudes, so the finite sign-linearization
  no longer closes the problem.

## Novelty audit

Bounded primary-source searches through 2026-08-11 used the source title,
local maximizers, one-norm, O(3), and almost Hadamard matrices. The later
paper arXiv:1202.2025 repeats the positivity criterion and identifies the
global O(3) optimizer, but the inspected text does not state the
classification or exact count of all local maximizers. No matching primary
result was located. Novelty confidence is moderate.

## Source and render audit

- source_paper.pdf was compiled locally from the archived arXiv source and
  has 17 pages.
- Source page 8 was visually inspected and fully reproduced in the packet.
- The packet compiled without warnings, overfull boxes, undefined
  references, or multiply defined labels.
- The final packet has 5 pages; all pages were visually inspected after the
  last material edit.
- Final packet SHA-256:
  930ac98599ff004b871b1d04c2500809cefc44f47aa7bdd68d970364059ef98c.
- Compiled source-paper SHA-256:
  789604e0bf3d8dc16c0740fd57fbd87d28ef0d1d1056f62ec40ede51304dcedc.
- Source-page image SHA-256:
  372f83bb4d79b97d386d4e25ddc34641527c585e07a31c07accf020058026868.

## Human verifier focus

Check the polar-factor implication, the reduction of the six binary tails to
one full signed-permutation orbit, and the factor 2^(3+3-1) in the count.
