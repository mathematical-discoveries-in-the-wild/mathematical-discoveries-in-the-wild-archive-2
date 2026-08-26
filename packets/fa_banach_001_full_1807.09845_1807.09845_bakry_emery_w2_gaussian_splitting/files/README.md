# Candidate full solution: a W2 Gaussian-factor splitting estimate

Status: `candidate_full_solution_likely_valid_needs_human_review`

Source: Thomas A. Courtade and Max Fathi, *Stability of the Bakry--Emery theorem on R^n*, arXiv:1807.09845. Remark 1.1 on source PDF page 3 says the authors do not know how to obtain a W2 estimate when `k<n`.

## Result

Under exactly the hypotheses of source Theorem 1.1, the packet proves that there are a k-plane `E` and `p in E` such that

`W2(mu, gamma_{p,E} tensor mubar) <= 13 k sqrt(epsilon)`.

This answers the stated topology question for every `k<=n`. The separate optimal-rate question—whether `sqrt(epsilon)` can be improved toward `epsilon`—is not settled.

## Mechanism

Caffarelli contraction controls the Brenier Jacobian on the first-Hermite-chaos plane selected by the approximate Poincare extremizers. A coupling independently resamples only the Gaussian coordinates in that plane; its target law is exactly the Gaussian-factor product, while Gaussian Poincare bounds its squared cost by three times the Jacobian defect.

## Files

- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: readable source-page crop containing Remark 1.1.
- `verification_report.md`: line-by-line proof audit and reviewer focus.
- `novelty.md`: bounded literature and duplicate search.
- `code/check_constants.py`: non-proof arithmetic and random-matrix sanity check.

Human-review recommendation: high priority. Review especially the partial-resampling coupling and the operator-trace step converting approximate directions into a k-plane defect bound.
