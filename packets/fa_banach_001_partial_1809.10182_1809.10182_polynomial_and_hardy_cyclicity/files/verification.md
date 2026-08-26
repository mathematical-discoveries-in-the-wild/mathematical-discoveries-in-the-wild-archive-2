# Verification report

Verdict: candidate substantial partial result, likely valid pending specialist
review.

## Boundary spectrum

For `zeta in T`, the peak polynomials
`q_n(z)=((1+conj(zeta)z)/2)^n` converge pointwise on the closed disk to the
characteristic function of `{zeta}` and are uniformly bounded by one. A bounded
evaluation at `zeta` contradicts dominated convergence if `mu({zeta})=0`. If
the atom is positive, the same convergence is in `L^2(mu)` and puts a
nontrivial characteristic function in `P^2(mu)`, contradicting irreducibility.
Thus there are no boundary bounded point evaluations. The standard adjoint
eigenvector calculation then makes every `S-zeta`, `zeta in T`, have dense
range.

## Interior division

For `a in D`, local uniform boundedness of point evaluations and the maximum
principle give a uniform `P^2(mu)` bound for
`D_a p=(p-p(a))/(z-a)`. The estimate is performed on a small disk around `a`
and its complement. Completion therefore gives
`(S-a)P^2(mu)=ker(ev_a)`. Iterating establishes closedness and the exact jet
description of `rP^2(mu)` for every polynomial `r` with roots in `D`, hence
codimension `deg r`.

## Polynomial factorization and module classification

Exterior polynomial factors are invertible because `||S||<=1`. Boundary
factors have dense range; their commuting product also has dense range.
Applying the closed interior factor shows `[q]=q_D P^2(mu)`, where `q_D`
retains precisely the roots in `D`.

If an invariant `M` contains `q`, then `[q] subset M`, so the quotient is a
submodule of the finite cyclic module `C[z]/(q_D)`. Its preimage is an ideal of
`C[z]`, hence principal; lifting yields `M=dP^2(mu)`. Conversely, a
finite-codimensional `M` contains the minimal polynomial of the induced shift
on `P^2(mu)/M`. This proves all claimed equivalences.

## Hardy-equivalent class

If the boundary density is bounded above and below and the interior part is an
`H^2` Carleson measure, the two norms are equivalent on polynomials. Their
completions are the same topological shift module, so Beurling's theorem gives
cyclicity. For rotationally invariant interior measures, orthogonality of
monomials proves the Carleson estimate directly.

## Literature and scope

Cheap run-index searches found no prior packet for this arXiv id. Bounded exact
question, title, finite-codimension, and polynomial-containing searches on
13 August 2026 found the source and general shift-invariant-subspace literature,
but no later resolution or this exact classification. The classification is
elementary enough that novelty confidence is modest. The unrestricted
infinite-codimensional, polynomial-free case is not claimed.

