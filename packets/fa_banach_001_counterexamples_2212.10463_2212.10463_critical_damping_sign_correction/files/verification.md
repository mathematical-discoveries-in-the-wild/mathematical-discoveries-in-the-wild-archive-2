# Verification record

## Source audit

- Official arXiv:2212.10463v2 PDF downloaded on 2026-08-11; 43 pages.
- Page 9, Lemma 4.3(iii), contains the false minus-sign recurrence.
- Page 23 defines the affected critical `M` and `J` kernels and the correct
  `N` kernel.
- Pages 25 and 27 show that the authors first obtain the correct Prabhakar
  inverse transforms and introduce the bad signs only when reducing
  `E^2_{α,β}` to two-parameter Mittag-Leffler functions.

## Independent mathematical checks

1. **Coefficient proof.** Since `(2)_k/k!=k+1`, the coefficient of
   `z^k/Γ(αk+β)` in `αE^2_{α,β}` is `α(k+1)`. The corrected right side has
   coefficient
   `(αk+β-1)+(1+α-β)=α(k+1)`. The printed side does not.
2. **Constant term.** The printed identity at `z=0` is valid only when
   `β=α+1`.
3. **Laplace transforms.** Termwise integration yields
   `L[t^(β-1)E^2_{α,β}(-at^α)] = s^(2α-β)/(s^α+a)^2`, exactly the repeated
   factor in the transformed equation.
4. **Initial velocity.** On compact Fourier support, the printed multiplier
   divided by `t` converges in every derivative to `(2-α)/α`; the corrected
   multiplier converges to `1`.
5. **Unaffected kernel.** Direct partial-fraction decomposition of the
   initial-displacement rational multiplier gives the paper's printed
   `E_{α,1}(-z)+(z/α)E_{α,α}(-z)`.

The script `source_material/verify_sign_identity.py` checks coefficients
through degree 12, high-precision numerical values, and the geometric
series form of the Laplace transform.

Run in the `sandbox` environment on 2026-08-11:

```text
alpha=0.75 beta=2.0 z=-0.3
alpha*E2              = 0.5225067321992348894378991751118000786108
correct plus formula  = 0.5225067321992348894378991751118000786108
printed minus formula = 0.9413096180212058658039213393231936597068
Laplace series check  = 0.06986671360962442105894038073337768439928
Laplace closed form   = 0.06986671360962442105894038073337768439928
printed velocity factor  = 1.6666666666666666667
corrected velocity factor = 1.0
all checks passed
```

## Duplicate and literature checks

- A prior claim for this arXiv id had been screened off as a broad PDE
  target and archived with no artifact or result; the present packet is a
  material mathematical upgrade.
- The run registry contained no earlier result for this paper.
- A bounded full-source search found the false recurrence only in this
  source.
- Exact web searches for the recurrence, paper title plus erratum, and
  critical-damping Mittag-Leffler correction found no later correction.
- The arXiv abstract page confirms v2 (16 July 2023) is the current version.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed.
- Final packet: 4 letter-size pages, 475,767 bytes.
- The final log contains no LaTeX warnings, undefined references,
  overfull/underfull boxes, or errors.
- All four pages were rendered at 150 dpi and inspected individually.
- Both source crops are legible; equations and captions are contained
  within the page bounds; no text or figure is clipped; there are no blank
  or near-blank artifact pages.
