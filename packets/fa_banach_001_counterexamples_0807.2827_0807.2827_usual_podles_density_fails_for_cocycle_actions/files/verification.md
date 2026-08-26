# Verification note

Verdict: full counterexample to the ordinary Podles-density analogue, with an
exact stabilizer-twisted replacement.

Mathematical checks:

1. `C*(S_3)` has block decomposition `C + C + M_2`; the counit is the trivial
   scalar block.
2. The exterior perturbation formulas
   `alpha = X* beta(.) X` and
   `U = X_23* (id tensor beta)(X*) (Delta tensor id)(X)` satisfy both cocycle
   equations by direct expansion.
3. The chosen `X` is identity on the counit block, hence
   `(epsilon tensor id) alpha = id` and
   `(epsilon tensor epsilon tensor id)(U) = 1`.
4. On the `M_2` block, the flip gives `alpha_p(b) = b tensor 1`, so the usual
   density span restricts to `M_2 tensor C1`, a 4-dimensional proper subspace
   of the 16-dimensional `M_2 tensor M_2` block.
5. For any stabilizer `X`, applying source Lemma 2.2 to
   `beta = X alpha(.) X*` and multiplying on the left by `X*` gives precisely
   the corrected density condition `alpha(B) X* (A tensor 1)`.

Human review should focus on the leg ordering in the exterior perturbation
formula and on the deliberately limited interpretation of the source's broad
phrase “some natural density conditions.”

Artifact checks:

- `latexmk` completed in two passes with no warnings, undefined references,
  overfull boxes, or underfull boxes.
- The final PDF reopens as a four-page A4 document; Ghostscript text
  extraction contains the theorem, upgrade, and references.
- All four final pages were rendered at 144 dpi and visually inspected.  No
  clipping, overlap, broken glyphs, or illegible equations were found.
