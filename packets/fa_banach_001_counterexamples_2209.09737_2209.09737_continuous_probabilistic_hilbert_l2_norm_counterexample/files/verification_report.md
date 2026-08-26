# Verification report

Status: `candidate_counterexample_likely_valid_needs_human_review`

Date: 2026-08-11

Agent: `agent_lane_19`

## Source check

- The official arXiv:2209.09737 PDF was saved as `source_paper.pdf` and has
  66 pages.
- The one-dimensional kernel formula appears as (1.25) on PDF page 7 and as
  the decomposition `K_H=J+1/(pi z)` in Corollary 9.3 on PDF page 52.
- Theorem 9.5 on PDF page 53 gives the interval between the classical norm and
  that norm plus `||J||_1`.
- Conjecture 9.6, also on PDF page 53, predicts equality with the classical
  norm. `figures/open_question_crop.png` is an actual 3x crop of it.

## Kernel and moment check

- The source formula makes `J` real, odd, and strictly positive on `(1,infty)`.
- For `x>=1`, replacing `y^2+pi^2x^2` by `pi^2x^2` gives
  `0<J(x)<=C/x^3`, with
  `C=pi^(-3) integral_0^infinity 2y^3/sinh(y)^2 dy<infinity`.
- Therefore `M=integral_1^infinity xJ(x)dx` is finite and strictly positive.
- As an independent numerical sanity check, changing integration order gives

  ```text
  M = (2/pi^2) integral_0^infinity
        y^2/sinh(y)^2 [pi/2-arctan(pi/y)] dy
    approximately 0.10471316692723628.
  ```

  Numerical positivity is not used in the proof.

## Fourier check

- Under `hat f(xi)=integral f(x)e^{-ixxi}dx`, the principal-value kernel
  `1/(pi x)` has multiplier `-i sign(xi)`.
- Oddness gives `hat J(xi)=-2i integral_1^infinity J(x)sin(xxi)dx`.
- Since `xJ(x)` is integrable, dominated convergence yields
  `hat J(xi)=-2iM xi+o(xi)` as `xi -> 0+`.
- Thus the correction has the same imaginary sign as the Hilbert multiplier
  for small positive frequency; it does not cancel it.
- Continuity of `hat J` turns the strict multiplier inequality into one on a
  positive-measure interval, so the essential supremum is strictly above one.
- At `p=2`, `p*=2` and the conjectured value is exactly `cot(pi/4)=1`.

## Duplicate and novelty checks

- The registry, solution, attempt, and proof-gap indexes had no exact hit for
  arXiv:2209.09737 or Conjecture 9.6.
- Bounded arXiv-facing searches for the exact title, probabilistic continuous
  Hilbert transform, conjectured norm, and the source numerical constant found
  no matching resolution.
- Human review should check for an erratum or later discussion not using the
  source's terminology.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed.
- The final log was checked for warnings, undefined references, and overfull or
  underfull boxes.
- Every page was rendered and visually inspected for equations, margins,
  clipping, overlap, page breaks, references, and crop quality.
- The conjecture crop was inspected separately at original resolution.

## Human review focus

1. Confirm the sign convention: with either standard Fourier convention, the
   odd positive correction and the Hilbert kernel acquire the same sign at
   small positive frequencies.
2. Confirm the decomposition in Corollary 9.3 has a plus sign, as transcribed.
3. If accepted, compute or bound the exact `L^2` multiplier maximum as a
   follow-up; it is not needed for the counterexample.
