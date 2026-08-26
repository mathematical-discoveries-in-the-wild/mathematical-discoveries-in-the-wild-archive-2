# 2412.11191 — K-theory rules out the proposed Calkin/stable-corona isomorphism

Status: literature_implied_answer (full source question).

Model: GPT5.6.

Source question: Damian Głodkowski and Piotr Koszmider, *Products of C*-algebras that do not embed into the Calkin algebra*, arXiv:2412.11191, Question 32 on source PDF page 15.

Supporting source: Hannes Thiel, *Real rank of some multiplier algebras*, arXiv:2402.01022, source PDF pages 5–6, especially Corollary 3.3 and Example 3.4. Thiel invokes the standard theorem that the K-theory of the multiplier algebra of a stable C*-algebra vanishes and applies the six-term exact sequence to the stabilization of the Calkin algebra.

## Identification

Question 32 asks, under CH, whether the Calkin algebra

    Q = B(ell_2)/K(ell_2)

can be isomorphic to the stable corona

    C = M(Q tensor K)/(Q tensor K).

The answer is no in ZFC. The standard Calkin extension gives

    K_0(Q)=0,  K_1(Q)=Z.

Since the K-theory of `M(Q tensor K)` vanishes, the six-term sequence for the stable-corona extension shifts the groups:

    K_0(C)=Z,  K_1(C)=0.

An isomorphism would induce degree-preserving K-theory isomorphisms, which is impossible. CH plays no role.

The supporting paper predates the source question and does not claim to answer it. The relation is an agent-identified direct implication of established K-theory, hence the `literature_implied_answers` classification rather than a new proof packet.

## Files

- `main.tex`: compact source-question transcription and K-theory identification.
- `solution_packet.pdf`: compiled status note.
- `source_paper.pdf`: official PDF of arXiv:2412.11191.
- `supporting_paper_2402.01022.pdf`: official PDF of the supporting paper.

## Scope

This fully answers Question 32 under the usual meaning of C*-algebra isomorphism. It does not address Question 33 about masas of the Calkin algebra.
