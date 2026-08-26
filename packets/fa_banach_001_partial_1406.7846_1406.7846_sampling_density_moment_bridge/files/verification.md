# Verification report

Date: 2026-08-17  
Agent: `agent_lane_13`  
Verdict: `candidate partial; likely valid`

## Mathematical audit

1. **Density/sample identity.**  Conditional on the latent vertices, sampled
   edge multiplicities are independent and the expectation of the product of
   their powers is the product of the corresponding conditional moments.
   This is exactly the node-and-edge density formula.
2. **Uniform integrability.**  For a monomial involving `q` positive
   edge-pairs with powers `r_e`, generalized Hölder gives

   ```text
   E(product_e M_e^r_e)^2
     <= product_e (E M_e^(2 q r_e))^(1/q).
   ```

   Each factor is a bond density.  A uniform `L^2` bound is therefore valid
   without unconditional independence of the edge coordinates.
3. **Forward implication.**  Weak convergence of the finite sample vector and
   the preceding uniform-integrability bound justify passage of every mixed
   monomial expectation to the limit.
4. **Reverse implication.**  The bounded first bond moment gives tightness by
   a union bound and Markov's inequality.  Bounded higher bond moments make
   every mixed monomial uniformly integrable along a weakly convergent
   subsequence, so all cluster points have the same mixed moments.
5. **Determinacy step.**  The proof invokes the half-line extension of
   Petersen's theorem from Dvurečenskij--Lahti--Ylinen: Stieltjes-determinate
   coordinate marginals imply determinacy of the joint measure on a product
   of half-lines.  The cited paper's abstract explicitly describes this
   extension.  An attempted local retrieval of the full supporting source was
   blocked by the environment's external-download quota, so a human verifier
   should confirm the exact support formulation first.
6. **Exponential corollary.**  The estimate
   `m_p <= C p! alpha^(-p)` implies Carleman's divergence because
   `((2p)!)^(1/(2p)) <= 2p`.  The same exponential bound yields `L^2`
   control of every marginal monomial in the forward direction.
7. **Sharpness examples.**  For
   `(1-1/n) delta_0 + (1/n) delta_n`, a fixed sample is nonzero with
   probability at most `binom(k,2)/n`, while the second bond moment is `n`.
   Alternating distinct laws with identical moments makes every constant-
   kernel multigraph density constant but makes the two-vertex law alternate.

No computational lemma is used as proof.

## Source and evidence

- `source_paper.pdf` was rebuilt from the locally ingested arXiv source
  `data/parsed/arxiv_sources/1406.7846/source.tex` in three LaTeX passes.
- `figures/open_problem_crop.png` is a genuine full-width raster crop of
  source PDF page 32 showing the natural question and the two stated
  obstructions.
- `figures/open_problem_scope_crop.png` is a genuine full-width raster crop of
  source PDF page 33 showing the authors' expected-settings sentence.
- Both crops were generated reproducibly by
  `code/make_open_problem_crops.py` and visually inspected at original
  resolution.

## Packet build and visual QA

- Build command:

  ```text
  env TEXMFVAR=/tmp/1406.7846_packet_texmfvar \
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
  ```

- The final LaTeX log has no warnings, unresolved references, overfull boxes,
  or underfull boxes.
- `solution_packet.pdf` has 7 US-Letter pages.
- Every page was rendered at 144 dpi with `pdftoppm` into
  `tmp/rendered_pages/` and visually inspected.  All text, formulas,
  references, status labels, and both source crops are readable; no content
  is clipped or overlapping.

## SHA-256

```text
072334abf511d2137c4155606fd5e6a0278eb408dd4738dc09d093b1c63b5248  solution_packet.pdf
55945e167026b903d5bd67a9045577ba61e02341c4a8da44aeb265fe7d4ab08e  source_paper.pdf
b4080df40367df33675e80b07cf4683671c50a640086d4e294f1049748179e31  figures/open_problem_crop.png
5a8b1c9cf653ac14464b55c08e2f54bfc9878d0755d877618106ef0a02a4f198  figures/open_problem_scope_crop.png
46a40d5f4d8c74bcd40b1ff264d755a1b3ba504adac98061b1f2346f49c299a6  main.tex
0d2b14e18dae90fffcb0761e17c40ec297d65e9661012807df8b6e7e89cd10df  README.md
fa64736711861d8156057a27c5b6e5abe00a894c57924f1bba5decd921be9942  code/make_open_problem_crops.py
```

## Reviewer priority

Confirm the exact half-line marginal-determinacy theorem used in the reverse
direction.  The forward theorem, the exponential-tail implication through
Hamburger Carleman determinacy, and both counterexamples are otherwise
elementary.
