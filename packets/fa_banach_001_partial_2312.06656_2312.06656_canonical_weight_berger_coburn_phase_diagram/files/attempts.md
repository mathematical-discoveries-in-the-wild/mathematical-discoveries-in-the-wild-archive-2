# Upgrade-attempt record

Target: arXiv:2312.06656, Open Problem 1 (Berger–Coburn for `S_p`, `1<p<infinity`).

1. **Extract the source's conditional mechanism.** Remark 6 reduces the positive implication for bounded symbols to boundedness of the Ahlfors–Beurling transform on `L^p(rho^(p-2))`, hence to `rho^(p-2) in A_p`. Applying the same implication to the conjugate symbol makes it an equivalence with norm comparison.

2. **Specialize the geometry.** The source's canonical-weight lemma gives `rho(z) ~ |z|^(1-m/2)` outside a disk. On the disk, positivity and local comparability replace this by the global model `(1+|z|)^(1-m/2)` without changing the `A_p` question.

3. **Prove the exact radial criterion.** For `w_gamma=(1+|z|)^gamma` on the plane, centered large disks force `-2<gamma<2(p-1)`. A near/far disk split proves sufficiency, including disks not centered at the origin.

4. **Solve both endpoint inequalities.** For `m<=2` they hold for every `p>1`. For `m>2` they become `2m/(m+2)<p<2m/(m-2)`. Exact arithmetic also shows the endpoints are Hölder conjugates.

5. **Push the source's Xia computation beyond `p<=1`.** The source already proves `H_f in S_p` for every `p>0` for the cutoff symbol `f(z)=1/z` outside the unit disk. Its mean oscillation satisfies `MO(f)(z) ~ rho(z)/|z|^2`, so the simultaneous Schatten condition reduces to a single radial power integral.

6. **Resolve the low endpoint sharply.** For `m>2`, the radial integral diverges exactly for `p<=2m/(m+2)`; at equality its exponent is `-1`, giving logarithmic divergence. The source's simultaneous characterization then forces `H_bar(f) notin S_p`. This abuts the positive interval with no gap.

7. **Audit duality and interpolation for the high range.** The formal symmetry `p_-^{-1}+p_+^{-1}=1`, Schatten nesting, and interpolation with the Hilbert–Schmidt case do not transfer nonmembership or produce a bounded conjugation map on Hankel symbols. No valid high-`p` conclusion follows.

8. **Audit alternative high-`p` counterexamples and later literature.** Unboundedness of the Beurling transform outside `A_p` does not directly manufacture a bounded symbol with the required IDA/IMO asymmetry. A bounded function holomorphic off a disk has Laurent decay no slower than `1/z`; the Xia symbol is therefore the strongest radial exterior-holomorphic tail of this type, and it cannot reach `p>=p_+`. Searches through 2026-08-12 found adjacent standard/generalized-Fock results but no later solution for doubling Fock spaces. The credible elementary routes are exhausted, so the packet records the high range as open.
