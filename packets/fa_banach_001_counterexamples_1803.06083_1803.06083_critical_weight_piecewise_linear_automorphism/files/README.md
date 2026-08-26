# Critical-weight piecewise-linear automorphism

**Status:** claimed full negative resolution / counterexample; likely valid,
pending human review.

**Source:** Yulia Kuznetsova and Safoura Zadeh, *On isomorphisms between
weighted $L^p$-algebras*, Canadian Mathematical Bulletin 64 (2021), no. 4,
853--866, arXiv:1803.06083, DOI 10.4153/S0008439520000880.

On published page 864, immediately after the polynomial-weight rigidity
corollary, the authors write: “For $a=1$ and $p>1$, the question is open.”
The question is whether the preceding canonical classification persists for
the critical weight

\[
\omega_1(n)=\max(1,|n|).
\]

The packet gives a negative answer for every $1<p<\infty$.  On
$\mathbb T=\mathbb R/\mathbb Z$, let the lift of a circle homeomorphism be

\[
\Phi(x)=
\begin{cases}
2x,&0\le x\le 1/3,\\
(x+1)/2,&1/3\le x\le1.
\end{cases}
\]

Composition by the induced non-affine circle homeomorphism is a bounded
invertible operator on the Fourier image of
$\ell^p(\mathbb Z,\omega_1)$, hence conjugates back to a noncanonical algebra
automorphism of the convolution algebra.

The proof is not based on numerical evidence.  Its key lemma says that a
rational affine change localized to an interval is bounded on
$\mathcal F L^p(\mathbb T)$.  Splitting input frequencies into residue classes
reduces the operator to sparse reindexings followed by multiplication by
bounded-variation functions; the latter are controlled by the discrete
Hilbert transform.  The first-order weighted norm is then controlled by the
distributional derivative, branch by branch.  The inverse lift is again
rational piecewise affine.

Files:

- `solution_packet.pdf`: expert-facing statement and proof.
- `source_paper.pdf`: published source paper.
- `figures/open_problem_crop.png`: source statement on published page 864.
- `code/numerical_smoke_test.py`: optional finite Fourier sanity check; not
  used as proof.

Novelty check (bounded, 2026-08-09): the run registry and solution/attempt/gap
indexes were searched by arXiv id, title, and core terms; exact-phrase web
searches for the open sentence, DOI/title searches, author-plus-critical-case
searches, and searches combining piecewise-linear changes with weighted
Fourier--Lebesgue spaces found the source paper and general change-of-variable
literature, but no later resolution of this exact question.  This supports,
but does not certify, novelty.

**Human-review focus:** verify the bounded-variation multiplier lemma on
$\mathcal F L^p$, the residue-class formula for rational slopes, and the
density/continuity passage from trigonometric polynomials to the weighted
algebra.

