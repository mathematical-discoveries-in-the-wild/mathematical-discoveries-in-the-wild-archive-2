# Corrected Grothendieck rank stabilization

Result type: `counterexamples`

Status: candidate exact statement correction and conditional complexity
counterexample, likely valid, pending expert review.

## Source problem

Shmuel Friedland and Lek-Heng Lim, *Symmetric Grothendieck inequality*,
arXiv:2003.07345, Conjecture 2.18 on page 15.

The conjecture places the real norms in the NP-hard range when
`d(d+1)/2 <= N` and the complex norms there when `d^2 <= N`, with `N=n` for
the symmetric norms and `N=m+n` for the rectangular norm.

## Contribution

The packet proves the exact universal stabilization threshold for the two
symmetric norms:

- real: `rho_R(n) = floor((sqrt(8n+1)-1)/2)`;
- complex: `rho_C(n) = floor(sqrt(n))`.

The proof is self-contained and covers both correlation and subcorrelation
matrices. It also proves sharpness: below those thresholds some Hermitian
matrix has a strict rank-constrained norm gap.

Consequently, the full real band
`d(d+1)/2 <= N < (d+1)(d+2)/2` and complex band
`d^2 <= N < (d+1)^2` are already ordinary SDP computations. The rectangular
claim follows in these bands from the source paper's block-symmetrization
identity. These are infinite uniform families inside all four clauses of the
conjecture.

The unconditional result is polynomial-time SDP computability. Calling this
a counterexample to NP-hardness uses the standard `P != NP` convention. If
the conjecture meant asymptotic hardness separately for each fixed `d`, the
result instead corrects the printed parameter frontier while leaving the
strict large-`n` range open.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Conjecture 2.18 and surrounding source text.
- `verification.md`: proof, scope, and novelty audit.
- `tmp/`: build and rendered-page artifacts used for visual QA.

## Novelty check

A bounded search used the local run indexes and web/arXiv queries for the
exact title, Conjecture 2.18, the stated hardness inequalities, extreme
correlation ranks, and Grothendieck-norm stabilization. It found the classical
rank characterizations of Grone--Pierce--Watkins and Li--Tam, and real
bipartite correlation work of Gribling--de Laat--Laurent, but no explicit
erratum or later correction of this frontier. Because the underlying extreme
rank theorem is classical, novelty confidence is moderate.

## Human review focus

Check the intended uniform-versus-fixed-`d` complexity reading, the converse
argument via symmetrized convex hulls, and whether the result should be
presented as a conjecture counterexample or a statement correction.
