# Verification report

Status: full counterexample; mathematical audit passed locally.

## Source evidence

- `source_paper.pdf` is the official arXiv PDF.
- Problem 3.31 is on source PDF page 15.
- `figures/problem331_crop.png` is a readable 220-dpi crop containing the
  complete premise and conclusion with the decisive `>=` sign.

## Mathematical audit

1. Checked that Corollary 3.29 with zero smoothing gives the lower bound
   `H(x)+H(Fx) >= 2 log(delta)` for every normalized 2-box, making the
   printed premise automatic.
2. Checked the group-subfactor specialization to the unitary two-point
   Fourier matrix and Jones index `delta^2=2`.
3. Checked that `x=(1,i)/sqrt(2)` and its Fourier transform both have uniform
   squared moduli and entropy `log 2`.
4. Checked the finite-group bi-shift formula from Proposition 8.1 of
   arXiv:1408.1165.
5. Enumerated both subgroups and both characters of `Z_2`, yielding exactly
   four complex minimizer lines.
6. Checked the exact `L2` distance `1/sqrt(2)` from `x` to each line.
7. Checked the robust operator-norm lower bound `1/2` in case the source's
   unadorned norm means the C*-norm.
8. Checked that `C(epsilon,sqrt(2))->0` contradicts either distance bound.

No numerical experiment or external solver is used as proof.

## Priority human checks

- Confirm the standard classical `Z_2` realization and trace normalization.
- Confirm that the source did not define a different norm immediately before
  Problem 3.31; the counterexample gives positive separation in every norm,
  with explicit bounds for the two natural choices.

## Final artifact audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed successfully.
- The final log contains no warnings, overfull or underfull boxes, undefined
  references, or fatal errors.
- `solution_packet.pdf` has three pages.  All three were rendered at 150 dpi
  with Poppler and visually inspected after the final layout repair.
- The embedded source crop is readable, the decisive inequality sign is
  visible, and no proof text, equation, citation, or footer is clipped.

## SHA-256

- `solution_packet.pdf`:
  `a7f65e9d924ba0a9ea81eb63258b271591e19457d36183317200061f5b324a7a`
- `source_paper.pdf`:
  `2bec0f8589ca0c41ba4b28f3f21a499c83e91b500d4a13b87faad70e7e7dd7dd`
- `figures/problem331_crop.png`:
  `1dadfc856fe136c5a6e9cdc92bf0562d9062e07e7a5dce03cf29136d7501e995`
- `supporting_papers/1408.1165.pdf`:
  `aa017d3719255a95e0399bfcc0e940c16954206aec23fcee784f58f257e628e5`
