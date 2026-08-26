# Two positive regimes for uniform IDS approximation

Status: **candidate partial results; likely valid; human review requested**

Source: Felix Pogorzelski, *Convergence theorems for graph sequences*,
arXiv:1304.0945, Section 6.2, page 12.

## Results

Let `(G_n)` be any weakly convergent finite graph sequence of uniformly
bounded degree, and let `(H_n)` be a fixed-range, pattern-invariant,
selfadjoint operator sequence in the sense of the source paper. The packet
proves two coefficient regimes.

1. **Algebraic coefficients.** If every local kernel value is a real
   algebraic number, then

   ```text
   nu_n({lambda}) -> nu({lambda})  for every real lambda.
   ```

   Consequently, the spectral distribution functions converge uniformly.

2. **Arbitrary coefficients with finite limiting spectrum.** With no
   arithmetic restriction on the complex local kernel values, the same
   conclusions hold whenever the weak limit `nu` has finite support.

The packet also proves that, for any uniformly sparse family whose entries
come from a fixed finite complex alphabet, eigenvalues with normalized
multiplicity at least `epsilon` belong to a finite set depending only on the
alphabet, sparsity bound, and `epsilon`. Therefore a counterexample to the
remaining arbitrary-coefficient problem cannot use a moving macroscopic
eigenvalue. It must instead have an infinite-support limiting IDS and a
diffuse cloud of increasingly small eigenspaces coalescing at the failed
atom.

## Proof mechanisms

For algebraic coefficients, one global scaling puts the alphabet in the ring
of integers of a finite Galois number field. The field norm of a generalized
discriminant supplies the anti-clustering bound used in the
Abért--Thom--Virág argument. A high normalized multiplicity also bounds the
degree of the eigenvalue over the coefficient field; bounded absolute
conjugates then leave only finitely many possible large atoms.

For a finite-support limit `{x_1,...,x_m}`, set
`p(t) = product_j (t-x_j)`. Moment convergence gives
`||p(H_n)||_HS^2 = o(|V(G_n)|)`. The matrices `p(H_n)` are still local, and
their entries range over one fixed finite set, so every nonzero row has a
uniformly positive Hilbert--Schmidt contribution. Hence
`rank p(H_n) = o(|V(G_n)|)`, and almost the whole finite-volume spectrum lies
exactly in `{x_1,...,x_m}`.

The macroscopic-eigenvalue obstruction reduces a sparse finite-alphabet
matrix to a fixed element of a free group algebra: edge-colour its bipartite
support into partial permutations, express each partial permutation as the
average of two signed permutations, and pass to the ordinary permutation
double cover. Jaikin-Zapirain's strict eigenvalue theorem then applies.

## Novelty and current boundary

The exact all-weakly-convergent-graph-sequences statements were not located
in a bounded search, so originality is **provisional**. Andreas Thom's
arXiv:math/0701294 contains the algebraic-coefficient analogue for sofic group
approximations. Jaikin-Zapirain proves arbitrary-coefficient deterministic
sofic group approximation and the strict eigenvalue theorem used here. The
March 2026 preprint arXiv:2603.01610 explicitly says that fixed arbitrary real
or complex values remain open in its random/general setting and that it is
unknown whether Jaikin-Zapirain's techniques extend there.

Thus the general infinite-spectrum transcendental case is not settled. A
direct attempt to transplant the base-change proof reaches the missing
group/groupoid symmetry identified in that 2026 paper; the separate attempt
note records this barrier precisely.

## Verification report

Verdict: **likely valid**.

No computational experiment is used as proof evidence. Recommended human
review should focus on:

1. the generalized discriminant's membership in the number-field ring of
   integers;
2. the fixed finite entry alphabet for `p(H_n)`;
3. the reduction from partial permutations to one fixed free-group element
   and its signed-permutation double cover.

## Files

- `solution_packet.pdf`: complete review packet
- `main.tex`: proof source
- `source_paper.pdf`: original source paper
- `supporting_paper_jaikin_2019.pdf`: strict-eigenvalue and deterministic
  arbitrary-coefficient comparison source
- `figures/open_problem_crop.png`: source page 12
- `../../../attempts/1304.0945_arbitrary_coefficient_upgrade_barrier.md`:
  full-upgrade attempt and exact remaining obstruction
