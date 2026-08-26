# Full solution packet: nonseparable quasitubal qSVD and Eckart--Young

## Source

- Uria Mor and Haim Avron, *Quasitubal Tensor Algebra Over Separable
  Hilbert Spaces*, arXiv:2504.16231.
- Question: Section 9, pages 32--33 of the arXiv PDF, asking how to define
  the framework and establish optimality results for nonseparable Hilbert
  spaces.
- Model: GPT5.6.

## Classification

- Status: `full_solution_likely_valid`.
- Scope: full affirmative solution of the nonseparable-Hilbert-space branch
  of the source's theoretical future-work question.
- The separate Banach/semi-inner-product branch is not claimed.

## Result

Let `H` be an arbitrary Hilbert space, with no separability assumption, and
fix an orthonormal basis indexed by an arbitrary set `I`. The coordinate
transform identifies `H` with `ell_2(I)`. Coordinatewise multiplication gives
the tubal algebra on `H`, every module endomorphism is automatically bounded,
the endomorphism algebra is exactly `ell_infinity(I)`, and matrices over this algebra admit a qSVD obtained by a
finite-dimensional matrix SVD at each index.

For every finite matrix `X` with entries in `H`, all scalar singular values
form a square-summable family and hence have countable support even when `I`
is uncountable. Ordering them decreasingly as `sigma_1 >= sigma_2 >= ...`, the
truncation retaining the largest `q` scalar singular components has implicit
rank at most `q` and satisfies

```text
inf_{implicit-rank(Y) <= q} ||X-Y||_H,F^2
    = sum_{n>q} sigma_n^2.
```

It also converges in the induced operator norm, with residual norm
`sigma_{q+1}`. Each truncation uses at most `q` basis coordinates and is
therefore finitely representable.

## Idea of Proof

Nothing in the quasitube algebra requires the basis to be countable:
diagonal bounded multipliers of `ell_2(I)` are `ell_infinity(I)`. Likewise,
pointwise matrix SVD needs no measurable-selection theorem because
`ell_infinity(I)` contains every bounded scalar family. The only apparent
obstacle is globally sorting singular values over an uncountable set. It
disappears for actual Hilbert-valued tensors: an `ell_2(I)` family has at most
countable support. Matrix Eckart--Young on each active slice, followed by the
elementary optimal allocation of a total rank budget across slices, gives the
global formula.

## Verification and novelty

- `code/verify_nonseparable_extension.py` exhaustively checks every allocation
  of a finite total rank budget across randomly generated slices, comparing it
  with global singular-value truncation.
- The proof isolates the one point where finite rank, rather than an
  erroneous algebraic treatment of infinite sums, is used.
- Cheap run indexes had no exact duplicate. Bounded exact-title and keyword
  searches found the source and later finite-dimensional tubal-product work,
  but no nonseparable arbitrary-index extension.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: compiled and visually inspected proof.
- `source_paper.pdf`: downloaded source paper.
- `figures/open_problem_crop.png` and
  `figures/open_problem_crop_continuation.png`: exact source excerpt.
- `code/verify_nonseparable_extension.py`: deterministic finite-model check.
- `verification_report.md`: recorded mechanical and visual checks.
- `novelty.md`: bounded novelty search record.
