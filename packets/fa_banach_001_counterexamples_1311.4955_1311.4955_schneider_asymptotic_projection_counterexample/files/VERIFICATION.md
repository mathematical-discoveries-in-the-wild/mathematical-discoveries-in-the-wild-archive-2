# Verification

Status: candidate full negative solution; mathematical, source, build, and
visual checks completed on 13 August 2026.

## Mathematical checks

- For polytopes `K` and `L`, every facet of `K x L` is of the form
  `F x L` or `K x G`.  Its area and normal give exactly
  `Pi(K x L)=|L| Pi(K) x |K| Pi(L)` through Cauchy's surface-area formula.
  Polytope approximation extends the identity to all convex bodies.
- Taking volume in the projection-body identity and dividing by
  `|K x L|^(a+b-1)` was checked exponent by exponent; all factors of
  `|K|` and `|L|` cancel, so `P(K x L)=P(K)P(L)`.
- The eight facets of `B_1^3` have area `sqrt(3)/2` and normals
  `s/sqrt(3)`.  Pairing antipodal signs gives the four zonotope generators
  used in the packet.
- All four raw 3-by-3 determinants have modulus 4.  Scaling every generator
  by `1/2` gives determinant modulus `1/2`; the symmetric-zonotope formula
  gives `|Pi B_1^3|=2^3*4*(1/2)=16`.
- Since `|B_1^3|=4/3`, the exact value is `P_3(B_1^3)=9`, strictly larger
  than `P_3(C_3)=8`.
- `T_n=S_n/2^n` is supermultiplicative.  The source's uniform exponential
  upper bound makes `log(T_n)/n` bounded above, so Fekete's lemma applies
  and gives existence of the full limit, not merely a bad subsequence.
- The exact checker completed successfully and reproduced the determinant,
  volume, ratio, and first eight Cartesian-power identities.

## Novelty and source checks

- The official arXiv PDF has 12 US-letter pages.  Problem 4.2 on PDF page 9
  was inspected visually and is embedded from `figures/problem_4_2_crop.png`.
- The source TeX was inspected around the definition of `P`, Problem 4.2,
  the exponential upper bound, and the adjacent comparison with the
  Blaschke body of the simplex.
- Cheap run-index searches for the arXiv id, title, Schneider projection
  problem, and projection-body asymptotics found no prior packet, attempt,
  or ledger.
- Bounded exact-phrase and topic searches found the source and later
  descriptions of the still-open exact Schneider projection problem, but
  no cited resolution of Problem 4.2 or the Cartesian-product
  amplification.  This is a bounded search report, not a priority claim.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully in two passes.
- The final log has no warnings, overfull boxes, underfull boxes, undefined
  references, multiply-defined labels, or errors.
- Final artifact: three US-letter pages, 433384 bytes, PDF 1.7, unencrypted.
- All three pages were rasterized at 150 dpi and inspected at original
  detail.  The source crop, formulas, determinant computation, main limit,
  scope, and references are legible, with no clipping, overlap, or stray
  glyphs.
- Ghostscript text extraction was inspected through the full packet and
  contains every logical step and the final qualification.

## Artifact hashes (SHA-256)

- `solution_packet.pdf`:
  `38517d90727775a2bb3e82e0d4bd5ab8df23e91201c7dc99406c5f9968bfbf85`
- `source_paper.pdf`:
  `cb277d90b55fcf999bf5a609c20a39014d498caddc716549fe1b89f0a86e54df`
- `figures/problem_4_2_crop.png`:
  `e88fcfcbaeed724614523d8465cb164804d8a9dbe3b1b790864290539ec7b05a`
- `attempts/1311.4955_asymptotic_schneider_product_counterexample.md`:
  `abe82eb166aebdba0aaf033ae35988be9280491ebb5d9391b1bd56b669c4f7a2`
- `code/verify_projection_product.py`:
  `46901f1d5502dd57412e6b431ef18582dcc4ca6d90193ddeb0ef4da99bc57980`

