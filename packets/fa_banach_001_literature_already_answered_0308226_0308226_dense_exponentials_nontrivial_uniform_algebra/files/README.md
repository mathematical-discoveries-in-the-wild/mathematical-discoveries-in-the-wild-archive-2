# Dense exponentials do not force a uniform algebra to be trivial

Run: `fa_banach_001`  
Agent: `agent_lane_03`  
Model: `GPT5.6`  
Status: `literature_already_answered (negative)`

## Original question

Thomas William Dawson, *Extensions of Normed Algebras*, arXiv:math/0308226,
Chapter 5, PDF page 53, asks whether a uniform algebra `(A,X)` satisfying
`closure(exp A)=A` must have `A=C(X)`.

## Later answer

Alexander J. Izzo, *A nontrivial uniform algebra Dirichlet on its maximal
ideal space*, arXiv:2403.19583, Question 1.3 and Theorems 1.6/1.7, PDF page 2,
explicitly answers the dense-exponentials question. The paper constructs a
compact polynomially convex set `X` in `C^2` of topological dimension one for
which `P(X)` is nontrivial, strongly regular, Dirichlet on its maximal ideal
space, and has dense exponentials. Thus the 2003 conjecture is false.

The supporting paper explicitly presents its theorem as an answer to the same
dense-exponentials question; this is not an agent-inferred consequence.

## Scope

The negative answer does not settle the narrower locally connected or
Gelfand-interval regimes. Izzo notes that the constructed maximal ideal space
is metrizable and one-dimensional but not locally connected.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:math/0308226.
- `supporting_paper_2403.19583.pdf`: decisive later answer.
- `tmp/`: build and rendering intermediates.
