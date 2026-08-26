# Verification report

Status: candidate full solution, likely valid pending expert review.

## Claim-to-source check

- The source asks whether (z^1 z^2)^s, for the range 0 <= s <= 1/2 fixed in
  the immediately preceding example, can be approximated by rational
  functions in the Löwner class.
- The theorem in this packet supplies compact-open rational Löwner
  approximation for every positive monomial whose total exponent is at most
  one, hence includes the exact source family.

## Proof audit

1. The beta-integral substitutions for the one-variable power and the
   weighted geometric mean were checked algebraically.
2. Every quadrature coefficient is positive.
3. The harmonic block (x^{-1} + lambda y^{-1})^{-1} is jointly operator
   monotone because inversion reverses Löwner order twice.
4. The resolvent block t/(t+lambda) is operator monotone because it equals
   1-lambda(t+lambda)^{-1}.
5. If two scalar functions of a commuting tuple are globally operator
   monotone, their outputs form a commuting pair within each tuple; applying a
   globally operator-monotone binary function therefore preserves order.
6. Rationality and absence of positive-orthant poles survive finite positive
   sums and nested composition.
7. Uniform tail bounds at zero and infinity, followed by ordinary quadrature
   on a compact lambda interval, give local uniform convergence. Recursive
   composition is safe because the positive limit functions have compact
   ranges bounded away from zero on each compact domain.
8. The source paper’s Theorem 8.1 identifies locally operator-monotone
   functions with the Löwner class. Global operator monotonicity implies the
   required local monotonicity.

## Computational status

No computation is used in the proof. No verifier code is included because the
only identities are one-line substitutions and all decisive steps are
operator-order arguments. The rendered PDF was compiled with halted-on-error
LaTeX and every page was inspected after rendering.

## Main review risk

The only interpretive issue is the topology intended by the source’s word
“approximated.” The packet proves locally uniform convergence on the positive
orthant, the standard compact-open interpretation and a stronger conclusion
than pointwise convergence.
