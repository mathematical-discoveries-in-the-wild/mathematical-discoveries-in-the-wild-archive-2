# A self-adjoint operator whose norm is not attained

Status: `literature_implied_answer (full for Open Question 1)`

N. B. Okelo, *Various notions of norm-attainability in normed spaces*,
arXiv:2004.05496, asks in Section 7, page 12, whether a separable
infinite-dimensional complex Hilbert space admits a bounded self-adjoint
operator that does not attain its norm. Definition 2.5 on page 2 makes clear
that the intended comparison is on unit vectors.

S. Shkarin, *Norm attaining operators and pseudospectrum*, arXiv:1209.1218,
page 2, gives exactly the needed example: the diagonal operator on
`ell_2` with diagonal entries `1 - 2^{-n}`. Shkarin states that its norm is
1 and is not attained. The entries are real and positive, so the operator is
positive and self-adjoint. Unitary transport gives the example on every
separable infinite-dimensional complex Hilbert space.

The implication is agent-identified: Shkarin's paper predates Okelo's question
by eight years and does not claim to answer it. This is therefore a
literature-implied answer, not an original pipeline result.

The literal phrase "for all x_0 in H" cannot hold without a unit-norm
restriction. For a nonzero bounded operator, scaling any vector on which it is
nonzero eventually makes `||Ax|| > ||A||`; for the zero operator, strict
inequality fails. The packet records both this literal reading and the intended
unit-sphere reading.

Scope limitation: this packet fully answers only Open Question 1. Open
Question 2, concerning the coincidence of p-norm-attainability and
p-normality, is not addressed.

Files:

- `solution_packet.pdf`: compact literature-status note.
- `source_paper.pdf`: arXiv:2004.05496.
- `supporting_paper_1209.1218.pdf`: arXiv:1209.1218.
- `main.tex`: LaTeX source.
- `tmp/`: build and rendering intermediates.

Human-review focus: confirm that Definition 2.5 supplies the omitted unit-vector
restriction in Open Question 1 and that Shkarin's diagonal example is read over
the complex scalar field. Both checks are explicit in the cited papers.
