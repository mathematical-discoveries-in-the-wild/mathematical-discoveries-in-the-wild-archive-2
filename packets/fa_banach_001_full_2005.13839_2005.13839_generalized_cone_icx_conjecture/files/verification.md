# Verification

Date: 2026-08-09

## Formal and numerical checks

Command:

    conda run --no-capture-output -n sandbox python code/verify_icx.py

Output:

    symbolic elasticity derivative: OK
    worst quantile-crossing violation: 1.665e-15
    worst mean violation:              0.000e+00
    worst stop-loss violation:         0.000e+00
    numerical stress tests: OK

The numerical grid covered dimensions 2, 3, 4, 10, and 50; truncation
parameters from 0 through 10^8, including values on both sides of 1; 4001
quantile points; and 401 stop-loss thresholds. The computation is only a
stress test, not part of the proof.

## Proof audit

- The normalized cross-sectional density is proportional to
  (1+(q-1)t)^(n-1). Its CDF, inverse, and median normalization were derived
  directly and checked against the source's reduced formula.
- SymPy verifies the displayed derivative of the elasticity E.
- The sign argument for the parameter derivative was checked separately for
  v<0 and v>0 and for u below and above 1/2.
- The positive-series quotient derivative was expanded pairwise. Each term
  has sign (j-i)(rho_j-rho_i)>0.
- The stop-loss proof was audited separately for thresholds below and above
  the common median.
- For n at least 2, the strict mean gap for every a>0 makes the stop-loss gap
  strict on 0<s<1; strict convexity then forces a strict expectation gap.
- Reversing which base carries the zero value merely reverses the axis and
  replaces the base ratio by its reciprocal, already covered by a in
  [0,infinity].

## Source and novelty audit

- The official arXiv PDF is stored as source_paper.pdf; SHA-256:
  442e5e40b73ad102f3ef98a4b9c6d3ac989b113a2093b28fefe8d65eba0d9866.
- The published Springer HTML for DOI 10.1007/s10231-021-01080-y was checked:
  it retains the statement as Conjecture 1.7.
- Exact-title, arXiv-id, formula-fragment, and core-keyword searches found no
  later proof or counterexample.
- Crossref reported is-referenced-by-count 0; OpenAlex reported
  cited_by_count 0, with its record updated on 2026-08-08.

## Packet build and visual QA

- latexmk completed with no remaining warnings, undefined references,
  overfull boxes, or underfull boxes.
- The final PDF has 6 letter-sized pages.
- All 6 pages were rendered at 150 dpi and visually inspected. No clipping,
  overlap, missing glyphs, broken equations, or unreadable text was found.
- solution_packet.pdf SHA-256:
  4a5bfb0a7db3e5cfab467e0b757e9ed2d1f5d82219d35223a267398ab4e82423.

## Human review focus

- Confirm that the source's Theorem 1.1 may be used with the stated
  volume-halving point exactly as normalized here.
- Check the endpoint a=infinity by continuity.
- Check the equality transfer from the unique scalar maximizer a=0 through
  the source's equality theorem.
- Note that the source's literal equality clause needs the nonzero
  normalization: f=0 is an unavoidable degenerate equality case.
