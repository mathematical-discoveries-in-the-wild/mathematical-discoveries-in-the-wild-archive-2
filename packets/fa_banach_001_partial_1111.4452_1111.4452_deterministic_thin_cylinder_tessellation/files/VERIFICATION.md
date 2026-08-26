# Verification

## Mathematical audit

- The exact conjecture and its allowance of not-necessarily-Gaussian
  hyperplanes were checked in Section 1.7 of arXiv:1111.4452.
- arXiv:2508.05194 was checked for the deterministic/Gaussian distinction,
  the lifted thin-cylinder construction, its final parameter substitution,
  and its sharp iid-Gaussian lower and upper bounds.
- The projective-grid proof was independently audited by a numerical checker
  for interval discrepancy, fiber-to-axis distance, and endpoint arc length.
- The separate attempt note records eight focused full-upgrade routes and the
  obstruction encountered on each unsuccessful route.

## Scope guard

The packet does not claim to prove or disprove Plan--Vershynin's unrestricted
deterministic conjecture. It proves the exact deterministic order only for the
lifted thin-cylinder family used in the 2025 Gaussian counterexample.

## Artifact checks

- [x] Both cited arXiv PDFs are present and readable (18 and 12 pages).
- [x] `main.tex` compiles without errors, warnings, or unresolved references.
- [x] Final PDF metadata and text extraction are healthy (3 letter-size pages).
- [x] Relevant source/support pages were rendered and inspected: original
  conjecture p. 6; 2025 distinction p. 2; construction and final parameter
  substitution pp. 9--10.
- [x] Every page of the final PDF was rendered in RGB and inspected after the
  final compile.
- [x] SHA-256 hashes are recorded below.

Verification completed at `2026-08-11T20:48:49Z`.

## SHA-256

- `main.tex`: `d9615fa18ec98169a55c4d2f36b6386e949bf65e3c5439df7f9d455ff8daaf36`
- `README.md`: `f7b060f73bbc317ea9e57de0ac1622c81a4f93ffa61c62c5c0961de3f8c81aea`
- `solution_packet.pdf`: `b1aa97b1d7fc0a0b7a94a4519344c0001beba777f4896cf9d88132e1b3387d33`
- `source_paper.pdf`: `03cdc94981953db59ecd6d3528dafe3ea4384f7c001e59869da6afe6a3817a57`
- `supporting_2025_paper.pdf`: `209019cc8ae966fd8992cbc29245b352d0f58e2b06d5ce2aab2f0a49dc39befc`
- upgrade attempt: `db2f1b6289c7ff9e13eae0d3da5e36d4ebeafaf3e8801015e60e513dd652723d`
- numerical checker: `ca4d576c8a57ba005b4120787c082ad25257b5c517e9c64f958835d54726b258`
