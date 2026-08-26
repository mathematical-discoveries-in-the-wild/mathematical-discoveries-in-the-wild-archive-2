# A lifted dual fiber need not fill the fiber dual

Status: candidate counterexample / full negative answer to the surjectivity question after Proposition 3.22 of arXiv:2508.19635 and Problem 3.11 of the cited source.

## Result

Let `X = N union {infinity}`, put mass `2^{-n}` on `n` and zero mass on `infinity`, and let a free ultrafilter `U` select the value of the scalar lifting at `infinity`. For the constant separable fiber `c_0`, take

```text
M = L^infinity(mu; c_0) = ell_infinity(N; c_0).
```

The lifted fibers at the null point are

```text
ell(M)_infinity       = (c_0)_U,
ell(M*)_infinity      = (ell_1)_U.
```

The map in the question becomes the canonical isometric embedding

```text
(ell_1)_U -> ((c_0)_U)*.
```

It is not onto. Its domain has cardinality at most the continuum `c`. Meanwhile `(c_0)_U` contains an isometric copy of `ell_infinity`, whose `2^c` ultrafilter-limit functionals extend by Hahn--Banach to `((c_0)_U)*`.

## Files

- `main.tex`: complete proof and audit notes.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: arXiv source PDF.
- `figures/open_problem_crop.png`: Proposition 3.22 and the printed open question on page 17.

## Review focus

The key checks are the explicit lifting model and generation identity, the coordinatewise identification `M* = ell_infinity(N; ell_1)`, and the cardinality obstruction. The source paper's weak-star density lemma is compatible with the example: the image is proper but still weak-star dense.

Bounded local and web searches through 2026-08-09 found the original problem and the 2025 paper repeating it as open, but no prior answer. Novelty confidence is medium pending expert bibliographic review.
