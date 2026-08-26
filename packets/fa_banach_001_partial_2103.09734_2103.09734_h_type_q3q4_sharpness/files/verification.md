# Verification report

Status: candidate substantial partial result, likely valid.

## Mathematical checks

- Recomputed the input-volume, output-volume, and cap-measure exponents in
  local sphere coordinates.
- Expanded every vertical coordinate and checked that skew-symmetry plus
  common invariance of `V` makes the mixed `V`--`V^perp` terms vanish.
- Checked that `Lambda|_{V^perp}=0` is exactly what controls the tilt term in
  this construction.
- Symbolically substituted the paper's formulas for `Q3` and `Q4`; the
  invariant-block line meets both exactly when `dim V=m+1`.
- Checked concrete 4-dimensional quaternionic and 8-dimensional octonionic
  Clifford models by exact integer matrix multiplication.

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2103.09734_h_type_q3q4_sharpness/code/verify_exponents_and_clifford.py
```

Expected output:

```text
PASS: Q3/Q4 identities and real Clifford models m=3,7 verified
```

The code is not a proof of the measure estimates or of the Clifford-module
classification; those are supplied in the packet.

## Literature/novelty bounds

The four lightweight run indexes, the locally available source corpus, exact
phrases around `Q3 Q4`, `m>=2`, H-type, and Metivier sharpness, and the later
arXiv:2309.07725 were checked.  Two external web searches returned no exact
match.  No source in this bounded search stated the invariant-block theorem or
the `m=3,7` consequence.  Novelty confidence is therefore provisional, not a
claim of exhaustive bibliographic novelty.

## Scope audit

The proof does **not** cover a general Metivier pencil, a general H-type center
dimension, or an arbitrary tilt.  It proves a common-invariant-block theorem
and applies it to untilted H-type groups in center dimensions 3 and 7 (and to
compatible tilts whose transpose range lies in the chosen block).

## Build and visual QA

`main.tex` was compiled from the packet directory with `latexmk`, placing all
intermediates under `tmp/`.  The final log has no undefined references,
overfull/underfull boxes, or substantive warnings.  The final packet is four
A4 pages.  All four pages were rendered at 160 dpi and inspected individually;
the source crop and all formulas are readable, with no clipping or overlap.

Final SHA-256:

```text
1acb390257b86d28e392b532900fc5bdf1c2b7d283765b6bc7eea537e3190683
```
