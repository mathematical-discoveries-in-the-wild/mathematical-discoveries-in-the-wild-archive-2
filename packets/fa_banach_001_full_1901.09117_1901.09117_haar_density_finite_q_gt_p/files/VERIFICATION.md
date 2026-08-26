# Verification report

## Claim audited

For `d/(d+1) <= p < 1`, the algebraic span of the inhomogeneous Haar system
is dense in `B^1_{p,q}(R^d)` exactly when `p < q < infinity`.

## Source checks

1. The exact question occurs in the introduction and again in Section 8.1
   of Garrigós--Seeger--Ullrich, arXiv:1901.09117v2.
2. Corollary 8.4 proves non-density when `0 < q <= p`.
3. The introduction explicitly notes non-density when `q = infinity`
   because `B^1_{p,infinity}` is nonseparable.
4. The source's local-means characterization, equation (12), is valid with
   compactly supported kernels having arbitrarily many vanishing moments.
5. The official source PDF has 55 pages.  The exact-question crop is from
   physical/printed page 28 and visibly contains the complete Section 8.1
   statement.

## New proof audit

- For `f in C_c^infinity`, global Lipschitz continuity gives
  `|f-E_N f| <= C_f 2^(-N)`.
- The `M=2^R` slabs are dyadic rectangles of volume `|K|/M` and uniformly
  bounded boundary area.  Taking `N_i >= R` aligns every slab boundary with
  the level-`N_i` grid.
- Each restricted expectation `1_(Omega_i) E_(N_i) f` is a compactly
  supported level-`N_i` dyadic step function, hence a finite Haar
  combination.
- At local-mean scale `t=2^(-k) <= 2^(-N)`, the level-`N` grid neighborhood
  inside a slab has volume at most
  `C(|Omega| t/2^(-N) + surface(Omega) t)`.
- Away from that grid neighborhood and the slab boundary, cancellation of
  the local-mean kernel reduces the defect to `L_k f`, which decays faster
  than needed by the available vanishing moments.
- At `k <= N`, the crude amplitude bound and the tubular-volume estimate
  give the low-scale half of the same two-sided weight.
- After taking the `p`th power, the main scale weight is
  `W(m)=2^(pm)` for `m<=0` and `W(m)=2^(-(1-p)m)` for `m>0`; it belongs to
  `ell^1(Z)`.
- Pointwise `p`-subadditivity combines the disjoint-resolution defects.
  With `r=q/p>1`, discrete Young gives the main error
  `M^(1/q-1/p)`.
- The slab-boundary remainder is bounded by
  `(sum_i 2^(-p N_i))^(1/p) <= C 2^(-N_0)`.
- Both terms tend to zero for finite `q>p`; density of `C_c^infinity` in
  finite-index Besov spaces completes the proof.

## Independent exponent check

`verify_exponents.py` directly evaluates truncated copies of the discrete
convolution for four parameter pairs, including the one-dimensional critical
value `p=1/2` and cases below and above `q=1`.  It verifies monotone decay and
the predicted normalization `M^(1/q-1/p)`.  This check does not replace the
geometric local-means estimate.

## Deep-upgrade audit

Eight focused routes were recorded.  The seventh route exposed spatial
dilution as the missing effect in all global-grid obstructions.  The eighth
route exploited it and upgraded the earlier `q>1` Cesàro result to all
finite `q>p`.  The attempt record also explains why the source's uniform
expectation argument stops at `q=p`.

## Search and novelty audit

The run's cheap indexes contained no duplicate result for arXiv:1901.09117.
A bounded search by exact title, exact question phrase, authors, and core
Haar/Besov density terms found the target and related endpoint Haar papers,
but no later resolution of this density question.  In particular, the
companion Triebel--Lizorkin paper arXiv:1907.03738 does not imply the Besov
claim through the standard embeddings.  This packet therefore labels the
proof a candidate full solution, not a literature result.

## Scope and limitations

- The theorem concerns density, not the Schauder basis property.  The source
  still rules out every strongly admissible enumeration as a Schauder basis
  in this `s=1` range.
- Constants depend on the smooth test function and its containing dyadic
  cube; uniform operator bounds are neither claimed nor needed.
- The endpoint `q=infinity` is negative for the already-known separability
  reason and is not approached by the construction.

## Artifact QA

- `main.tex` was compiled with two successful `pdflatex` passes.
- The final `main.log` contains no warning, undefined-reference, overfull-box,
  underfull-box, multiply-defined-label, or error line.
- `solution_packet.pdf` has 5 letter-size pages and opens as PDF 1.7.
- Ghostscript `txtwrite` extraction recovered the theorem, Proof Intuition,
  the slab lemma, all ten numbered displays, the phase table, and all three
  references.
- All five packet pages were rasterized at 150 dpi and inspected at original
  detail.  Text, equations, screenshot, table, page breaks, and references
  are legible; no clipping, overlap, or malformed glyph was found.
- The official source PDF opens successfully, has 55 letter-size pages, and
  the page-28 screenshot was inspected before inclusion.
- `verify_exponents.py` passed all four parameter suites.  The tested costs
  decreased monotonically for `M=32,64,128,256`, and normalization by the
  predicted power stayed within the stated finite-truncation tolerance.
- SHA-256 of the final packet:
  `4374980ce6b3468d96c3413c93cb12cdc66cc4164c6c07080efc2a7948aa290c`.
