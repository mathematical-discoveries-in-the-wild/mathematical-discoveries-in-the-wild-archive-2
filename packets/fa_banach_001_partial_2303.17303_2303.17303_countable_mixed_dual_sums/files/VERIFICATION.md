# Verification report

Verdict: `strong partial result - likely valid`.

Checks completed:

1. The source question was verified in arXiv:2303.17303v1, page 12, immediately after the equivalence between weak* Lebesgue density and almost-everywhere weak* differentiability of absolutely continuous curves.
2. The proof treats all canonical dual-sum preduals separately:
   - `s=1`: the `c0`-sum of the preduals;
   - `1<s<infinity`: the `ell^{s'}`-sum;
   - `s=infinity`: the `ell^1`-sum.
3. At a point with bounded difference quotients, finite-coordinate weak* limits satisfy the uniform norm bound by weak* lower semicontinuity. Taking the supremum over finite coordinate sets places the assembled derivative in the full `ell^s`-sum.
4. Pairing convergence in the full canonical predual follows from finite-support approximation and the uniform bound on the difference quotients and assembled derivative.
5. For separable-predual coordinates, the simultaneous differentiability set is a countable intersection over a dense scalar test family.
6. For Radon-Nikodym coordinates, the common ACL representative is norm differentiable on almost every coordinate line. Norm-Cauchy convergence of rational difference quotients makes the good set measurable, so Fubini applies.
7. The example `ell^infinity direct-sum_2 ell^1(Gamma)` was checked against both source hypotheses: the first summand prevents the RNP, while choosing `|Gamma|` larger than the continuum prevents any separable predual by cardinality.
8. Bounded local-index and web/arXiv searches found no explicit resolution of the general question or prior statement of this countable mixed-sum class.
9. `solution_packet.pdf` compiled without warnings or box errors. All four
   pages were rendered at 150 dpi and inspected visually; the source crop,
   theorem, proof, endpoint formulas, example, and references are legible and
   unclipped. Text extraction found all expected theorem and scope headings.

No numerical computation is used. The only packet script reproducibly crops the source-question evidence.

Human review should concentrate on items 3, 4, and 6.
