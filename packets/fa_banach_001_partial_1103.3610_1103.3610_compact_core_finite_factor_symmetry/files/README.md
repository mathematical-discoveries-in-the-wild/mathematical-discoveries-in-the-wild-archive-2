# Spectral invariance on the compact core and a nonabelian full subcase

Result type: partial.

Status: candidate substantial partial result, likely valid pending expert
review.

Source paper:

- Yulia Kuznetsova and Carine Molitor-Braun, “Harmonic analysis of weighted
  Lp-algebras,” arXiv:1103.3610; Expositiones Mathematicae 30 (2012),
  124--153, DOI 10.1016/j.exmath.2012.01.002.
- Conjecture location: source PDF page 12, immediately after Theorem 3.9.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

Let G be a compactly generated locally compact group of polynomial growth,
let 1<p<infinity, and suppose (G,omega) satisfies (LPAlg) and condition (S).
Writing A=Lp(G,omega), the packet proves:

1. For every compactly supported f in A,
   r_A(f)=r_{L1(G)}(f). If f is self-adjoint, its complete spectrum in A
   equals its L1(G) spectrum and is real. Thus the standard dense compact core
   is spectrally invariant on self-adjoint elements.
2. If G is discrete, the radius equality extends to every central element of
   A, and central self-adjoint elements have the same real spectrum as in
   L1(G).
3. The source conjecture has a full affirmative answer for G=H x F whenever
   H is abelian and F is finite. This is genuinely nonabelian when F is; for
   example it covers R x S_3 with every weight satisfying (LPAlg) and (S),
   not only Pytlik-polynomial weights.

The compact-core theorem follows from support growth, unweighted Young's
inequality, and condition (S). The finite-factor theorem reduces the algebra,
up to an equivalent norm, to a finite direct sum of matrix algebras over the
abelian weighted Lp algebra.

## Why this is not labeled full

The general completion step remains open. Hulanicki's transfer lemma requires
spectral-radius equality for every element, whereas compact truncations need
not preserve spectral radius in a noncommutative Banach algebra. The weighted
L1 annular proof also needs a weighted first moment not supplied by the
weighted p-moment in (LPAlg). Eight focused attempts and the exact obstruction
are recorded in the linked attempt note.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `supporting_fgl_2006.pdf`: supporting weighted-L1/Hulanicki reference.
- `figures/open_problem_crop.png`: source conjecture and preceding theorem.
- `verification.md`: proof audit and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

On August 11, 2026, the cheap run indexes and bounded exact-title,
exact-conjecture, author, GRS, condition-(S), and weighted-Lp web searches
found no later solution of the general conjecture and no statement of the
finite-direct-factor subcase. The search found the source, the weighted-L1
theorem of Fendler--Grochenig--Leinert, a 2018 habilitation reference, and
later citing papers. Novelty confidence is moderate pending a specialist
citation search.

## Human review focus

Review should check the polynomial-separation step in the compact-core
spectrum theorem, the restriction of (LPAlg) from H x F to H, and the
finite-dimensional tensor/matrix decomposition. The general conjecture is
explicitly not claimed.

