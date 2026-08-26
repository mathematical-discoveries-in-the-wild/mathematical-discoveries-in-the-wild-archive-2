# Verification report

Verdict: `candidate_full_likely_valid` for the concrete separated Schrödinger
example on page 8 of arXiv:1503.02508.

## Proof audit

- The source states that its Gaussian/off-diagonal theory gives `(R_q)` for
  every lower exponent `1 < q < 2`; the displayed Schrödinger semigroup has
  Gaussian bounds, so its lower endpoint is one.
- The quadratic-form inequality
  `||partial_x1 u||_2^2 <= <Lu,u>` proves `L^2` boundedness of
  `T = partial_x1 L^{-1/2}`.
- Because `V` is independent of `x1`, first-coordinate translations commute
  with `L`.  Their generator `partial_x1` therefore commutes with the spectral
  calculus of `L` on the natural core.
- Since `partial_x1` is skew-adjoint and `L^{-1/2}` is self-adjoint,
  commutation gives `T* = -T` on `L^2`.
- For `p > 2`, let `q=p' < 2`.  On core functions,
  `|<Tf,g>| = |<f,Tg>| <= C_q ||f||_p ||g||_q`; duality gives the `L^p`
  estimate.  Together with the source's lower range and `p=2`, this proves
  boundedness for every `1 < p < infinity`.
- The same proof applies to any Euclidean coordinate absent from a
  nonnegative potential, provided the standard lower-exponent estimate holds.

## Upgrade attempts

1. The initial operator-valued Fourier-multiplier route requires uniform
   functional-calculus or R-boundedness estimates for the transverse
   Schrödinger operator.
2. The decisive upgrade observes that the already-known below-two theorem is
   self-dual here because the partial transform is skew-adjoint.
3. The argument was extended from the displayed two-dimensional operator to
   arbitrary separated Euclidean coordinates.

## Novelty check

A bounded primary-source search used the exact model, `V(x_2)`, “partial Riesz
transform”, “Schrödinger”, and the source title and authors.  It found the
source and arXiv:1202.2136 on different localized/degenerate partial
transforms, but no primary source stating this duality answer.  Novelty
confidence is moderate because the proof is elementary.

## Packet and visual checks

- `latexmk` completed with resolved references and no overfull boxes,
  underfull boxes, or final logged warnings.
- The final packet contains three A4 pages.
- Every final page was rendered at 150 DPI and inspected at original
  resolution.  The source excerpt is readable; formulas, margins, proof
  endings, references, and page numbers are clean; nothing is clipped.
- Text extraction finds Theorem 2, the full range `1 < p < infinity`, the
  skew-adjoint identity, and the separated-coordinate corollary.

## SHA-256

```text
177775edd93f9f74369c4ae3f32cb58535313e8c3509bdf41ca4ba46ff2a75fe  solution_packet.pdf
1f1de8c0914b521400283849047a3813a6353c6dccf2998164c746abd5b21bbc  source_paper.pdf
fbb32460e45643a6e3e3844ae93fd8e81b0079ba1e26c365b328a942dada065e  figures/open_problem_crop.png
```

## Human-review recommendation

Check that the source's recalled lower-exponent theorem applies to the scalar
choice `Gamma=partial_x1` exactly as stated, and verify the strong-commutation
identity on the natural form/core domains.  The duality step is then immediate.
