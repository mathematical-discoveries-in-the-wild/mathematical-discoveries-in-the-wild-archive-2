# Verification audit

## Source match

The reproduced crop from page 18 of arXiv:2203.12765 asks whether

\[
R(\lambda,A)^\bullet X^\bullet\subset D(A^\bullet)
\]

holds for every \(\lambda\in\rho(A)\). The packet uses exactly the hypotheses
and notation of Theorem 4.7 and Proposition 4.8 in that paper.

## Proof obligations

1. **Seed points.** Proposition 4.8(a) gives the inclusion for every
   \(\operatorname{Re}\lambda>\omega_0(T)\), so the good set contains a
   connected right half-plane.
2. **Equality at a good point.** Theorem 4.7(a) says that if the inclusion
   holds at \(\lambda_0\), then \(\lambda_0\in\rho(A^\bullet)\) and
   \(R(\lambda_0,A)'|_{X^\bullet}=R(\lambda_0,A^\bullet)\).
3. **Relative openness.** For
   \(|\lambda-\lambda_0|\,\|R(\lambda_0,A)\|<1\), the Neumann-series formula
   for \(R(\lambda,A)'\), restricted to \(X^\bullet\), is the identical
   series in \(R(\lambda_0,A^\bullet)\). Its value is
   \(R(\lambda,A^\bullet)\), whose range lies in \(D(A^\bullet)\).
4. **Relative closedness.** If good points \(\lambda_n\to\lambda\in\rho(A)\),
   norm-resolvent continuity gives
   \(R(\lambda_n,A)'x^\bullet\to R(\lambda,A)'x^\bullet\) in \(X'\).
   Closedness of \(X^\bullet\subset X'\) puts the limit in \(X^\bullet\).
   The graph images equal
   \(\lambda_nR(\lambda_n,A)'x^\bullet-x^\bullet\) and converge in
   \(X^\bullet\); closedness of \(A^\bullet\) therefore places the limit in
   \(D(A^\bullet)\).
5. **Component conclusion.** A clopen subset of \(\rho(A)\) is a union of
   connected components. Since the right half-plane is connected, it lies in
   one component, and that whole component is good. Connectedness of
   \(\rho(A)\) forces the good set to be all of \(\rho(A)\).

## Upgrade audit

Four materially different upgrades were pursued after obtaining the partial
theorem: functional calculus across other resolvent components, invariant
subspace spectral-mismatch constructions, standard shift/multiplication
semigroup examples, and an ordinal endpoint-projection example. None settles
an unseeded component while preserving the d-consistent Saks hypotheses. The
last example fails d-consistency and is explicitly excluded, not claimed as a
counterexample.

## Novelty and limitations

The four cheap run indexes were searched by arXiv id, exact title, the exact
open-question phrase, and combinations of “sun dual”, “full resolvent”,
“connected component”, and “spectral hole”. No duplicate solution was found.
The component argument is short enough that it may be unindexed folklore;
novelty confidence is therefore moderate. Human review should focus on the
restriction of the Neumann series to \(X^\bullet\) and the graph-limit argument.

This is a partial result only. It does not prove the inclusion on components
of \(\rho(A)\) disjoint from the right half-plane, and it does not answer the
separate mixed-topology-continuity question.

