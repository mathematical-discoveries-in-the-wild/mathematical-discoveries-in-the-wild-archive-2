# Verification

Verified on 2026-08-13 by `agent_lane_15`.

## Mathematical checks

1. **Routing and duplicate audit.**  arXiv:1803.06409 explicitly records the
   extreme-ray problem and cites arXiv:0801.0941.  The local run index contains
   a packet answering only Question 3's second clause; its ledger explicitly
   leaves the first clause open.  The present theorem is complementary.
2. **Cone/Fourier interval audit.**  If `g,h-g` are in the doubly-positive
   cone and `h=f*gamma`, then `0<=g<=h` makes both terms integrable.  Their
   positive definiteness gives the pointwise transform inequality
   `0<=G<=F exp(-pi xi^2)` under the packet's Fourier convention.
3. **Gaussian deconvolution audit.**  Defining
   `U=exp(pi xi^2)G` gives `0<=U<=F=sinc^2(pi xi)`, so `U in L1` and
   `u=check U` is bounded continuous.  Fourier inversion and self-duality of
   the Gaussian give `g=u*gamma` with no distributional ambiguity.
4. **Critical support-lemma audit.**  For
   `L(z)=int u(t)exp(-pi t^2)exp(2 pi zt)dt`, the crude indicator bound is
   `h(theta)<=pi cos^2(theta)`.  The real and imaginary axial improvements,
   two-trigonometric convexity on sectors of width below `pi/2`, and the limit
   to the critical quadrant show order-two minimal type.  The critical
   Phragmen--Lindelof theorem then propagates the boundary exponential bound
   to all quadrants.  Rotating and applying the L2 Paley--Wiener theorem gives
   `supp u subset [-R,R]`.  This explicitly closes the critical-order issue
   that an informal tail argument would miss.
5. **Zero-multiplicity audit.**  Once `supp u subset [-1,1]`, `U` is entire of
   type `2 pi`.  At each nonzero integer, `0<=U<=F` forces `U=0`; real-axis
   nonnegativity forces even multiplicity, hence at least the double
   multiplicity of the sinc-square zero.  Therefore `U/F` is entire.
6. **Quotient-growth audit.**  Away from fixed disks around the integers,
   the explicit sine lower bound and compact-support upper bound yield
   `|U/F|<=C(1+|z|)^2`.  The maximum principle gives the same inside the
   disks.  Thus the quotient is a degree-at-most-two polynomial, and its
   real-axis bound between zero and one forces it to be constant.
7. **Upgrade audit.**  Natural multiplier, smoothing, and shift perturbations
   were checked and fail because they enlarge the Gaussian tails.  The
   remaining product clause cannot use sinc-zero rigidity because the Fourier
   transform becomes strictly positive; the existing run packet supplies an
   independent explicit non-extremality decomposition instead.  Together the
   two results settle all of Question 3.
8. **Novelty audit.**  Exact question, formula, title, convolution/product,
   Borisov-conjecture, and arXiv-restricted searches through 2026-08-13 found
   no later answer to the first clause.

## Source and packet checks

- Official PDFs: `https://arxiv.org/pdf/1803.06409` and
  `https://arxiv.org/pdf/0801.0941`.
- The routing crop is visibly from PDF page 9 of arXiv:1803.06409; the exact
  Question 3 crop is visibly from PDF page 18 of arXiv:0801.0941.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex`
  completed without unresolved references, overfull boxes, underfull boxes,
  or warnings after the final layout pass.
- Final packet: 3 US-letter pages.
- Every final page was rendered at 150 DPI with Poppler.  All three PNGs were
  confirmed RGB, `1275 x 1650`, and visually inspected at original detail.
  There are no clipped lines, collisions, unreadable crops, blank pages, or
  margin overflows.
- Text extraction confirms the Status, Theorem 1, Proof Intuition, Gaussian
  domination support lemma, Scope and provenance, and References sections.

## SHA-256

- `solution_packet.pdf`:
  `4f6322041aadbf5144063e769df63dafd9d3be524f2c6c8f7672d72520b3269b`
- `source/1803.06409.pdf`:
  `2923a4730ed6e160d87c86db21dadbb0fb41de922173748b4700f96ea6be98f8`
- `source/0801.0941.pdf`:
  `84b2c5f9adeffc43f964f17b5fe1b40bbf3396c8f771dea683fa72a341907e48`
- `source/route_open_problem_page9.png`:
  `3c0e16fd064574315c92c0f85f2fa6340ac27dd617716f8a62002374f1e1cbf6`
- `source/question3_page18.png`:
  `9c089dae8a7fb0cc5c227a15cf0e79232da03f72fde26e023cee514cf776b0c3`
- `main.tex`:
  `7795e82e51599c7cf4842c1a7682987c9b125f28c66b3d1560331feb30319b80`
- attempt note:
  `7382fc3e9f80045e42dd97c5dce2b1d2f4075b57833592118370f5f9dd494a7a`
