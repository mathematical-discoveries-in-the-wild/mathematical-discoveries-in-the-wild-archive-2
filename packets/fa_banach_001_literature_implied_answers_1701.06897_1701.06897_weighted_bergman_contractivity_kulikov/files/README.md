# Weighted Bergman contractivity: full literature-implied answer

Status: **literature_implied_answer (full affirmative answer)**.

Bayart--Brevig--Haimi--Ortega-Cerdà--Perfekt, arXiv:1701.06897, ask
whether

`||f||_{A_beta^q} <= ||f||_{A_alpha^p}`

whenever `0<p<=q`, `alpha,beta>=1`, and `q/beta<=p/alpha`.

The answer is yes for all stated parameters. Put
`beta_0=alpha*q/p`. Kulikov's Corollary 1.3 (arXiv:2203.12349,
GAFA 2022) proves the contraction at the critical line
`p/alpha=q/beta_0`, including the Hardy endpoint. The hypothesis of the
source question says `beta>=beta_0`; normalized weighted Bergman norms at a
fixed exponent decrease as the weight parameter increases. This follows
from stochastic ordering of the radial beta measures and monotonicity of
analytic integral means. The case `p=q` follows from the same radial
monotonicity alone.

This is not an original mathematical result of the run: the decisive
critical-line theorem is in later literature, and the full wedge is its
elementary consequence.

Files:

- `solution_packet.pdf`: complete proof and provenance note
- `source_paper.pdf`: arXiv:1701.06897
- `supporting_paper_kulikov_2203.12349.pdf`: Kulikov's primary paper
- `figures/open_question_crop.png` and `open_question_continuation_crop.png`:
  source question across PDF pp. 9--10
- `figures/supporting_corollary_crop.png`: Kulikov's Corollary 1.3
- `verification.md`: compilation, rendering, visual-QA, and checksums

