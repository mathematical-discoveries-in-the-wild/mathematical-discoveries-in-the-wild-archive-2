# Counterexample: multiplicity defeats the universal orthogonal family

Status: `counterexample_likely_valid`

Source: Samuel A. Hokamp, *A Class of Homeomorphisms on Homogeneous Spaces
of a Group Action*, arXiv:2308.09799. Conjecture 1.1 on PDF page 1 asserts
that every compact transitive action admits one pairwise-orthogonal family of
minimal invariant subspaces whose subcollections generate all uniformly
closed invariant subspaces of `C(X)`.

## Result

The conjecture is false. Take the finite compact group `G=S_3`, let `X=S_3`
with the discrete topology, and use left translation. The standard
two-dimensional irreducible representation occurs with multiplicity two in
the regular representation `C(S_3)`.

More generally, the packet proves that the conjectured property holds for a
compact homogeneous action `X=G/K` if and only if the quasi-regular
representation on `L^2(X)` is multiplicity-free, equivalently

```text
dim(V_pi^K) <= 1
```

for every irreducible representation `V_pi` of `G`.

## Proof mechanism

Any universal family must contain every minimal invariant subspace: applying
the family property to a minimal space `M` forces the representing
subcollection to contain `M` itself. But in two equivalent copies `V + V`,
the coordinate copy `V + 0` and the diagonal copy `{(v,v)}` are both minimal,
distinct, and nonorthogonal. Therefore multiplicity at least two is fatal.

For an explicit witness inside `C(S_3)`, let `V` be the standard
two-dimensional representation and choose orthonormal vectors `a,b`. Matrix
coefficient maps produce minimal subspaces `M_a`, `M_b`, and `M_(a+b)`.
Schur orthogonality gives

```text
M_a perpendicular to M_b,
M_(a+b) = diagonal(M_a,M_b),
M_a not perpendicular to M_(a+b).
```

The universal family would have to contain both `M_a` and `M_(a+b)`, which
contradicts its pairwise orthogonality.

## Verification

Run the exact checker:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2308.09799_s3_regular_action_counterexample/code/verify_s3_counterexample.py
```

It enumerates all six group elements and checks exact ranks, invariance,
irreducibility, orthogonality, nonorthogonality, and distinctness. The
computation is a consistency check; the written proof is exact.

Verifier focus:

- Check that applying the conjectured property to a minimal invariant space
  forces that space to be a member of the fixed family.
- Check the Schur-orthogonality formula for the three coefficient embeddings.
- For the stronger characterization, check the uniform finite-spectrum
  density argument inside each closed invariant subspace of `C(X)`.

## Novelty and scope

The bounded search on 2026-08-11 covered the run indexes, exact arXiv id and
title, author plus conjecture, the core orthogonal-minimal and
multiplicity-free phrases, the source paper, and arXiv:2110.12060. The source
is still arXiv v1 from 2023. No later paper explicitly proving or disproving
Conjecture 1.1 was found. Because the obstruction uses standard compact-group
representation theory, novelty confidence is moderate.

This settles the conjecture exactly as stated. It does not address variants
where the orthogonal family may depend on the invariant subspace.

Human review recommendation: start with the two-line minimal-space lemma and
the explicit `S_3` coefficient spaces; then review the general
multiplicity-free equivalence.

Files:

- `source_paper.pdf`: arXiv:2308.09799.
- `figures/open_problem_crop.png`: source PDF page 1, Conjecture 1.1.
- `main.tex`, `solution_packet.pdf`: complete counterexample and exact
  characterization.
- `code/verify_s3_counterexample.py`: exact symbolic checks.
