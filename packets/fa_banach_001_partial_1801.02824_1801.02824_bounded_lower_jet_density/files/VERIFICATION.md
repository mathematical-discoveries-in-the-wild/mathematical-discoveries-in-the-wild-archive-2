# Verification

## Source audit

- The question is on source PDF page 2, immediately after Corollary 1.2, and
  at TeX line 155 of the downloaded source.
- Theorem 1.1 proves only homogeneous `L^{k,p}` density on arbitrary bounded
  simply connected planar domains.
- Corollary 1.2 uses the global `p`-Poincare hypothesis for the full norm.
- The source Section 4 construction and its exact polynomial normalization
  were checked directly from the TeX source.

## Proof audit

1. Descending through the moment identities controls every coefficient of an
   associated polynomial from the bounded lower jet; boundedness of the domain
   turns coefficient control into uniform control throughout `Omega`.
2. In the source partition, every term with a differentiated cutoff can be
   rewritten using `u-P_i` or `P_j-P_i`. Local Poincare/chaining contributes
   scale `2^{-n(k-|beta|)}`, cancelling the cutoff growth down to
   `2^{-n(k-m)}` at derivative order `m<k`.
3. The only uncancelled lower-order pieces are plain `D^m P_i` terms. Uniform
   polynomial control and bounded overlap bound their `L^p` sum by
   `C M |Omega minus D_{n-1}|^{1/p}`.
4. The core exhaustion makes the lower derivative of `u`, the polynomial
   tail, and the scale-decaying chain term all vanish.
5. A flat smooth minorant of boundary distance has every derivative bounded.
   The variable maps `x -> x-eta r(x)y` are uniformly bi-Lipschitz, so
   composition is continuous in `L^p`; every nonprincipal chain-rule term has
   an `O(eta)` derivative of the radius and only a lower derivative of `u`.
6. The argument covers `p=1`; it uses absolute continuity and composition
   continuity in finite `L^p`, not reflexivity or a maximal inequality.

## Scope audit

- The packet claims density only for data in
  `W^{k,p} intersect W^{k-1,infinity}`.
- It does not claim that bounded-lower-jet data are dense in all `W^{k,p}` on
  an arbitrary domain.
- It does not claim a domain-geometric condition weaker than Poincare.
- No counterexample to the unrestricted question is claimed.
- Human review remains unchecked.

## Artifact audit

- `solution_packet.pdf` has 4 pages and 1,447 extracted words.
- The final build has no LaTeX warnings, undefined references, overfull boxes,
  or underfull boxes.
- All four pages were rendered after the final build and visually inspected;
  no clipping, overlap, malformed mathematics, or stale page was found.
- Packet SHA-256:
  `1a4d7d662a18df6b20fefb507d5b74327829fa1e5399557555906a1b1793f94b`.
- Source-paper SHA-256:
  `0d8f283ae89b5738734b130035f309e90afb60d4b7c37f5471f3619147b9df79`.
- Audit timestamp: `2026-08-13T15:21:48Z`.

