# Verification report

Verdict: `likely valid partial result`.

## Checks performed

1. **Block criterion.** A lifting of `D_a` has a linear first coordinate.
   Restriction to the `n`-th block and projection to the `n`-th kernel block
   gives the necessary bound `|a_n| delta_n <= C`. Conversely, uniformly good
   block linearizations assemble on the algebraic direct sum; the uniformly
   bounded error defines a bounded lifting into the completed ELP twisted sum.

2. **Upper ELP estimate.** The displayed recursion gives
   `||phi_1|| <= 1/2` and
   `||phi_(n+1)||^2 <= ||phi_n||^2 + 1/4`. Hence
   `delta_n <= ||phi_n|| <= sqrt(n)/2`.

3. **Lower ELP estimate.** The supporting paper records that the canonical
   kernel in the `n`-th ELP block is at least a constant times `sqrt(n)`
   complemented. A projection associated with a linearization `L` has norm at
   most `max(1, ||phi_n-L||)`, so `delta_n >= c sqrt(n)`. This lower estimate is
   needed only for the exact if-and-only-if characterization, not for the
   positive Macaev and logarithmic-decay conclusions.

4. **Singular-value counting.** The `n`-th scalar block contributes `3^n`
   singular values equal to `|a_n|`, so `s_(3^n)(D_a) >= |a_n|`. If
   `M=sum_j s_j(D_a)/j`, then
   `M >= |a_n| H_(3^n) >= |a_n| n log 3`. Thus
   `sup_n sqrt(n)|a_n| < infinity`. The same follows immediately from
   `s_j(D_a) <= C/log(j+1)`.

5. **Scope audit.** The proof never asserts universal lifting. It applies only
   to operators scalar on the canonical ELP blocks and only to the ELP
   extension. The source problem therefore remains open.

No numerical experiment is used as proof. The only imported mathematical fact
is the published finite-block ELP complementability lower bound, clearly cited
in the packet.

