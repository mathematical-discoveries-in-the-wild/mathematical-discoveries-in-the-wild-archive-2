# A square-zero counterexample to Conjecture 2.1

Status: `candidate_counterexample_likely_valid`

Source: Manuel Norman, *A conditional proof of the ISP for quasinilpotent
operators*, arXiv:2008.03253v2 (2021).

Target: Conjecture 2.1, page 5 of the arXiv PDF.

## Result

Conjecture 2.1 is false as printed. Let `H` be a complex separable
infinite-dimensional Hilbert space with orthonormal vectors `e1,e2`, and let

```text
N e2 = e1,   N e1 = 0,   N|{e1,e2}^perp = 0.
```

Thus `N` is rank one, `N^2=0`, and `||N||=1`. Take `T=N`. For every positive
triple `a,b,t` that the conjecture might choose, its normalization is
`T_tilde=aN`; choose the admissible perturbation `F=bN`.

For every nonzero complex `alpha`, the restriction of

```text
T_tilde^* + alpha F = a N^* + alpha b N
```

to `span{e1,e2}` has matrix

```text
[ 0       alpha b ]
[ a       0       ]
```

and eigenvalues `+/-sqrt(alpha*a*b)`. Hence the hypothesis involving the
adjoint perturbation holds for every nonzero `alpha`.

On the other hand,

```text
T_tilde + alpha F = (a+alpha b)N
```

is square-zero for every `alpha`, so its spectrum is `{0}`. Every metric
thickening of that spectrum is a disk centered at zero and is connected.
Therefore the disconnectedness demanded by conclusion (ii) is impossible for
every possible set `S` and every possible radius function `Phi`.

## Scope

This disproves Conjecture 2.1 exactly as stated, and therefore the paper's
conditional invariant-subspace consequences cannot be invoked from that
statement. It does not solve the invariant subspace problem and does not rule
out a modified conjecture whose hypothesis and conclusion use the same
adjoint orientation.

## Files

- `solution_packet.pdf`: review-ready statement, proof, limitations, and
  novelty record.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: full-width page-5 rendering containing
  Conjecture 2.1.
- `VERIFICATION.md`: explicit proof audit.
- `code/check_matrices.py`: finite-matrix sanity check; not used as proof.

## Novelty and review

The run indexes were searched for arXiv:2008.03253, the exact title,
quasinilpotent rank-one perturbations, and the invariant-subspace terms. A
bounded web search on 2026-08-11 used the exact source title with
`counterexample`, the arXiv id with `Conjecture 2.1`, and the author with the
quasinilpotent invariant-subspace conjecture. It found the current v2 source
and adjacent invariant-subspace papers, but no later answer or this
counterexample. Novelty remains subject to expert review.

Human review should focus on the exact adjoint orientation in the printed
conjecture. Once that transcription is confirmed, the remaining argument is a
two-dimensional square-zero computation valid inside the required
infinite-dimensional Hilbert space.
