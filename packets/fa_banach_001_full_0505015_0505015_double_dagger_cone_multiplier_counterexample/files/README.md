# Double-dagger norm counterexample

Source: arXiv:math/0505015, Baladi--Tsujii, Appendix A.

## Result

The proposed double-dagger norm is not equivalent in general to the
Baladi--Tsujii anisotropic Sobolev norm.

For every compact K in R^3 with nonempty interior and every
1<t<infinity, t different from 2, there are a valid cone combination Theta
and numbers q<0<p (with p-q arbitrarily small) such that

    ||P(D)u||_t + ||Q(D)u||_t

cannot be bounded by a constant times

    ||(P(D)+Q(D))u||_t

on C_c^\infty(K).  Since the paper proves the first expression equivalent
to its original anisotropic Sobolev norm, this answers its question
negatively.

For t=2 the two norms are equivalent by Plancherel.

## Mechanism

Choose the zero set of the positive angular cutoff to be a circular cone.
At high frequency the quotient P/(P+Q) converges to the characteristic
function of the complement of that cone.  A fixed-support rescaling and
truncation argument would make this cone projection a local L^t multiplier
if the norms were equivalent.  Its affine slice is the complement of a
disk, contradicting de Leeuw restriction and Fefferman's ball-multiplier
theorem for t different from 2.

## Files

- main.tex: complete proof packet
- solution_packet.pdf: compiled packet
- verification.md: proof and artifact audit
- source_paper.pdf: official arXiv PDF
- figures/source_question.png: exact Appendix A question, rendered from page 19
- supporting/: reserved for supporting primary papers

