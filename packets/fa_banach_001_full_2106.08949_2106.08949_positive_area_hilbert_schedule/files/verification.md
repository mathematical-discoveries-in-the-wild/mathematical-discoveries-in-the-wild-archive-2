# Verification report

verdict: `candidate_full_solution_likely_valid`

date: `2026-08-17`

model: `GPT5.6`

## Source checks

- arXiv:2106.08949, Question 2.5 on PDF page 6 asks whether any
  positive-Lebesgue-measure parameter set works for
  `w_n(lambda)=1+lambda/sqrt(n)` on `c0 x c0`.
- Bayart-Costa-Menet, arXiv:2103.13152, Theorem 2.1 gives the exact
  necessary-and-sufficient covering characterization for continuous
  monotone weight families.  Its hypotheses hold on `[1,2]` with
  `F(n)=ceil(sqrt(n))`.

## Proof audit

1. **Weight estimates.** On `[1,2]`,
   `f_n(a)=sum_{s<=n} log(1+a/sqrt(s))` obeys
   `f_n(a)>=sqrt(n)/3` and
   `|f_n(a)-f_n(b)|<=2sqrt(n)|a-b|`.
2. **4-adic cells.** The largest 4-adic length below `beta/n_h` is larger
   than `beta/(4n_h)`.  The exponents are nondecreasing, so every successive
   cell begins on the required finer grid and fits before the endpoint 1.
3. **Finite termination.** If the construction did not reach 1 in finitely
   many cells, their disjoint lengths would dominate a positive multiple of
   `sum_h 1/n_h`, which diverges along the arithmetic progression.
4. **Geometric cover.** A 4-adic interval of length `ell_h` maps under the
   Hilbert construction onto a dyadic square of side `sqrt(ell_h)`.  The
   choice `beta<=tau^2/(4L^2)` puts that square inside the characterization
   rectangle tagged by its upper-right corner.
5. **Pairwise schedule estimate.** Hilbert `1/2`-Holder continuity and the
   harmonic sum between two cells give the desired quadratic jump estimate
   when `n_j/n_k<=2`.  When the ratio is at least 2, the small diameter of the
   fixed parameter square gives it directly.
6. **Cross terms.** The exact logarithm of a cross coefficient is at most
   `2sqrt(n_j+N)|a_k-a_j|-(1/3)sqrt(n_j-n_k)+C_N`.  The pairwise estimate
   makes the positive term at most half of the negative term.
7. **Characterization.** A large arithmetic gap makes all cross terms small;
   a large initial time makes all reciprocal-product terms small.  The finite
   cells cover the entire square, so every clause of Theorem 2.1 holds.
8. **`ell_p` extension.** The direct and cross estimates have summable
   `p`-powers, respectively `exp(-cp sqrt(n_h))` and
   `exp(-cp sqrt((j-k)H))`, uniformly in the finite truncation.

No computational assumption is used.

## Novelty check

The run ledger, registry, attempt index, and local arXiv source corpus were
searched for the source id and exact question.  Exact-phrase and close
weighted-shift web searches through 2026-08-17 returned the source paper and
unrelated common/frequent hypercyclicity results, but no later positive-area
answer.  arXiv:2306.16026 treats critical self-similar fractals of zero area
and does not answer this question.

## Reviewer focus

The two nonstandard points deserving specialist review are the variable-scale
4-adic Hilbert partition and the passage from its Holder estimate to the exact
cross-product ratio in the weighted-shift characterization.
