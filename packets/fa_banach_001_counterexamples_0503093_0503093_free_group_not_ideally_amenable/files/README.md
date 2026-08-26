# The free group algebra is not ideally amenable

Status: `candidate counterexample likely valid`.

This packet gives a negative answer to Question 4.4 of M. E. Gordji and
T. Yazdanpanah, *Derivations into duals of ideals of Banach algebras*
(arXiv:math/0503093): `ell^1(F_2)` is not ideally amenable.

The witness is the closed two-sided ideal

`I = ker(ell^1(F_2) -> ell^1(Z^2))`

induced by abelianization.  An explicit scalar bounded two-cocycle is placed in
a nonidentity abelianization fiber.  It remains nonzero in `I^perp`, but becomes
a coboundary in the full conjugation module because every nontrivial centralizer
in a free group is cyclic.  The associated connecting one-cocycle gives a
non-inner bounded derivation `ell^1(F_2) -> I^*`.

Files:

- `main.tex` and `solution_packet.pdf`: full counterexample proof.
- `source_paper.pdf` and `source_paper.tex`: source evidence.
- `figures/source_question_page.png`: source page containing Question 4.4.
- `code/verify_split_quasimorphism.py`: exact finite checks of the explicit
  quasimorphism and cocycle identities.
- `verification.md`: mathematical, literature, and packet QA record.

