# Verification

Status: verified.

Primary-source checks:

- arXiv:1210.1848 asks the gauge inclusion, seminorm-generation, and
  countable-concatenation-base questions following Propositions 2.22--2.24.
- arXiv:1404.0357 states the neighborhood-base characterization and gives
  the partition example `U_epsilon`.
- arXiv:1503.08695 independently confirms that Zapata and Wu--Guo supplied
  counterexamples.

The distinct pre-barreled-versus-barreled question in arXiv:1210.1848 is
not included in the result.

Artifact checks:

- Compiled twice with `pdflatex -interaction=nonstopmode -halt-on-error`.
- Final log has no LaTeX/package warnings, undefined references, overfull
  boxes, or underfull boxes.
- `pdfinfo` reports a two-page, unencrypted PDF with letter-size pages.
- Ghostscript text extraction contains the status, complete construction,
  gauge argument, scope limitation, and references.
- Both pages were rendered at 150 dpi after the final compilation and
  visually inspected; there is no clipping, overlap, malformed formula, or
  illegible text.
- SHA-256 of `solution_packet.pdf`:
  `b6026fa8a094e96516c35a498814694fac883b8b9e63e216de9ea11d679de5c8`.
