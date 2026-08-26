# A Connes–Dixmier-measurable operator that is not Dixmier measurable

**Status:** candidate full counterexample to Question (i) of Carey–Sukochev,
likely valid and awaiting expert review.

**Source:** Alan L. Carey and Fyodor A. Sukochev, *Dixmier traces and some
applications to noncommutative geometry*, arXiv:math/0608375v2. The question
appears after Corollary 6.8 on PDF page 22.

## Result

The two measurable-operator spaces do **not** coincide. The packet constructs
a compact self-adjoint operator

\[
B\in \mathcal L^{(1,\infty)}(\ell_2\oplus\ell_2)
\]

such that every Connes–Dixmier trace takes the value zero on `B`, while two
Dixmier traces take respectively the values `0` and `2/log(2)`.

The positive and negative Jordan parts are diagonal. Their singular masses are
placed in dyadic rank blocks. A short doubling ramp in the positive part
creates a long plateau in the normalized trace profile; a matching ramp in the
negative part cancels it exactly. The plateaux grow without bound, so a
dilation-invariant generalized limit can detect them. Their logarithmic density
tends to zero, so the logarithmic Cesàro operator used by every
Connes–Dixmier trace erases them.

## Verification

- `code/verify_pulses.py` checks exact ramp cancellation, the dyadic
  monotonicity inequalities needed for decreasing singular values, the growth
  estimates, and convergence of the plateau value to `2/log(2)`.
- `figures/open_problem_crop.png` is a rendered crop of the source question.
- `solution_packet.pdf` contains the complete construction and proof.
- `supporting_paper_1612.04509.pdf` records the previously known affirmative
  result on the strictly smaller weak trace ideal
  `\mathcal L_{1,\infty}` (Theorem 7.7), clarifying the novelty boundary.

Verifier command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/0608375_connes_dixmier_measurable_not_dixmier/code/verify_pulses.py
```

## Scope and reviewer focus

This settles Question (i) negatively in the original Dixmier–Macaev ideal,
already for diagonal self-adjoint operators on a type-I algebra. It does not
address Questions (ii) or (iii) in the source survey.

The principal review points are the elementary prefix estimate proving that
both Jordan parts lie in `\mathcal L^{(1,\infty)}`, and the passage from Følner
interval ultralimits in logarithmic coordinates to dilation-invariant states.

The ledger record is
`runs/fa_banach_001/ledger/results/0608375_connes_dixmier_measurable_not_dixmier.json`.
