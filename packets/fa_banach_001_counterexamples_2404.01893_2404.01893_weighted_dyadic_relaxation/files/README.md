# A sparse-log-frequency counterexample to weighted dyadic summability

Status: `counterexample_likely_valid`

Source target: the first question in the concluding remarks of
arXiv:2404.01893 (PDF page 31), specifically the proposed replacement of
the dyadic sum in Theorem 3.3(2) by the same sum divided by `1+|n|`.

On the one-point space take `A=I`.  A bounded smooth multiplier is built
from sine waves of frequencies `K_j=2^j` supported near log-dyadic centers
`N_j=2^(6j)`.  Its localized `W_2^4` costs are `O(K_j^4)`, so the proposed
weighted sum is finite.  But `t -> m(t)` has at least order `K_j`
fixed-size oscillations in the `j`th block; consequently its `V^q` norm is
infinite for every finite `q`.  Thus the proposed relaxation fails already
for a scalar Hilbert space and the identity semigroup generator.

The packet makes no claim about the analogous time-dependent maximal
estimate or the separate square-summability question.

Files:

- `solution_packet.pdf`: exact construction and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_question_crop.png`: exact concluding question.
- `code/verify_scales.py`: exact exponent and oscillation transcription
  checks.
