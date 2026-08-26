# Minimal Laplacian with sectorial numerical range and full numerical spectrum

Status: `candidate_full_solution_likely_valid`

Run: `fa_banach_001`

Source: Martin Adler, Waed Dada, and Agnes Radl, *A semigroup approach to the numerical range of operators on Banach spaces*, arXiv:1507.01418; published in *Semigroup Forum* 94 (2017), 51-70.

## Result

The final open question in the source asks whether a closed densely defined operator can have closed convex spatial numerical range contained in a proper sector while its numerical spectrum is all of `C`.

The answer is yes. On `H=L^2(0,1)`, define

```text
Af = -f''
D(A) = {f in H^2(0,1): f(0)=f'(0)=f(1)=f'(1)=0}.
```

This minimal positive Laplacian is closed and densely defined. Integration by parts gives

```text
<Af,f> = ||f'||_2^2 >= 0,
```

so the closed convex hull of its numerical range is contained in the positive real ray, hence in every proper sector around that ray.

On the other hand,

```text
A* g = -g'',   D(A*) = H^2(0,1).
```

For every complex `lambda`, the equation `-g'' = conjugate(lambda) g` has nonzero `H^2` solutions. Thus `Ran(lambda-A)` has nonzero orthogonal complement and is not dense. Hence every complex number belongs to the residual spectrum, the ordinary resolvent is empty, and the source definition gives

```text
sigma_n(A) = C.
```

This is a full affirmative solution.

## Verification and novelty

- The proof is exact and noncomputational; the central checks are the adjoint domain and the range-kernel orthogonality identity.
- Cheap run indexes and the local corpus were searched for arXiv:1507.01418, the exact sector/full-spectrum question, and minimal-Laplacian terminology.
- Bounded web searches used the exact question, `numerical spectrum`, `sector`, `residual spectrum`, and `minimal Laplacian`. They found the source and later papers developing related essential numerical spectra, but no later answer to this question.
- Novelty confidence is moderate: the construction uses classical minimal symmetric-operator facts, so an unindexed prior observation remains possible.

## Files

- `main.tex`: full expert-facing proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local rendering of arXiv:1507.01418.
- `figures/open_problem_crop.png`: source-page crop of the final open question.

Ledger: `runs/fa_banach_001/ledger/results/1507.01418_minimal_laplacian_sector_full_numerical_spectrum.json`.
