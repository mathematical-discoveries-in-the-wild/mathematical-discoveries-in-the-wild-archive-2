# Wolff reiteration for compatible complemented lattice dilations

**Status:** candidate substantial partial result, likely valid.

**Source:** Moritz Egert and Benjamin W. Kosmala, *A Note on Complex
Interpolation of Quasi-Banach Function Spaces*, arXiv:2412.12769, Remark 1.3
on source PDF page 2.

The source asks for its Wolff-reiteration theorem beyond quasi-Banach function
spaces, for general A-convex quasi-Banach spaces. This packet proves the full
conclusion for possibly non-lattice spaces that occur as the ranges of one
compatible bounded projection on a function-space quadruple, provided the
complementary quadruple has the same two local interpolation identities. A
stationary complement makes that extra condition automatic.

## Main result

For parameters

`0 < theta < eta < 1`, `theta = lambda eta`, and
`eta = (1-mu)theta + mu`, write

`Y_j = X_j direct_sum W_j`

using a common bounded projection on four A-convex quasi-Banach function
spaces. If

`X_1=[X_0,X_2]_lambda`, `X_2=[X_1,X_3]_mu`

and the analogous two identities hold for the `W_j`, then

`X_1=[X_0,X_3]_theta`, `X_2=[X_0,X_3]_eta`.

The proof lifts the local identities through the direct-sum decomposition,
applies the source theorem upstairs, and projects the global identities back.

## Contents

- `solution_packet.pdf`: theorem, proof, obstruction analysis, and review notes.
- `main.tex`: packet source.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: Theorem 1.2 and Remark 1.3 from the source.
- `verification.md`: proof and literature audit.
- `tmp/`: LaTeX and render intermediates.

## Scope

This is a proper abstract extension because a complemented range of a function
lattice need not be an order ideal or admit a compatible lattice structure.
It does not prove Wolff reiteration for every A-convex quadruple. Eight focused
upgrade attempts all ultimately meet the missing reverse-reiteration / outer-
versus-inner complex-method problem.

## Human-review recommendation

Verify compatibility of the common projection and the complement identities
in any proposed application. The direct-sum interpolation argument is then
formal. A full upgrade requires a genuinely new outer complex
reverse-reiteration theorem or a counterexample.

