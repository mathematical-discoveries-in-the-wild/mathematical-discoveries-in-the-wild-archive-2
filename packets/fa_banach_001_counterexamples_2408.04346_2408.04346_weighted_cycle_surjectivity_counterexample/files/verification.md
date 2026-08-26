# Verification report

## Claim checked

The map from SO(n) defined by

    Theta_ij^2 = (O_ij^2 + O_ji^2)/2

is not surjective onto symmetric nonnegative matrices with doubly stochastic
Hadamard square. Failure occurs at n=6 and hence in every n >= 6.

Verdict: candidate counterexample; likely valid.

## Step audit

1. The displayed 6 by 6 matrix P is symmetric and nonnegative.
2. Each row has one 1/3 and one 2/3 entry, so all row and column sums are
   one. Thus Theta=P^(circ 1/2) lies in the conjectured target.
3. If P_ij=0, the defining equality is a sum of two nonnegative squares and
   forces O_ij=O_ji=0. Any preimage is therefore supported on C6.
4. For a fixed column j, rows j-1 and j+1 have only column j in common.
   Their orthogonality forces the product of the two possible column entries
   to vanish.
5. Column normalization forces the remaining entry to have modulus one.
   Repetition makes O a signed permutation.
6. A signed permutation has squared entries in {0,1}, so the corresponding
   symmetrized square has entries only in {0,1/2,1}, contradicting every
   nonzero entry of P.
7. The same support lemma works for every cycle C_m with m >= 5.
   Alternating a,1-a weights yield a counterexample for every even m >= 6
   whenever a is strictly between zero and one and is not 1/2.
8. Direct sum with an identity block extends the obstruction to every
   dimension n >= 6.

## Independent exact check

The packet-local script code/verify_weighted_cycle.py uses rational
arithmetic to check P and enumerates all cycle-supported permutation
matrices. It reports:

    symmetric_doubly_stochastic=true
    cycle_supported_permutations=4
    all_image_entries_in={0,1/2,1}
    weighted_cycle_in_image=false

The computation is confirmatory only; the packet contains a direct proof.

## Upgrade-attempt log

- Attempt 1 sought a single boundary-support obstruction.
- Attempt 2 found the alternating weighted 6-cycle.
- Attempt 3 isolated the cycle-support rigidity lemma.
- Attempt 4 upgraded the example to a one-parameter family in every even
  dimension at least six.
- Attempt 5 used block embedding to obtain counterexamples in all
  dimensions n >= 6.
- The small cases n=3,4,5 were not needed to refute the conjecture and are
  not claimed.

## Novelty audit

Bounded primary-source searches through 2026-08-11 used the exact formula,
the source title, symmetrized orthostochastic matrices, and symmetric
bistochastic matrices. They found the source and neighboring literature but
no explicit later resolution or matching weighted-cycle counterexample.
Novelty confidence is moderate.

## Source and render audit

- source_paper.pdf is the official 39-page arXiv PDF.
- Source page 5 was visually inspected and fully reproduced.
- The packet compiled without warnings, overfull boxes, undefined
  references, or multiply defined labels.
- The final packet has 4 pages; every page was visually inspected after the
  last material edit.
- Final packet SHA-256:
  9a7138d226bae62d130e02395e9b84525ddc767e153ed2d02d32aae5210ae1e1.
- Source-paper SHA-256:
  de032da25bb7f7f037282f7727eccc1a1c9b37b7615c5680e6f612bb8843d620.
- Source-page image SHA-256:
  dc8a3c4b4b747ccb7040a45dbcf61ce5cd0899efc85415f31ba52f25cf8a4169.
- Checker SHA-256:
  8a0d7b7a5de835e71b06b17bee1ce75db9c61e957d55847999476b6df37e5337.

## Human verifier focus

Check the zero-propagation step, the unique common column for rows at
distance two, and the direct-sum extension.

