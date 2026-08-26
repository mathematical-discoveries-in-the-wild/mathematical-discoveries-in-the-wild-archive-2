# First-order axiomatisability of `CompHaus^op`: answered negatively

Status: `literature_already_answered`

## Source question

Vincenzo Marra and Luca Reggio, *Stone duality above dimension zero:
Axiomatising the algebraic theory of C(X)*, arXiv:1508.07750,
*Advances in Mathematics* 307 (2017), 253-287.

Remark 1.5 on source-PDF page 3 asks whether the opposite of the category of
compact Hausdorff spaces is axiomatisable by a first-order theory.

## Supporting answer

Michael Lieberman, Jiří Rosický, and Sebastien Vasey, *Hilbert spaces and
C*-algebras are not finitely concrete*, arXiv:1908.10200v6,
*Journal of Pure and Applied Algebra* 227(4) (2023), 107245,
<https://doi.org/10.1016/j.jpaa.2022.107245>.

The supporting paper explicitly says in its introduction that its
non-elementarity result answers Marra-Reggio's Question 1.5.  Theorem 22 proves
that commutative unital C*-algebras are not an abstract elementary category.
Using Gelfand duality, Corollary 24 on supporting-PDF page 8 concludes that
`CompHaus^op` is not an abstract elementary category.  Since every category of
models of a first-order theory with all homomorphisms is abstract elementary,
the answer to the source question is **no**.

The supporting theorem is strictly stronger: it rules out not only a
first-order presentation but the broader abstract-elementary framework.

## Files

- `solution_packet.pdf`: compact source-to-answer identification.
- `main.tex`: LaTeX source for the status note.
- `source_paper.pdf`: arXiv:1508.07750.
- `supporting_paper_1908.10200.pdf`: arXiv:1908.10200v6.

## Scope

This is an already-known literature answer, not a new proof produced by the
run.  It settles only the first-order axiomatisability question in Remark 1.5;
the source paper's main infinitary equational axiomatisation is a separate,
positive result.

