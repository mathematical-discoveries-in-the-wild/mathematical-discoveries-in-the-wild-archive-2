# Literature resolution: rank of the 2-Steiner distance matrix of a tree

- Source: A. Azimi, R. B. Bapat, and S. Goel, *Steiner distance matrix of
  caterpillar graphs*, arXiv:2108.12798.
- Later answer: A. Azimi and S. Sivasubramanian, *The 2-Steiner distance
  matrix of a tree*, Linear Algebra and its Applications 655 (2022), 65--86,
  DOI `10.1016/j.laa.2022.09.007`.
- Status: `literature_already_answered`.
- Agent: `agent_lane_18`; model: `GPT5.6`; date: 2026-08-11.

The source proves the formula for caterpillar trees and asks for the rank for
an arbitrary tree. The later paper answers the question exactly: if `T` has
`n` vertices and `p` pendant vertices, then

`rank D_2(T) = 2n - p - 1`.

The answering paper gives this as Theorem 1 and proves it inductively in
Section 3. It also constructs a row-space basis and derives inverse,
determinant, and inertia results.

Files:

- `solution_packet.pdf`: compact attribution and verification note.
- `source_paper.pdf`: source paper, arXiv:2108.12798.
- `answer_paper.pdf`: published answering paper.
- `figures/open_problem_crop.png`: exact source question.
- `figures/answer_theorem_crop.png`: exact answering theorem.
- `main.tex`: packet source.
