# Flat-Discrepancy Prefix Criterion for the Commutator Conjecture

Status: `candidate_partial_likely_valid`.

## Source target

- Pourya Habib Zadeh and Suvrit Sra, “Introducing Discrepancy Values of
  Matrices with Application to Bounding Norms of Commutators,”
  arXiv:2111.11855; *Linear Algebra and its Applications* 651 (2022),
  359–384.
- Conjecture 7.1 (source PDF page 20) asks whether
  `sigma([A,B]) <=_w 2 delta(A) delta(B)` for all complex square matrices.

## Partial result

Fix a prefix `k`. If either matrix has a flat discrepancy prefix,

```text
delta_1(A) = ... = delta_k(A),
```

then the conjectured weak-majorization inequality is true at that prefix:

```text
sum_{j=1}^k sigma_j([A,B])
    <= 2 sum_{j=1}^k delta_j(A) delta_j(B).
```

The other matrix is arbitrary. As a concrete new consequence, if `A` is any
normal `3 x 3` matrix and `B` is arbitrary, then Conjecture 7.1 holds at
prefixes `k=1,2`. The geometry behind the nontrivial `k=2` assertion is that
the first two discrepancy values of a normal `3 x 3` matrix both equal the
radius of the smallest disk containing its three eigenvalues.

This does **not** prove the `k=3` trace-norm prefix, even for a normal `3 x 3`
matrix against an arbitrary matrix, and it does not settle Conjecture 7.1 in
full.

## Proof mechanism

Shift the flat-prefix matrix by an operator-norm minimizing scalar and shift
the other matrix by a Ky Fan `k`-norm minimizing scalar. The commutator is
unchanged. The Ky Fan ideal inequality and triangle inequality then give

```text
||[A,B]||_(k) <= 2 delta_1(A) sum_{j=1}^k delta_j(B),
```

which is exactly the conjectured right-hand side when the first `k`
discrepancy values of `A` are equal.

## Files

- `main.tex`: complete partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2111.11855v3.
- `figures/open_problem_crop.png`: Conjecture 7.1 and its stated status on
  source PDF page 20.
- `code/random_search.py`: non-proof numerical stress test.
- `tmp/`: LaTeX and PDF-render verification artifacts.

## Human review recommendation

Review as a likely-valid partial theorem. The two central checks are the use
of the Ky Fan ideal inequality after independent scalar shifts and the planar
smallest-enclosing-disk argument proving `delta_1(A)=delta_2(A)` for normal
`3 x 3` matrices. Do not promote this as a full solution: the final prefix
remains open.

