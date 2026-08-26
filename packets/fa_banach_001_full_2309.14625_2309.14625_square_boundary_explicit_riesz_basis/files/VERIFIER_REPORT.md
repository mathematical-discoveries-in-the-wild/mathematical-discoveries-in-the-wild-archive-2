# Verifier report

Verdict: `candidate full affirmative solution; likely valid`.

## Mathematical audit

- The four edge restriction formula was derived independently from
  `exp(2 pi i (p x + q y))`.
- Each of the four frequency families was checked against the symmetric and
  antisymmetric horizontal/vertical channels.
- The reflection identity `R(s f)=-s^{-1} Rf` was checked directly.
- All input and output reductions are unitary on `L2(0,1)`.
- The remaining constant matrix has determinant `-2` and is therefore onto
  and one-to-one.
- Its Gram characteristic polynomial is exactly
  `(x^2-4x+2)^2`; after the channel factor `sqrt(2)`, the squared bounds are
  exactly `4-2 sqrt(2)` and `4+2 sqrt(2)`.
- Forty randomized direct edge-synthesis checks passed the proved bounds.
- The proof does not rely on the numerical discovery step.

## Novelty audit

Bounded searches on 2026-08-17 covered exact question/title phrases, the
source arXiv id, square and polygon boundary Riesz-basis terminology, the
authors, citation-style queries, arXiv:2507.00581, and a 2025 open-problems
talk. The 2025 paper settles only orthonormal spectrality negatively, and the
2025 slides still list the Riesz-basis issue as open. No matching answer was
found. Novelty remains plausible, not certified.

## Packet audit

- Source paper copied locally: yes.
- Genuine source crop from PDF page 3: yes; full question and immediate
  context are readable.
- Required proof intuition: yes.
- Definitions, theorem, proof, verification, limitations, references, and
  human-review recommendation: yes.
- PDF build: 4 pages, no LaTeX warnings.
- All four rendered pages visually inspected at 150 dpi: yes; no clipping,
  overlap, illegible formulas, or broken references found.
- Packet PDF SHA-256:
  `dee580d156de6caedcfc0280a3812d2e9a1aa4f61b4cb9141e1f56e306db308b`.
- LaTeX source SHA-256:
  `0f82fa07760586b2cacf05472e2e650a550ccb588aa46a0479b48a48c5b0455e`.
- Source paper SHA-256:
  `be9dd5734af616abe9f255edf0b2ed256e3fcb556a5400e5d44c32cacaa4019c`.

## Human-review recommendation

High priority. Verify the channel identities and the indexing of the second
family `(n,n+1)` first. If those are correct, the remaining completeness and
Riesz-bound argument is an exact unitary conjugation to an invertible constant
matrix.
