# Verification report

## Mathematical checks

- [x] Checked `c=a^p`, `q=2/p`, `c^(1/2)=a^(p/2)`, and
  `c^(-q/2)=a^(-1)`.
- [x] Checked the squared-norm identity and the bijective substitutions
  `x -> x^p` and `y -> c^(1/2)y c^(1/2)`.
- [x] Checked every implication in
  `z <= tc iff z^q <= t^q c^q`.
- [x] Checked both exponent branches: `q>1` uses the forward implication;
  `0<q<1` uses the reverse implication with exponent `1/q`.
- [x] Checked the inversion proof of the lower local power rigidity lemma
  against Nagy, Theorem 1.
- [x] Checked sufficiency for central `a` and arbitrary `p`, and for arbitrary
  `a` when `p=2`.
- [x] Ran non-proof floating-point sanity checks in `M_2(C)`.

## Provenance checks

- [x] Confirmed that the problem is at raw-source lines 1581--1587.
- [x] Confirmed that `\end{document}` is at line 1568, so the problem is
  absent from the rendered source PDF.
- [x] Confirmed that the rendered 25-page target ends with its bibliography.
- [x] Confirmed Nagy's Theorem 1 directly from the primary PDF.

## Artifact checks

- [x] LaTeX compiled without errors or warnings.
- [x] No overfull/underfull boxes or undefined references remain.
- [x] Extracted PDF text contains the theorem, both proof branches, and the
  provenance warning.
- [x] Every rendered page was visually inspected (three pages).
- [x] The raw-source problem screenshot was visually inspected.
- [x] File types, page counts, and SHA-256 values were recorded.

The final packet is a three-page, US-letter PDF 1.7. The target source is a
25-page A4 PDF 1.4; Nagy's supporting paper is an 11-page PDF 1.6. SHA-256:

- `solution_packet.pdf`: `0c3f22fbe88bbf21367c3a274e40c6152608b0bf2c0e20e9253efd19b3882035`
- `source_paper.pdf`: `b8356d9bb7cbeb6c44af5a721d6183fc2d7b5ad2db2a4961fd08e3c9c8b7d261`
- `supporting_nagy_2019.pdf`: `4d624e6dd57ba31c6712c7de48955cb8542162c134759e127e57421da37db70c`

## Human review

- [ ] Human expert review completed.
