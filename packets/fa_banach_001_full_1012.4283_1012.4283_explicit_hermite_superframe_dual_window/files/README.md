# Explicit dual window for Hermite Gabor superframes

Status: `candidate_full_solution_likely_valid`

Source: Luis Daniel Abreu, *Banach Gabor frames with Hermite functions:
polyanalytic spaces from the Heisenberg group*, arXiv:1012.4283.

Supporting source: Karlheinz Gröchenig and Yurii Lyubarskii, *Gabor
(Super)Frames with Hermite Functions*, arXiv:0804.4613.

## Result

The source says that the reconstruction obtained from the Hermite
superframe is not explicit because the dual vectorial window is not known
explicitly. For every lattice in the sharp superframe range
`s(Lambda) < 1/(n+1)`, this packet gives a closed formula for such a dual
window.

Let `N=n+1`, let `Omega` be the conjugate adjoint lattice, put
`S=sigma_Omega^N`, and remove the zero at the origin by setting
`q(z)=S(z)/z^N`. If `[a]_r` denotes the degree-`r` Taylor truncation at zero,
then the ordinary Bargmann transforms of the dual components are

```text
G_j(z) = s(Lambda) sqrt(pi^j j!) (z^j/j!) q(z) [1/q]_{N-1-j}(z),
0 <= j < N.
```

The truncation identity gives exactly the required cardinal jets at zero;
the sigma factor gives zeros of order `N` at every other adjoint-lattice
point. The full matrix Wexler–Raz identities follow, including all
off-diagonal component conditions. The density inequality implies every
component lies in the Feichtinger algebra `M^1`, hence the formula supplies
Hilbert and Banach superframe reconstructions and an explicit polyanalytic
sampling kernel.

## Scope and novelty caveat

The supporting 2009 paper already reduces the construction to a finite
triangular system and states that its coefficients have a unique solution.
The contribution here is the closed inverse-Taylor formula solving that
system and the resulting explicit superframe kernel. It is not claimed to
be the canonical dual window.

A bounded local full-source search and arXiv API searches for `dual vectorial
window`, `Hermite superframes explicit dual`, and related multi-window terms
found the two source papers but no later closed formula. Novelty remains
provisional pending specialist review.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: LaTeX source.
- `verification.md`: proof, normalization, literature, and rendering checks.
- `source_paper.pdf`: arXiv:1012.4283.
- `supporting_paper_0804.4613.pdf`: the superframe/Wexler–Raz source.
- `source_material/`: inspected TeX copies.
- `figures/open_problem_crop.png`: real crop of page 15 of the source PDF.

