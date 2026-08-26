# No universal weighted Sobolev-SVD tail bound

Result type: `counterexample`

Status: candidate full negative answer, likely valid pending expert review.

Source:

- Mazen Ali and Anthony Nouy, “Singular Value Decomposition in Sobolev
  Spaces: Part II,” arXiv:1912.11293 (journal version, 2021).
- Open question: Section 2, immediately after Proposition 2.1, PDF page 3.
- Local source: `source_paper.pdf`.
- Source evidence: `figures/open_problem_crop.png`.

## Claimed contribution

Under the natural uniform reading of the source question, no fixed finite
weight sequence `gamma(k)` can control the weighted `L2`-SVD tail by the
`H^(1,0)` singular-value tail for all Sobolev functions.

The counterexample is a smooth rank-two Fourier family on one fixed square.
At truncation rank one, the questioned left side grows as `1+N^2/2`, whereas
the only nonzero term on the proposed right side is `gamma(2)` times a squared
singular value smaller than `2`.  Thus no universal implicit constant works.
Swapping variables gives the same result for `H^(0,1)`.

## Interpretation caveat

The source writes “for some sequence” and uses an implicit comparison
constant.  The packet interprets both as fixed independently of the function,
which is the only nontrivial uniform formulation.  It does not rule out bounds
under additional regularity, spectral localization, or incoherence
assumptions, as the source itself anticipates.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: exact question and context.
- `code/check_rank_two_family.py`: exact symbolic regression check; not part
  of the proof.
- `verification_report.md`: build and QA record.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

A bounded local-index, arXiv, and web search on 17 August 2026 checked the
exact displayed question, title and arXiv id, and Sobolev-SVD weighted-tail
variants.  No later answer or this construction was found.  Novelty confidence
is moderate pending specialist review.

## Human review focus

Please check the `H1` Gram matrix, the identification of squared
`H^(1,0)` singular values with the two eigenvalues of `D G_N D`, and the
uniform interpretation of the source's implicit constant and sequence.
