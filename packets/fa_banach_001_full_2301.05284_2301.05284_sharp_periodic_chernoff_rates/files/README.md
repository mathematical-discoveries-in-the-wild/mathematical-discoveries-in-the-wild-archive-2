# Sharp Chernoff rates for `|sin x|^xi`

Candidate full mathematical resolution of the periodic numerical-rate question
in arXiv:2301.05284. For each fixed `t>0`, the packet proves the sharp
uniform-norm rates

- `G`: `Theta(n^{-min(1,(xi+1)/2)})`;
- `S`: `Theta(n^{-min(2,(xi+1)/2)})`, except `xi=2`, where the exact rate is
  `Theta(n^{-2})` because `sin^2 x` is a trigonometric polynomial.

The proof combines the formal low-frequency tangency error with a new sharp
high-frequency obstruction: the lattice convolution multipliers revive at
frequencies of order `sqrt(n)`, where the Fourier coefficients of
`|sin x|^xi` have size `n^{-(xi+1)/2}`.

## Files

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: official arXiv PDF downloaded from arXiv.
- `figures/source_question_crop.png`: readable crop from source PDF page 11.
- `code/crop_source.py`: deterministic crop script.
- `code/verify_formulas.py`: independent symbolic/numerical QA.
- `verification_report.md`: adversarial audit and scope assessment.

## Scope

This fully determines the asymptotic orders for the source's entire
trigonometric family and both concrete schemes. It does not solve the paper's
separate variable-coefficient superfast-approximation problem or its
exponential initial-condition experiments.
