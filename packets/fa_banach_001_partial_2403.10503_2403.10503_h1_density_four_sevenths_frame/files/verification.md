# Verification report

Status: candidate substantial partial, likely valid.

## Formal structure checked

- At density `p/q=4/7`, the Lyubarskii--Nes matrix is `4 x 7`.
- The two selected column sets are `(1,4,5,6)` for `0 <= x/a <= 1/8`
  and `(0,1,4,6)` for `1/8 <= x/a <= 1/4`.
- The chosen determinant permutations have no zero factor; every dominant
  factor has dimensionless magnitude at least `1/8`.
- Exact rational arithmetic gives a nearest-term exponent gap at least `7/2`
  for all 23 competing permutations.
- Every non-nearest 7-translate costs at least `7/4` in squared exponent.
  Consequently the absolute remainder-to-leading ratio is nonincreasing for
  `a >= sqrt(4/7)`.
- Fourier symmetry exchanges `a` and `b`, covering all aspect ratios with
  `ab=4/7`.

## Rigorous numerical certificate

Environment: Python 3.11.14, mpmath 1.3.0, 50-decimal outward-rounded
interval arithmetic. Each half interval was divided into 512 equal rational
boxes. Five Zak translates per entry were evaluated directly. The omitted
tail was bounded analytically and added to every entry before forming the
permanent upper bound.

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2403.10503_h1_density_four_sevenths_frame/code/verify_certificate.py
```

Output:

```text
Exact exponent geometry
  0 <= y <= 1/8: columns=(1, 4, 5, 6), lead=(3, 2, 1, 0), max|c|=27/8, min dominant |c|=1/8, permutation gap>=7/2, translate gap>=7/4
  1/8 <= y <= 1/4: columns=(0, 1, 4, 6), lead=(0, 3, 2, 1), max|c|=27/8, min dominant |c|=1/8, permutation gap>=7/2, translate gap>=7/4
Outward-rounded interval dominance at alpha^2=4/7
  0 <= y <= 1/8: worst T/D interval=[1.066358889677944469193530993460813627361907529640166595, 1.077023594634532296048102268937931714831481857700435034]; upper=1.0770235946345321; box=[511/4096,1/8]
    per-entry omitted-tail bound=[6.014401703650894654971789454731342760991840123918237597e-238, 6.014401703650894654971789454731342760991840123942955118e-238]
  1/8 <= y <= 1/4: worst T/D interval=[1.066358889677944469193530993460813627361907529640147885, 1.077023594634532296048102268937931714831481857700451071]; upper=1.0770235946345321; box=[1/8,513/4096]
    per-entry omitted-tail bound=[6.014401703650894654971789454731342760991840123918237597e-238, 6.014401703650894654971789454731342760991840123942955118e-238]
PASS: T/D < 2 on both halves; every selected determinant is nonzero.
PASS: positive exact exponent gaps make T/D nonincreasing for alpha>=sqrt(4/7).
```

Because `T` includes the dominant monomial `D`, `T/D < 2` is exactly the
strict inequality `T-D < D` needed for the reverse triangle inequality.

## Literature and novelty bounds

The run registry and attempt indexes, the source paper citations, arXiv, and
general web search were queried on 12 August 2026 using arXiv ids 2403.10503,
1108.2684, and 2605.26709 and the phrases “first Hermite Gabor frame”,
“rational density”, and “4/7”. No prior `ab=4/7` theorem was found. A May
2026 paper (arXiv:2605.26709) still calls `1/2 < ab < 1` open. This is bounded
novelty evidence, not a guarantee.

## Remaining reviewer checks

1. Compare the rank criterion in the packet with Theorem 2 of arXiv:1108.2684.
2. Recompute the two centered coefficient tables from the selected columns.
3. Confirm the determinant/Zak expansion is absolutely convergent and that
   the permanent counts the absolute mass of all monomials.
4. Inspect `mpmath.iv` outward rounding and the two-sided tail integral.
