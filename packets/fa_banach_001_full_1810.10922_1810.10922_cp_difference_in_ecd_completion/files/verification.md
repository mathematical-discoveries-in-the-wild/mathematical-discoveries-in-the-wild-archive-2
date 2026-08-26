# Verification

Status: passed.

## Mathematical audit

- The weighted transform sends every input state to a subnormalized positive
  operator of `G`-energy at most `E_0`.
- For an energy-`E_0` state, the inverse weighted positive operator has trace
  at most `2`, yielding the reverse norm inequality.
- Discreteness of `G` makes `(I+G/E_0)^(-1/2)` compact and its inverse bounded
  on each finite spectral corner.
- Weighted duals of ordinary bounded approximants are cb-approximable by
  normal Hermitian finite-corner maps.
- Summably accurate corner approximants have summable telescoping increments.
- Normal Wittstock decomposition gives CP positive/negative parts with
  summable cb norms.
- Finite-corner conjugation lifts each CP part to the dual of an ordinary
  bounded CP map, and the weighted norm equivalence preserves summability.
- The source's Theorem 1B places both ECD limits in `F_G^0`.
- The weighted transform is injective on `Y_G` by rank-one density inside
  common energy-bounded positive sets.

## Build and visual QA

- `latexmk` ran `pdflatex` twice with no warnings, overfull boxes, underfull
  boxes, undefined references, or errors in the final log.
- Final packet: 5 US-letter pages, 354281 bytes.
- All five pages were rendered at 120 dpi and visually inspected. The source
  crop, text, equations, proof breaks, bibliography, and margins are clean;
  nothing is clipped or overlapped.

## Final artifact hashes

```text
source_paper.pdf          acbf2692f21d651937fd34afcd0f20216ce9a89cd4613b83a543620812fd0e93
open_problem_crop.png    0604c3bccaaf60f238f7ee632e23647909f3decbdc571bee0fa34bd001782070
solution_packet.pdf       3af9fe75dabab4f026c66da3cc1a06bd3d4a7608be19fcdee58989fe57697d53
```
