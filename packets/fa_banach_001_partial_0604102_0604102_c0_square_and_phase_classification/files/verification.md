# Verification report

Status: `candidate_strong_partial_likely_valid`

## Proof audit

- **Source match:** pages 16--17 isolate the real nonsurjective functions
  `g(t)=t^2` and `g(t)=-t^2`; page 18 asks whether the complex subgroup
  properties are equivalent.
- **Positive direction:** the packet proves the Daugavet slice criterion by a
  local cutoff at a non-atom of the slice-defining regular measure.
- **Availability of a non-atom:** every nonempty open subset of a locally
  compact Hausdorff space without isolated points is an uncountable Baire
  space, while a finite measure has only countably many atoms.
- **Real positive-square obstruction:** the explicit witness has norm one,
  trace `1/8`, square `(1/8)T`, and exact row norm `17/16`, strictly below
  `1+||T^2||=18/16`.
- **Real negative-square obstruction:** the isolated-coordinate projection
  gives `||I-P^2||=1<2`.
- **Complex phase obstruction:** the same projection gives
  `||I+omega P||=max(1,|1+omega|)<2=||I+P||` for every `omega!=1`.
- **Endpoint:** the assumption `|L|>=2` is necessary for the real positive
  square theorem because `C_0({p},R)=R` satisfies that identity trivially.

No mathematical gap is currently identified inside the stated scope.

## Computational guard

`code/check_obstruction.py` uses exact rational arithmetic to verify the three
evaluation row norms, the `1/8` trace, and the final `1/16` gap. The analytic
total-variation calculation in the packet is the proof.

## Literature bounds

Searched the lightweight run indexes, local full-source corpus, official
arXiv, and bounded web results using arXiv:math/0604102, the source title, both
square identities, `rank-one square Daugavet`, `extremely non-complex`, and
the fixed-phase identity. Adjacent arXiv:0811.0577 and arXiv:0901.1512 cite
the source and construct extremely non-complex spaces, but do not state this
classification. Novelty remains provisional.

## Artifact QA

- `source_paper.pdf` is the official 21-page arXiv PDF.
- Source-question crops come from rendered PDF pages 16--18.
- The final four-page packet compiled without LaTeX warnings, overfull boxes,
  or underfull boxes.
- All four frozen pages were rendered at 144 dpi and visually inspected after
  the last edit; the source crops, theorem statements, displayed formulas,
  exact obstruction, references, and page boundaries are clear and unclipped.
- Ghostscript text extraction found no stray `qquad`/`quad` tokens from the
  display-source markup.
- Final SHA-256:
  `7c2f2b58ed6b2952ba3dc7214a8d3912769e4b6b3673e86242306ff4ec36e051`.
