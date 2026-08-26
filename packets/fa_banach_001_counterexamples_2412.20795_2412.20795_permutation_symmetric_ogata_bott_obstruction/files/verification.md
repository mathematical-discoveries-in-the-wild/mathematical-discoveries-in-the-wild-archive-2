# Verification notes

## Claim checked

For the norm-one-half Pauli matrices `s_i`, let `H_{i,N}=T_N(s_i)` on
`(C^2)^(tensor N)`.  If self-adjoint matrices `Y_{1,N},Y_{2,N},Y_{3,N}`
commute pairwise and are fixed under conjugation by the tensor-factor
permutation unitaries for `(1 2)` and `(1 2 ... N)`, then

    max_i ||Y_{i,N}-H_{i,N}|| >= 1/6.

## Formal proof audit

1. The two permutations generate `S_N` for `N>=2`.
2. Fixedness under their conjugations is equivalent to commuting with their
   implementing unitaries; hence each `Y_i` commutes with every permutation
   unitary and with their average `P_N`.
3. `P_N` is the orthogonal projection onto `Sym^N(C^2)`.  Compression therefore
   preserves self-adjointness, pairwise commutativity, and does not increase
   the approximation error.
4. On `Sym^N(C^2)`, `H_i` is `J_i/N` in the spin `j=N/2` representation.
5. The packet computes the localizer spectrum directly in the `J_z` basis:
   `1/2` has multiplicity `N+2`, and `-(1/2+1/N)` has multiplicity `N`.
   Thus its gap about zero is exactly `1/2`.
6. Simultaneous diagonalization of a commuting self-adjoint triple makes its
   Pauli localizer a direct sum of blocks `z dot tau`, each with eigenvalues
   `+|z|,-|z|`.  If invertible, its inertia is balanced.
7. The perturbation estimate is
   `||sum_i (Z_i-X_i) tensor tau_i|| <= 3 max_i||Z_i-X_i||`.
   Error strictly below `1/6` preserves invertibility and inertia, giving a
   contradiction.  Ruling out strict inequality proves the stated weak lower
   bound.

No external stability theorem is needed.  The argument is valid over complex
matrices, as in the source.

## Computational check

Executed:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/2412.20795_permutation_symmetric_ogata_bott_obstruction/code/verify_localizer.py

For every `1 <= N <= 24`, the script checked to numerical tolerance below
`3e-16`:

- the predicted two-point localizer spectrum and multiplicities;
- the spectral gap `1/2`;
- the spin commutator relations;
- the Casimir identity `sum_i (J_i/N)^2=(1/4+1/(2N))I`.

The computation is corroborative only; the packet contains an exact proof.

## Bounded novelty and literature audit (2026-08-11)

Searched the run's registry/results/attempt indexes for arXiv:2412.20795 and
the core phrases `Ogata symmetry`, `tensor permutation`, `Schur-Weyl`, `spin
triple`, `Bott index`, and `localizer`; no duplicate was present.

External bounds:

- OpenAlex record `W4405957111` for arXiv:2412.20795 reported zero citing works.
- Web/arXiv exact-phrase searches for `symmetry version of Ogata's theorem` and
  `How much symmetry that is preserved` found no later answer.
- Close-variant searches combining permutation invariance, symmetric tensor
  powers, spin matrices, commuting approximation, Bott index, and localizer
  found general Bott/localizer literature, but no application to this source
  question.
- The source paper, Ogata's theorem (arXiv:1111.5933), Herrera's constructive
  qubit proof (arXiv:2212.06012), Hastings--Loring (arXiv:0910.5490), and
  Loring's localizer guide (arXiv:1907.11791) were checked for the relevant
  formulation.  None states this simultaneous permutation-symmetry
  counterexample.

Novelty confidence is moderate-to-high under this bounded audit, not a claim
of exhaustive bibliographic priority.

## Visual and build verification

The source-question crop was rendered from PDF page 15 and inspected.  The
packet was built with `latexmk`, checked for LaTeX warnings/overfull boxes, and
all rendered pages were visually inspected.  Build intermediates and rendered
QA pages are kept under `tmp/`.

## Human-review recommendation

Prioritize review.  The proof is short, quantitative, and self-contained.  The
main interpretive issue is scope: it disproves simultaneous preservation of
the two tensor-permutation generators, not preservation of a single fixed
permutation or every unrelated symmetry pattern.
