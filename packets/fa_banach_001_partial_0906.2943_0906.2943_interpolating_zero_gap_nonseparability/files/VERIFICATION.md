# Verification record

## Mathematical dependency audit

- The proof uses the normalized reproducing-kernel formula at a zero of
  `Theta=E#/E`, written in the proof of Proposition 3.8 of the source.
- The only added functional-analytic hypothesis is explicit: the selected
  normalized kernels form a Riesz sequence, so their synthesis map is bounded
  on `ell_2`.
- Both majorization conditions are checked.  The `F` quotient has poles at
  conjugate zeros; the `F#` quotient carries the factor `Theta` and poles at
  the upper-half-plane zeros.  On `iy`, `|Theta| <= 1` and the second
  denominator is uniformly comparable to `max(y,|v|)` after discarding a
  finite initial set.
- The block coefficient identity is exact:
  `sum |lambda_v|^2/Im(v) = |Delta_k|^2/H_k`.
- The lower bound is taken only from the `F` majorization term and recovers
  bounded-sequence partial sums at geometric-mean gap points.

## Automated sanity check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/0906.2943_interpolating_zero_gap_nonseparability/code/verify_weighted_blocks.py
```

The script tests 80 deterministic random bounded sequences on five finite
lacunary blocks.  It checks the energy identity, both scaled Cauchy transforms,
and recovery at gap points.  These finite checks do not prove the theorem.

Transcript:

```text
trials=80
worst_energy_identity_error=7.994e-15
worst_scaled_cauchy_ratio=1.387441
worst_block_recovery_relative_error=0.019704
finite weighted-block checks passed (not a proof)
```

## Packet build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed
  in two passes with resolved references and no final warnings or errors.
- The final packet has five letter-size pages.  All five pages were rendered
  and inspected; the two proof pages affected by the final clarification were
  re-rendered at 160 dpi and remain unclipped and legible.
- The source-evidence crop on page 5 includes the complete statements of
  Theorem 3.2 and Remark 3.3 from source-paper page 7 and is readable at the
  packet's native scale.
- Ghostscript text extraction confirms the theorem conclusion, the completed
  low-`y` block estimate, and the quoted Remark 3.3 evidence are present.

## Human-review focus

1. Verify the unimodular normalization in equation (11).
2. Check the denominator comparison for the sharp-conjugate transform.
3. Check that recursive block selection can impose both arbitrarily large
   total height and the stated lacunary gap.
4. Confirm the interpolating property of the explicit sequence
   `2^n+i/n`, or omit the example without affecting the main theorem.
5. Treat clustered/multiple zeros as unresolved.
