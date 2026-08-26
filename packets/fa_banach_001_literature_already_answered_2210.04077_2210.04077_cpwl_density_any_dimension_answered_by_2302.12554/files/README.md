# 2210.04077 — arbitrary-dimensional CPWL density answered by 2302.12554

Status: literature_already_answered (full intended conjecture, affirmative in
the natural `L^1` topology).

Model: GPT5.6.

Source: Luigi Ambrosio, Shayan Aziznejad, Camillo Brena, and Michael Unser,
*Linear Inverse Problems with Hessian-Schatten Total Variation*,
arXiv:2210.04077; published in *Calculus of Variations and Partial
Differential Equations* 63, article 9 (2024), DOI
10.1007/s00526-023-02611-6. Conjecture 1 appears on source PDF page 14.

Supporting answer: Luigi Ambrosio, Camillo Brena, and Sergio Conti,
*Functions with Bounded Hessian-Schatten Variation: Density, Variational, and
Extremality Properties*, arXiv:2302.12554; published in *Archive for Rational
Mechanics and Analysis* 247, article 111 (2023), DOI
10.1007/s00205-023-01938-w. Theorem 2.4 appears on supporting PDF page 14.

## Identification

The source's published Conjecture 1 asks whether its two-dimensional CPWL
density-in-energy theorem extends to every hypercube `(0,1)^d`, replacing the
two-dimensional `L^infty` topology by `L^1` in higher dimension. The arXiv v1
wording is terser and omits that topology clarification.

The supporting paper explicitly says that Theorem 2.4 gives a positive answer
to that conjecture. It proves, for every `d`, that each function of bounded
Hessian–Schatten variation on `(0,1)^d` admits CPWL approximants converging in
`L^1`, with convergence of the Schatten-1 Hessian energies. The source authors
also acknowledge the announced proof in their conjecture footnote.

## Scope

This is a full answer to the intended, published `L^1` conjecture. It is not a
claim of `L^infty` approximation for arbitrary dimension; the source's
dimension-two theorem remains stronger in its function topology.

## Files

- `main.tex`: compact theorem correspondence and scope note.
- `solution_packet.pdf`: rendered literature-status packet.
- `source_paper.pdf`: locally rebuilt arXiv:2210.04077 source PDF.
- `supporting_paper_2302.12554.pdf`: locally rebuilt arXiv:2302.12554 PDF.
- `verification.md`: build, hash, and visual-inspection record.

