# Verification

Status: candidate full affirmative solution; mathematical, source, build,
and visual checks completed on 12 August 2026.

## Mathematical checks

- The packet reconstructs the unrestricted lifting theorem rather than using
  it as a black box.  A Hamel basis gives every `e in E` a unique finite
  expansion, so the formula defining `X(omega)(e)` is well-defined and linear
  in `e` for every `omega`.
- Each coordinate `X(·)(e)` is a finite linear combination of measurable
  representatives.  Since `E*` carries the cylinder sigma-algebra, this is
  exactly the measurability required for `X:Omega -> E*`.
- Linearity of `Y:E -> L^0(Omega)` implies `[X(·)(e)]=Y(e)` for every `e`;
  hence the constructed map is a genuine `kappa_0` preimage.
- If `e_n -> e`, sequential continuity of `Y` into `L^0` gives convergence
  of `Y(e_n)` to `Y(e)` in the `L^0` topology.  The source identifies this
  topology with convergence in probability.  Coordinate equality in `L^0`
  therefore puts `X` in `L^0(Omega:E*)_prob`.
- On this restricted domain `kappa_0` is, by definition, `kappa_1`; thus the
  proof establishes surjectivity for every probability space and Hausdorff
  locally convex `E`.
- The null-set issue was audited separately.  Probability convergence is
  invariant under changes of representatives on null sets; it does not impose
  the common exceptional set required at the stronger pathwise level.
- Scope was checked against the source diagram: the proof concerns only
  surjectivity of `kappa_1` and does not conflict with the source's
  counterexamples to injectivity or to maps involving the sequential dual.

## Novelty and source checks

- The official arXiv PDF has 22 A4 pages.  The exact open question at the end
  of Section 7 on printed page 17 was inspected visually and is embedded in
  the packet from `figures/source_open_question.png`.
- The source TeX was inspected around Proposition 4.1, the definitions of the
  `prob` spaces, the mapping diagram, and the final open question.  The
  packet's proof follows those definitions literally and reconstructs the
  Hamel-basis argument.
- Cheap run-index searches for the arXiv id, title, `kappa_1`, surjectivity,
  and algebraic-dual probability continuity found no prior packet, attempt,
  or ledger.
- Bounded exact-phrase/title searches found the arXiv paper and its 2025
  journal publication but no later work answering the question.  This is a
  bounded novelty check, not a priority claim.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully in two passes.
- The final log has no warnings, overfull boxes, underfull boxes, undefined
  references, or multiply-defined labels.
- Final artifact: two A4 pages, 262854 bytes, PDF 1.7, unencrypted.
- Both pages were rasterized at 150 dpi and inspected at original detail.
  The title, notation, theorem, source excerpt, Hamel-basis construction,
  continuity step, null-set audit, scope statement, references, margins, and
  page breaks are clear; no clipping, overlap, or stray glyphs were found.
- Ghostscript text extraction was inspected through the full document and
  contains every logical step and the final qualification.

## Artifact hashes (SHA-256)

- `solution_packet.pdf`:
  `9a41b40268a55e7f67c7dca5efddeb676531dfd4b3106f71eeeed2b3771eef1d`
- `source_paper.pdf`:
  `e89b0048003beeb383ddd7694558c9663d2c459382f91e2056f9bda9b43c70d2`
- `figures/source_open_question.png`:
  `be07b75d377cc351db7a190d03adb7acf72eb135af6a81e63a1dc82bad26f335`
- `attempts/2402.04926_kappa1_surjectivity.md`:
  `d190a534690ff71e394307f1520bedff6e2494adede37d4350ed767d657c7430`
