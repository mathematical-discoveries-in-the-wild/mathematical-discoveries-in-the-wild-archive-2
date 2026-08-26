# Higher-dimensional spin ball versus max ball: explicit later answer

Run: `fa_banach_001`

Agent: `agent_lane_00`

Status: `literature_already_answered (full for every m >= 3)`

## Original question

Farenick, Huntinghawk, Masanika, and Plosker, *Complete order equivalence of
spin unitaries*, arXiv:2006.06810, ask immediately after Theorem 5.12 on PDF
page 19 whether their equality of the spin ball and max ball in dimensions
one and two extends to higher dimensions.

## Explicit later answer

Evert and Passer, *Matrix convex sets over the Euclidean ball and polar duals
of real free spectrahedra*, arXiv:2507.20325, restate this exact problem as
Question 1 on PDF page 6 and say that they resolve it negatively. Theorem 2.9
on PDF page 10 constructs higher-level free extreme points for the corrected
three-variable universal spin spectrahedron. Remark 2.11 on PDF page 11
explicitly identifies this as a negative answer to the question after the
source paper's Theorem 5.12, and Corollary 3.9 on PDF page 19 extends the
failure to every `g >= 3`.

The identification also avoids a false shortcut: the corrected universal
three-variable tuple is `P direct-sum conjugate(P)`, so a Pauli/transpose
witness that tests only `P` is not in the corrected spin ball.

The supporting authors knew they were answering the source question. The
answer is complete: equality holds for dimensions one and two and fails for
every dimension at least three.

## Files

- `main.tex`: compact identification and status note.
- `solution_packet.pdf`: rendered status packet.
- `source_paper.pdf`: arXiv:2006.06810.
- `supporting_paper_2507.20325.pdf`: explicit later answer.
