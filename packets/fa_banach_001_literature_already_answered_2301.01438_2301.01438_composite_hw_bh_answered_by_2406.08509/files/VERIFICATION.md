# Verification report

Verdict: `literature_already_answered`; exact for the source's broad
composite-HW residual, with a stated degree-loss caveat.

## Mathematical and provenance checks

- Source arXiv:2301.01438v3, PDF page 32, asks what can be said for the HW basis
  when `K` is composite and separately asks whether exponential dependence of
  quantum BH constants on degree is necessary.
- Supporting arXiv:2406.08509, Theorem 7 on PDF pages 5--6, treats every
  non-prime `K >= 4` and proves
  `||Ahat||_{2(K-1)d/((K-1)d+1)} <= C(d,K)||A||_op` with
  `C(d,K) <= K^(2d) BH_{Omega_K}^{<=(K-1)d}`.
- The same theorem says `K^(2d)` may be replaced by `|Sigma_K|^d`.
- The text immediately after Theorem 7 says the cyclic BH constants make the
  result dimension-free. Supporting PDF page 6 was checked directly.
- The official arXiv page for 2406.08509 was checked on 11 August 2026. Its
  comments identify an old version in arXiv:2301.01438v2 and describe the
  focused paper as an extension to more general qudit systems. Three of the four
  authors coincide, confirming a direct split/follow-up.
- Section 3 of the supporting source was audited for the scalarization route:
  primitive-pair cyclic subgroups, overlapping composite subgroups, the two
  possible local spectra, averaged eigenprojections, disjoint monomial support,
  scalar degree at most `(K-1)d`, and cyclic BH application.
- Two apparent `(K+1)d` slips occur later in the proof text. The packet uses only
  Theorem 7's displayed `(K-1)d` statement and the preceding degree calculation,
  so it does not propagate those slips.
- The packet does not claim the prime-strength exponent and does not claim that
  optimal quantum BH growth is known.

## Artifact checks

- Both source papers were compiled from their locally cached arXiv TeX sources.
- `source_paper.pdf`: 35 pages; exact question visually inspected on page 32.
- `supporting_paper_2406.08509.pdf`: 30 pages; Theorem 7 visually inspected on
  pages 5--6.
- `solution_packet.pdf`: 2 letter-sized pages; final LaTeX log has no warnings,
  undefined references, overfull boxes, or underfull boxes.
- Both final packet pages were rendered at 170 dpi to 8-bit RGB PNG and visually
  inspected at original resolution. No clipping, overlap, missing glyphs, or
  malformed formulas were found.
- Extracted PDF text contains the status, degree-loss, optimal-growth caveat,
  and provenance statements.
- The result ledger parses as valid JSON and records `"model": "GPT5.6"`.

## SHA-256

- `solution_packet.pdf`:
  `73c6491e235015f66c86e1bd2ba517798bdfc04602af34549cb3bfe81998d994`
- `source_paper.pdf`:
  `9af800344600bec1f0e4ee58c7d8bb0d3d5f7bcf7e4ab5009604344e6f638a8e`
- `supporting_paper_2406.08509.pdf`:
  `b75888017dc404247d5fcc54bb0983636af8c2c4cfe2933905ff186fe92f8df7`

## Human review recommendation

Compare source PDF page 32 with supporting Theorem 7 on pages 5--6, retaining
the theorem statement's `(K-1)d` degree loss. Treat the separate necessity of
exponential dependence on `d` as still open.
