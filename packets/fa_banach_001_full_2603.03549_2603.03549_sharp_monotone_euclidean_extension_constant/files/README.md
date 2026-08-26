# Sharp monotone Euclidean extension constant

Source: E. Gargiulo and E. A. Ok, *Order-Preserving Extensions of Hadamard
Space-Valued Lipschitz Maps*, arXiv:2603.03549v1 (2026).

Status: candidate full answer to the quantitative sharpness question in the
concluding paragraph, likely valid.

## Result

For every `n>=1`, there is a finite radial metric poset `X_n` such that

```text
e_{2n,up}(X_n,R^n) = e_up(X_n,R^n) = sqrt(n),
```

where `R^n` has Euclidean distance and coordinatewise order. Hence the
source's coordinatewise `sqrt(n)` upper bound is exactly sharp, already on
data sets of size `2n`. More generally,

```text
e_{2m,up}(X_n,R^n) >= sqrt(m)   (1 <= m <= n).
```

The extremizer is a discrete height-three poset. Its middle antichain maps to
the `2n` points `+/- e_j/2`; monotonicity forces the top and bottom images to
be at Euclidean distance at least `sqrt(n)`.

The packet also corrects a scope issue: the scalar premise behind the upper
bound requires radiality. For arbitrary metric posets, a three-point example
makes the constant arbitrarily large, and one countable separated union has
`e_{2,up}=infinity`.

## Files

- `main.tex`: theorem, proof, finite-k consequence, and scope correction.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_question_crop.png`: exact source paragraph on PDF page 12.
- `code/verify_extremizers.py`: finite arithmetic checks.
- `verification.md`: build, checksum, proof, and visual-QA record.

## Human review recommendation

Check the source's radiality premise, the discrete-poset order convention,
and the two coordinatewise inequalities forcing the top-bottom gap. The
extremal construction itself is finite and elementary.

