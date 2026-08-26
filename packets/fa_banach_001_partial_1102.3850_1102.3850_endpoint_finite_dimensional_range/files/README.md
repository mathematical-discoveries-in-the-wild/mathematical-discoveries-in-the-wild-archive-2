# Partial Solution Packet: Critical-Degree Endpoint for Finite-Dimensional Ranges

- status: candidate partial result, likely valid
- run: fa_banach_001
- model: GPT5.6
- agent: agent_lane_17
- source arXiv id: 1102.3850
- source paper: Verónica Dimant and Silvia Lassalle, *M-structures in vector-valued polynomial spaces*
- target passage: source PDF page 22, immediately before Corollary 4.9

## Result

Let \(E\) be a Banach space whose critical degree \(n=cd(E)\) exists,
and let \(F\ne\{0\}\) be finite-dimensional. If
\(\mathcal K(E)\) is an \(M\)-ideal in \(\mathcal L(E)\), then
\(\mathcal P_w(^nE,F)\) is an \(M\)-ideal in \(\mathcal P(^nE,F)\).

Moreover \(cd(E,F)=cd(E)\). Thus the endpoint left open after Corollary
4.9 has an affirmative answer for every finite-dimensional range \(F\).
The source required \(n=cd(E,F)<cd(E)\); here equality holds.

## Proof Mechanism

The scalar paper arXiv:1005.1260 proves that property \((M)\) of \(E\)
implies scalar \(n\)-polynomial property \((M)\) at \(n=cd(E)\).
Finite dimensionality lets us lift this scalar inequality to \(F\)-valued
polynomials: along a subnet realizing a limsup, choose norming functionals
\(f_\alpha\in S_{F^*}\). A further subnet converges in norm to one
\(f\in S_{F^*}\), and the vector norm reduces without error to the scalar
polynomial \(f\circ P\). The source paper's Theorem 4.7 then yields the
\(M\)-ideal conclusion.

## Scope

This is a solved endpoint subcase, not a solution for arbitrary property-\((M)\)
ranges. The upgrade attempt to infinite-dimensional \(F\) stops because
weak-star convergence of norming functionals does not control the diagonal
term \((f_\alpha-f)(P(x_\alpha))\).

At the critical degree \(P(x_\alpha)\) need not be weakly null, so property
\((M)\) of \(F\) does not remove that obstruction. The source already covers
important infinite-dimensional targets such as \(M_\infty\)-spaces under
additional hypotheses.

## Files

- main.tex: exact statement, proof, limitations, and references
- solution_packet.pdf: rendered review packet
- source_paper.pdf: local copy of arXiv:1102.3850
- figures/open_problem_crop.png: page-22 crop of the open endpoint
- verification.md: independent dependency and edge-case audit

## Novelty Check

The run indexes were searched for arXiv id 1102.3850, its title,
n-polynomial property (M), cd(E,F)=cd(E), and finite-dimensional ranges.
No exact packet was found.

Bounded external searches on 2026-08-11 used the exact phrases
"finite-dimensional" "n-polynomial property (M)",
"finite dimensional" "M-ideal" "vector-valued polynomials", and
"cd(E,F)=cd(E)" finite dimensional F. They found the source, its
published version, the scalar predecessor arXiv:1005.1260, and the later
related paper arXiv:1512.08741, but no statement of this endpoint theorem.
This is evidence rather than a guarantee of novelty.

## Human Review Focus

Check the subnet argument for arbitrary directed nets and the two literature
dependencies: scalar Proposition 3.10 in arXiv:1005.1260 and vector-valued
Theorem 4.7 in arXiv:1102.3850. No computation is used.
