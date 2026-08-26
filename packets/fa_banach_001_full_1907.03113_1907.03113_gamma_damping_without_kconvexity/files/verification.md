# Verification report

Status: `candidate_full_likely_valid`

## Exact target

- Source: arXiv:1907.03113v1, Corollary 5.5 and Question 5.8, PDF page 20.
- Question: can the K-convexity hypothesis in Corollary 5.5 be dropped?
- Answer proved here: yes.  The conclusion holds on every Banach space.

## Proof audit

1. A family `(A_n)` with `sum_n ||A_n||<infinity` is gamma-bounded.  For
   repeated selected indices, group equal indices.  Each grouped Gaussian
   block is a conditional expectation of the full Gaussian sum, so it is a
   contraction in `L^2(X)`.  The triangle inequality gives gamma-bound at
   most `sum_n ||A_n||`.
2. Products of two gamma-bounded families have gamma-bound at most the
   product of their gamma-bounds.
3. If one damped orbit is gamma-bounded, restriction to `0<=s<1` and the
   Gaussian contraction principle show that every desired local family
   `{exp(-delta s)T_s}` is gamma-bounded.
4. Write `t=n+s`, `n>=0`, `0<=s<1`.  Boundedness of the semigroup gives
   `sum_n ||exp(-delta n)T_n|| <= M/(1-exp(-delta))`.
5. The semigroup law factors the desired operator into one member of the
   discrete summable family and one member of the local family.  The product
   lemma completes the proof for every `delta>0`.
6. For the growth-bound corollary, shift by an ordinary type `b<omega(A)`.
   The shifted semigroup is bounded and one lower gamma-type supplies one
   damped gamma-bounded orbit.  Applying the theorem at damping `b-beta`
   proves that every `beta<omega(A)` is a gamma-type.

## Source evidence

`figures/source_question_page.png` is rendered from page 20 of the official
arXiv PDF and contains Corollary 5.5, the uniformly continuous special case
in Remark 5.6, and Question 5.8.

## Novelty audit

The run's cheap indexes were searched for arXiv:1907.03113, the exact
K-convexity question, Corollary 5.5, and the damped-orbit formula.  No prior
answer was found.  Bounded exact-title and exact-formula web searches did not
recover an indexed later resolution.  The source only proves the uniformly
continuous special case.  Novelty confidence is moderate because this short
factorization may be unindexed folklore.

## Reviewer focus

Check the conditional-expectation treatment of repeated indices in the
summable-family lemma and the sign choices in the growth-bound shift.  Neither
step uses K-convexity, finite cotype, or property alpha.

