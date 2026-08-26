# Sharp norms for involutory dilations

This packet gives candidate full answers to Questions 3.2 and 3.4 of
Bourin--Lee, arXiv:2602.19599.

For the involution already displayed in Proposition 3.3,

\[
S_A=\begin{pmatrix}A&I+A\\I-A&-A\end{pmatrix},
\]

a fixed Hadamard conjugation gives

\[
H S_A H=\begin{pmatrix}I&0\\2A&-I\end{pmatrix}.
\]

The exact norm is

\[
\|S_A\|=\|A\|+\sqrt{1+\|A\|^2}.
\]

Thus the source's constant `3` improves sharply to `1+sqrt(2)`, and `S_A`
itself is a real-preserving involutory dilation in dimension `2n`.  The
source's numerical-range obstruction proves this is the optimal universal
constant over the complex field and over the real field for `n >= 2`.  For
real `n=1`, arbitrary dilations have the exceptional optimum `1`, while the
uniform norm bound for the specific family `S_A` is still `1+sqrt(2)`.

Artifacts:

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: editable proof source.
- `code/verify_involutory_dilation.py`: exact symbolic and numerical checks.
- `verification_report.md`: recorded verification and rendering checks.
- `novelty_search.md`: bounded literature search.
- `source_paper.pdf`: source paper.
- `figures/question_3_2.png`, `figures/question_3_4.png`: exact source excerpts.

Status: candidate full resolution, likely valid; priority is not asserted.
