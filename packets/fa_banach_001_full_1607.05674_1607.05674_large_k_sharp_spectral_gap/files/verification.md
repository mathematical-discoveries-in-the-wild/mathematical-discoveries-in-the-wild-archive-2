# Verification record

Date: 2026-08-11  
Agent: `agent_lane_12`  
Model: `GPT5.6`

## Symbolic proof checks

- Re-derived the source Fourier coefficient as the normalized dimension of
  the `U(k)`-fixed subspace.
- Checked that the cases listed from source Lemma 2.8 exhaust all nonzero
  coefficients after excluding the trivial, defining, and conjugate-defining
  representations.
- Checked the `k=n-1` boundary: the only source line requiring `k<n-1` has
  hypotheses `lambda_k=1` and `lambda_{n-1}=0`, hence cannot occur there.
- Expanded Weyl's product independently and verified the cancellation formula
  in packet equation (3).
- Checked both comparisons with the proposed sharp constant and verified
  attainment by `Sym^2(C^n)` through fixed-space dimensions.

## Exact computational check

Ran:

`conda run --no-capture-output -n sandbox python verify_small_ranks.py`

The script completed without assertion failures for `2 <= n <= 9` and every
`ceil(n/2) <= k < n`, enumerating partitions with first row at most five.  In
every case it found the exact maximum
`(n-k)(n-k+1)/(n(n+1))`, with the symmetric-square and conjugate
symmetric-square partitions among the witnesses.

## Source and novelty checks

- arXiv:1607.05674v7 source and PDF page 17 were inspected directly.
- The source screenshot verifies both the stated question and the reversed
  inequality in Remark 2.11; PDF page 14 verifies Lemma 2.8(ii)'s hypothesis
  `n-k <= k`.
- Exact arXiv title/id/formula queries and the four works indexed as citing the
  published chapter found no correction or answer.
- The nearest 2026 result, Alon--Puder arXiv:2603.00353v1, was inspected at
  source level.  It treats noncentral coordinate-hypergraph Laplacians and
  does not state this central normalized-rank maximum.

## PDF QA

`solution_packet.pdf` was compiled with `latexmk`, checked for undefined
references and overfull/underfull boxes, rendered to PNG at 130 dpi, and all
four pages were visually inspected.  Formulas, source excerpt, theorem breaks,
and references are readable; no substantive LaTeX warnings remain.
