# Literature Resolution: the sharp Krasnosel'skii--Mann constant is `1/sqrt(pi)`

- **Source:** R. Cominetti, J. A. Soto, and J. Vaisman, *On the rate of convergence of Krasnoselski-Mann iterations and their connection with sums of Bernoullis*, arXiv:1206.4195.
- **Question:** Find the smallest universal constant `kappa` in the asymptotic-regularity bound.
- **Answer:** `kappa = 1/sqrt(pi)`.
- **Answering paper:** M. Bravo and R. Cominetti, *Sharp convergence rates for averaged nonexpansive maps*, arXiv:1606.05300, Theorem 1.1.
- **Status:** `literature_already_answered_full`.
- **Model:** `GPT5.6`.

The later paper proves tightness by constructing a nonexpansive map on the infinite unit cube in `ell_infinity` whose Krasnosel'skii--Mann iterates attain the universal recursive distance bounds. It then shows that any constant smaller than `1/sqrt(pi)` fails. Together with the source paper's upper bound, this determines the optimum exactly.

## Files

- `main.tex` — concise source-backed resolution.
- `solution_packet.pdf` — compiled packet.
- `source_paper.pdf` — official source-question PDF.
- `supporting_paper.pdf` — official answering-paper PDF.
- `VERIFICATION.md` — theorem and presentation checks.
