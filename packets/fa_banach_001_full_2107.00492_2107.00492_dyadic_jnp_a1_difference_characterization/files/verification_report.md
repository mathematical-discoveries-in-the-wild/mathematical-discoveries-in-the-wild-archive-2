# Verification report

## Mathematical audit

- Checked that the seminorm estimate for the dyadic maximal operator is
  Theorem 4.2 of the source PDF, and that the open Coifman--Rochberg-type
  question is stated on source page 2.
- Checked the passage from the seminorm to the normalized Banach norm using
  the dyadic weak-`L^p` embedding, finite-measure `L^{p,infinity}->L^q` for
  `1<q<p`, and strong `L^q` boundedness of the dyadic maximal operator.
- Checked the absolute-value estimate cube by cube, including the mean term.
- Checked norm convergence and pointwise identification of the Rubio de
  Francia series using the continuous embedding into `L^1(Q_0)`.
- Checked positivity, the exact identity `f=u-v`, the comparison
  `w<=u<=3w`, and the resulting uniform dyadic `A_1` bounds.
- Checked the maximal-power refinement from dyadic reverse Holder:
  `z <= (M^d(z^r))^(1/r) <= B M^d z <= B[z]_{A_1^d}z`.
- The theorem intentionally allows bounded positive multipliers in the final
  maximal-power representation. It does not claim the stronger bare
  fixed-`1/p` representation.

## Computational sanity check

Command:

```text
python3 code/verify_finite_dyadic_rubio.py
```

Output:

```text
seed=210700492 depth=8 p=2 trials=40
worst decomposition residual=1.776e-15
smallest majorant slack=6.710e-01
largest Rubio A1 ratio=2.434297
largest u A1 ratio=3.008287
largest decomposition norm ratio=11.860700
PASS
```

The script computes the dyadic maximal function and the exact finite-tree
`JN_p` antichain seminorm. It is an audit aid, not part of the proof.

## Build and visual QA

- Built `main.tex` with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Final log had no undefined references, warnings, overfull boxes, or
  underfull boxes.
- Rendered all four pages at 150 dpi with Ghostscript and visually inspected
  every page. No clipping, overlap, broken formula, or layout defect was
  found.
- `solution_packet.pdf`: 4 pages, letter size.
- SHA-256 `solution_packet.pdf`:
  `8281bc737b3a1d1e4f5ffcf171fa1089e03e671377b943c8a2b658614661af43`.
- SHA-256 `source_paper.pdf`:
  `a7b81a949e04910b150ebc918a1eec2fef69c20f844fb8045680ef08569201a1`.

## Literature audit

Exact-phrase and keyword searches through 2026 found no later statement of
the `A_1^d` difference characterization or its bounded-multiplier
maximal-power refinement. The 2026 paper by Fu--Tao--Yang treats preduals and
fractional dyadic maximal operators, not this decomposition. This is a
bounded search, not a claim of exhaustive bibliographic novelty.
