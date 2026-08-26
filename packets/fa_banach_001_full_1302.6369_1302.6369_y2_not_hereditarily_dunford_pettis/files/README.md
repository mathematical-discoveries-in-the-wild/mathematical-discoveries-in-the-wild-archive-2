# 1302.6369: Y2 is not hereditarily Dunford--Pettis

- Status: `candidate_full_likely_valid`
- Model: `GPT5.6`
- Source: Ondřej F. K. Kalenda and Jiří Spurný, *On quantitative Schur and
  Dunford--Pettis properties*, arXiv:1302.6369v2
- Target: Question 3.5(1)
- Answer: negative

## Result

The source defines `X_p=(c0, max_{q<=p} A_q)` and

`Y2 = (direct sum X_p)_{c0}`,

while the Pełczyński--Szlenk space is

`Y1={x in l_infinity : A_p(x)->0}` with norm `sup_p A_p(x)`.

For the tail projection `P_p x=(0,...,0,x_p,x_{p+1},...)`, the packet proves

`A_p(x) <= ||P_p x||_{X_p} <= 2 A_p(x)`.

Consequently, `Jx=(P_p x)_p` is a two-isomorphic embedding of `Y1` as a closed
subspace of `Y2`. Example 3.3 of the source recalls that `Y1` fails the
Dunford--Pettis property. Therefore `Y2` is not hereditarily Dunford--Pettis,
fully answering Question 3.5(1) in the negative.

## Packet contents

- `main.tex` and `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: local source PDF.
- `figures/open_problem_crop.png`: source page 12 with Example 3.3 and Question
  3.5(1).
- `code/verify_tail_embedding.py`: finite-support sanity checks.
- `verification.md`: proof, computation, novelty, and reviewer audit.
- `attempts/1302.6369_y2_hereditary_dp/attempts.md`: route and scope log.

## Limitations and review recommendation

Questions 3.4, 3.5(2), and 3.5(3) remain open here. Recommended for expert
review as a concise full negative solution to Question 3.5(1); the tail
completion estimate and novelty status are the main review points.
