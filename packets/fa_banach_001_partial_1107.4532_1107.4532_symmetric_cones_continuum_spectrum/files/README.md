# Continuum cone spectra: symmetric cones and a nonpolyhedral obstruction

Status: `candidate_partial_result_likely_valid`.

Source: Bas Lemmens and Roger Nussbaum, *Continuity of the cone spectral
radius*, arXiv:1107.4532.

## Results

- Gripenberg (Proc. AMS 2015) answered the source's general radius-equality
  question negatively by constructing a continuous order-preserving
  homogeneous map with `tilde r_C(f) >= 1 > 1/2 >= r_C(f)`.
- New: a finite-dimensional symmetric cone supports a continuous
  order-preserving homogeneous map whose cone spectrum contains a
  nondegenerate interval if and only if the cone is nonpolyhedral.
- New: there is a closed pointed full-dimensional nonpolyhedral cone in
  `R^3` on which every order-preserving homogeneous self-map has countable
  cone spectrum. Thus nonpolyhedrality is not sufficient in general.

The symmetric-cone map is explicit:

```text
F_a(x) = sqrt(<a,x> x).
```

Its cone spectrum is exactly `sqrt(<a,c>)` over nonzero Jordan idempotents
`c`.

The general classification of all finite-dimensional cones remains open.

Files:

- `solution_packet.pdf`: proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:1107.4532 compiled from the cached official TeX.
- `supporting_eja_1911.00579.pdf`: background on Euclidean Jordan algebras,
  compiled from cached official TeX.
- `verification_report.md`: proof, literature, and artifact checks.

