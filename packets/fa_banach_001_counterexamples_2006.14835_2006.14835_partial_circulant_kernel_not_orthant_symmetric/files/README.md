# Partial circulant kernels are not orthant symmetric

Result type: `counterexample`

Status: candidate full negative answer, likely valid pending expert review.

Source:

- Sandra Keiper, “Recovery of Binary Sparse Signals from Structured Biased
  Measurements,” arXiv:2006.14835 (2020).
- Open question: Section 4, PDF pages 13--14; the explicit question is on page
  14.
- Local source: `source_paper.pdf`.
- Source evidence: `figures/open_problem_crop.png`.

## Claimed contribution

The packet gives an iid Gaussian partial circulant matrix with `M=N/2` whose
kernel law is not invariant under coordinate sign changes.  For

```
Phi = [a b c d]
      [d a b c],
```

all row spaces satisfy an additional homogeneous Pluecker equation `Q=0`.
After flipping coordinate zero, `Q` becomes a nonzero polynomial of
`(a,b,c,d)`, so it is nonzero almost surely.  The original and sign-flipped
row-space laws are therefore separated by a probability-one algebraic event.
Orthogonal complementation transfers this failure to the kernel law.

This answers the source's first future-work question negatively for its
Gaussian partial-circulant ensemble, in the motivating balanced regime.

## Scope caveat

The result does not classify all dimensions or row subsets, does not settle the
Rademacher ensemble in a fixed-rank formulation, and does not provide the
alternative proof of the recovery threshold that the source also requests.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: exact source definition and question.
- `code/check_plucker_obstruction.py`: symbolic and numerical regression
  checks; not part of the proof.
- `verification_report.md`: build and QA record.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

A bounded local-index, arXiv, and web search on 17 August 2026 used the exact
question, arXiv id, partial-circulant/orthant-symmetry combinations, and the
small-dimensional kernel formulas.  No later answer or this Pluecker
obstruction was found.  Novelty confidence is moderate pending specialist
review.

## Human review focus

Please check the six Pluecker coordinates, the homogeneous identity `Q=0`,
the signs induced by flipping coordinate zero, and the transfer between row
spaces and nullspaces.
