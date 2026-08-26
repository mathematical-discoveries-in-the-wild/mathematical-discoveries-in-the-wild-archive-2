# Verification note

Verdict: full negative answer to Open Question 8.

Mathematical checks:

1. `N=closed_D(0,1/4) union J` is compact and connected and contains a
   relatively open neighborhood of 0 in the closed unit disk `X`.
2. The arc `J` can be chosen Jordan, of infinite length, inside the unit disk,
   and disjoint from the smaller disk except at its initial endpoint.
3. Straight-line integration in the convex disk proves `Q_X(0)<=1`; the
   coordinate function proves equality.
4. Source Lemma 10.4 applies for every `A>0` because `J` has infinite length.
5. The patched function is differentiable at the attachment point because its
   difference quotient is zero on the disk and tends to the source function's
   endpoint derivative zero on the arc.  Its derivative is continuous there
   for the same reason.
6. Scaling by 1/3 places the patched function in the defining unit derivative
   ball for `Q_N`, and the lower bound `A/(6|w|)` diverges.

Human review should focus on the standard topological meaning of
“neighborhood” and on the two-piece derivative check at the attachment point.

Artifact checks:

- `latexmk` completed with no warnings, undefined references, overfull boxes,
  or underfull boxes.
- The final PDF reopens as a three-page A4 document; Ghostscript extraction
  finds the theorem, source lemma, proof conclusion, and references.
- All three final pages were rendered at 144 dpi and visually inspected after
  the final equation correction and source-crop adjustment.  No clipping,
  overlap, broken glyphs, or illegible text remains.
