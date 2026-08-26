# Verification record

Status: final checks passed; mathematical result remains subject to human
review and the stated 2026 literature-overlap audit.

## Mathematical checks

- The scalar weights `(1+x^2)^(+/-a/2)` are `A_2` for `0<a<1`.
- The three eigenvalues `s^-1`, `2s^-1`, `4s` are strictly ordered globally.
- Direct spectral comparison gives `D <= W <= 2D`.
- The Loewner-comparability lemma is proved with the squared matrix `A_2`
  convention used in the source paper.
- On each full cosine period `I_N`, the unweighted mean is zero and the
  oscillation integral is exactly 4, while the Bloom-weight mass tends to 0.
- The numerical script checks the spectral inequalities and illustrates the
  divergent quotients for three choices of `a`.

## Literature boundary

The 2026 Nielsen--Šikić paper is a required human comparison. Its abstract is
close enough that the packet makes no priority claim; its publisher full text
could not be inspected during this run.

## Build and visual QA

- `code/crop_open_problem.py` reproduced the 1095-by-605-pixel crop from
  source PDF page 19; the crop was visually inspected and contains the exact
  question and higher-dimensional necessity sentence.
- `main.tex` was compiled twice with pdfLaTeX after the final source change.
- The final log contains no warnings, undefined references, overfull boxes,
  or underfull boxes.
- `solution_packet.pdf` has four pages. Every final page was rendered at 160
  dpi with Ghostscript's RGB PNG device and visually inspected after the last
  source and crop changes. Equations, crop, bibliography, page breaks, and
  margins are legible; no clipping or overlap was found.
- `code/verify_counterexample.py` completed successfully for
  `a=0.2,0.5,0.8`, checking strict spectrum and both Loewner inequalities at
  representative points. The displayed BMO lower bounds grow with the tested
  period indices.
