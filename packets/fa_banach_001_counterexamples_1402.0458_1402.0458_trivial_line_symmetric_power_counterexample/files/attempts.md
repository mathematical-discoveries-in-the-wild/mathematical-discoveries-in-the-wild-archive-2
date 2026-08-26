# Attempts and robustness audit

1. **Literal rank-one test.** Taking `L=O_X` makes every symmetric power
   trivial and globally generated. This immediately tests whether the question
   intended strict positivity or semipositivity.

2. **Convention audit.** Definition 4.5 was checked directly. The source first
   requires semidefinite curvature and then requires the curvature operator to
   be nonzero in every nonzero base direction. For a line bundle on a curve,
   this is strict scalar positivity; zero curvature does not qualify.

3. **Topological obstruction.** Chern-Weil theory shows a strictly positive
   curvature form on a compact curve has positive degree, while `deg O_X=0`.
   This yields the stated contradiction independently of a chosen metric.

4. **Analytic cross-check.** In a global frame, every metric is `e^phi`; its
   curvature is `partial bar-partial phi` up to convention. Stokes gives zero
   integral, again ruling out strict positivity.

5. **Higher-rank upgrade.** For `O_X^r`, every symmetric power is globally
   generated. Strict Griffiths positivity would make trace curvature strictly
   positive, contradicting `c_1(det O_X^r)=0`. This confirms the issue is not
   peculiar to rank one.

The result is already a full counterexample. Further attempts would only vary
the same topologically trivial family. The neighboring ample-bundle conjecture
and infinite-dimensional Koszul-Malgrange problem require fundamentally
different ideas and remain outside this packet.
