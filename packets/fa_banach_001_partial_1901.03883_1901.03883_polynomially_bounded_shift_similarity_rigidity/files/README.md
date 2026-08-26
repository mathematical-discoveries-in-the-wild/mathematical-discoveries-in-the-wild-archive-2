# Polynomially bounded shift-similarity rigidity

Status: `candidate substantial partial result; likely valid; human review requested`

Source: Maria F. Gamal', *On power bounded operators with holomorphic eigenvectors, II*, arXiv:1901.03883, abstract and source p. 2.

## Result

The source asks whether a polynomially bounded operator `T` must be similar to the unilateral shift `S` when a quasiaffinity `X` satisfies

```text
X T = S X
```

and the normalized adjoint eigenvectors `X^*u_lambda` have norms uniformly bounded above and below.

The full question is not closed. The packet proves four directly relevant partial conclusions:

1. The answer is affirmative when `T` is completely polynomially bounded, by combining Paulsen's similarity theorem with Uchiyama's contraction criterion.
2. The answer is affirmative for unilateral weighted shifts under the weaker assumptions of power boundedness and the existence of any nonzero bounded intertwiner to `S`.
3. On every `H^infinity`-interpolating sequence, the normalized eigenvectors form a Riesz sequence and `X^*` is bounded below on the associated Hardy-kernel span.
4. A cluster--orthogonality theorem proves that the direct shift extension of the cyclic polynomially bounded examples in arXiv:2412.14130 cannot satisfy the requested lower estimate for any intertwiner. Thus the strongest obvious later construction does not settle the 2019 problem negatively.

## Main mechanism

Polynomial interpolation implements every finite sign change on an interpolating family of adjoint eigenvectors, and the polynomial bound controls those sign changes. Rademacher averaging gives Riesz estimates.

Conversely, normalized Hardy kernels at pseudohyperbolically close points are almost parallel. A bounded operator cannot map such kernels to uniformly nonzero orthogonal vectors. The 2024 construction has exponentially many eigenvalues in compact block regions while the relevant finite-block adjoint eigenlines are orthogonal. This forces the lower eigenvector norm to collapse.

## Scope

- No full proof or counterexample is claimed.
- The 2024 exclusion concerns the published Theorem 6.3 / Theorem 7.1 / Corollary 2.3 route and any intertwiner for the resulting shift extension.
- A different polynomially bounded construction with nonorthogonal clustered eigenlines could still be a counterexample.
- The global positive step remains blocked because interior Hardy kernels do not provide a sampling Riesz basis and the hypothesis does not control generalized eigenvectors.

## Files

- `main.tex`, `solution_packet.pdf`: statements, proofs, construction audit, eight-route upgrade audit, and novelty audit.
- `source_paper.pdf`: official arXiv PDF for arXiv:1901.03883.
- `supporting_paper_2412.14130.pdf`: the later candidate construction audited in the packet.
- `figures/open_problem_crop.png`: source p. 2 open-question passage.
- `verification.md`: mathematical and artifact verification.

Human-review focus: check the one-dimensional eigenspace transfer in Theorem 4, the identification of the mutually orthogonal lower-block eigenlines in the 2024 construction, and the interpolating-polynomial approximation step.
