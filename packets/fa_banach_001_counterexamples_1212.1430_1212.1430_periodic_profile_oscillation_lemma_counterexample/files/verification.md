# Verification report

Verdict: `candidate_counterexample_likely_valid`

Checked on 2026-08-13 by `agent_lane_12` / GPT5.6.

## Mathematical audit

- Checked the Fourier-mode separation for localized periodic waves: distinct
  modes separate at scale `j`, the outer high-pass limit deletes exactly the
  zero mode, and the multiplier tends to its value at `sign(k)n_0`.
- Checked absolute convergence of the corrected coefficient series by
  Parseval and Cauchy--Schwarz.
- Checked passage from trigonometric polynomials to bounded periodic profiles
  using uniform `L^2` multiplier bounds and periodic averaging.
- Checked the real square-wave example directly: weak limit zero, unit
  `L^2` energy, true constant-multiplier pairing one per unit volume, and
  source prediction two.
- Checked the complex exponential directly: after zero extension on `(0,1)`,
  its negative-frequency energy is the tail of the Fourier transform of the
  interval indicator translated by `j`, hence tends to zero, while the source
  predicts one per unit volume.
- Checked that both examples satisfy the exact hypotheses of Lemma 4.1 and
  use admissible `p=2` tests.
- Checked that the second example rules out repair by merely normalizing
  `delta_{-n_0}+delta_{+n_0}` by one half.

## Upgrade audit

- Eight distinct routes are recorded in the attempt file, including signal
  disambiguation, literature search, PDE--Young compatibility, positivity,
  scalar one-dimensional reduction, normalization and directional
  counterexamples, and the exact replacement theorem.

## Artifact audit

- LaTeX built successfully in two final passes.  The final log has no
  warning, overfull-box, underfull-box, undefined-reference, or fatal-error
  message.
- All four A4 packet pages were rendered at 150 dpi and visually inspected.
  No clipping, collision, malformed formula, unreadable evidence image, or
  stranded heading was found.
- Source-paper pages 28, 30, and 38 were rendered and inspected.  The packet
  contains readable full-width crops of Lemma 4.1 and the generability
  problem after Example 5.8.
- Ghostscript text extraction contains the signed cross-spectrum theorem,
  both counterexamples, the conservative scope statement, and the reference.
- The finite Fourier verifier returns `1` versus `2` for the square wave and
  numerical zero versus `1` for the one-sided wave, exactly as proved.

SHA256:

- `solution_packet.pdf`:
  `2a378ad82205b58474a7f614cc3964f0108878c41608e5083cfa0e03575c4bc1`
- `source_paper.pdf`:
  `c574a0115127f792f201b96e3811e165260de614d0b5f6e2c0d15a69f4ece883`
- `main.tex`:
  `d1f78a5f13ca48cb0d4c3ff01a246f8497b83c7ed43a07973242e48ba41e80a9`
- `figures/open_problem.png`:
  `26c6b9d7df76e6cf275cfa7d088df3a6cb552da2f108d458c62fd2939921a778`
- `figures/oscillation_lemma.png`:
  `db1a108c0b40d147f8453ced2f1a38bb6b7a523a8bf16980b16bfc375ee0e58b`

## Recommended reviewer focus

Check the localized Fourier-mode argument in the exact replacement theorem,
the multiplier convention determining which exponential is the positive
direction, and every downstream source formula that imports Lemma 4.1.
