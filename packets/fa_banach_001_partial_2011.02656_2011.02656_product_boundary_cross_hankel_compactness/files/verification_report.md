# Verification report

Verdict: candidate substantial partial theorem, likely valid. Human review is
required before any public mathematical claim.

## Claim audited

For `Omega = D x G`, with `D subset C^a` and `G subset C^b` bounded and
strictly convex, the continuous-symbol version of Theorem 1 in arXiv:2011.02656
holds on `K^2_(0,q)(Omega)` for every `0 <= q <= a+b-1`.  For `q=0`, the
result extends to arbitrary finite products of bounded convex domains.

## Proof checks

- Operator closure: verified
  `||H_phi^q-H_psi^q|| <= ||phi-psi||_infinity`; compact operators are closed
  in operator norm.
- Boundary-cross lemma: verified that the trace of `A(D)` is closed in
  `C(boundary D)` because restriction is an isometry.  Weak holomorphy of the
  boundary-valued map follows from Morera and finite measures.  The annihilator
  argument, Hahn--Banach, inverse trace map, and Hartogs theorem are applied in
  the correct order.
- Boundary geometry: verified by the supporting-functional maximum principle.
  If either coordinate of an analytic boundary variety reaches its factor
  boundary, strict convexity makes that coordinate constant.  If the first
  coordinate never reaches the boundary, the product-boundary condition puts
  the second coordinate on its boundary everywhere, so it is constant.
- Dimension split: checked the exhaustive cases `a,b >= q+1`, exactly one
  factor dimension at least `q+1`, and `a,b <= q`.
- Two-sided case: the cross lemma gives `phi=h+g`, with `h` holomorphic and
  `g` zero on the full boundary.  Only `C^1` approximants to `g` are submitted
  to the source theorem.
- One-sided case: the relevant boundary data form a continuous `A(D)`-valued
  map.  Radial extension is valid because the second factor is convex.
  Polynomial density in `A(D)` follows by inward dilation plus Oka--Weil.
  Smooth partitions of unity give uniform `C^1`, first-variable-holomorphic
  approximants.  The remainder is approximated by functions zero near the
  constrained side.
- Vacuous case: when both factor dimensions are at most `q`, the geometry
  lemma rules out varieties of dimension `q+1`, so arbitrary smooth
  approximation is legitimate.
- Form-level pitfall: the proof does not use compactness of interior-supported
  multiplication on `K^2_(0,q)`, which is generally false for `q>0`.
- Finite-product corollary: after grouping one factor against the remaining
  product, the source hypothesis at `q=0` supplies both boundary-cross slice
  conditions.

No logical dependence on a numerical experiment or unproved computational
claim remains.

## Source and novelty checks

- Theorem 1 and Remark 2 were checked directly in the ingested arXiv TeX for
  arXiv:2011.02656 and in the reconstructed source PDF.
- External retrieval of the official PDF was unavailable.  `source_paper.pdf`
  was compiled from the run's already-ingested official arXiv TeX after the
  clerical correction `onehalfspace -> onehalfspacing`; mathematical content
  was not altered.
- Four cheap run indexes had no hit for the exact question or result.
- Bounded searches found arXiv:2005.14323 (the earlier finite-variety result),
  arXiv:1004.0720 (products of Hankel operators on polydisc/product settings),
  and arXiv:1608.08670 (continuous symbols on convex Reinhardt domains), but no
  theorem matching the packet.  Novelty remains plausible, not certified.

## Artifact checks

- `main.tex` compiled with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error`.
- Final log contains no warning, overfull-box, underfull-box, or undefined
  reference message.
- Text extraction was inspected for all five pages.
- All five rendered page images were visually inspected; no clipping,
  overlap, malformed formula, or unreadable crop was found.
- The source crop contains the complete source Theorem 1 and Remark 2.
- `solution_packet.pdf` SHA-256:
  `5b7932156ad8b73a3d075abbf70909e29c7d7fbb9f273d3df2a09f07b9afc413`.

## Scope limitation

The packet does not answer Remark 2 for an arbitrary bounded convex domain.
The surviving obstruction is compatible smooth approximation across a
possibly nested or accumulating system of affine boundary faces.

