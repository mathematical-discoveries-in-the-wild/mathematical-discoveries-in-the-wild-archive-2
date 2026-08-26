# Literature-implied full answer: balanced monomials violate the ball estimate

status: `literature_implied_answer (full negative answer)`

source: J. Milne Anderson, Michael A. Dritschel, and James Rovnyak,
*Schwarz--Pick inequalities for the Schur--Agler class on the polydisk and
unit ball*, arXiv:math/0702269.

supporting source: Shaoyu Dai, Huaihui Chen, and Yifei Pan,
*The Schwarz--Pick lemma of high order in several variables*,
arXiv:1109.2791.

## Result

For every `d >= 2`,

`F_d(z)=d^(d/2) z_1 ... z_d`

maps the Euclidean unit ball `B_d` into the disk. At the origin its completely
mixed derivative has modulus `d^(d/2)`, whereas estimate (42) of the source
allows only `d^((d-1)/2)`. Thus the estimate fails by the exact factor
`sqrt(d)`. In particular, `F_d` is not in the ball Schur--Agler class, and Open
Problem 2 has a full affirmative answer to its existence question. The smallest
example is `F_2(z_1,z_2)=2z_1z_2`, with `2 > sqrt(2)`.

This is classified as literature-implied rather than new: Dai--Chen--Pan's
Theorem 2 independently gives the sharp coefficient bound on ball Schur
functions and its monomial extremals. That paper does not cite the source open
problem or state this contradiction; the identification with estimate (42) is
the run's contribution.

## Additional explicit tests

The packet also proves two companion facts left explicitly undecided by the
source:

- every homogeneous quadratic Schur polynomial on a polydisk satisfies all of
  the source's polydisk estimates, hence so does the Kaijser--Varopoulos
  polynomial;
- every pure-coordinate higher derivative of an arbitrary ball Schur function
  satisfies both ball estimates, hence every Alpay--Kaptanoğlu polynomial
  singled out by the source satisfies them all.

These companion statements are not needed for the full counterexample.

## Files

- `main.tex` and `solution_packet.pdf`: review note and complete proofs.
- `source_paper.pdf`: arXiv:math/0702269.
- `supporting_paper_1109.2791.pdf`: the later sharp ball coefficient theorem.
- `code/verify_balanced_monomial.py`: exact finite-dimensional arithmetic check.

