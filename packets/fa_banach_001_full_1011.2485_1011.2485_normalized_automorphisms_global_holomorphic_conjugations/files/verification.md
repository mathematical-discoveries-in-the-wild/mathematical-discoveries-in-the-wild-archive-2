# Verification record

Status: candidate full solution, likely valid, human review needed.

## Mathematical checks

1. The derogatory locus is the finite projection of
   `rank(lambda I-X)<=n-2`; its complex codimension is exactly three.
2. The spectral incidence hypersurface is Stein and Cohen--Macaulay.  The
   inverse image of the derogatory locus has codimension three.
3. Removing that set gives `H^1(O)=0` by the depth/local-cohomology exact
   sequence and Cartan theorem B.
4. On cyclic matrices the quotient algebra `O[t]/(chi_X)` is the full
   centralizer algebra, including at ramified fibers corresponding to cyclic
   Jordan blocks.
5. Common cyclic vectors give local conjugators jointly continuous in the
   scaling parameter and holomorphic in the matrix variable.
6. The resulting line bundle is topologically trivial by the normalized
   scaling isotopy and holomorphically trivial by injectivity of `c_1`.
7. Hartogs extends the glued conjugator across the codimension-three locus.
   Its determinant cannot acquire zeros supported only there.
8. The argument handles all `n>=2`; `n=1` is immediate.

## Novelty audit

Bounded exact/close searches on 2026-08-13 used the phrases “spectral ball
global holomorphic conjugation”, “spectral unit ball holomorphic
conjugation”, “normalized automorphism spectral ball”, and “derogatory
matrices spectral ball automorphism”.  The source arXiv:1011.2485, Thomas's
arXiv:0801.3396 local result, and Kosiński's arXiv:1202.5793 local/density
result were inspected.  No global conjugator theorem or exact answer to the
first bullet was found.  Novelty confidence is moderate, not definitive.

## PDF verification

The packet was built with `latexmk -pdf -interaction=nonstopmode
-halt-on-error -outdir=tmp main.tex`.  The final PDF is byte-identical to
`tmp/main.pdf`, is 551,326 bytes, has five US-Letter pages, and has SHA-256
`86a6222513fbd3d6df404bd71df262a3bc9a221ad29385c85dcf5a6ff48a4474`.
The final log has no warnings, overfull/underfull boxes, or unresolved
references.  All five pages passed final 150-dpi visual inspection.

## Human reviewer focus

Please check the analytic local-cohomology implication
`codim(W,Y)=3 => H^1(Y\W,O)=0`, and that the parametric Krylov construction
indeed defines one topological line bundle over `[0,1] x Y_U` whose endpoint
is the holomorphic obstruction bundle.
