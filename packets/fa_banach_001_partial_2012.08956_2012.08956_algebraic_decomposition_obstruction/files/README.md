# Algebraic decomposition obstruction for the Pirkovskii--Piszczek example

**Status:** candidate substantial partial result, likely valid.

**Source:** Alexei Yu. Pirkovskii and Krzysztof Piszczek, *Topological
amenability and Köthe co-echelon algebras*, arXiv:2012.08956; *Banach Journal
of Mathematical Analysis* 16 (2022), Article 13.  The conjecture occurs after
Proposition 5.10 on source PDF page 19, with the referenced statement (v) on
page 18.

The packet proves the conjecture completely when “isomorphic” means a
topological algebra isomorphism.  Any such decomposition pulls a summand
identity back to a coordinate characteristic idempotent, reducing it to the
coordinate partition excluded by source Lemma 5.8.

For the actual, stronger locally convex-space conjecture, the packet proves a
new reduction.  Every hypothetical Banach summand must lie continuously in a
single weighted `ell_infinity` step and be complemented in every later step;
the complementary projection is compact from every Banach step into the
inductive limit.  It also yields an explicit compact-perturbation
factorization of the tail-corona quotient.  The remaining gap is stated
precisely and the full arbitrary-linear-isomorphism conjecture is not claimed
solved.

## Contents

- `solution_packet.pdf`: theorem, proof, reduction, limitations, and review notes.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_context_page18.png`: Proposition 5.10(v).
- `figures/open_problem_conjecture_page19.png`: the conjecture and its context.
- `tmp/`: LaTeX and rendering intermediates.

## Verification

The idempotent proof was checked directly coordinate by coordinate.  The
Baire lemma uses closed extended-norm sublevel sets.  The tail-corona map was
checked for independence of the chosen Banach step: two tail truncations
differ in finitely many rows and hence by an element of
`c_0(N;ell_infinity)`.  No computation is used.

## Novelty check

On 2026-08-11 the run registry and solution/attempt/proof-gap indexes were
searched for arXiv:2012.08956 and the core decomposition terms.  Exact-phrase
and keyword web searches found the source, its published version, and general
Köthe-space background, but no later resolution.  Novelty confidence is
moderate: the ingredients are standard, while this combination and its
application to the source conjecture were not located.

## Human-review recommendation

First verify that the completeness argument covers order-zero contractible
co-echelon summands, then check the Baire localization lemma.  The most useful
next step is to decide whether the tail-corona compact-perturbation
factorization is incompatible with a projection extending to every weighted
step.  Compactness only in the inductive-limit topology must not be silently
upgraded to compactness in the fixed-step norm.

