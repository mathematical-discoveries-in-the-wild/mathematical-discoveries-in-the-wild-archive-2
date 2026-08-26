# Minimal shift systems produce the requested statistical measure

Source: V. Kadets and D. Seliutin, *Conglomerated filters, statistical
measures, and representations by ultrafilters*, arXiv:2012.02866. The
substantially rebuilt published article is V. Kadets, D. Seliutin, and
J. Tryba, *Conglomerated filters and statistical measures*, JMAA 509
(2022), 125955.

Status: candidate full affirmative solution to preprint Problem 4.6 and
published Problem 4.2, likely valid.

## Result

Let `T` be the shift homeomorphism of `N*`. Choose a minimal nonempty
closed `T`-invariant set `K` and `U in K`. Cesaro orbit averages yield an
invariant probability measure `nu` on `K`; minimality forces
`supp(nu)=K`. Defining

```text
mu(A) = nu(A* intersect K)
```

gives a shift-invariant statistical measure satisfying

```text
F_mu = intersection_{n in Z} (U+n).
```

The shifted ultrafilters are all free and pairwise distinct. This answers
the existence question affirmatively.

## Files

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source PDF.
- `figures/open_question_crop.png`: source Problem 4.6.
- `verification.md`: hypothesis, build, checksum, and visual-QA record.

## Human review recommendation

Check the identification of the source's ultrafilter shift with the
homeomorphism induced on `N*`, the weak-star subnet argument, and the
full-support equivalence `mu(A)=1 iff K subset A*`. The rest is elementary
Stone duality.

