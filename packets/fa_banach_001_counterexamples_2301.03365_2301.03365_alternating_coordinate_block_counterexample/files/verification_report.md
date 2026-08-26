# Verification report

## Mathematical checks

- [x] The blocks `I_k={k^2,...,(k+1)^2-1}` partition the positive integers
  and have size `2k+1`.
- [x] Their alternating signs start and end at `+1`, sum to one, and have
  partial sums only zero or one.
- [x] The ordered frame partial sums are coordinate projections `P_{k-1}` or
  `P_k`, hence converge strongly to the identity on `ell_2`.
- [x] `|f_n(tau_n)|=1` for every index, so the ASF is bounded below.
- [x] The pigeonhole argument defeats every finite partition.
- [x] The repeated-vector argument also defeats the usual Riesz-sequence
  interpretation.
- [x] The construction is nonlocalized, so it does not contradict Theorem
  2.7.
- [x] Exact finite checks passed for the first 29 blocks and exhaustive small
  colorings.

## Source and novelty checks

- [x] Definition 2.4 and Conjecture 2.5 were checked in the rendered primary
  PDF and raw TeX.
- [x] The `ARBs`/`ARSs` terminology mismatch was recorded rather than silently
  repaired.
- [x] Bounded local and web searches found no prior explicit counterexample.

## Artifact checks

- [x] LaTeX compiled without errors or warnings.
- [x] No overfull/underfull boxes or undefined references remain.
- [x] Extracted PDF text contains the construction, frame verification,
  coloring obstruction, and scope limitation.
- [x] Every rendered packet page was visually inspected (three pages).
- [x] The open-problem source crop was visually inspected.
- [x] File types, page counts, and SHA-256 values were recorded.

The final packet is a three-page, US-letter PDF 1.7. The target is a five-page
PDF 1.4. SHA-256:

- `solution_packet.pdf`: `b195094340caf1ca00a89dcad456712887efea68bb6fb7b96dc12d776893eaeb`
- `source_paper.pdf`: `ec76e6554be762992cedad1dbb46dc3ce65b4a5ab80b8a5a12f93b80f16dfe12`

## Human review

- [ ] Human expert review completed.
