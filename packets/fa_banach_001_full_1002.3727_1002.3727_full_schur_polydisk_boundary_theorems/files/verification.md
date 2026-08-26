# Verification report

## Exact proof checks

- Abate's full-Schur Julia inequality uses the maximum only over active
  indices `J(tau) = {j : |tau_j| = 1}`.  Substitution
  `z = tau - t delta` makes its right side `O(t)` locally uniformly on the
  inward cone.
- If `x = |phi - omega|` and `s = |phi|`, then
  `x^2 <= C t (1-s^2) <= 2 C t (1-s) <= 2 C t x`; hence
  `|phi(tau-t delta)-omega| = O(t)` and the scaled quotients are locally
  bounded.
- The affine analytic disks in the proof map the unit disk into the polydisk:
  active coordinates are convex combinations of a boundary point and the
  disk variable, while inactive coordinates obey
  `2 |xi_k|/A < 1-|tau_k|`.
- The convergence set contains a real open box in all active coordinates and
  a complex open polydisc in all inactive coordinates.  Iterated one-variable
  identity theorems make this a uniqueness set.
- The slope has real part at most zero.  Its radial value is `-alpha < 0`, so
  the harmonic maximum principle makes the sign strict.  In every inactive
  coordinate, `exp(h)` is bounded entire; Liouville therefore makes the slope
  independent of that coordinate.
- With two active coordinates, writing `F(a,b)=b p(b/a)`, endpoint rotations
  within `{a in H, az in H}` give `Im p(z) >= 0` and
  `Im(-z p(z)) >= 0` for `Im z > 0`.  Positive real directions give
  `p((0,infinity))` real and `p(1)=-alpha`.
- For the C-point theorem, Cauchy's estimate is taken on coordinate circles of
  radius half the surrounding polydisc radius, so no closure issue occurs.
  The converse segment union remains nontangential by convexity of the sup
  norm.

## Source and literature checks

- `source_paper.pdf` is the official current arXiv PDF for 1002.3727, has 44
  pages, and has SHA-256
  `237ecd89985883ba390ae174c88641b7041aede0ab70a69fffe40f17db32b5bf`.
- `figures/open_problem_crop.png` is rendered from PDF page 43 and contains
  the complete final open-question paragraph.
- Abate, arXiv:math/9612202, lines corresponding to Lemma 3.1 give both the
  active-coordinate Julia inequality and the radial identity used here.
- McCarthy--Pascoe, arXiv:1606.09629, uses a related normal-family mechanism,
  but its scalar Corollary 6.2 assumes the multiplier/Schur--Agler norm.
- Agler--Evans--Lykova--Young, arXiv:2508.13742v2 (17 July 2026), Theorems
  1.14--1.15, still assumes the Schur--Agler class and treats torus points.
- No exact full-Schur all-boundary result was found in the bounded search
  recorded in `README.md` and the attempt log.

## Build and visual QA

Build command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The final build has seven letter-sized pages, with no unresolved references,
LaTeX warnings, overfull boxes, or underfull boxes.  The PDF was rendered page
by page and visually inspected.

## Expert review priorities

1. Confirm the passage from uniqueness on the mixed slice to local-uniform
   convergence of the entire one-parameter family of quotients.
2. Check that the complex homogeneity continuation domain in the scalar
   multiplier is connected (it is an intersection of open half-planes).
3. Check the two endpoint limits proving the Pick conditions and the sign
   convention against source formula (2.11).
4. Decide the cataloguing scope of “our results”: the packet proves both
   principal function-theoretic results and explains why the model statements
   cannot extend outside the Schur--Agler class.

