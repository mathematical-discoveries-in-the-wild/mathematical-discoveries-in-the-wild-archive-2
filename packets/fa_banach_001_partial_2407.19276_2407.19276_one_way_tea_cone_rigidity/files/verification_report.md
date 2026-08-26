# Verification report

Verdict: `candidate partial result likely valid; TEA branch fully solved`.

## Claim audit

The packet claims only one-way TEA preservation. It does not infer TEA
preservation from norm-parallel preservation and does not claim the remaining
bijective/rank-greater-than-one parallel case.

The main theorem was checked in the following order.

1. **Kernel lemma.** If a kernel vector has a coordinate below its norm, the
   exact pairs `rv+e_i, rv-e_i` and then `re_i+x, re_i-x` force the whole map
   to vanish. For an `ell_infinity` kernel vector unimodular at every
   coordinate, diagonal normalization gives `T1=0`; three coordinate tests
   force every `Te_i=0`, after which the same plus/minus argument kills all
   vectors. Therefore a nonzero preserver is injective.
2. **Pulled-back norm.** Injectivity makes `q(x)=||Tx||` a genuine norm.
   Linearity of `T` turns one-way TEA preservation into exact additivity of
   `q` on every sup-norm TEA cone.
3. **Cone extension.** The displayed decompositions prove algebraically that
   each cone generates the stated real hyperplane. Additivity therefore gives
   a well-defined real-linear functional; no continuity is invoked.
4. **Complex phase.** For a vector/function vanishing at two norming points,
   the phase-`1` comparison gives `Phi_i(d)=Phi_j(d)`, while phase `-1` gives
   `Phi_i(d)=-Phi_j(d)`. Hence both vanish. This argument is valid over both
   scalar fields.
5. **Third-point step.** In `c_0`, a two-term coordinate split reduces every
   zero-`i` vector to two vectors covered by the two-point result. In `C(K)`,
   an Urysohn partition performs the same split. At least three points are
   available because `Lambda` is infinite.
6. **Global conclusion.** Every `c_0` vector has a norming coordinate and
   every continuous function on compact `beta Lambda` has a norming point.
   A unimodular rotation places the vector in a cone, proving the norm
   identity globally.

## Edge cases

- Zero images and zero vectors are handled explicitly.
- No countability of `Lambda` is used.
- The complex proof treats cone functionals as real-linear, avoiding an
  unjustified complex-linear extension.
- The Urysohn interpolation is disk-valued and explicit:
  `(1-rho)+rho*zeta`.
- The theorem does not assume that the algebraic linear map is initially
  bounded.
- The rank-one parallel counterexample is separated from the TEA theorem.

## Literature and novelty audit

The original arXiv PDF and the authors' final manuscript were inspected. The
question appears as Problem 3.7 in arXiv:2407.19276 and Problem 3.10 in the
2026 JMAA manuscript. Exact phrase, arXiv/title, author-page, run-index, and
close-topic searches through 2026-08-13 found no stated answer. This is a
bounded search, so novelty is not certified.

## Build and visual audit

- `latexmk` completed with no warnings, undefined references, overfull boxes,
  or underfull boxes in the final log.
- The final PDF has five letter-sized pages.
- All five pages were rasterized and visually inspected at 130 dpi.
- The source crop is legible and contains the complete problem statement.
- No clipped equations, stray literal control words, or nearly blank spill
  pages remain.

Recommendation: high-priority specialist review. The proof is short enough
to audit directly; attention should concentrate on Lemmas 2 and 3.

## Checksums

- `solution_packet.pdf`: `d0a456f4b1e06fb38dfa8259b2da3a1b9de87196a9b0c79b1afd1852178f4296`
- `source_paper.pdf`: `28828247d557e181316fbf2c8a6af5261cc79c2ad72b2faa2a8244bb713fd08a`
- `main.tex`: `4d3b2ded4dd0d73fc271a185f024d4afc653dfc49e4614df153f4d3332a651cf`
