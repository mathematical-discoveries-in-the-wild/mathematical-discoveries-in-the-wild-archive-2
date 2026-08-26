# Resolution packet: gamma-composition total positivity

Status: candidate full resolution, likely valid, needs human review.

Source: Donald St. P. Richards and Caroline Uhler, *Loading Monotonicity of
Weighted Premiums, and Total Positivity Properties of Weight Functions*,
arXiv:1806.07957.

Question: Remark 4.4 asks whether, for fixed `c>0`,

`C_c(u,v) = Q(u+c,Q^{-1}(u,v))`

is strictly totally positive of orders two and three as a kernel in `(u,v)`.

Result:

- For every `c>0`, `C_c` is STP2 on `(0,infinity) x (0,1)`. It extends as a
  TP2 kernel to `v=0`, but cannot be strict there because `C_c(u,0)=0`.
- The proposed STP3 assertion is false in general. At `c=1/8`, the decreasing
  triples `u=(100,18/5,6/25)` and `v=(99/100,63/100,3/20)` give a strictly
  negative 3-by-3 determinant. Outward-rounded interval arithmetic certifies
  that the determinant lies between `-0.000121058521276380747056567349942252`
  and `-0.000121058521276380747056567349942124`.

The order-two proof differentiates in `v`. The derivative is a positive
multiple of the `c`-th power of a gamma quantile. Saunders and Moran's strict
gamma-quantile ratio theorem makes this derivative kernel STP2; integration
from the common zero boundary preserves strict order-two positivity.

Files:

- `main.tex`: full mathematical packet.
- `solution_packet.pdf`: compiled and visually checked packet.
- `source_paper.pdf`: official arXiv PDF.
- `supporting_paper_saunders_moran_1978.pdf`: the decisive 1978 result, as
  reproduced in Appendix B of Saunders's ANU thesis.
- `supporting_source_saunders_thesis.pdf`: official ANU repository source of
  that appendix.
- `figures/open_problem_crop.png`: source page containing the open problems.
- `code/interval_certificate.py`: reproducible interval certificate.
- `VERIFICATION.md`: verifier report and commands.

Review recommendation: check the orientation of the quantile-ratio
inequality and independently run the interval certificate. The result does not
claim a classification of the values of `c` for which STP3 might separately
hold; one certified value of `c` suffices to refute the conjectured general
STP3 statement.
