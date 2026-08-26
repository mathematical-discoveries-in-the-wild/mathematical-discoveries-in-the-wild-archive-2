# Verification report

Status: candidate counterexample, likely valid, pending human review.

## Proof obligations

1. **Schrodinger hypothesis:** `H=Delta_D+M_v` is the standard bounded
   nearest-neighbor half-line discrete Schrodinger operator with real bounded
   potential `v in {0,1}`.
2. **No DOS:** a compactly supported continuous function equal to the identity
   on `[0,5]` has volume traces whose two dyadic endpoint subsequences differ.
3. **Block balance:** each alternating dyadic block has harmonic mass
   `log(2)+O(2^(-j))`, yielding half the logarithmic mass for each potential.
4. **Locality:** for a degree-`r` polynomial, diagonal matrix coefficients only
   see radius `r`; the `1/n`-mass of all radius-`r` interface neighborhoods is
   finite.
5. **Continuous functional calculus:** uniform polynomial approximation on
   `[0,5]` preserves the normalized harmonic limit.
6. **Eigenvalue conversion:** Theorem 4.5 of arXiv:2202.03676 applies to
   `f(H)M_(1/n)` and changes the relevant partial sums only by `O(1)`.
7. **Dixmier criterion:** convergence of the normalized ordered eigenvalue
   sums is exactly the criterion used by the source for Dixmier measurability.

All seven obligations are explicitly addressed in `main.tex`. No unproved
lemma is hidden in the packet; obligations 6 and 7 invoke cited published
operator-theory results already used in the source paper.

## Computational sanity check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2202.03676_discrete_schrodinger_dos_dixmier_counterexample/code/check_dyadic_schrodinger.py
```

The script checks dyadic endpoint oscillation, the proved slow
`O(1/log N)` convergence of the harmonic potential average to `1/2`, and the
predicted logarithmic limit `44.5` for the diagonal of `p(H)` with
`p(t)=1+t+t^2+t^3`. At `N=2^20` it returned harmonic values `0.56128268`
and `46.85903388`, consistent with those limits, and ended with `checks: PASS`.
This finite check is not a proof.

## Literature bound

Local run indexes plus bounded web/arXiv searches on 2026-08-09 found no prior
answer. arXiv:2506.21950 (2025), a later thesis by a source author, explicitly
retains the discrete Schrodinger case as unknown.

## Reviewer focus

- Confirm that “discrete Schrodinger type” in the source includes the standard
  half-line operator `Delta_D+M_v`.
- Confirm the indexing/order convention in the modulated eigenvalue formula.
- Check that comparing good sites to the bi-infinite constant-potential model
  is legitimate for every polynomial degree.

## Artifact QA

`latexmk` completed without unresolved references or layout warnings. The
five-page packet and the source-question crop were rendered to PNG, and every
page was visually inspected at full resolution. No clipped text, overlapping
objects, broken glyphs, or unreadable formulas were found. A final extraction
check confirmed the theorem and Dixmier-measurability statement are present.
