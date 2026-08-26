# 0907.0986 — Segal-module projectivity forces compactness

Status: candidate full result, likely valid, human review needed.

Model: GPT5.6.

Source: Brian E. Forrest, Hun Hee Lee, and Ebrahim Samei, *Projectivity of modules over Segal algebras*, arXiv:0907.0986, introduction on source PDF page 2.

## Result

The source's open converse has a positive answer. For either

    S = S^1 A(G)  or  S = S_0(G),

the Fourier algebra `A(G)` is operator projective as a left `S`-module if and only if `G` is compact.

The new direction is elementary once the correct range norm is retained. An operator Segal algebra `S` is an essential ideal in `A=A(G)`, so `A` is an essential `S`-module. Projectivity therefore supplies a splitting

    rho : A -> S operator-projective-tensor A

of multiplication. But multiplication on `S tensor A` is bounded with values in `S`, not merely in `A`. Hence multiplying `rho(a)` shows that every `a in A` actually belongs to `S`, with a uniform `S`-norm bound. Thus `A=S`.

Both `S^1A(G)` and `S_0(G)` embed continuously into `L^1(G)`, so this gives a continuous inclusion `A(G) -> L^1(G)`. A self-contained translate argument proves that this is impossible for noncompact `G`: choose a nonzero compactly supported coefficient `u` of the left regular representation and `n` disjoint translates. Their `L^1` norm is linear in `n`, while their Fourier-algebra norm is at most of order `sqrt(n)` because the translated coefficient vectors are orthogonal.

The compact-to-projective implication was already established in the source.

## Files

- `main.tex`: theorem, proof intuition, full proof, scope, and novelty audit.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: PDF reconstructed locally from the official arXiv source archive.
- `figures/open_problem_crop.png`: readable crop of source PDF page 2.
- `code/crop_source.py`: reproducible source-crop script.

## Human review recommendation

Review as a likely valid full positive solution. The highest-value check is the essential-module passage: essentiality of `S` as an `A`-module and density of `S` in `A` imply density of `SA` in `A`, so the non-unitized projectivity criterion applies. After that, the range argument and the translate obstruction are direct.
