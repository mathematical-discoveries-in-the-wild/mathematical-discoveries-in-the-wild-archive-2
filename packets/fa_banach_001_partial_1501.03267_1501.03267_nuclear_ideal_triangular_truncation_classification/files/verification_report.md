# Verification report

## Verdict

Likely valid strong partial answer to Problem 7.4 of arXiv:1501.03267. Human
review is recommended before dissemination.

## Claim audited

For E_a=ell_a when a is finite and E_infinity=c0, standard upper triangular
truncation is bounded on the nuclear ideal N(E_a,E_b) exactly when b<a or
a=b is one of the two endpoints 1 and infinity. In all excluded cases the
finite-section norms grow at least logarithmically.

## Adversarial checks

1. **Matrix orientation.** The source keeps entries with output-row index at
   most the input-column index. Under tr(ST), the trace adjoint therefore
   keeps reverse-operator entries with row at least column. This is lower,
   rather than upper, triangular truncation.

2. **Lower and upper triangles have equal norm.** Reversing both finite
   coordinate orders is an isometry on every ell_a^n and conjugates lower
   triangular truncation to upper triangular truncation. No transpose
   isometry between different ell_p spaces is assumed.

3. **Finite nuclear duality is exact.** For finite-dimensional E and F,
   N(E,F)^*=L(F,E) isometrically under trace pairing. Hence the two finite
   truncation norms are equal, not merely comparable.

4. **Exponent reversal.** Source Proposition 6.3 is applied to the reverse
   arrow L(ell_b,ell_a). Its positive non-endpoint condition is b<a. Its
   negative condition becomes b>=a except for the equal endpoints. This
   confirms the direction of the phase diagram.

5. **Logarithmic lower bound transfers without loss.** Equality of the finite
   norms transfers the source's c log n estimate directly; no
   dimension-dependent duality constant is introduced.

6. **Density in the b<a region.** That inequality forces a>1. The dual of
   ell_a has dense finite-support vectors for 1<a<infinity, and the dual of
   c0 is ell_1 when a=infinity. Finite-support vectors are also dense in
   E_b. Therefore coordinate-finite tensors are dense in the projective
   tensor product defining the nuclear ideal.

7. **The ell_1 endpoint.** For a rank-one matrix y_i alpha_j, its upper
   triangle decomposes by rows. Each tail functional has norm at most
   ||alpha||_infinity, and summing |y_i| gives the original rank-one nuclear
   bound. This avoids the false claim that finite-support vectors are dense
   in ell_infinity.

8. **The c0 endpoint.** Decomposing by columns uses
   sum_j alpha_j e_j^* tensor P_j y. Its nuclear cost is at most
   ||alpha||_1 ||y||_infinity, and every P_j y lies in c0.

9. **Representation independence.** The endpoint estimates are first proved
   on every rank-one tensor, then summed over an arbitrary nuclear
   representation and infimized. The resulting operator is determined by
   its matrix entries, so the construction does not depend on a chosen
   representation.

10. **Necessity for the infinite ideal.** Every coordinate n-by-n nuclear
    ideal embeds isometrically by coordinate inclusions and projections. A
    bounded infinite triangular map would therefore uniformly bound all
    finite restrictions, contradicting logarithmic growth.

11. **Scope.** The theorem answers the source's open-ended existence question
    for other ideals and classifies the nuclear case. It makes no claim to
    classify Pi_{p,q}(ell_r1,ell_r2), the first and harder clause.

## Literature and novelty check

The four cheap run indexes contained no result for arXiv:1501.03267.
Exact-phrase searches on 11 August 2026 for Problem 7.4 and triangular
truncation on summing and nuclear ideals found the source paper and general
triangle-projection references, but no explicit later classification matching
this statement. Because the proof is an immediate-looking trace-dual
consequence of classical results, novelty confidence is deliberately modest.

## Recommended verifier focus

Check the trace-pairing indices and the ell_1 endpoint row decomposition.
Those are the only places where a reversal or a hidden density assumption
could alter the statement.
