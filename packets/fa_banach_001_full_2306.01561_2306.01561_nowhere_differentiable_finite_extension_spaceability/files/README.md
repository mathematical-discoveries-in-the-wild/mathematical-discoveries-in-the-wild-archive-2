# Finite prescribed subspaces extend to closed continuum-dimensional ND spaces

**Status:** candidate full proof, likely valid, requiring human review.

**Source:** G. Araújo, A. Barbosa, A. Baganha Raposo Jr., and G. Ribeiro,
*Complements of unions: insights on spaceability and applications*,
arXiv:2306.01561; *Mathematika* 71 (2025), e70006. The target passage is on
PDF page 4.

The source asks whether the continuous nowhere-differentiable real functions
on `[0,1]` are `(1,c)`-spaceable: must every prescribed one-dimensional
nowhere-differentiable subspace lie in a closed continuum-dimensional subspace
whose nonzero functions are all nowhere differentiable?

The packet proves more. For every finite positive integer `n`, every
`n`-dimensional subspace `E` whose nonzero members are nowhere differentiable
is contained in such a closed continuum-dimensional subspace.

The mechanism combines the common modulus of continuity of the compact unit
ball of `E` with Hencl's quantitative Cantor-space embedding. Hencl's range is
chosen to oscillate faster than that common modulus, so adding any fixed
member of `E` cannot cancel the range's small-scale oscillations. The direct
sum of the closed Hencl range and `E` is then the required extension.

Files:

- `solution_packet.pdf` — theorem, proof, verification scope, and novelty audit
- `source_paper.pdf` — arXiv:2306.01561v2
- `figures/open_problem_crop.png` — complete source question on PDF page 4
- `verification.md` — adversarial checks of every load-bearing step
- `code/make_open_problem_crop.py` — reproducible source crop

**Human-review focus:** check the precise quantifiers in Hencl Proposition 2,
the common-modulus lemma, the two limiting scale comparisons, and whether any
non-indexed literature already combines Hencl's proposition with prescribed
finite-dimensional perturbations. A July 2026 preprint proves only the weaker
`(n,aleph_0)` algebraic extension result.
