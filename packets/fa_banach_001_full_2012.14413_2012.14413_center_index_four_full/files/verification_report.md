# Verification report

## Mathematical audit

The proof was audited around the following possible failure points.

1. **Group structure.**  Center index four gives a unique nonidentity
   commutator `c`, with `c^2=e`, derived subgroup `{e,c}`, and irreducible
   degrees at most two.  An irreducible representation lies in the `+`
   central sector exactly when it factors through the abelian quotient
   `G/{e,c}`, so that sector consists exactly of characters.

2. **Operator diagonal averaging.**  Simultaneous translation by `(c,c)`
   preserves the operator approximate-diagonal equations.  The multiplication
   of its translate is the translate of a bounded approximate identity, hence
   is again a bounded approximate identity.  Averaging therefore retains a
   contractive operator approximate diagonal.

3. **Annihilation of the off-diagonal restriction.**  Restricting a translated
   module-commutator defect to the diagonal yields
   `(tau(a)-a) q_alpha`.  Odd elements give the claim directly.  For even
   elements, four coefficients of a fixed two-dimensional irreducible and the
   identity `sum |u_ij|^2=2` recover the element.  Only the standard
   contractive `B(G)` multiplier action on `A(G)` is used.

4. **Exact half-mass split.**  The central spectral projections are
   preadjoints of central von Neumann algebra summands, so the two surviving
   block norms add.  Each block multiplication acts asymptotically as one half
   of the identity.  Contractivity forces both norms to converge to `1/2`.

5. **Tensor inverse costs.**  The `++` block is the Fourier algebra tensor
   square of the locally compact abelian quotient `G/{e,c}`, so the Banach
   tensor inverse is isometric there.  Runde's degree-two bound controls the
   `--` block by two.  The ordinary approximate diagonal therefore has
   limsup norm at most `3/2`.

No computational experiment is used as proof; the argument is abstract.

## Artifact audit

The packet compiled with `latexmk` in two passes, with no remaining warnings,
undefined references, or overfull/underfull box diagnostics.  The four-page
PDF was rendered at 160 dpi and every page was visually inspected.  The source
crop was rendered from physical PDF page 25 at 220 dpi, retains the full page
width and both margins, contains all of Question 6.2 and its equivalent
center-index-four formulation, and was separately inspected at original
resolution.

SHA-256 values:

- `solution_packet.pdf`:
  `cccd32ad502df02c285dea36acfd8b67f033d6a4e63b862a07089b2d2f4f8275`
- `source_paper.pdf`:
  `a256fb55862d6b47cb4e3e585abf99a28b661a6ec31d3a48764b9022575c73cf`
- `figures/open_problem_crop.png`:
  `d696e5999931f53593e6108c377b50ee7ce1e90ff4c4ad8d944b66f3a8268d10`
- `supporting_papers/2507.05243.pdf`:
  `47d99671e501d020d1547bcaebc0c30ae14353b06b1acdb08adb09cd36cf3fdf`
- `supporting_papers/0409454.pdf`:
  `34ecf404f1ce7de4eb2c01b3336a5f272fac0eeb392e5c22a33cec2bd30f3095`

## Verdict

Candidate full solution, likely valid.  Human review should focus first on
the even-sector matrix-coefficient argument and the identification of the
`++` block with the abelian quotient tensor square.
