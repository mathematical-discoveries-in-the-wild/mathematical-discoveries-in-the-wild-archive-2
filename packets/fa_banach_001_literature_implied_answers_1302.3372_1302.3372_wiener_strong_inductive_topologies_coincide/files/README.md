# Literature-implied answer: the two Wiener topologies always coincide

status: `literature_implied_answer_full_scope`

source: Daniel Alpay and Guy Salomon, *On algebras which are inductive
limits of Banach spaces*, arXiv:1302.3372v2, Remark 5.2, pp. 10--11.

supporting theorem: Juan Carlos Diaz and Pawel Domanski, *On the Injective
Tensor Product of Distinguished Frechet Spaces*, Math. Nachr. 198 (1999),
41--50, DOI: [10.1002/mana.19991980104](https://doi.org/10.1002/mana.19991980104).

corroborating survey: Klaus D. Bierstedt and Jose Bonet, *Some aspects of
the modern theory of Frechet spaces*, RACSAM 97 (2003), 159--188,
especially p. 183.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1302.3372_wiener_strong_inductive_topologies_coincide/`

ledger: `runs/fa_banach_001/ledger/results/1302.3372_wiener_strong_inductive_topologies_coincide.json`

## Source question

Remark 5.2 starts with a decreasing sequence of reflexive Banach spaces
`Phi_p` whose intersection

`E = intersection_p Phi_p`

is a reflexive Frechet space. It sets

`Psi_p = c_0(Z; Phi_p)` and `Psi_p' = ell_1(Z; Phi_p')`

and asks when the inductive-limit topology on `union_p Psi_p'` coincides
with its topology as the strong dual of `intersection_p Psi_p`.

## Identification

Let `K = Z union {infinity}` be the one-point compactification of the
discrete space `Z`. Directly from the seminorms,

`intersection_p c_0(Z; Phi_p) = c_0(Z; E)`.

The latter is the kernel of evaluation at infinity in `C(K,E)` and is
topologically complemented there: subtract the constant function with value
`f(infinity)`. Diaz--Domanski prove that `C(K,E)` is distinguished whenever
`E` is a reflexive Frechet space and `K` is compact Hausdorff. A complemented
subspace of a distinguished Frechet space is distinguished, so `c_0(Z;E)` is
distinguished.

For a Frechet space, distinguishedness is equivalent to equality between
the strong-dual topology and the inductive topology obtained from the duals
of its local Banach spaces. Those local duals here are exactly
`ell_1(Z;Phi_p')`. Therefore the two topologies in Remark 5.2 coincide under
all of the hypotheses stated there.

## Status and novelty

This is a full affirmative answer to the topology question as posed in
Remark 5.2, but not a new result. The decisive theorem was published in 1999,
before the 2013 source paper. Diaz--Domanski could not have known they were
answering Alpay--Salomon's later remark; the connection is an agent-identified
specialization, hence the `literature_implied_answers` classification rather
than `literature_already_answered`.

The bounded search used the exact source sentence, the terms `distinguished
Frechet`, `C(K,E)`, `injective tensor product`, and the source title. It found
the official Wiley abstract for DOI 10.1002/mana.19991980104 and the 2003
Bierstedt--Bonet survey, whose p. 183 states the needed theorem explicitly.
No later paper explicitly naming Remark 5.2 was found in that bounded search.

## Files

- `main.tex`: compact review note.
- `solution_packet.pdf`: rendered review note.
- `source_paper.pdf`: original arXiv paper.
- `supporting_survey_bierstedt_bonet_2003.pdf`: local supporting survey.
- `tmp/`: LaTeX and rendering intermediates.

