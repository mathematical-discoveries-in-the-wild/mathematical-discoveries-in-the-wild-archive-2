# Verification Report

Status: `candidate_full_solution_likely_valid` for the first source question.

## Source

- `source_paper.pdf` is the 19-page arXiv PDF for arXiv:math/0312501.
- The two questions are in Remark 5.5 on PDF page 18.
- `figures/question_crop.png` is a direct readable crop of the full remark.

## Proof checks

1. The source realizes `X` in the 12-corner `I(X)` of its injective-envelope
   linking C*-algebra `I(S_X)`, with `M_l(X)` in the 11-corner and `M_r(X)` in
   the 22-corner.
2. Hence `(a x)b=a(x b)` for a left multiplier `a`, `x in X`, and a right
   multiplier `b`; all three products have the required corner types.
3. The quasicentralizer identity may be used with either outer argument:
   `m(m(x,y),z)=m(x,y) psi(z)` and
   `m(x,m(y,z))=gamma(x)m(y,z)`.
4. Substitution gives both bracketings as `gamma(x)y psi(z)`, proving
   associativity without norm, contractivity, nondegeneracy, or approximate
   identity assumptions.
5. The internal quasihomomorphism check agrees with source Proposition 5.2:
   both `gamma(x)gamma(y)` and `gamma(m(x,y))` act on every `z` as
   `gamma(x)y psi(z)`; multiplier actions are faithful.
6. The theorem answers only the first question. No claim that `QC(X)=QMB(X)`
   is made.

## Upgrade and computational checks

- `attempts/0312501_quasicentralizer_search/search_patterns.py` exhaustively
  checked all connected matrix-unit supports in dimensions through `3x3`:
  4 patterns in `2x2`, 18 each in `2x3` and `3x2`, and 204 in `3x3`.
- `search_subspaces.py` checked all 105 independent 0/1 pairs in `M_2,2`, all
  1,953 pairs in each of `M_2,3` and `M_3,2`, and 400 seeded random independent
  0/1 triples in `M_3,3`.
- Every computation used exact SymPy rational linear algebra. No
  nonassociative QC product was found, as the theorem predicts, and no QC/QMB
  separation was found. These finite checks are not used as proof.

## Novelty check

The cheap run indexes have no exact-id or core-question result. Bounded web and
arXiv searches through 2026-08-13 used the exact source question, paper title,
`quasicentralizer`, `associative quasicentralizer`, and `QMB(X)`. They found
the source paper but no later answer. Novelty confidence is moderate pending
specialist review.

## Rendering checks

- `latexmk` completed after the required passes with no warnings, unresolved
  references, overfull boxes, or underfull boxes.
- `solution_packet.pdf` has 2 US-letter pages. PyMuPDF extracted 3,556
  characters, including text from both pages.
- Both pages were rasterized at 170 dpi and inspected at original resolution.
  The source remark is readable, and no text, equation, footer, or reference
  is clipped, overlapped, or off-page. A stray literal spacing token found on
  the first render was corrected and page 1 was rerendered and reinspected.
- SHA-256: `source_paper.pdf`
  `e10eea18504266a26e5d612caecd677f3f5871e01f53cf02bfac697370f04b68`;
  `figures/question_crop.png`
  `efac3c4543a4ef991234941a082d93e8f61523a8c5c55e0182471642e2a089f7`;
  `solution_packet.pdf`
  `24737454aa2e6dc313171574007a17d10aad4195d5bb45591ece7122ad17d27e`.
