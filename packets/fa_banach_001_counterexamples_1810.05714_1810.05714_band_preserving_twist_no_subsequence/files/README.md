# A complete rectangular function space without the subsequence property

Status: candidate_counterexample_likely_valid

Source: J. M. Calabuig, M. Fernández Unzueta, F. Galaz-Fontes, and
E. A. Sánchez Pérez, Equivalent Norms in a Banach Function Space and the
Subsequence Property, arXiv:1810.05714, Section 4.2, PDF page 12.

## Result

The source asks whether every Banach rectangular function space has the
subsequence property.  The answer is no.

On the Lebesgue unit interval, take a local Hamel basis of L0 containing the
constant function 1 and q(t)=t.  Swapping those two local coordinates defines
a band-preserving linear involution U of L0.  Transport the L2 norm to

X = U(L2[0,1]).

Since U commutes with every restriction by a measurable set, X is a Banach
space of measurable functions with the strict rectangular estimate

||chi_A x||_X <= ||x||_X.

But U:L2->L0 is discontinuous: it sends simple functions s to qs, while
U(q)=1.  Hence there is an X-null sequence that stays uniformly away from zero
in measure, and no subsequence can converge almost everywhere.  Thus X does
not have the subsequence property.

## Provenance and scope

The local-Hamel-basis representation is taken from Gutman, Kusraev, and
Kutateladze, The Wickstead Problem, arXiv:0712.2378.  The transported-L2
construction and its application to the 2018 question are proved in the
packet.  Bounded exact-question and arXiv searches found no later answer.
This makes novelty plausible, not certified.

The counterexample is deliberately nonconstructive and uses choice through a
local Hamel basis.  It does not contradict the source's positive result for
rectangular sequence spaces.

## Packet contents

- main.tex and solution_packet.pdf: full construction and proof.
- source_paper.pdf: arXiv:1810.05714.
- supporting_paper_0712.2378.pdf: the decisive local-Hamel-basis source.
- figures/open_problem_crop.png: the question on source PDF page 12.
- VERIFICATION.md: mathematical, provenance, and rendering checks.

Human review should focus on the well-defined local coordinate swap and its
commutation with every band projection.

