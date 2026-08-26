# Exact column–row phase transition on `(R,C)_theta`

This packet gives a complete classification of the column–row property on the
canonical Hilbertian interpolation scale

```text
H_theta = (R,C)_theta,  0 <= theta <= 1.
```

It is a substantial partial answer to the broad question on page 1 of
arXiv:2210.07223, not a classification of all operator spaces.

## Result

For every finite length `n`, the exact norm of column-to-row transposition is

```text
gamma_n(H_theta) = n^max((1-2 theta)/2, 0).
```

Therefore the infinite-dimensional `H_theta` has the column–row property if
and only if `theta >= 1/2`; throughout that range its optimal constant is 1.
The reverse norm is `n^max((2 theta-1)/2, 0)`, so both directions are uniformly
bounded only at `OH = H_(1/2)`.

The packet also proves that column–row constants interpolate by the geometric
mean for every compatible operator-space couple.

## Proof idea

Interpolate the exact endpoint norms `sqrt(n)` on `R`, `1` on `OH`, and `1`
on `C`. Matching lower bounds below the midpoint come from the first `n`
coordinate vectors. Their column and row norms are computed exactly using a
diagonal trace functional in the dual interpolation couple.

## Files

- `main.tex`: full statement and proof.
- `solution_packet.pdf`: compiled proof packet.
- `verification.md`: mathematical and render audit.
- `source_paper.pdf`: arXiv source PDF.
- `source_question_crop.png`: page-1 question and definition.

Status: candidate exact subclass classification, likely valid. Independent
human verification is still requested.
