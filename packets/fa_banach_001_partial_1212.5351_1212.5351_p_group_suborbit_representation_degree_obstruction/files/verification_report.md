# Verification report

## Result and limitation

The theorem gives a quantitative necessary representation-theoretic condition
for a finite-group orbit to approximate a k-sphere. It settles Problem 2.6
negatively for all proposed actions whose real irreducible degrees are less
than k. It does not settle p-groups possessing and using irreducibles of degree
at least k.

## Proof checks

- The orthogonal irreducible decomposition consists of invariant blocks, so
  each block norm of an orbit point is constant.
- The reverse triangle inequality gives a valid lower bound by the product of
  block-radius spheres; no independence across blocks is assumed.
- For every noninjective block projection, a kernel direction exists.
- The spherical disintegration around that direction has density proportional
  to \((1-t^2)^{(k-3)/2}\), with the transverse direction independent of t.
- The scalar inequality is exactly the variance remaining after optimal
  constant approximation to \(\sqrt{1-t^2}\).
- The beta-integral computations give
  \(E(1-t^2)=(k-1)/k\) and the displayed gamma quotient for
  \(E\sqrt{1-t^2}\).
- Summation uses linearity of expectation only. Parseval for the orthogonal
  block decomposition makes the total energy one when every block is
  noninjective.
- The trace formula for low-degree energy follows by averaging
  \(vv^*\) over the unit sphere of L.

No computational or unproved dependency remains.

## Constant audit

`code/check_constants.py` checks positivity for 2 <= k <= 10 and verifies the
closed form \(\delta_3=1-3\pi^2/32\) to machine precision. This computation is
only a sanity check.

## Novelty and provenance

The local run indexes were searched for arXiv id 1212.5351 and the core weak
Knaster, p-group, and suborbit terms. Exact-title, exact-question, and citation
searches on 11 August 2026 found no later resolution of Problem 2.6 and no
statement of this representation-degree obstruction. Search coverage was
bounded rather than exhaustive.

## Human-review focus

Verify the spherical disintegration and the passage from blockwise average
lower bounds to the trace concentration corollary. The remaining high-degree
case should not be inferred to be impossible from this packet.

