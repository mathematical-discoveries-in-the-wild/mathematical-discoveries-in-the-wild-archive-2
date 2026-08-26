# Investigation and upgrade attempts

1. **Exact extraction and duplicate check.** Located Remark 4.9 and equation
   (4.3) on PDF page 21. Searched the run indexes for the arXiv id, title,
   “complex interpolation”, “weighted Sobolev”, and the exact equation's core
   terms. No prior run packet answered the question.

2. **Boundary-layer scaling.** Tested normal boundary correctors of the form
   `chi(x_1/delta) x_1 g(x')`. Their endpoint norms scale with the critical
   exponent `1+(gamma+1)/p`, explaining exactly why the first derivative trace
   should disappear below the conjectured threshold. This supplied the right
   threshold but not by itself a complex-interpolation proof.

3. **Direct kernel interpolation.** Tried to construct approximate projections
   from the Dirichlet endpoint onto the full-zero endpoint. The required
   analytic family of boundary layers is delicate, and a bare real-method
   estimate does not prove equality for the complex method.

4. **Audit of arXiv:2503.14636.** Roodenburg's Sobolev theorem only gives
   integer interpolation parameters outside the Muckenhoupt range, explaining
   the gap in the source. Its Bessel-potential theorem, however, gives arbitrary
   smoothness inside the Muckenhoupt range and distinguishes boundary
   conditions solely by trace thresholds.

5. **One-step weight shift.** Set `beta=gamma-p` and use multiplication by the
   normal coordinate. This is an isometry at the lower `L^p` endpoint and moves
   `beta` into `(-1,p-1)`. Product-rule trace identities show that the
   Dirichlet endpoint maps into the kernel of normal traces 0 and 1, while the
   full-zero endpoint maps into the kernel of traces 0, 1, and 2.

6. **Surjectivity upgrade.** Proved that the first endpoint map is onto, which
   is the only nonstandard step. Given a function with traces 0 and 1 zero,
   remove its second trace using the universal order-one trace extension at
   the original weight. The remainder has traces 0, 1, and 2 zero, so the known
   multiplication isomorphism on full-zero spaces divides it by the normal
   coordinate with a uniform norm estimate.

7. **Full interval and critical indices.** Applied the arbitrary-smoothness
   Bessel-potential interpolation theorem to the two transformed boundary
   systems. Below smoothness `2+(beta+1)/p`, the order-two condition is absent,
   so the spaces agree at every noncritical parameter. Exact complex
   reiteration between nearby noncritical parameters fills the two critical
   trace indices. Exact-phrase, title/citation, author-page, and arXiv searches
   through 12 August 2026 found no later explicit resolution.

