# Verification report

Status: likely valid full counterexample to the literal operator/self-adjoint
formulation, pending human review; scoped partial result for the historically
intended positive-semidefinite conjecture.

## Mathematical checks

1. **Exact source statement.** Equations (1.5)--(1.7) and the sentence declaring
   the constant-one norm comparison open were checked in arXiv:1803.02435.
2. **Scope boundary.** The positive-definite context on page 2 of the 2018 paper
   was checked. Recht--Ré's original arXiv:1202.4184 Conjecture 1 explicitly
   assumes positive semidefinite matrices. The packet therefore does not claim
   a PSD counterexample.
3. **Witness regularity.** The three displayed matrices are symmetric,
   pairwise nonproportional, and have determinants `-4,-6,-3`; hence all are
   invertible and indefinite.
4. **Word enumeration.** Exact enumeration of the six distinct-index words and
   all 27 words gives
   `E_wo=[[521/6,27],[27,641/6]]` and
   `E_wr=(1/27)[[3081,302],[302,3083]]`.
5. **Operator norms.** The larger eigenvalues are exactly
   `581/6+sqrt(829)` and `(3082+sqrt(91205))/27`.
6. **Strict gap.** Since `sqrt(829)>1439/50` and `sqrt(91205)<303`, the norm
   gap is larger than `164/675>0`. No floating-point comparison is used in the
   proof.
7. **Independent exact check.** `code/exact_verifier.py` reran successfully in
   exact SymPy arithmetic and asserted every matrix, eigenvalue, and rational
   bound.
8. **Nonself-adjoint cross-check.** The shorter nilpotent witness in the packet
   independently gives ratio `36/25`, confirming the arbitrary-operator
   failure by a second exact mechanism.

## Upgrade attempts and remaining obstruction

Eight focused attempts covered source/literature auditing; arbitrary-matrix
search; nilpotent exactification; real PSD search; complex Hermitian PSD search;
positive block and shift embeddings; self-adjoint search and bounded-integer
exhaustion; and final exact certification. Real and complex PSD searches through
`n=k=6` and dimensions two and three found no violation, and positivity lifts
destroyed the gap. These computations do not prove the PSD conjecture; they
explain why the result is stopped at the precise self-adjoint/PSD boundary.

## Novelty check

Bounded searches through 2026-08-12 covered the exact arXiv id and title;
symmetrized AGM and weak-variance terminology; the source's citing literature;
Recht--Ré's original paper; and the 2020 Lai--Lim result. The latter resolves a
different, unsymmetrized first-moment/bias conjecture. No located source gives
this `2x2` self-adjoint norm counterexample or records the literal-operator scope
failure. Novelty confidence is moderate pending expert review because the
calculation is elementary once the correct witness is known.

## Artifact checks

- `solution_packet.pdf` SHA-256:
  `62e94e4a0a9c6183d62ee7860ac6c0d9cd1084001e7aa915e2a7909ceeda1813`.
- `source_paper.pdf` SHA-256:
  `c502645bf6024a1e52f47fa6bd194379377f9194f0cf6cb47f2d88f142a7b78e`.
- `original_recht_re.pdf` SHA-256:
  `bc55a0b1d8e320dc9aeebcf213f7e102ce115ac3a0d8e17327110d181b04c263`.
- `code/exact_verifier.py` SHA-256:
  `3b55bba17f1312b1b365fe032e70fde9c96a58779886da74b314f8a4cf446b54`.
- The final packet has three A4 pages and 110 extracted text lines.
- Two-pass compilation completed with no LaTeX warnings, undefined references,
  underfull boxes, or overfull boxes.
- All three pages and both final evidence crops were rendered at 150 dpi and
  visually inspected. Text and formulas are readable; no clipping, overlap, or
  malformed glyphs were found.
