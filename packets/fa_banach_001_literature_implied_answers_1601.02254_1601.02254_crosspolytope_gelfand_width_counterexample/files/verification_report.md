# Verification report

Status: `literature_implied_answer_full_counterexample_needs_human_review`

Date: 2026-08-11

Agent: `agent_lane_19`

## Source and scope

- The official arXiv:1601.02254v2 PDF was saved as `source_paper.pdf`.
- Question 1.1 appears on PDF page 2 and asks for
  `R(K cap F) <= c_0 sqrt(n/k) sqrt(n) L_K` for a random codimension-`k`
  subspace.
- `figures/open_question_crop.png` is an actual 3x raster crop from that page,
  not a transcription.
- The packet addresses Question 1.1 only. The separate sub-Gaussian-direction
  question is explicitly left untouched.

## Supporting theorem check

- The official arXiv:1002.0672v2 PDF was saved as
  `supporting_paper_1002.0672.pdf`.
- Its Theorem 1.1 defines the width as the infimum over kernels of
  `m x N` matrices and gives, at `p=1`, `q=2`,

  ```text
  d^m(B_1^N, ell_2^N) >= c min{1, sqrt((ln(N/m)+1)/m)}.
  ```

- Therefore the lower bound applies to every fixed codimension-`m` subspace:
  represent the subspace as the kernel of a rank-`m` matrix and compare its
  radius to the infimum.

## Normalization check

- `|B_1^n| = 2^n/n!`, hence `a_n=(n!/2^n)^(1/n)` makes
  `K_n=a_n B_1^n` volume one.
- Sign symmetry gives zero barycenter and zero mixed second moments;
  permutation symmetry makes all diagonal second moments equal.
- On the positive simplex, the Dirichlet integral is
  `integral x_1^2 dx = 2/(n+2)!`. Multiplying by `2^n` and dividing by
  `2^n/n!` yields `2/((n+1)(n+2))`.
- Thus `L_(K_n)^2=2a_n^2/((n+1)(n+2))`, and
  `nL_(K_n)/sqrt(k) <= sqrt(2)a_n/sqrt(k)`.

## Contradiction check

For `k_n=floor(sqrt(n))` and every codimension-`k_n` subspace `F`, the width
bound gives

```text
R(K_n cap F) >= c a_n sqrt((1+log(n/k_n))/k_n)
```

for all sufficiently large `n`. Dividing by the conjectured scale gives a
universal multiple of `sqrt(1+log(n/k_n))`, which diverges. Hence, for any
proposed universal constant, sufficiently large `n` makes the estimate fail
for every `F`. This is stronger than failure with positive Haar probability.

## Duplicate and literature checks

- The registry, solutions, attempts, and proof-gap indexes had no exact hit
  for arXiv:1601.02254.
- Core-keyword searches for the paper title, cross-polytope, Gelfand widths,
  and the conjectured radius scale found no matching run artifact.
- Bounded arXiv-facing searches found the source paper, arXiv:1002.0672, and
  later work on random sections of ellipsoids, but no explicit resolution of
  Question 1.1 by this normalization-and-width deduction.
- The supporting width theorem is older than the source question; novelty is
  claimed only for the explicit deduction, subject to human literature review.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed.
- The final log contains no undefined references, LaTeX warnings, overfull
  boxes, or underfull boxes.
- `solution_packet.pdf` has 3 pages.
- All three pages were rendered to PNG and inspected. Equations, the embedded
  crop, theorem statements, page breaks, margins, and references are legible;
  no clipping or overlap was found.
- The question crop was separately inspected at original resolution.

## Human review focus

1. Confirm the standard interpretation of the source's phrase “a random
   subspace”; the proof bypasses probability by showing failure for every
   subspace in the selected dimensions.
2. Confirm the indexing convention for `d^k`; the cited theorem and packet
   both use `k x n` kernels, so there is no off-by-one issue affecting the
   asymptotic contradiction.
3. Search for an erratum or an explicit prior observation that Question 1.1 is
   contradicted by the cross-polytope widths.
