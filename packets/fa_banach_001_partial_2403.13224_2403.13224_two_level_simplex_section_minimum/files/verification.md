# Verification record

Status: `likely_valid_partial_result`

## Analytic checks

1. The zero-sum and unit-norm equations give
   `alpha=sqrt(m/(k(k+m)))` and `beta=sqrt(k/(m(k+m)))`.
2. The density at zero is the overlap integral of the two scaled Gamma
   densities. The resulting Gamma integral has exponent `k+m-2`, hence the
   factor `Gamma(k+m-1)`.
3. Simplifying the scale factors gives the displayed closed formula
   `D(k,m)` with homogeneity degree `-1` already fixed by unit normalization.
4. The adjacent ratio was expanded independently; the binomial ratio and
   both power ratios reduce to `A(k)/A(m-1)`.
5. Differentiating `log A` and substituting `t=1/x` gives a negative
   derivative because the comparison function has derivative
   `t^2/(2(1+t)^2)>0`.
6. The strictness range is only the half-range
   `1 <= k <= floor((k+m)/2)`; sign reversal handles the other half.

## Computational check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2403.13224_two_level_simplex_section_minimum/code/verify_two_level.py
```

The script compares selected high-precision Gamma overlap integrals with the
closed formula, checks the adjacent-ratio identity, and verifies strict
monotonicity for all total multiplicities from 3 through 200. Expected result:

```text
PASS: Gamma overlap, closed formula, and ratios checked through d=200
```

This finite computation is a sanity check only. The proof is dimension-free.

## Literature and scope checks

- Tang arXiv:2403.13224, Question 16, is the exact source target.
- Dirksen arXiv:1509.06408 proves the one-sign chamber and dimensions at most
  four. His Remark 3.4/Lemma 3.6 block the naive claim that every sign chamber
  is minimized by its balanced two-level point.
- No exact all-two-level multiplicity comparison was found in the bounded
  local/arXiv search. Novelty confidence is moderate.
- The arbitrary multi-level normal remains open; this packet is not a full
  solution of Question 16.

## Reviewer focus

Check the Gamma-density scaling and the exponent simplification in `D(k,m)`.
These are the only places where a silent factor error could affect the result.

## PDF build and visual QA

- Built with latexmk in nonstop, halt-on-error mode.
- Final packet: 4 US-letter pages, 219 KB.
- Final LaTeX log: no warnings, undefined references, overfull boxes, or
  underfull boxes.
- Rendered all four final pages at 140 dpi with Poppler and inspected every
  page. The source crop, equations, theorem, page breaks, references, margins,
  and page numbers are readable; no clipping, overlap, missing glyphs, or
  broken images were found.
