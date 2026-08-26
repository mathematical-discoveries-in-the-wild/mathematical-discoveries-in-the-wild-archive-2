# Verification report

## Verdict

`candidate_full_solution_likely_valid_needs_human_review`

The packet proves both de Leeuw directions and the exact multiplier-norm
identity for the source paper's space `dot W^{1,1}(R^d)`, `d>=2`.

## Source audit

- Official source: Kazaniecki--Wojciechowski, arXiv:1306.1437v4, published in
  Annales de l'Institut Fourier 66 (2016), no. 3, 1247--1260.
- Source PDF page 3 (printed page 1248) says that no equivalent of de Leeuw
  transference was known for the homogeneous Sobolev space and that the
  general de Leeuw-type question remained open.
- The paper then states the classical restriction and shrinking-lattice
  approximation theorems for `L^p`.  The packet proves those two formulations
  for the exact homogeneous space treated in the paper.
- The official published PDF and a readable crop of the statement are
  included.

## Proof audit

1. **Local `L^1` reduction.** On a smooth compact frequency set away from
   zero, a coordinate derivative can be inverted.  The homogeneous
   multiplier estimate then makes `m chi` an ordinary `L^1` multiplier, hence
   the Fourier transform of a finite measure.
2. **Wave-packet limit.** For that finite measure, the normalized error is
   bounded by an integral of `L^1` translation differences of the Schwartz
   envelope.  Dominated convergence proves the limit term by term.
3. **Periodic averaging.** The normalized integrals of a slowly varying
   nonnegative Schwartz envelope times a periodic function converge to the
   product of the envelope mass and the torus average.  Leibniz errors carry
   an extra factor `delta`.
4. **Restriction constant.** The input and output limits have the same
   averaging constant, so the torus norm is bounded by the Euclidean norm
   with constant exactly one.  Dilation gives every lattice spacing.
5. **Poisson normalization.** With Fourier inversion factor `(2 pi)^(-d)`,
   coefficients `(epsilon/(2 pi))^d hat f(epsilon k)` periodize `f` with
   period `2 pi/epsilon`.
6. **Boundedness in the reverse direction.** Testing the torus multipliers on
   single exponentials bounds every sampled value by `C`; shrinking lattice
   points approximate every Euclidean frequency, so continuity gives
   `|m|<=C` everywhere.
7. **Input convergence.** On the central period cube, triangle inequalities
   sandwich the norm of the periodization between the central mass minus the
   exterior tail and the total Euclidean mass.
8. **Output convergence.** Rescaled torus output derivatives are Riemann sums
   for `partial_j T_m f`; continuity of the compactly supported integrand
   gives convergence uniformly on every fixed compact set.
9. **Passage to the whole space.** Fixed-ball limits followed by monotone
   exhaustion give the Euclidean estimate.  The endpoint Sobolev inequality,
   cutoffs, mollification, and a band-limited approximate identity prove the
   required density in the quotient.

No computational claim is used in the mathematical proof.

## Novelty audit

Checked through 12 August 2026:

- current arXiv record, TeX source, and official published PDF;
- exact arXiv id, title, open-statement phrase, and homogeneous
  Sobolev/de Leeuw searches;
- Eduard Curca's 2022 extension of multiplier continuity to higher-order
  homogeneous endpoint spaces;
- Curca--Wojciechowski, arXiv:2604.23161 (2026), including its transference
  proposition for the inhomogeneous spaces `W^{l,1}`.

The 2026 proposition is not the shrinking-lattice homogeneous theorem here,
and no answer in the exact `dot W^{1,1}` setting was found.  This is a bounded
web/arXiv screen, not an exhaustive literature guarantee.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully and produced a five-page packet.
- The final log contains no LaTeX warnings, undefined references, or
  overfull/underfull box diagnostics.
- All five final pages were rendered at 150 dpi and visually inspected.  The
  theorem, formulas, citations, proof endings, and source evidence are
  legible, with no clipping, overlap, orphan page, or blank-page defect.
- The source page and final crop were separately inspected at original
  resolution; the full de Leeuw open paragraph is readable.
- SHA-256: `solution_packet.pdf`
  `fd6fab2f0bacc9851635411e740c8d0220626a6e19c9579dd4ed3529491a1402`;
  `source_paper.pdf`
  `78fdad955521307d4b4c003a08269095483a89bf300dc615629440956c0dab31`.

## Human review focus

High priority.  Check the local `L^1` reduction, the exact norm asymptotics in
the restriction argument, and the periodization/Riemann-sum limit in the
reverse implication.
