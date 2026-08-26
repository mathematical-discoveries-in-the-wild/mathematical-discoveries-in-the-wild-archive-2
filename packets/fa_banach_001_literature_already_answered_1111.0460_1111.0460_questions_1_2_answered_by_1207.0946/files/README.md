# Questions 1 and 2 answered by arXiv:1207.0946

Status: `literature_already_answered`

## Source questions

Eugenio Hern\'andez, *Lebesgue-Type inequalities for quasi-greedy bases*,
arXiv:1111.0460.

Section 3.4, arXiv PDF page 7, asks:

1. whether the upper bound `e_N <= C mu(N) log N` can be sharp; and
2. whether every quasi-greedy basis satisfies
   `tilde_sigma_N(x) <= C sigma_N(x) log N`.

## Explicit later answers

Gustavo Garrig\'os, Eugenio Hern\'andez, and Timur Oikhberg,
*Lebesgue-Type inequalities for quasi-greedy bases*, arXiv:1207.0946,
explicitly identifies arXiv:1111.0460 as its preliminary source [10].

On arXiv PDF pages 2--3, Theorem 1.1 proves
`C_N \asymp max{mu(N), k_N}`.  The following remarks state that democratic
quasi-greedy examples with `k_N \asymp log N` are constructed in Section 6,
attaining the logarithmic bound and answering the question in [10].  This
answers Question 1 affirmatively in general Banach spaces.

On arXiv PDF page 3, Theorem 1.2 proves
`k_N/4 <= D_N <= 2k_N`, where
`D_N = sup_x tilde_sigma_N(x)/sigma_N(x)`.  The next remark combines this
with `k_N <= c log N` and explicitly says that this answers a question from
[10].  This answers Question 2 affirmatively.  The upper estimate also has
the immediate projection proof included in the compact note.

Question 3 of the source is a separate broad characterization problem and is
not claimed resolved here.

Files:

- `source_paper.pdf`: arXiv:1111.0460.
- `supporting_paper_1207.0946.pdf`: separate answering paper.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

Ledger:
`runs/fa_banach_001/ledger/results/1111.0460_questions_1_2_answered_by_1207.0946.json`.
