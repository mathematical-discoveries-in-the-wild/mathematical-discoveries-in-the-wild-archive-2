# Verification record

Date: 2026-08-11

## Source evidence

- Official arXiv PDF: `figures/source_2210.07019.pdf`
- Question page: PDF page 7, rendered as `figures/source_page7.png`
- The page contains Theorem 1.3's bound and Question 1.4 verbatim.

## Mathematical checks

The proof was audited along four independent axes:

1. Compact derivative bootstrap: multiplication of a compactly supported
   measure by a coordinate is represented by convolution with a Schwartz
   transform, preserving every subcritical Fourier-decay exponent.
2. Peak geometry: the resulting gradient estimate produces balls of radius
   `R^{-(u-v)/2}`, and their weighted energy exponent was solved symbolically.
3. Compact construction: fixed-width Fourier bumps have critical exponent
   `(s-t)/theta-d`, hence threshold `t+d theta`.
4. General construction: the finite-alpha-moment scaling contributes the
   extra volume exponent `-td/(2 alpha)`, yielding exactly Fraser's bound.

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2210.07019_sharp_fourier_spectrum_holder_bounds/code/verify_exponents.py
```

The script checks the three symbolic identities, evaluates signs on both
sides of each threshold for several parameter choices, and confirms the
superlacunary power dominates fixed exponential losses.

## Review focus

The highest-value human checks are the recursive noninteraction clause in
Lemma 2, the weighted shifted-bump estimate for negative weight exponent,
and the uniform subcritical decay split establishing exact Fourier dimension.
