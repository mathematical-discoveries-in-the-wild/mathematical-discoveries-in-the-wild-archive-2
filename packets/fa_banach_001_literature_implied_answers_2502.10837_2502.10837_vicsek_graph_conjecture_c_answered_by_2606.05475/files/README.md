# Vicsek quasi-Riesz Conjecture C: later classification

Status: `literature_implied_answer_with_negative_companion`.

Conjecture C of arXiv:2502.10837v3 asks, on Vicsek graphs, for the reverse
estimate `RR_(p,gamma)` when `p>2` and

```text
gamma > theta(p) = 1/beta + (2 - 2/beta)/p.
```

Theorem 1.3 of arXiv:2606.05475v2 proves the stronger non-endpoint
classification, with `beta=D+1` and

```text
gamma_*(p) = 1/beta + (1 - 2/beta)/p:
R holds and RR fails for gamma < gamma_*(p);
R fails and RR holds for gamma > gamma_*(p).
```

Because `theta(p)=gamma_*(p)+1/p`, this proves source Conjecture C. It also
disproves the companion proposal immediately following Conjecture C, which
asserted `R` throughout `gamma<theta(p)` for `p<2`: the interval
`gamma_*(p)<gamma<min(theta(p),1)` supplies failures.

Only equality `gamma=gamma_*(p)` remains open. The existing lane packet
`2606.05475_vicsek_critical_single_cut_and_truncation` gives partial endpoint
progress but does not claim a full answer.

Files:

- `main.tex`: exact threshold comparison and scope note.
- `solution_packet.pdf`: rendered literature-status packet.
- `source_paper.pdf`: arXiv:2502.10837v3.
- `supporting_paper_2606.05475.pdf`: later classification theorem.
- `tmp/`: build and render intermediates.

No new mathematical result is claimed.
