# Negative answer to both strict-dual-norm converse questions

Status: `literature_implied_answer (full negative answer)`

Source paper: Richard J. Smith, *Gruenhage compacta and strictly convex dual
norms*, arXiv:0710.5396, Problem 2.13 on PDF page 9.

Decisive supporting paper: Richard J. Smith, *Tree Duplicates,
G_delta-diagonals and Gruenhage spaces*, arXiv:1102.0982, Theorem 1.4 and
Corollary 2.5.

Supporting theorem source: Jose Orihuela, Richard J. Smith, and Stanimir
Troyanski, *Strictly convex norms and topology*, arXiv:1012.5595, Theorem 3.1.

## Identification

Problem 2.13 of arXiv:0710.5396 asks whether strict convex dual renormability
of `C(K)^*` forces `K` to be Gruenhage and, more ambitiously, whether any
strictly convex dual norm on `X^*` forces its weak-star dual unit ball to be
Gruenhage.

Corollary 2.5 of arXiv:1102.0982 constructs in ZFC a scattered compact
non-Gruenhage space `K` with property `(*)` and states that `C(K)` admits an
equivalent lattice norm whose dual norm is strictly convex.  It invokes
Theorem 1.4 there, quoted from Theorem 3.1 of arXiv:1012.5595.  This is already
a counterexample to the first question.

The same example also answers the ambitious question negatively.  For the
renormed `X=C(K)`, the Dirac map `x -> delta_x` is a weak-star homeomorphic
embedding of `K` into `X^*`.  Equivalent norms make the Dirac set uniformly
bounded, so after multiplying every Dirac measure by one fixed scalar its
image lies in the new dual unit ball.  Since Gruenhage spaces are hereditary,
that ball cannot be Gruenhage.

## Provenance and scope

The supporting paper does not label Corollary 2.5 as an answer to Problem 2.13,
although it cites Smith's 2009 paper and states the exact counterexample.  The
relation to the first question is immediate; the fixed-scalar Dirac embedding
is the additional identification for the second.  Accordingly this packet is
classified as a literature-implied answer, not as a new counterexample.

Both parts of Problem 2.13 are answered negatively.  No part of that stated
problem remains open.

## Files

- `source_paper.pdf`: arXiv:0710.5396.
- `supporting_paper_1102.0982.pdf`: decisive construction and Corollary 2.5.
- `supporting_paper_1012.5595.pdf`: source of the scattered-`(*)` renorming theorem.
- `main.tex`, `solution_packet.pdf`: compact status note.

