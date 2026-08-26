# Diffeological regularity and Frobenius question answered by arXiv:1607.02636v3

Status: `literature_already_answered (regularity/Frobenius question)`

## Source question

Jean-Pierre Magnot, *On the domain of implicit functions in a projective
limit setting without additional norm estimates*, arXiv:1710.11076,
published in *Demonstratio Mathematica* 53 (2020), 112--120.

On arXiv PDF page 6, Section 2.2 observes that the constructed domain
`D_infinity` need not be open, so the classical derivative `D_1 J` needed in
the Banach-space proof of Frobenius is unavailable.  It asks which generalized
notion of differentiation is best adapted to this setting.  The abstract and
introduction formulate the same issue as the paper's main open question.

## Explicit later answer

The same author's separate paper *On the differential geometry of numerical
schemes and weak solutions of functional equations*, arXiv:1607.02636v3,
*Nonlinearity* 33 (2020), 6835--6867, DOI
10.1088/1361-6544/abaa9f, answers the question using Cauchy diffeology and the
subset diffeology.

Although the answering arXiv identifier is numerically older, the decisive
version is v3, revised on 12 August 2020 after arXiv:1710.11076 and accepted
for publication in *Nonlinearity*.  On PDF page 20 it explicitly says that
the earlier paper left regularity open and that the new paper fills the gap.
Theorem 4.2 (PDF page 21) finds a domain `D` between the Banach unit ball and
the earlier domain on which the implicit map is smooth for the subset
diffeology.  Theorem 4.3 (PDF pages 22--23) then proves the corresponding
diffeological Frobenius theorem.

This completely answers the regularity/Frobenius signal.  It does not answer
the separate final question in arXiv:1710.11076 asking for the structure of
`G L_infinity / GL(B)`; that question is qualitative and depends on the
chosen ILH scale.

Files:

- `source_paper.pdf`: arXiv:1710.11076.
- `supporting_paper_1607.02636.pdf`: arXiv:1607.02636v3.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

