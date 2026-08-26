# Verification record

## Source audit

- Target PDF: `source_paper.pdf`, arXiv:1808.01197.
- Exact target: item 3 on PDF page 10, reproduced in
  `figures/source_question.png`.
- The question asks for conditions ensuring evenness of the canonical
  full-line almost-periodic extension of a positive `C`-distribution cosine
  orbit.
- The introduction's “interested in question whether” occurrence is only a
  description of the paper's program.
- The later printed problem on PDF page 12 says “almost periodic” and is, as
  written, already covered by Theorem 2.7(ii); its heading and context indicate
  that “weakly almost periodic” was intended. It is outside this packet.

## Mathematical audit

1. The extension map `F:AP([0,infinity);E)->AP(R;E)` is the source's linear
   surjective isometry and commutes with positive translations. Hence a
   positive half-line almost period has exactly the same uniform error on the
   full-line extension.
2. Relative density supplies arbitrarily large almost periods, so for fixed
   `t` one may require `tau_n>t`.
3. `G(delta_r)Z_2(A) subset Z_2(A)` and the positive-time cosine identity are
   stated in the source immediately after its definition of `Z_2(A)`.
4. The proof does not assume that the component `G(delta_t)` is closed. It
   uses the associated `2 x 2` distribution-semigroup operator, which is
   closed by the source's general `G(T)` construction.
5. The first coordinate of the associated orbit is derived directly:
   `(integral_0^s u(r)dr,u(s))` satisfies the first-order mild equation when
   `u` satisfies the second-order mild equation with initial velocity zero.
6. The cosine identity and the full-line period estimate give uniform
   convergence on `[0,t]`; therefore the first coordinates converge by Bochner
   integration, while the second coordinates converge pointwise at `t`.
7. Closedness and single-valuedness identify the limit with the associated
   orbit from `(0,x)`, whose second coordinate is `G(delta_t)x` by definition.

## Literature audit

Searches performed on 2026-08-11 included:

- exact source title and arXiv identifier;
- the formula `C(-t)x=C(t)x` with distribution-cosine terminology;
- the source phrase “what conditions ensure”;
- author/title and later citations;
- later monograph treatments of subspace almost-periodic
  `C`-distribution cosine functions.

They found the original journal/arXiv versions and later expository reuse of
the framework, but no later theorem answering this exact even-extension
question. This is a bounded search, not a claim of exhaustive novelty.

## Artifact audit

- [x] LaTeX compiled without errors or unresolved references (three passes).
- [x] `solution_packet.pdf` has 3 pages; SHA-256
  `f731ac55c4af17b9eaa18df2e103f8214ec3875e64d50e039929f9c9f52e2887`.
- [x] All 3 rendered pages were visually inspected at full detail.
- [x] The source question crop was visually inspected and is complete.
