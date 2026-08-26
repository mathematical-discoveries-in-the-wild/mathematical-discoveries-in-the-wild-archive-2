# Verification Report

## Verdict

`substantial partial result, likely valid`

## Proof audit

| Component | Verdict | Check |
| --- | --- | --- |
| Adjacent finite-q theorem | valid | The integration-by-parts identity is exact. The Holder exponent calculation reduces to `(q(2a+b)-2-b/a) aq/(aq-1)=q(2a+b)`. The `aq=1` endpoint is treated separately. |
| Explicit constant | valid | After Holder, `I^(1/q) <= (q kappa-1)^a ||G||_q`, and `I^(1/q)=||f'||_(q kappa)^kappa`. |
| Symmetric q=1 gaps | valid | `d` integrations by parts give the signed identity exactly; absolute values yield the claimed constant one. |
| Phase-plane energy | valid | Differentiating both `(y')^2` and `H_epsilon(y)` along the ODE gives the same derivative. The first turning point exists because `A=-1` for large values. |
| Smooth compact support | valid | The value cutoff is flat at the orbit minimum. Core and transition-strip estimates give a uniform bound for `f f''`. |
| Higher-center lift | valid | The separated finite difference annihilates moments through order `j-2`; the repeated primitive is therefore compactly supported. Homogeneity cancels the binomial coefficients in the bad ratio. |
| Fractional q=1 failure | valid | `||u u'||_1` is half the total variation of `u^2`, while a rectangular subregion of the Gagliardo double integral gives the stated logarithmic lower bound. |
| Fractional q=infinity bound | valid | Same-sign pairs use Lipschitz continuity of `u^2`; opposite-sign pairs insert an intermediate zero. |

## Computational audit

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2306.06668_adjacent_product_dichotomy/code/verify_adjacent_product.py
```

Results:

- five finite-`q` adjacent tests passed, with normalized left/right ratios
  between `0.46845412` and `0.86974487`;
- five signed symmetric-gap identities through `d=5` had relative errors at
  most `4.55e-16`;
- the sampled phase-plane ratio `sup(f')^2/sup|f f''|` increased from
  `0.435055` to `1.045222` as `log(1/epsilon)` increased from `4` to `16`.

These checks are nonessential sanity tests; the packet proofs are analytic.

## Literature and novelty audit

- No hit for arXiv:2306.06668 or the exact product-coercivity problem appeared
  in the four cheap run indexes before work began.
- Exact-id/title, Open Problem 1.10, product-formula, supremum-endpoint,
  higher-gap, and Opial searches were performed.
- Kałamajska--Peszek arXiv:1104.1967 explicitly contains the known
  one-low/one-high finite-exponent base inequality and is credited/copy-held.
- Klaassen arXiv:2312.05150 treats higher-order Opial inequalities but the
  inspected statements do not give the source problem's derivative-product
  coercivity or endpoint dichotomy.
- No explicit prior statement of the promoted repeated-factor theorem or
  compact-support endpoint obstruction was located. Novelty remains
  provisional and needs specialist review.

## Limitations

- This does not classify wider derivative gaps for `q>1`.
- It does not classify general fractional mean orders.
- For the fractional pair `(0,1)`, only `q=1` and `q=infinity` are newly
  settled here; the source already gives `q=2`.

## PDF QA

- `solution_packet.pdf` compiled to seven US-letter pages without LaTeX
  warnings, undefined references, or overfull/underfull boxes.
- All seven pages of the final binary were rendered at 150 dpi and visually
  inspected. Text, formulas, the source-paper crop, margins, and page breaks
  are legible and unclipped.
- SHA-256: `82840a1ac8daba0c0e7cdc6317ea2e3b3a4c2add0cb57c3d9c443b4ad569cee8`.
