# Conjecture 3 follows from unitary equivalence of left-definite operators

Status: `literature_implied_answer`

This is an identification of an earlier theorem's consequence, not a new
theorem proved by this run.

## Source conjecture

Dale Frymark and Constanze Liaw, *Perspectives on General Left-Definite
Theory*, arXiv:2012.01014, Conjecture 3 on arXiv PDF page 10.

For a semibounded self-adjoint operator `A`, the conjecture says that an
eigenvalue `lambda` of multiplicity `m` remains an eigenvalue of multiplicity
`m` for every left-definite operator `A_r` acting in the left-definite Hilbert
space `H_r`.

## Earlier theorem implying the answer

Lance L. Littlejohn and Richard Wellman, *On the Spectra of Left-Definite
Operators*, *Complex Analysis and Operator Theory* 7 (2013), 437--455,
doi:10.1007/s11785-011-0178-6.

Theorem 6.2(iii), PDF page 11, states that `A`, `A_r`, and `A_s` are unitarily
equivalent. In particular, the unitary `U_r=A^{r/2}:H_r -> H` satisfies
`U_r A_r U_r^{-1}=A`. Therefore

```text
U_r(ker(A_r - lambda I)) = ker(A - lambda I).
```

The eigenspaces are linearly isomorphic and have the same dimension. This is
exactly Conjecture 3 (in the positive normalization used by left-definite
theory; the usual scalar shift handles a merely semibounded operator).

## Why the status is implied rather than explicit

The supporting theorem predates arXiv:2012.01014 and cannot name its
Conjecture 3. The source paper cites Littlejohn--Wellman for spectral stability
but does not draw the multiplicity consequence. The match is therefore a
direct agent-identified implication from a cited theorem.

## Scope

This fully settles Conjecture 3 as stated. It does not address the source's
stronger informal question about interlacing of eigenvalues belonging to two
different self-adjoint extensions after applying left-definite theory.

Files:

- `source_paper.pdf`: arXiv:2012.01014.
- `supporting_paper_littlejohn_wellman_2013.pdf`: decisive theorem source.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.
