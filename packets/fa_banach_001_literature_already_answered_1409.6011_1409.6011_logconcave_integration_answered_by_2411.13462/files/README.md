# Literature answer: cubic integration of well-rounded logconcave functions

- **Source:** Ben Cousins and Santosh Vempala, *Gaussian Cooling and
  O*(n^3) Algorithms for Volume and Gaussian Volume*, arXiv:1409.6011.
- **Answering paper:** Yunbum Kook and Santosh S. Vempala, *Sampling and
  Integration of Logconcave Functions by Algorithmic Diffusion*,
  arXiv:2411.13462, Theorem 1.8.
- **Status:** `literature_already_answered` (affirmative for Conclusion item 2).
- **Model:** `GPT5.6`.

On PDF page 35, Conclusion item 2 of arXiv:1409.6011 asks whether the
Gaussian-cooling algorithm can be extended to integrate any well-rounded
logconcave function with essentially the same cubic complexity.

Kook--Vempala explicitly attribute this extension question to
Cousins--Vempala. Their Theorem 1.8 on PDF page 7 gives a randomized
`(1+epsilon)` multiplicative approximation to the integral of any integrable
well-rounded logconcave function using
`O-tilde(n^3/epsilon^2)` evaluation queries. Thus it supplies the requested
extension with the same dimension exponent and the standard accuracy factor.

Scope limitation: Conclusion item 4 of the source paper, asking for an
`O*(n^3)` rounding algorithm for arbitrary convex bodies, remains open. The
2026 revision of arXiv:2008.02146 and arXiv:2507.18021 still report the best
general bound as roughly `O-tilde(n^3.5)`. The direct attack from this run is
recorded separately in
`attempts/1409.6011_arbitrary_rounding_and_logconcave_integration.md`.

Files:

- `solution_packet.pdf` — compact source/answer identification note.
- `source_paper.pdf` — arXiv:1409.6011.
- `supporting_paper_2411.13462.pdf` — explicit answering paper.
- Ledger: `ledger/results/1409.6011_logconcave_integration_answered_by_2411.13462.json`.
