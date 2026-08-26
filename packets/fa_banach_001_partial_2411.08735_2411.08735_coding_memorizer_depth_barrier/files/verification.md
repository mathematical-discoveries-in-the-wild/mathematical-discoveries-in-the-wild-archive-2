# Verification record

Status: candidate_partial_result_likely_valid  
Agent: agent_lane_03  
Model: GPT5.6  
Date: 2026-08-11

## Mathematical audit

- The exact source target is Remark 79 and Table 3 on printed page 52. It asks
  whether the exponentially deep coding constructions can be implemented more
  efficiently at minimal width.
- The encoder is a bijection from C_K^(d_x) to C_(d_x K), so the scalar
  memorizer has exactly N=2^(d_x K) distinct input sites.
- Arbitrary dyadic data on those sites genuinely arise from continuous source
  targets: pairwise disjoint bumps interpolate arbitrary first-coordinate
  values, and the source encoder preserves a vector whose only nonzero
  coordinate is the first.
- At M=1, arbitrary labels in {0,1/2} imply shattering after thresholding
  at 1/4. Every variable LReLU or stepped-LReLU unit expands into at most
  three fixed ReLU/STEP units. Bartlett--Harvey--Liaw--Mehrabian Theorem 8
  therefore gives VCdim <= C * parameters * units <= C(w+1)^3 L^2, yielding
  the stated Omega(sqrt(N)/(w+1)^(3/2)) depth lower bound.
- The same threshold argument is stable under uniform coding-grid error
  strictly below 1/4.
- For one depth cap independent of M, the evaluation set contains C_M^N
  for every M. This union is dense in [0,1]^N. The evaluation set is a
  finite union of semialgebraic images, and a depth-n, width-w network has
  at most n w(w+3) affine plus activation parameters. Semialgebraic closure
  preserves dimension, so N <= L w(w+3).
- Yang--Yang Theorem 2.1 was checked from the included March 2026 paper. With
  scalar separation delta=1/N, C=2^(d_y M), its bit parameter chosen above
  both logarithms, and its balanced sample block, the displayed width is at
  most 20 and depth is O(sqrt(NB)+B), B=1+d_x K+d_y M.
- The exact identity
  ReLU(t)=(sigma_alpha(t)+alpha sigma_alpha(-t))/(1-alpha^2) converts every
  width-20 ReLU hidden layer to width 40 with one fixed positive LReLU and no
  depth increase.
- The qualification is essential. The width-40 construction is at the
  source's exact minimal width only when that minimal width is at least 40.
  The fixed-precision low-width cases, FLOOR-enabled cases, and decoder
  dependence on M remain open.

## Upgrade-attempt audit

The durable attempt note records eight materially distinct attempts:
parameter dimension, precision-uniform closure, fixed-precision VC capacity,
architecture-independent extension, the post-source constructive upper bound,
exact LReLU transfer, low-width serialization, and FLOOR bit extraction. The
first route's quantized-label gap was repaired by the second and third routes.
The last two expose concrete remaining obstructions, so partial classification
is appropriate.

## Reproducible checks

Command:

    conda run --no-capture-output -n sandbox python code/verify_depth_bounds.py

Output:

    ReLU-to-LReLU identity: exact on 183 rational cases
    parameter bound: checked for widths 1..7 and depths 1..8
    FLOOR bit extraction: checked on four six-bit labelings

The verifier checks exact algebra and bookkeeping, not the cited VC theorem or
the semialgebraic dimension theorem.

## Source and literature audit

- The current 71-page source PDF was downloaded from arXiv and its December
  2025 source archive was inspected directly.
- source_excerpt.pdf contains exact printed pages 52--53; both pages were
  rendered and visually inspected.
- The 2019 JMLR/arXiv paper's Theorem 8 was text-audited: for W parameters,
  U units, and bounded-piece piecewise-polynomial activations, it gives
  VCdim = O(WU log((d+1)p)), hence O(WU) here.
- The March 2026 Yang--Yang paper's Theorems 2.1 and 3.2 and its explicit
  parameter formula were text-audited. It postdates the active source.
- No exact-ID or core-keyword duplicate was found in the run registry,
  solution index, attempt index, or proof-gap index. This is a bounded novelty
  check, not an exhaustive priority claim.

## Build and visual QA

- latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
  completed successfully.
- Final log search found no LaTeX warnings, undefined references, overfull
  boxes, or underfull boxes.
- Ghostscript null-device validation completed successfully.
- The final four-page packet was rendered at 180 dpi with the RGB device.
- Every final page was visually inspected. The exact source crop is legible;
  no text, equations, citations, borders, images, or page numbers are clipped
  or overlapped.

## SHA-256

- solution_packet.pdf:
  2f42972ff0fbc011561e027e773a1ac41ca881c223c4a6ddfc90a063dbb7ef97
- source_paper.pdf:
  45d04bc31bbe270a9e0122a7d87c859c91a71f28f5ed33943a3db3f2a109706b
- source_excerpt.pdf:
  837dc5d38848e0ce0d669e43772fc0c7e5c2b8d23d9a27b3996f85c6f9b31574
- question_crop.png:
  23340e17c54a64cd9d0459ddf9f5f0450a25f54575047578177f0059843a8a5b
- references/bartlett_harvey_liaw_mehrabian_vc_dimension.pdf:
  0939bf61d8ea81b9167a3e958ca3864af5c25874710f7b03bfc0d76248bab643
- references/yang_yang_memorization_capacity_2026.pdf:
  c1a226c9d802fdf4b56342fef2a5e3b7c64a973e8706a68d433f45377b59d608
