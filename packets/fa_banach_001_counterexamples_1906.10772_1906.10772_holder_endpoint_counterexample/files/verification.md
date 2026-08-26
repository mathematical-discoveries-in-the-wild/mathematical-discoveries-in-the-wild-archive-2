# Verification record

## Proof checks

- At `alpha=1`, the source norm is exactly `||-t f'||_s` because
  `W_+^1 f=-f'` and `Gamma(2)=1`.
- With `b=a+1/q`, `g^q=t^-1 L^(-bq)` is integrable because
  `bq=aq+1>1`.
- The derivative identities near zero are
  `-t f'=aL^(a-1)` and `-t g'=(1/q-b/L)g`.
- `D_+^1 f` is in the uniform closure of `C_c^infinity(0,infinity)`;
  `D_+^1 g` is in `L^q`. The source's exact inverse map therefore puts both
  examples in the natural completions of the claimed spaces.
- `(fg)^q=t^-1 L^-1`, whose integral diverges after the substitution
  `u=L(t)`.
- The source proves `T_q^(1)(t) -> L^q`; failure of `L^q` membership is
  therefore decisive.
- The exponent relation is exactly the conjectured one:
  `1/r=1/infinity+1/q=1/q`, so `r=q`.

## Provenance

- `source_paper.pdf` was downloaded from the official arXiv PDF endpoint on
  12 August 2026.
- PDF page 41 contains Open Question (ii).
- PDF page 13 contains Remark 3.1 defining the proposed endpoint norm.
- Both exact pages are bundled as one-page PDF excerpts and rendered PNGs.

## Literature audit

Run indexes and bounded official-arXiv searches by exact ID, exact title,
endpoint terminology, and core keywords found no later matching
counterexample through 12 August 2026. This is not a priority claim.

## Packet QA

- LaTeX build: passed twice with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error`; final packet has three pages.
- Log warning scan: passed; no `Warning`, `Overfull`, `Underfull`,
  `undefined`, or `multiply defined` entries in the final log.
- Rendered-page inspection: passed at 130 dpi for all three final pages; the
  exact source statement is legible and there are no clipped, overlapping,
  or orphaned elements.
- Final SHA-256:
  `ab8140dfd41e81b3c0d0e1d277d00c4c966968df81c575c15a561f47705e92af`.
