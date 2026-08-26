# Kleinberg’s random-graph Poincaré question answered by arXiv:2506.17433

Status: `literature_already_answered`

## Source question

Manor Mendel and Assaf Naor, *Expanders with respect to Hadamard spaces and random graphs*, arXiv:1306.5434; Duke Math. J. 164 (2015), 1471–1548.

Section 2.1, Question 2.4 (printed page 11) asks whether two independent random 3-regular graphs are asymptotically almost surely expanders with respect to each other: equivalently, whether `gamma(G,d_H^2)` is bounded by a universal constant independently of both vertex-set sizes.

## Explicit later answer

Dylan J. Altschuler, Pandelis Dodos, Konstantin Tikhomirov, and Konstantinos Tyros, *Discrete Poincaré inequalities and universal approximators for random graphs*, arXiv:2506.17433v2.

The abstract explicitly says that it gives a complete affirmative resolution of Kleinberg’s problem. Problem 1.2 restates the Mendel–Naor question, and Theorem 1.3 (printed page 3) proves a stronger result: for arbitrary fixed degrees `d, Delta >= 3` and every `p >= 1`, two independent uniform regular graphs satisfy `gamma(G,dist_H^p) <= Gamma(d,p)` with probability `1-O_{d,Delta}(min{n,m}^{-tau})`.

Taking `d=Delta=3` and `p=2` gives exactly the requested universal constant and limit. The supporting authors explicitly identify and solve the source question, so this belongs in `literature_already_answered`, not as an agent-derived mathematical result.

The source paper’s separate union-stability question for nonlinear spectral gaps (the remark on printed page 26) is not addressed by this identification.

Files:

- `source_paper.pdf`: arXiv:1306.5434.
- `supporting_paper_2506.17433.pdf`: the separate answering paper.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

