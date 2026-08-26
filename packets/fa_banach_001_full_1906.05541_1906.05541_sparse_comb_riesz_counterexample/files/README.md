# Full Solution Packet: Sparse Combs Answer Open Problem 1.6

Run: `fa_banach_001`  
Agent: `agent_lane_05`  
Model: `GPT5.6`  
Result type: `full_solution_likely_valid`

## Source problem

- Daniel Spector, *A Noninequality for the Fractional Gradient*,
  arXiv:1906.05541, Port. Math. 76 (2019), 153--168.
- Source location: page 6, Open Problem 1.6.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

For `0<beta<1`, the problem asks whether there is
`u in L^1(H^{d-beta}_infty)` whose vector Riesz transform has infinite weak
Hausdorff-content quasi-norm.

## Claimed answer

Yes, for every ambient dimension `d>=2` and every `0<beta<1`.

Set `q=1-beta`.  A one-dimensional comb consisting of `N` intervals of
length `N^{-r}`, placed at spacing `1/N`, produces a Riesz value of order
`log N` just to the right of every interval.  If the test gaps have width
`N^{-p}` with `1<r<p<1/q`, their union has uniformly positive
`q`-dimensional content.  Tensoring with a fixed `(d-1)`-cube converts the
last Riesz component into the Hilbert kernel up to a bounded error and gives
uniformly positive `(d-beta)`-content.

Widely separated smooth combs with amplitudes `2^{-n}` and
`log N_n` comparable to `4^n` have summable Choquet cost but Riesz levels
growing like `2^n` on sets of uniformly positive content.  This gives one
function, rather than merely a sequence witnessing failure of a uniform
operator bound.

## Verification status

- All content estimates are proved by explicit Frostman probability
  measures.
- The kernel reduction is derived directly by integrating the last Riesz
  kernel in the tangential variables.
- The completion-of-`C_c` issue is handled by using mollified finite combs;
  their partial sums are smooth and compactly supported, and the Choquet
  tails are summable.
- Cross-block interactions are absolutely bounded by choosing exponential
  vertical separation.
- `code/check_comb_estimates.py` numerically checks the finite-comb Hilbert
  lower bound and the three Frostman regimes for representative parameters;
  it is corroborative and not used as proof.

## Novelty check

On 2026-08-09 the run indexes and local source corpus were searched for
`1906.05541`, the paper title, the exact Open Problem 1.6 wording, and close
Riesz/Hilbert-transform plus Hausdorff-content/Choquet variants.  Bounded web
searches used the same phrases and inspected the related sparse-operator
paper arXiv:2310.10135.  They found the original open problem and adjacent
Choquet-space work, but no later resolution or duplicate of this construction.
Novelty is therefore plausible, not certified.

## Files

- `main.tex`: expert-facing proof.
- `solution_packet.pdf`: rendered solution packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: page-6 evidence crop.
- `code/check_comb_estimates.py`: finite numerical sanity check.
- `code/crop_source_page.py`: reproducible evidence crop.
- `tmp/`: build and rendering intermediates.

## Human-review recommendation

High-priority expert review.  The key points to check are the uniform
Frostman estimate for the union of target gaps, the tangential-kernel formula
`K(h)=kappa_d/h+O(|h|)`, and the Choquet-tail argument for the single glued
function.  Those points are fully written out in the packet and no unproved
lemma remains.
