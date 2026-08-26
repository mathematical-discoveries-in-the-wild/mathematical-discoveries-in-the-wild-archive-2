# Verification report

Verdict: **likely valid candidate full answer**, pending specialist review.

## Exact scope

The packet answers only Remark 3.3 of arXiv:2206.00549: the endpoint
Fourier-to-Schur multiplicatively bounded transference theorem for a
second-countable unimodular locally compact group, with one input exponent and
the output exponent equal to 1 and all other input exponents equal to infinity.
It does not claim the analogous non-unimodular theorem or answer the source's
weak-L1 Calderón–Zygmund question.

## Proof checks performed

1. **Trace-one approximant.** For `k_U=mu(U)^(-1/2)lambda(1_U)=u_U h_U`,
   `h_U^2=k_U^*k_U` has L1 norm one. Left and right group unitaries preserve
   that norm.
2. **Coefficient orientation.** With the inner product linear in the first
   variable,
   `<pi(sr)xi,pi(s)eta>=<pi(r)xi,eta>=m(r)`. The frozen vectors give
   `<pi(b)xi,pi(a^-1)eta>=m(ab)`, matching the Fourier support of
   `lambda_a h_U^2 lambda_b`.
3. **Legitimate L1 estimate.** The proof uses vector-valued Plancherel and
   `||X^*Y||_1<=||X||_2||Y||_2`; it does not infer an L1 multiplier bound from
   the supremum norm of a localized symbol.
4. **Strong-continuity limit.** The two scalar Fourier factors are supported
   in `U a^-1` and `U b`. Their column-vector errors are bounded by the two
   representation moduli of continuity on `U`, hence tend to zero.
5. **First missing source limit.** Source equation (3.8) at the sole L1 index
   has exactly the form covered by the coefficient lemma. All infinity-index
   instances are exact.
6. **Two further CJKM uses.** After the source's `x_j=1` specialization,
   commutators vanish and all later nested terms are scalars. The terminal and
   telescoping uses reduce to `T_m(h_U^(2/q))-m(e)h_U^(2/q)`, with cumulative
   `q` equal to 1 or infinity. The former is the lemma and the latter is exact.
7. **Amplifications.** Finite matrix amplification introduces no new group
   limit; the lemma tensors with matrices or applies entrywise to the finite
   coefficient family. The source finite-truncation theorem then gives the
   global mb estimate.

## Literature check

- Cheap run indexes: exact arXiv id, title, endpoint transference, and core
  Fourier/Schur multiplier phrases.
- Locally ingested arXiv sources: exact-id citations and the phrases describing
  the endpoint exponent pattern.
- arXiv web search on 2026-08-11: exact source id, exact endpoint pattern, and
  later non-unimodular transference paper.
- arXiv:2308.16595 explicitly repeats the endpoint as unknown in 2023.
- No later source in the bounded searches claimed the unimodular endpoint.

## Artifact checks

- The source PDF and decisive CJKM PDF were compiled from their exact locally
  stored arXiv source releases.
- The open-question image is a real crop rendered from source PDF page 11 and
  was visually inspected for completeness and legibility.
- The final packet PDF was compiled to five pages with intermediates under
  `tmp/`. All five pages were rendered at 130 dpi and visually inspected;
  there are no clipped formulas, unreadable figures, or layout defects. The
  final LaTeX log has no overfull, underfull, undefined-reference, or other
  warnings.

## Highest-priority expert checks

- Recheck the vector-column product identity and convention at equation (4.5).
- Compare the two nested reductions line by line against CJKM Lemma 4.6 and
  the modifications stated in the paragraph immediately before source Remark
  3.2.
- Confirm that the source's multiplicative-amplification argument needs no
  uniformity beyond the finite family supplied by the lemma.
