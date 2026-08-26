# Three-vertex polyhedral counterexample

Candidate new full negative answer to the open question on PDF page 16 of
arXiv:2511.20345.

## Result

On `R^3` define

```text
||(a,b,c)|| = max(|a|,|b|,|c|,|-4a+2b+6c|/7).
```

The packet gives three linearly independent extreme points and an explicit
invertible rational operator which preserves full local Birkhoff--James
orthogonality at all three but is not a scalar multiple of an isometry.

The preservation proof is exact: at a simple vertex, non-orthogonality is a
strict-sign condition on the three active support functionals. The three
claims reduce to two displayed entrywise-nonnegative rational matrices.

## Files

- `main.tex`: full counterexample and proof.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: exact source question on PDF page 16.
- `verify_counterexample.py`: exact rational matrix and norm assertions.
- `tmp/`: build and render artifacts.
- `../../../../attempts/2511.20345_*search.py`: discovery and stress-test code.

## Status

Candidate new full counterexample. Human review is recommended for the
active-normal cone lemma and literature novelty.
