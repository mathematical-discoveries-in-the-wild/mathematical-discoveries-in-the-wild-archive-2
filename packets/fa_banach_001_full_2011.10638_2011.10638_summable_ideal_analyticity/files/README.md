# Questions 6.1 and 6.2: regularization and analyticity

This packet gives candidate full affirmative solutions to both concluding
questions of Balcerzak--Leonetti, arXiv:2011.10638.

Main result:

\[
x\in\mathscr A
\quad\Longleftrightarrow\quad
\exists A\subseteq\mathbb N\;
\bigl(A\in\mathcal I_x\text{ and }A-1\notin\mathcal I_x\bigr).
\]

The witness relation is Borel, hence `mathscr A` is analytic. The proof's new
ingredient is a regularization lemma showing that backward-shift invariance of
`I_x` is equivalent to ideal-equivalence with a sequence whose consecutive
ratios are bounded below. After rearranging any null positive divergent
sequence in nonincreasing order, the exceptional downward drops have summable
predecessor mass. The same lemma therefore shows that every `I_x` is
isomorphic to a single `I_y` with `y` in `mathscr Y`, which strengthens the
Fubini-sum conclusion requested in Question 6.1.

Artifacts:

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: editable source.
- `source_paper.pdf`: source paper.
- `figures/problem_crop.png`: exact source excerpt containing Question 6.2.
- `novelty_search.md`: bounded novelty search.
- `verification_report.md`: proof and rendering checks.

Status: candidate full solutions, likely valid; priority is not asserted.
