# Counterexample packet: Haar-countable sets are not always an ideal

Status: candidate full counterexample, likely valid, needs human review.

Source target: Adam Kwela, *Haar-smallest sets*, arXiv:1711.09753,
Question 7.5.

Result: in the abelian Polish group `R^omega` there are two closed Haar-1
sets whose union is not Haar-countable.  Consequently, Haar-countable sets do
not form an ideal in the unrestricted class of abelian Polish groups.

Mechanism: split `R^omega = Y x Z` into even and odd coordinates.  Apply the
universal closed-set theorem of Banakh--Glab--Jablonska--Swaczyna separately
to the Borel families of compacta on which the `Y`- and `Z`-coordinate
projections are injective.  The theorem's localization clause makes the two
resulting closed sets Haar-1.  Lusin--Novikov uniformization and the perfect
set theorem show that every Cantor set contains a Cantor subset belonging to
one of the two families.  The universal absorption clause then puts a
translate of that subset into one of the closed sets, defeating every
possible Haar-countable witness for their union.

Scope: this is a full negative answer to the formulation over arbitrary
abelian Polish groups.  It does not settle a stricter interpretation confined
to the real line or to locally compact groups.

Files:

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:1711.09753.
- `supporting_paper_1803.06712.pdf`: local copy of the universal-theorem source.
- `figures/open_problem_crop.png`: source crop containing Question 7.5.

Novelty check: bounded searches by exact question, title, arXiv identifier,
authors, and close keywords found no later explicit answer.  The current arXiv
abstract contains a sentence saying that Haar-countable sets do not form an
ideal, but the current TeX/PDF and the published paper still pose Question
7.5; the packet treats that sentence as a metadata inconsistency, not a proof.

Review recommendation: check the Borel hyperspace lemma, both uses of the
universal theorem, the Lusin--Novikov dichotomy, and whether Question 7.5 was
intended only for `R`.  Also note the packet's compatibility discussion of
Theorem 2.3 in the source paper.
