# Verification report

Status: `candidate_major_partial_likely_valid`

## Claims checked

1. Exact Hilbert operator-range formula for dense closed `A,B` with
   `D(A) -> D(B)`.
2. Closed joint-spectral formula for strongly commuting nonnegative `A,B`.
3. Complete exponents for `A=G`, `B=cG^epsilon`, `0<=epsilon<=1`.

## Proof-obligation audit

- **Source match:** the exact open sentence occurs in Section 5, Example 5.3,
  printed page 13 of arXiv:1404.2967. The packet solves substantial particular
  choices, exactly within the source's stated scope.
- **Graph-space equivalence:** `D(A)->D(B)` turns the original requirements
  into `H^(2+theta)(H) intersect H^(1+theta)(D(B)) intersect
  H^theta(D(A))`.
- **Finite interval:** one scalar reflection/cutoff operator is bounded on all
  three Hilbert-valued Bessel spaces and preserves consistency across spatial
  graph spaces.
- **Form pencil:** the common form domain is `D(A)`; graph embedding controls
  `B`, giving closedness and norm-resolvent continuity. The tails
  `tau^(-4-2theta)` and `tau^(-2-2theta)` give norm convergence of `K_0,K_1`.
- **No coupling:** the mixed Gram operator is the integral of an odd
  operator-valued function and vanishes.
- **Exact range and norm:** `Ran(T)=Ran((TT*)^(1/2))` gives both surjectivity
  and the quotient/operator-range norm, including nonclosed ranges.
- **Two scales:** the scalar pencil is uniformly comparable to
  `(tau^2+r^2)(tau^2+S^2)`. Scaling at `r` for displacement and at `S` for
  velocity proves the two uniform reciprocal-weight estimates; precisely
  `theta<1/2` controls the small interval.
- **Phase algebra:** substituting `B=cG^epsilon` gives `S~a^(1/2),r~a^(1/2)`
  below `epsilon=1/2` and `S~a^epsilon,r~a^(1-epsilon)` above it. The two
  exponent formulas agree at the transition.
- **Scope obstruction:** the `A e_n=n e_n`, `B e_n=n^3 e_n` example checks
  that a finite-interval constant path admits every displacement in `D(A)`,
  whereas the naive decaying whole-line weight is strictly stronger.

No unresolved mathematical dependency remains inside the stated scope.

## Numerical transcription check

`code/check_integrals.py` checks the original critical normalization and the
new two-scale predictions for `theta=0.1,0.3,0.49` and weak, critical,
separated, and overdamped pairs `(r,S)`. All predicted ratios remain positive
and finite. The analytic lemma, not the computation, is the proof.

## Literature bounds

Searched the run indexes, local source corpus, official arXiv, and bounded web
results using arXiv:1404.2967, the exact open sentence, the source title and
authors, `second order Cauchy trace space`, the fractional-domain exponent
pairs, `operator range`, `quadratic pencil`, `strongly commuting`, and
`strong damping`. The source and adjacent general trace/maximal-regularity
literature were found; no primary source stating any of the three upgraded
results was located. Novelty remains provisional.

## Artifact and render QA

- `source_paper.pdf` is the official 18-page arXiv PDF.
- `figures/open_problem_crop.png` is a real 180-dpi crop from PDF page 13 and
  includes the printed page header and full open sentence.
- `solution_packet.pdf` compiled to six pages with no unresolved references,
  overfull/underfull boxes, or LaTeX warnings in the final log.
- All six final pages were rendered at 144 dpi and visually inspected after
  the last edit. Text, formulas, source crop, theorem boxes, hyperlinks, and
  bibliography are clear; no clipping, overlap, blank-page, or glyph defect
  remains.
- Ghostscript text extraction retained the theorem labels, operator-range
  formula, fractional phase diagram, status line, and references.
- Final SHA-256: `f77e0faf8116648c4367a306ff9431f624e712a014a6af613087e86c7b450d22`.

## Human review focus

1. The common time-extension operator in Lemma 1.
2. Norm-resolvent continuity of the fixed-domain form pencil.
3. The constants and signs in the Gram operator calculation.
4. Uniformity of the two-scale estimates when `r/S` tends to zero.
5. Whether any upgraded formula is implicit in an unsurfaced trace theorem.
