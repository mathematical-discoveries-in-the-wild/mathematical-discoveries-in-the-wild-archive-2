# Verifier report

Verdict: `candidate_full_solution_likely_valid`

Target: the converse of Theorem 4.3 in arXiv:2002.00462 for arbitrary
noncommutative regular polydomains.

## Proof audit

1. Multiplying the source Brown--Halmos equation by `C_i` and `C_i^*` is
   domain-correct and turns both Cauchy-dual products into the nonvacuum
   projection `P_i`.
2. The alternating polynomial is exactly `I-(I-Phi_i)^(m_i)`, with the signs
   and binomial indices checked directly.
3. The negative-binomial inverse is only used coefficientwise.  Its sum is
   finite because every application of `Phi_i` removes at least one letter
   from both indexing words.
4. The reversal in the right shifts and the reversal in `tilde f_i` cancel in
   the path parameterization.  A path stripping `delta` contributes an
   ordered factorization of `delta` with coefficient equal to the product of
   the original `a_(i,eta)` values.
5. Both creation weights telescope.  Summing paths produces exactly
   `b_(i,delta)^(m_i)`, and the remaining factor is the source `tau` ratio.
6. Boundary reachability is equivalent to right-comparability.  This proves
   both the forced zeros and the recurrence.
7. Other tensor coordinates and coefficient-space vectors are spectators;
   applying the recurrence coordinatewise multiplies to the full `tau` ratio.
8. Proposition 1.3 of the source then gives weighted multi-Toeplitzness.

## Computational sanity check

`code/verify_finite_words.py` uses asymmetric nonlinear positive coefficients
and exhausts all 961 scalar matrix coefficients on binary words through
length four for each of `m=1,2,3`.  It checks the path coefficient formula,
the negative-binomial reconstruction, the boundary defect, forbidden
noncomparable entries, and exact Toeplitz weights.  This is not part of the
proof.

## Reviewer focus

The highest-value manual checks are the operator multiplication in Lemma 1
and the word reversal/telescoping factor in Lemma 3.  No unproved lemma,
external theorem beyond the source definitions/Proposition 1.3, or numerical
claim is needed for the conclusion.
