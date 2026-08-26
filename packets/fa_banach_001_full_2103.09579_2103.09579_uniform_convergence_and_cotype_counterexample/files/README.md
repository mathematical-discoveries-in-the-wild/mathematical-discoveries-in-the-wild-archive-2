# Uniform convergence and a cotype obstruction for dependent Gaussian Fourier series

Status: candidate full results, likely valid.

## Source questions

Remark 2 of arXiv:2103.09579 asks:

1. whether its coefficient condition (8) upgrades almost-sure boundedness
   of the dependent stationary Gaussian Fourier series to almost-sure
   uniform convergence; and
2. whether Pisier's cotype-2 conclusion has an analogue for general
   stationary Gaussian processes.

## Results

- The answer to the uniform-convergence question is **yes**, under exactly
  the hypotheses of the source's Theorem 4. The source's quadratic-form
  estimate applies simultaneously to all differences of all partial sums.
  Sudakov--Fernique comparison transfers the independent comparator's
  vanishing tail diameter, and monotonicity forces the dependent tail
  diameter to vanish almost surely.
- The general cotype-2 analogue is **false**, even inside the covariance
  class of Theorem 4. For the perfectly correlated stationary process
  `xi_n=Z`, the spectral measure is `delta_0` and
  `P(delta_0)=C(T)` with equivalent norm. This space has no finite cotype.
  The weighted covariance matrix is rank one and bounded whenever `b>1/2`.

The separate spectral-synthesis prompt in Remark 2 remains open in general.

## Files

- `solution_packet.pdf`: self-contained statements and proofs.
- `main.tex`: editable source.
- `verification.md`: detailed proof audit.
- `source_paper.pdf`: source paper.
- `figures/remark2_crop.png`: source theorem tail and Remark 2.

Human review should focus on the all-tail Gaussian comparison, the passage
from the comparator's almost-sure uniform convergence to expected tail
diameter convergence, and the intended norm in the cotype question.
