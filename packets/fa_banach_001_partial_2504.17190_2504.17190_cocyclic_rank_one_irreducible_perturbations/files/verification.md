# Verification record

## Mathematical claim

Let T be bounded. If an outer spectral-boundary point has unit approximate eigenvectors that are cyclic for T*, then for every epsilon there is a rank-one K with trace norm below epsilon such that T+K is irreducible. Consequently the result holds if the cyclic vectors for T* are dense, and dually if the cyclic vectors for T are dense.

## Proof audit checklist

- The selected boundary point belongs to the approximate point spectrum.
- The scalar resolvent coefficient `g(z)=<(T-z)^(-1)xi,xi>` is analytic and nonzero identically on the unbounded resolvent component, so a nearby nonzero value can be chosen.
- For `K=(mu I-T)(xi tensor xi)`, the exact factorization is `S-mu=(T-mu)(I-P)` and `||K||_1=||(T-mu)xi||`.
- `g(mu) != 0` is equivalent to the eigenvector not lying in the range of `S-mu`, excluding a generalized eigenvector at mu.
- Analytic Fredholm theory isolates the new eigenvalue in the resolvent component of T.
- The rank-one Riesz projection yields the orthogonal projection onto the eigenvector inside `W*(S)`.
- Since `K*` has range in the eigenvector line, the T* and S* Krylov flags coincide.
- Rank-one operators between the dense S*-orbit vectors belong to `W*(S)`, forcing `W*(S)=B(H)`.

## Literature/search scope

The run indexes were searched for the arXiv id, title, trace-class irreducible density, cyclic-adjoint, and rank-one perturbation phrases. Targeted arXiv searches found literature on cyclicity of rank-one perturbations and on normed-ideal irreducible perturbations, but no exact statement matching this theorem. Novelty remains unverified beyond that targeted search.

## Upgrade audit

Six focused upgrade routes were checked: factor cyclicity versus one-sided cyclicity; finite cyclic multiplicity; summable countable eigenvalue insertions; trace-class creation of a cyclic adjoint; projection recovery without an eigenvalue; and completion through relative normalizers. Each is recorded in the packet with its precise obstruction. The remaining type-II1 case requires a genuinely new structural input.

## Artifact hashes

- `solution_packet.pdf`: `1e850e9584ec33e027eab9a2f5da1b174e434c79758d344aa79360b95e116f0a`
- `source_paper.pdf`: `9c4c809361bbe9d91c02ef54d4a3d9fc00a60202746aa14542137b9d6276476d`

## Render review

The final packet has three letter-size pages. Every page was rendered at 150 dpi and visually inspected. The theorem statement, factorization, Fredholm-determinant step, Riesz-projection recovery, cyclic-orbit argument, and six-item obstruction audit are legible. No clipping, overlap, malformed formula, blank page, overfull/underfull box, or undefined reference remains.
