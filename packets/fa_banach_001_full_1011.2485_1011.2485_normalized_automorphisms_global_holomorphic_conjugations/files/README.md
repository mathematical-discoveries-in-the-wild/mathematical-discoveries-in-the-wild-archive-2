# Normalized spectral-ball automorphisms are global holomorphic conjugations

Status: `candidate_full_solution_likely_valid_human_review_needed`

Source: Łukasz Kosiński, *Note on the group of automorphisms of the Spectral
Ball*, arXiv:1011.2485, final paragraph and first bullet on PDF page 3.

## Result

For every `n >= 1`, every normalized automorphism `F` of the spectral ball
`Omega_n` has a global holomorphic conjugator:

`F(X) = u(X) X u(X)^{-1}`, with `u:Omega_n -> GL_n(C)` holomorphic.

This affirmatively answers the source's first final problem in every matrix
dimension.  The source's separate second problem—classifying all holomorphic
`u` for which the displayed map is an automorphism—is not claimed here.

## Mechanism

On the cyclic-matrix locus, local conjugators differ by invertible elements of
the centralizer.  The centralizer algebra is the function algebra of the
degree-`n` spectral cover, so the gluing obstruction is a line bundle on that
cover.  The normalized scaling isotopy deforms the automorphism to the
identity and forces this bundle's first Chern class to vanish.  A
codimension-three local-cohomology argument makes the Chern-class map
injective, hence the bundle is holomorphically trivial.  The resulting global
conjugator on cyclic matrices extends across the codimension-three derogatory
locus by Hartogs; purity of zero sets keeps its determinant nonzero.

## Files

- `solution_packet.pdf`: full theorem, proof, evidence, novelty audit, and
  reviewer checklist.
- `source_paper.pdf`: arXiv:1011.2485.
- `figures/open_problem_crop.png`: source PDF page 3 containing both problems.
- `verification.md`: structural stress tests and build/QA record.
- Attempt note:
  `runs/fa_banach_001/attempts/1011.2485_global_holomorphic_conjugator.md`.

Human review should focus on the codimension-three local-cohomology vanishing
and the parametric obstruction line bundle along the scaling isotopy.
