# Verification record

## Proof checks

- The source identity has the correct orientation:
  `T_f T_g - T_fg = -(H_conj(f))* H_g`. Setting `g = conj(f)` therefore
  produces exactly `-(H_conj(f))* H_conj(f)`.
- Singular values give the exact equality
  `||H*H||_{S_p} = ||H||_{S_{2p}}^2`.
- The source's dilation is unitary on both ambient and Fock spaces, so it
  preserves every Schatten norm, not only the operator norm displayed in
  the source.
- Under `u_r(z)=u(rz)`, normalized local analytic distance satisfies
  `G_1(u_r)(z)=G_r(u)(rz)`. Real dimension `2n` gives the factor
  `r^(-n/p)` in `L^{2p}`.
- Hu--Virtanen Theorem 1.1 applies because it explicitly states
  `L^infinity` is contained in the admissible symbol class. Its comparison
  constants are fixed after the weight and exponent are fixed.
- In the rigidity lemma, the normalized local `L^2` error contributes
  `r^n G_r`, while the `L^2` norm of the differentiated mollifier is
  `O(r^(-n-1))`; their product is `O(r^-1 G_r)`.
- The endpoint `p=n` is valid because the hypothesis yields little-o of
  `r`, not merely big-O.
- Boundedness is used only at the last step, to invoke Liouville for the
  entire representative of `conj(f)`.
- No computational verifier is needed; all identities and exponents were
  independently expanded and checked symbolically in the packet.

## Provenance

- `source_paper.pdf` was downloaded from the official arXiv PDF endpoint on
  12 August 2026; PDF page 10 states the precise open problem.
- `supporting_2012.13768v2_schatten_ida.pdf` was downloaded from the official
  arXiv PDF endpoint; PDF page 3 states Theorem 1.1 and its norm equivalence.
- `supporting_2012.13768v4_corrigendum.pdf` was also downloaded from official
  arXiv. It corrects Theorems 1.2 and 2.6; it does not alter Theorem 1.1,
  which is the only external theorem used here.
- Exact source/support pages and their rendered PNGs are bundled.

## Literature audit

Cheap run indexes and bounded official-arXiv searches by exact paper ID,
exact title, Hilbert--Schmidt Toeplitz quantization, Schatten
semicommutators, and citation links found no later explicit resolution
through 12 August 2026. This is a bounded novelty audit, not a priority
claim.

## Packet QA

- LaTeX build: passed twice with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error`; final packet has three pages.
- Warning scan: passed; no `Warning`, `Overfull`, `Underfull`, `undefined`,
  or `multiply defined` entries in the final log.
- Rendered-page inspection: passed at 130 dpi for all three pages. The exact
  source question is readable, every display is legible, and there are no
  clipped, overlapping, orphaned, or stray literal elements.
- Text-extraction audit: passed; all three pages extract and contain no stray
  `qquad` or `,quad` tokens. (The source screenshot is intentionally raster.)
- Final SHA-256:
  `40157e5378dfc3eb36c964dd9f0b8747dff94d0e380398256fd87171a3c86a45`.
