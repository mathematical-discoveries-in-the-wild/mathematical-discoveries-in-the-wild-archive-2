# Verification report

## Verdict

Likely valid candidate partial result. No computational dependency is used.

## General symbol theorem

- A nonzero horizontal direction is made the first basis vector.
- Exponential coordinates have polynomial horizontal vector fields with the
  correct weighted degrees.
- Dilating every coordinate except the selected weight-one coordinate gives
  transverse volume \(R^{Q-1}\).
- The sole all-derivatives-on-the-one-dimensional-factor term is killed by the
  assumed symbol kernel. Every remaining term costs at least \(R^{-1}\).
- Thus the left side has order \(R^{Q-2+1/Q}\) and the right side has order at
  most \(R^{Q-2}\).

## Heisenberg Rockland theorem

- The nontrivial dual consists of horizontal characters and Schrödinger
  representations. Characters are ruled out by the general symbol theorem.
- Smooth Schrödinger vectors are Schwartz. Matrix coefficients of Schwartz
  vectors are Schwartz in the horizontal variables and have pure central
  phase.
- A nonzero representation-kernel vector has a nonzero horizontal derivative
  of order \(k-1\); otherwise powers of every skew-adjoint infinitesimal
  generator kill it, hence every generator kills it, contradicting
  nontrivial irreducibility.
- Cutting a matrix coefficient off at central scale \(R^2\) gives
  \(L^{Q/(Q-1)}\) growth \(R^{2(Q-1)/Q}\). Every product-rule term in
  \(A(D)\) has a derivative on the cutoff, costs \(R^{-2}\), and is integrated
  over central length \(O(R^2)\); its \(L^1\) norm is uniformly bounded.
- A horizontal cutoff followed by a limit makes the tests compactly
  supported without changing the estimates, because the coefficient and all
  its horizontal derivatives are Schwartz.

## Novelty check

The four cheap run indexes, the local arXiv corpus, exact-title searches, and
the three works in the OpenAlex citation graph of the source paper were
checked through 2026-08-11. No explicit theorem matching either strengthened
necessity statement was found. This was bounded rather than exhaustive, so
novelty confidence is moderate.

## Main human-review focus

Check the left/right infinitesimal-representation convention in the matrix
coefficient and the uniform product-rule estimate for the central cutoff.

