# Diamond counterexamples to three Plebanek--Sobota questions

Status: literature_already_answered (relative-consistency negative under
Jensen's diamond).

Source: Grzegorz Plebanek and Damian Sobota, *Countable tightness in the
spaces of regular probability measures*, arXiv:1405.2527 (2014).

Supporting answer: Piotr Koszmider and Zdenek Silber, *Countably tight dual
ball with a nonseparable measure*, arXiv:2312.02750 (2023), Theorem 1 and the
two corollaries immediately following it.

## Identification

The supporting paper assumes diamond and constructs a compact Hausdorff space
K for which P(K) is countably tight although K carries a probability measure
of uncountable Maharam type. Its first corollary says P(K x K) has uncountable
tightness, and its second says C(K) has Corson's property (C) while C(K x K)
does not.

These statements give negative answers under diamond to three explicit source
questions:

1. Main Problem 1.1: must countable tightness of P(K) force every measure on K
   to have countable Maharam type?
2. Problem 5.1: must countable tightness of P(K) imply countable tightness of
   P(K x K)?
3. Problem 5.4: must property (C) of C(K) imply property (C) of C(K x K)?

This is explicit provenance, not merely an agent inference: Koszmider--Silber
cite the Plebanek--Sobota theorem/question, state that their example separates
P(K x K) from P(K) x P(K), and identify the property-(C) consequence as an
answer to Pol's question.

## Scope

The answer is relative-consistency negative, not an absolute ZFC
counterexample. The source's Problem 5.3 (property (C) of C(K) versus
countable tightness of P(K)) is stated by the 2023 supporting paper to remain
open in ZFC. The source's Frechet--Urysohn/countably-determined-measure question
is also not answered by this packet.

The source's Main Problem 1.1 was already represented in this run through an
earlier 2011 formulation. This packet records the two additional exact
Plebanek--Sobota product questions and prevents repeated queue work on the
2014 source.

Files:

- main.tex: compact identification note.
- solution_packet.pdf: rendered status note.
- source_paper.pdf: locally rendered from the exact archived arXiv TeX source
  for 1405.2527 after the direct PDF fetch timed out twice.
- supporting_paper_2312.02750.pdf: decisive supporting paper.
- tmp/: rendering intermediates.
