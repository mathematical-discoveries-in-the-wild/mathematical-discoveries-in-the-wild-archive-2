# Verification report

## Proof audit

- Every smooth circle-valued path on `[0,1]` has a smooth real lift.
- The lift range has diameter at most its total variation, hence at most `pi`
  on `Y_1`.
- Rotating the range endpoints to angles `0` and at most `pi` gives strict,
  opposite signs for the imaginary parts of the mean relative to the two
  endpoints. This proves both nonvanishing and strict interiority of the mean
  direction, including at the sharp endpoint.
- Strict interiority excludes the mean antipode from the compact path image,
  so the principal relative phase is smooth.
- Scaling the relative phase by `1-s` scales total variation exactly by
  `1-s`, fixes constants, and commutes with the antipodal action.
- For `L^1` continuity, the mean direction converges directly. The principal
  argument is uniformly continuous near the fixed limit image; the complement
  has vanishing measure by Markov's inequality and the argument is bounded by
  `pi` there. This establishes convergence of the phases in `L^1`.
- Therefore the construction is a `Z/2`-equivariant strong deformation
  retraction, not merely a homotopy equivalence.

## Computational stress test

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1906.04417_Y1_equivariant_deformation_retract/code/check_mean_contraction.py
```

The script checks a sharp monotone semicircle and forty seeded smooth random
phase curves rescaled below the `pi` threshold. It verifies nonzero mean,
positive distance from the mean antipode, and exact variation scaling along
the contraction.

## Novelty and scope

The run indexes contained no entry for arXiv:1906.04417. Bounded searches used
the exact Problem 6.3 language, `coind Y_n`, `homotopy type of Y_n`, `Y_1`,
`normalized mean`, and the paper title. They found the source paper and Matt
Superdock's 2021 thesis, which reproduces the general bounds and still states
that exact coindex determination is open, but no `n=1` deformation retraction
or later solution. Novelty is plausible rather than certified.

The packet resolves `n=1` and all variation thresholds at most `pi`; it does
not determine `Y_n` for `n>=2`. Five materially distinct routes toward the
general case are recorded in the run attempt note.

## Packet QA

- Source location: official arXiv PDF page 14, Theorem 6.2 and Problem 6.3.
- Official source PDF, TeX, and an exact source crop are included.
- The final PDF is compiled from `main.tex`; all pages are rendered and
  visually inspected before archiving.
- Final PDF: 3 A4 pages; no LaTeX box, reference, or layout warnings.
- SHA-256 `solution_packet.pdf`:
  `0f5e4ef535ae913d9f3f3517d7e143929c2f9e0aba0f5ad5ab93c313374db96f`.
- SHA-256 `source_paper.pdf`:
  `3250504f50f5fcfcc5e6616a8e0ad7878cc867dee092f73c0c6d857b81a1b74d`.
- SHA-256 `source_paper.tex`:
  `e7f73df0b7d9a1d85653127131446e547829456bf7904e532c54d16eae2b6979`.
- SHA-256 `figures/source_problem_page14.png`:
  `5a72f4347a284f7447faf46b4c6eb2c74bd95e9842608dc7ce8902c38a358608`.
- SHA-256 `code/check_mean_contraction.py`:
  `35a57d31eda0df29f1a70b7c807e3908b25e15bc08466ccb4420dd4fac77bd6d`.
