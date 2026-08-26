# Verification report

Status: `literature_implied_answer_partial_subcase`

Date: 2026-08-11

Agent: `agent_lane_19`

## Source question

- The official arXiv:1601.00948 PDF is saved as `source_paper.pdf` and has
  25 pages.
- On source PDF page 8, the authors ask whether Theorems 6, 7, 9, and 11 can
  be made algorithmic.
- Theorem 11 has the inverse bound transcribed in the packet, with
  denominator `sqrt(rank(A))-sqrt(k)` and the RMS of the reciprocals of all
  nonzero singular values.

## Later theorem

- The official arXiv:2005.01070 PDF is saved as
  `answer_paper_2005.01070.pdf` and has 16 pages.
- Theorem 1.1 gives the weighted estimate for every `k<=r<=rank(A)`.
- The paragraph immediately after Theorem 1.1 states a deterministic
  algorithm and the running time `O(k(m-k/2)n^(theta+1))`; Section 4 gives
  the selection algorithm.
- Corollary 1.2 is the unweighted specialization.

## Algebra check

- Put `W=I_m`, so `||W^(-1)||_F^2=m`.
- Put `r=R=rank(A)`, so the later denominator contains the same sum
  `sum_{i=1}^R sigma_i(A)^(-2)` as the source.
- Taking reciprocal square roots gives exactly the source Theorem 11 bound
  with `sqrt(k-1)` in place of `sqrt(k)`.
- Since `k<R`, both denominators are positive, and
  `sqrt(R)-sqrt(k-1) > sqrt(R)-sqrt(k)`.  The later guarantee is stronger.

## Scope and upgrade attempts

- The implication answers only the Theorem 11 part of the source's compound
  algorithmic question.
- A deep upgrade attempt on the separate hybrid estimate tested: trimming
  high dual-column norms before applying Theorem 9; block-correlated inverse
  matrices; exhaustive random matrices up to dimension 10; and a dual
  projected-synthesis reformulation.  These supported plausibility but did
  not prove the desired RMS/`sqrt(epsilon)` bound or produce a counterexample.
- Xie's theorem retains the `1/epsilon`-scale denominator near full rank, so
  it does not settle that hybrid question.

## Build and visual QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed.
- The log was checked for undefined references, overfull/underfull boxes,
  and warnings.
- Every page was rendered and inspected for margins, clipping, overlap,
  formula legibility, and page breaks.

