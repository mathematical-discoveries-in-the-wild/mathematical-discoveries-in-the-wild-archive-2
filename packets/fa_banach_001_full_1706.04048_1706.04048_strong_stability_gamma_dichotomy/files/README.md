# Strong stability of indirect LDDMM minimizers

Result type: `full`

Status: candidate full answer, likely valid pending expert review.

Source paper:

- Chong Chen and Ozan Öktem, “Indirect Image Registration with Large
  Diffeomorphic Deformations,” SIAM Journal on Imaging Sciences 11 (2018),
  arXiv:1706.04048v2, DOI `10.1137/17M1134627`.
- Open-question location: Remark 7.6, page 15.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The packet gives the sharp answer over the full parameter range printed in
Theorem 7.5:

- For `gamma > 0`, the requested strong subsequential stability always holds.
  The discrepancy values converge by the source argument. Minimality against
  the weak limit then forces convergence of the Hilbert norms, and weak
  convergence plus norm convergence is strong convergence.
- For `gamma = 0`, the statement is false. With zero template, zero forward
  operator, fixed zero data, and squared discrepancy, every velocity is a
  minimizer. An orthonormal velocity sequence is weakly null but has no
  strongly convergent subsequence.

The same example exposes a boundary issue in the printed Theorem 7.5: an
unbounded sequence of minimizers at `gamma = 0` has no weakly convergent
subsequence. The source proof divides by `gamma`, so its coercive argument
supports `gamma > 0`, not `gamma >= 0`.

## Files

- `main.tex`: full proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of the proof tail and
  Remark 7.6.
- `verification.md`: proof audit and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

On August 11, 2026, the cheap run indexes and exact-title/question phrases were
searched. OpenAlex listed 32 citing works; their indexed titles and abstracts
did not state the sharp positive/zero dichotomy. A targeted inspection of the
related arXiv:1810.08596 found another weak stability proposition, not the
strong upgrade. Novelty confidence is moderate pending a specialist search.

## Human review focus

Please check:

- that the varying-data discrepancy convergence used on page 15 is understood
  as an effective hypothesis (joint continuity is sufficient);
- the one-line limsup norm estimate obtained from minimality;
- the `gamma = 0` boundary, which is included in the printed theorem but not
  supported by its `1/gamma` coercive estimate.
