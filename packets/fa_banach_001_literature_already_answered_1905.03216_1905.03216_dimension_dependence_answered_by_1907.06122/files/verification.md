# Verification

Status: literature already answered; no new result claimed.

## Source checks

- arXiv:1905.03216, introduction: the paragraph after Theorem 1 asks whether
  the constants in inequality (1) remain bounded and whether the constants in
  Theorem 1 decay with dimension.
- arXiv:1907.06122, Theorem 2: the normalized optimal constants are
  nondecreasing and at least `max(n-1,1)`.
- arXiv:1907.06122, Proposition 1: the fixed-domain optimal subharmonic
  constant equals the maximum inward torsion normal derivative.
- arXiv:1907.06122, Theorem 3 and the following note: the scale-invariant
  constants have a dimension-uniform upper bound and the source ellipsoid
  construction is intended to give a matching-order lower bound.

## Independent arithmetic check

For the displayed source ellipsoid,

`Delta q_n = -1/2 -(n-1)/(n-1) = -3/2`.

Hence `u_n=(2/3)q_n` solves `-Delta u_n=1`, has zero boundary values, and has
inward derivative `2/3` at the endpoint of the short semiaxis.  Stirling's
formula gives

`omega_n^(1/n) sqrt(n) -> sqrt(2 pi e)`

and therefore the stated volume limit and positive lower bound.  This audit
avoids propagating the normalization slip while preserving the literature's
qualitative conclusion.

## Search check

The run's cheap indexes contained no existing record for either the source id
or this exact title.  Exact web searches located the direct follow-up, which
cites the source and answers its question in its abstract and theorem
statements.

## Artifact audit

- `solution_packet.pdf` was compiled from `main.tex` with `latexmk`; the final
  log has no LaTeX warnings, overfull or underfull boxes, or undefined
  references.
- The final PDF has two US-letter pages and is 147,232 bytes. Both pages were
  rendered with Poppler and inspected at original detail; no clipping,
  overlap, illegible text, or poor page break was found.
- Source page 2 and supporting-paper pages 2--3 were separately rendered and
  inspected. They visibly contain the source questions, the fixed-domain
  torsion proposition, `A_n >= max(n-1,1)`, and the improved scale-invariant
  theorem.
- SHA-256 `solution_packet.pdf`:
  `ac451f798b401cc712a79b8103d7e6f8409603a737b845205a920a103f1ad072`.
- SHA-256 `source_paper.pdf`:
  `f9eb25f71b17d292be5af17a9268973c21e7367cf533a6c02a7c2fb57941639d`.
- SHA-256 `supporting_paper_1907.06122.pdf`:
  `9ba91eb9fc0f9cf7c6923ac39d40940ed160f0e1f73a343bb3084ed2d21fef44`.
- SHA-256 `main.tex`:
  `57f84ddd0dde717368d10e522e52ccbddf03e2cd5af83f0f131b55c2224c0ca5`.
