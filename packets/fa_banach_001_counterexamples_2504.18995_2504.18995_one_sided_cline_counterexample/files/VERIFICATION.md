# Verification record

## Source

- Target: Kai Yan, *On the spectral identities and fundamental properties of
  one-sided Drazin inverses in Banach algebras*, arXiv:2504.18995.
- Exact target: Question 3.10, source PDF page 13.
- The official arXiv PDF is retained as `source_paper.pdf`; page 13 was
  rendered at 180 dpi and the question crop was visually checked.

## Exact proof audit

- `D` is an isometry and `C` is a bounded injective diagonal operator.
- `C` is the identity on `Ran(D)`, hence `CD=D` and `D*` is a left inverse.
- Induction gives `(DC)^m=D^m C` for every `m>=1`.
- Since `D^m` is isometric, `||(DC)^m x||=||Cx||`; injectivity of `C` gives
  `H_0(DC)={0}`.
- `||DC e_(2n-1)||=1/n`, so `DC` is not bounded below and has no bounded
  left inverse.
- If `X` is a left generalized Drazin inverse, `Q=XT` is idempotent,
  commutes with `T`, and `T(1-Q)` is quasinilpotent. Therefore
  `Ran(1-Q) subset H_0(T)`. If `H_0(T)=0`, then `Q=1`, forcing a left
  inverse. This contradiction is entirely algebraic plus the spectral-radius
  formula.
- Taking adjoints converts right generalized Drazin identities into left
  ones and preserves quasinilpotence, proving the right-sided failure.

## Later-paper audit

Kolundzija--Mosic, DOI `10.1007/s43036-025-00479-1`, was inspected. Its
Example 3.1 uses `BA e_1=0` and `BA e_n=e_(n+1)` for `n>=2`, so `BA` is the
direct sum of zero and a unilateral shift and is left Drazin invertible.
Since the other displayed diagonal block is quasinilpotent, their reversed
product is left generalized Drazin invertible. The claimed counterexample
therefore fails. This issue is recorded separately under `proof_gaps/`.

## Novelty screen

On 2026-08-12, checked all four cheap run indexes, exact-title and exact-
question searches, citations to arXiv:2504.18995, and searches for one-sided
Cline formulas and one-sided generalized Drazin products. No other valid
unconditional counterexample was found. This is a bounded search and is not
an exhaustive certification of all non-indexed literature.

## Packet QA

The packet was compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error`. Its log was checked for warnings and box diagnostics. Every
page and the source crop were rendered and visually inspected.
