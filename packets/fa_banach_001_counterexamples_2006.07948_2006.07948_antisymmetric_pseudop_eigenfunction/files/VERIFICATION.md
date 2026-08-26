# Verification report

Verdict: `candidate_counterexample_likely_valid` for the literal separated-
product classification in Remark 3.8 of arXiv:2006.07948.

## Proof audit

- The signed transposition `S u(x,y) = -u(y,x)` is a linear isometric
  involution of `W_0^{1,p}((0,1)^2)`.  Both the anisotropic p-energy and the
  Lp mass are S-invariant.
- Its fixed space is closed and nonzero; an explicit smooth compactly
  supported element is `eta(x) zeta(y) - eta(y) zeta(x)` for linearly
  independent `eta,zeta`.
- On the unit-Lp sphere in this fixed space, the direct method applies:
  Poincare coercivity, reflexivity, compact `W_0^{1,p} -> Lp`, weak closedness,
  and weak lower semicontinuity produce a nonzero minimizer.
- The constraint derivative is nonzero at the minimizer, so the Banach-space
  Lagrange multiplier theorem gives criticality against all fixed-space
  variations.
- Full criticality is proved directly.  If `J=E-lambda N`, invariance and
  `Su=u` give `J'(u)[Sv]=J'(u)[v]`.  For arbitrary `v`, the average
  `Pv=(v+Sv)/2` is fixed, hence `J'(u)[v]=J'(u)[Pv]=0`.  Expanding the
  derivative is exactly the weak pseudo-p-Laplacian eigenvalue equation.
- Testing the Euler equation with `u` gives the positive weak eigenvalue
  `lambda=E(u)>0` under the normalization `N(u)=1`.  The source's displayed
  divergence-sign convention has eigenvalue `-lambda`; this is stated in the
  packet.
- A nonzero separated product cannot be antisymmetric.  Its continuous
  signed-symmetry identity would vanish on the diagonal, forcing the product
  of two one-dimensional p-sines to vanish for every `t`; their finite zero
  sets leave a point where both factors are nonzero.
- The same invariant-minimization proof works in every cube of dimension at
  least two, and in boxes with two equal side lengths after translating the
  swapped coordinates.  This is the deep upgrade beyond the square example.

## Upgrade attempts

1. The square construction minimizes within the diagonal-antisymmetric
   symmetry class and already disproves the literal classification.
2. A deep upgrade replaces an appeal to a black-box symmetric-criticality
   theorem by the explicit averaging identity for arbitrary variations.
3. The signed-coordinate-swap mechanism is extended to every cube and to
   boxes with two congruent coordinate intervals.

## Novelty check

A bounded primary-source search used the exact source question and the terms
`pseudo-p-Laplacian`, `rectangle`, `eigenfunction`, `antisymmetric`, and
`coordinate swap`.  It found the source and papers on symmetry for the
isotropic p-Laplacian or on nonlocal pseudo-p operators, but no primary source
giving this counterexample to the displayed classification.  Novelty
confidence is moderate because the argument is elementary.

## Packet and visual checks

- `latexmk` completed with resolved references and no overfull boxes,
  underfull boxes, or final logged warnings.
- The final packet contains four A4 pages.
- Every final page was rendered at 150 DPI and inspected at original
  resolution.  The source question is readable; all formulas, margins, proof
  endings, references, and page numbers are clean; nothing material is
  clipped.
- Text extraction finds the square theorem, signed antisymmetry, and the
  all-cubes upgrade.

## SHA-256

```text
9c493d90660c3406c2eaa55e6901c5880f601f2203270f498170bf2250ab8ee6  solution_packet.pdf
a7f735d07c27b55017d7996448b4d1b6c8686edd6a30ae3091cc27c895795fbe  source_paper.pdf
1350601e5bd1bc7e15b64423efdc1c0d9b11603f5cde987fb799013630073ee3  figures/open_question_crop.png
```

## Human-review recommendation

Check the direct-method/Lagrange-multiplier step on the closed fixed subspace,
then verify the one-line averaging passage from restricted to full
criticality.  Also confirm that the source question is read literally as a
classification of individual eigenfunctions, rather than as a weaker claim
about eigenvalues or spanning families.
