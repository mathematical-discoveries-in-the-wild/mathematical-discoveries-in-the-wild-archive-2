# Verification

Verified on 2026-08-13 by `agent_lane_15`.

## Mathematical checks

1. **Projection/frame normalization.**  For an `N x M` Parseval synthesis
   matrix, `P=Phi^* Phi` is a rank-`N` projection and every such projection
   occurs.  The paper defines total coherence with ordered pairs, hence
   `E TC=M(M-1) E|P_12|`.
2. **Conditional spherical law.**  From `P^2=P`, the squared norm of the
   off-diagonal tail of column one is exactly `d(1-d)`, where `d=P_11`.
   Invariance under the stabilizer of the first coordinate makes its
   conditional direction uniform on the real or complex `D=M-1` sphere.
3. **Distribution audit.**  Normalized real/complex Gaussian coordinates give
   `d~Beta(N/2,q/2)` and `Beta(N,q)`, respectively, and the stated beta laws
   for a spherical coordinate.  Direct beta integration reproduces both exact
   gamma-function expectations.
4. **Constant audit.**  The two lower gamma-ratio estimates were checked by
   their integer recurrences.  Both upper ratios follow from
   `Gamma(x+1/2)^2 <= Gamma(x)Gamma(x+1)`.  Substitution gives the stated real
   constant `2 sqrt(2)/pi^(3/2)` and stronger complex constant
   `pi^(3/2)/8`.
5. **Boundary audit.**  The cases `N=1`, `q=1`, and `D=1` were checked
   separately; the gamma formulas remain valid.  The vacuous `N=M` case has
   zero right-hand side.
6. **Numerical independent check.**  With seed `191001733`, 10,000 Haar
   projections for `(M,N)=(5,2)` gave Monte Carlo means `3.3931429151` real
   and `4.0404875480` complex, versus exact values `3.3953054526` and
   `4.0391905546`.  Exhaustive exact-formula evaluation for `2<=M<=100`
   found minimum normalized ratios `0.6366197724` real and `0.7853981634`
   complex, both above the certified common constant `0.5079490875`.
7. **Literature audit.**  Exact arXiv-id, title, quotation, and core-keyword
   searches through 2026-08-13 found no later arXiv answer to this selected
   question.  A later negative answer about equal-norm maximizers concerns a
   distinct question in the same Discussion.

## Source and packet checks

- Official source: `https://arxiv.org/pdf/1910.01733`.
- The real source crop is from PDF page 25 and visibly contains both the exact
  question and the paper's proposed random-frame route.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex`
  completed without unresolved references, overfull boxes, or underfull-box
  warnings.
- Final packet: 3 US-letter pages.
- Every final page was rendered at 150 DPI with Poppler.  All three PNGs were
  confirmed RGB, `1275 x 1650`, and visually inspected at original detail.
  There are no clipped formulas, collisions, unreadable source evidence,
  blank pages, or margin overflows.
- Text extraction confirms the Status, Theorem 1, Proof Intuition, Scope and
  provenance, and References sections.

## SHA-256

- `solution_packet.pdf`:
  `8824ab80359eb015441b2e17dd023d31285f8efa0600d0d0fdbbc5492923a480`
- `source/1910.01733.pdf`:
  `b062ba448258843df704fbf0b5a6d7238f0454fb5cef88a7273a760326c64a72`
- `source/source_question_page25.png`:
  `a60a5dcc7d3eeaf5ae6797faba207073254dd1d9b1a6a477495ee713c738515e`
- `main.tex`:
  `b007b1bcd4998ae47d112f01cd91baad92731985d8f5b51a0c15f5d1e2897d00`
- attempt note:
  `bd05f130e2629b40a2c36f23ce3f2f42fc80d763d5e4ab4e96f6a0bfec605102`
