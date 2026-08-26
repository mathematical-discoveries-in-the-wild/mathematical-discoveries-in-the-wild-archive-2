# Verification record

## Exact source locations

- Gao--Troitsky, arXiv:1208.3498, source PDF page 23: immediately before
  Lemma 8.5, the authors say that they need `R_+ T` to consist of
  order-continuous operators and do not know whether this follows from order
  continuity of `T` itself.
- Their definition on source PDF page 3 says that `R_+ T` contains the
  positive scalar multiples of powers and all norm limits
  `lim_j b_j T^(n_j)`.
- Hadwin--Kitover--Orhon, arXiv:1205.5583v2, Example 11 starts on supporting
  PDF page 8. Page 10 proves that its operator `A` is order-continuous.
- Supporting PDF page 15, Remark 15, states that the positive
  order-continuous powers `A^n` converge in operator norm to a spectral
  projection that is not order-continuous (indeed not even sigma-order
  continuous).

Thus the direct literature implication uses `b_j=1` and `n_j=j`.

## Contextual strengthening check

Example 11 also supplies an order-continuous band-irreducible operator
`B_epsilon=A+epsilon L T`. Its construction has:

1. `X=J direct-sum span{1}`, with `J={x:x(0)=0}`.
2. `A(J) subset J` and spectral radius `r(A|J)=0` (the paper proves the
   stronger factorial estimate `||(A|J)^k|| <= 1/k!`).
3. `delta_0 B_epsilon=delta_0`, so `J` is invariant and the induced quotient
   operator is the identity.
4. For every positive `epsilon`, the paper's argument makes `B_epsilon`
   positive, order-continuous, and band irreducible.

Upper semicontinuity of spectral radius gives
`r(B_epsilon|J)<1` for sufficiently small positive `epsilon`. Relative to
`J direct-sum span{1}`, the operator then has block form

`[[C,d],[0,1]]`, with `r(C)<1`.

The power formula gives convergence to `u tensor delta_0`. Remark 15
identifies `J=ker(delta_0)` as an ideal that is not a band, so `delta_0` and
the resulting positive rank-one projection are not order-continuous.

## Artifact checks

- Both arXiv PDFs were downloaded and opened successfully (27 and 18 pages).
- The compact note was compiled into `tmp/build`.
- All final pages were rendered to PNG and visually inspected.
- The final LaTeX log was checked for undefined references, missing
  citations, overfull boxes, fatal warnings, and errors.

## Provenance decision

The supporting paper does not say that it answers the exact Gao--Troitsky
question. The connection is a direct agent identification, so this is a
`literature_implied_answer`, not an explicit `literature_already_answered`
match and not a new run-produced full solution.
