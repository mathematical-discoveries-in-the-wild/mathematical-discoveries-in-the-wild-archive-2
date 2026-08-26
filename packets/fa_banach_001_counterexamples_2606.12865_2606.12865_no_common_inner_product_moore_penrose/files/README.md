# No common inner product makes the canonical inverse Moore--Penrose

Result type: `counterexample`

Status: candidate full negative answer, likely valid pending expert review.

Source:

- Mohamed Amine Aouichaoui, Michał Buchała, and Stephan Ramon Garcia,
  “On m-partial isometries: spectra, weighted shifts, and similarity,”
  arXiv:2606.12865v1 (2026).
- Open question: Question 6, PDF page 17.
- Local source: `source_paper.pdf`.
- Source evidence: `figures/open_question.png`.

## Claimed contribution

The packet answers Question 6 negatively. Let

```
phi = (1+sqrt(5))/2,  a = sqrt(phi),  delta = 1-phi,
T   = [[a,0],[1,0]].
```

The source already notes that `T` is a 2-partial isometry and that
`S=2T*-T*^2T` is a generalized inverse. The packet observes that

```
ST = [[1,0],[0,0]],
TS = [[-1,2a],[a delta,2]].
```

If an alternate Hilbert inner product is represented by `G>0`, the
Moore--Penrose equations require both idempotents to be `G`-selfadjoint.
The first condition forces `G=diag(x,y)`. The second then forces
`2x=delta y`, impossible because `x,y>0` and `delta<0`.

## Scope caveat

This fully refutes the universal assertion in Question 6. It does not
classify the 2-partial isometries for which the canonical generalized inverse
can become Moore--Penrose, and it does not settle Questions 1--5.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_question.png`: source example and Question 6.
- `code/check_counterexample.py`: exact symbolic regression check.
- `verification_report.md`: build and visual-QA record.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

A bounded local-index, arXiv, and web search on 17 August 2026 found no later
answer. The arXiv record remains at version 1. Novelty confidence is moderate
pending specialist review.

## Human review focus

Please check the literal fixed-operator interpretation of Question 6, the
matrix products, and the simultaneous `G`-selfadjointness obstruction.
