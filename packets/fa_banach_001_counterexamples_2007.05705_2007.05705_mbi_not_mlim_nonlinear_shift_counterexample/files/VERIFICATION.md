# Verification record

## Mathematical checks

- The definitions of MLIM and MBI and the open dichotomy were checked directly
  in arXiv:2007.05705, Definitions 5.1--5.2 and the paragraph after
  Proposition 5.3.
- The scalar gain is continuous, strictly increasing, unbounded, fixes zero,
  and is globally 2-Lipschitz.
- The MBI implication was checked for arbitrary positive `v,w`; no attainment
  of the `ell_infinity` norm is used.
- The two invariant intervals cover every `delta=||w||`: the small-root
  interval for `delta<=1/4` and `[0,1+2delta]` for `delta>=1/4`.
- The displayed MBI modulus is continuous at `1/4`, strictly increasing,
  unbounded, and vanishes at zero.
- The zero-input tail indicators satisfy the recurrence with equality, are
  decreasing in the cone order, and have norm exactly one at every time.
- `code/exact_verifier.py` checks the rational branch identities and long
  recurrence/trajectory prefixes.

## Scope checks

- The counterexample is on the standard normal generating cone of
  `ell_infinity(N)`.
- The operator is continuous, monotone, globally Lipschitz, and has the exact
  max-type gain-operator form with one `K_infinity` edge gain per coordinate.
- The cone is not Levi and the operator is not compact, so there is no conflict
  with Proposition 5.4 of the source.
- The construction is nonlinear and therefore does not conflict with the
  source's linear equivalence theorem.

## Novelty bounds

Searches through 2026-08-12 covered the exact arXiv id and title, the phrases
`MBI property`, `MLIM property`, `monotone bounded invertibility`, and
`monotone limit property`, plus related small-gain literature.  The current
source of arXiv:2503.03925v6 was inspected because it studies closely related
infinite-network MBI conditions; it does not state this additive MBI--MLIM
counterexample or resolve the exact question.  No matching later resolution
was found.  Novelty remains pending expert review.

## Artifact checks

- `code/exact_verifier.py` completed successfully in the run's `sandbox`
  environment.
- The four-page A4 packet compiled without warnings, undefined references, or
  overfull/underfull box diagnostics.
- All four packet pages and the source crop were rendered and visually
  inspected; equations, crop boundaries, citations, and page breaks are clear.
- Packet SHA-256:
  `74423adc0a163030a1ce1009c186bc13541c75e48e31a0aad0f77d6f87f8c92e`.
- Source-paper SHA-256:
  `ec6e587c911db1d3933c5baeda8006a3b0a3d136df749c8b94ea72c5791acc33`.
- Verifier SHA-256:
  `e9fd7a08a163abccd679ed2e279745d38008ba41407d42f253a68785956daa83`.
- Source-crop SHA-256:
  `40391d8416060e1ac9aa6ed3154f5fb2c7da53054a198c5cf147f23a10e81ef6`.
