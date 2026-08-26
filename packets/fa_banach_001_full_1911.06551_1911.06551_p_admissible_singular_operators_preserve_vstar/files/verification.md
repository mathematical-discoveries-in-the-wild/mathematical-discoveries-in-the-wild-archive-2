# Verification report

Status: candidate full proof, likely valid.

## Mathematical checks

- The theorem uses exactly the source's three p-admissibility inputs:
  sublinearity, global `L^p` boundedness, and the off-ball size condition.
- The unit-cover estimate and Morrey estimate are both inherited by every
  measurable truncation of the tail.
- The dyadic exponents cancel to `eta_N` in the `(V*)` estimate and leave
  `2^{-k(n-lambda)/p}` in the Morrey estimate.
- `lambda<n` makes the geometric exponent positive; `lambda=0` is included.
- For fixed `N`, the bounded-origin term tends uniformly to zero on far unit
  balls.
- Far-center unit-ball decay implies the exact cut-off definition of `(V*)`.
- The authors' later generalized-Morrey paper (DOI 10.1002/mma.6235), Section
  5, repeats the same unknown statement; Theorem 5.3 only handles the closure
  of smooth compactly supported functions.

## Computational check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1911.06551_p_admissible_singular_operators_preserve_vstar/code/verify_dyadic_modulus.py
```

The script checks the exact dyadic sum against the displayed logarithmic
majorant over 75,636 parameter samples and compares independent finite sums,
each taken well past its parameter-dependent transition, against the closed
form. This checks arithmetic only and is not a proof.

Observed output:

```text
dyadic checks passed: 75636
worst exact/majorant ratio: 0.498925507192
```

## PDF checks

The final PDF is compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error`. All pages are rendered to PNG and inspected for clipping,
overlap, broken glyphs, figure readability, headers, footers, and page flow.
The final build has four pages and no LaTeX warnings, overfull boxes, or
undefined references. All four rendered pages were visually inspected.

Final SHA-256 values:

```text
solution_packet.pdf             3e9fa5b2a0228e06a6d4bf50bc79004df7d1b1193a16ea52bd86329a8a0c0895
source_paper.pdf                35b3e79cb375e2c7c16224d6e8d97ba6bd9175a7209c71985d0acd1a63ac0771
main.tex                        e11d106c70921fe3a3bc9ae56e1996f57165442377e46fae462a280ed9ff12d5
figures/open_problem_crop.png   73149573babab75388f7ea87a398c07abe6906e49ab57330e52b69fd0efcc8b0
code/verify_dyadic_modulus.py   b285535593e43eece84bbc163670b4028e803af32fbe17600407ab7c6a616bf4
```

## Human-review focus

1. Application of the source size condition to the noncompact truncated tail.
2. The dyadic annulus Holder estimate and transition index.
3. The final passage from far-center decay to the source's cut-off `(V*)`.
