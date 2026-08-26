# Verification Report

Status: `candidate_partial_solution_likely_valid`.

## Source

- `source_paper.pdf` is arXiv:2112.08504, 8 pages.
- The Open Problem is on PDF page 6.
- `figures/open_problem_crop.png` is a direct readable crop of that statement.

## Proof checks

1. A finite unbranched cover has locally constant `d`-point fibers, hence
   `pi_* O_U` is locally free of rank `d`.
2. The Grauert--Roehrl/Forster triviality theorem applies because the planar
   domain `Omega` is a noncompact Riemann surface. A global frame therefore
   identifies `O(U)` with `O(Omega)^d` exactly, not merely densely.
3. The balanced-lift definition identifies `L2(mu)` with measurable square
   integrable fiber sections equipped with normalized counting measure.
4. In a holomorphic frame the counting metric has a continuous positive
   definite Gram matrix. Its least and greatest eigenvalues attain positive
   finite bounds on compact `supp(nu)`, making its norm equivalent to the
   direct-sum scalar norm.
5. Equivalent norms preserve density; componentwise approximation proves the
   density equivalence in both directions.
6. A base ABPE bounds each frame coefficient, and the lower Gram estimate
   controls those coefficient norms by the upstairs norm. Local boundedness of
   the frame gives all upstairs evaluations over the base ABPE set.
7. An upstairs ABPE restricted to pullbacks `a compose pi` is a base ABPE,
   since balanced lifting preserves their `L2` norm exactly.
8. The source paper itself states the needed Brennan theorem and the Runge
   identification for precisely the planar connectivity/diameter hypotheses.
9. For the double-cover example, `chi(U)=2 chi(Omega)=-4`; four transposition
   boundary monodromies lift to four boundary components, so
   `2-2g-4=-4` and `g=1`.

## Scope checks

- No claim is made for arbitrary fiber disintegrations or for branching at
  the support.
- Balanced lifting is atomless whenever the base measure is atomless.
- Finite covers of finite-connectivity planar domains have finite genus, and
  collars allow the displayed domains to sit relatively compactly in a
  slightly larger covering surface.

## Novelty check

Bounded web/arXiv searches through 2026-08-13 covered the exact source wording,
finite/unbranched covering variants, balanced measures, direct-image bundles,
and matrix-valued Thomson theorems. No matching result was found. Confidence
is moderate pending specialist search in vector-valued rational approximation.

## Rendering checks

- `latexmk` completed after two `pdflatex` passes with no warnings,
  unresolved references, overfull boxes, or underfull boxes.
- `solution_packet.pdf` has 3 US-letter pages. PyMuPDF extracted 6,043
  characters, including text from every page.
- All three pages were rasterized at 160 dpi and inspected at original
  resolution. The source crop is readable; no text, equation, footer, or
  reference is clipped, overlapped, or off-page.
- SHA-256: `source_paper.pdf`
  `648d79fa997b905556491998c97adb252d01ab018df9b5456ac9990a49358ff3`;
  `figures/open_problem_crop.png`
  `88e447721641953498d7b9af6820363ef3bd420dc06508fbaf72ef38541ff2e0`;
  `solution_packet.pdf`
  `096fd2b6b9a71995c09811ac3733d113f118955f1187f9cd7da89f2c8c6357ff`.
