# Quiver-unitary invariance characterizes hyper-Reinhardt pencils

Status: **candidate full solution; likely valid; human review recommended**

## Source question

- Scott McCullough, *Hyper-Reinhardt Free Spectrahedra*,
  arXiv:2107.11641v4.
- Target: Remark 4.4, official PDF page 17.

For a monic pencil

```text
L_B(X) = I + sum_j (B_j tensor X_j + B_j^* tensor X_j^*)
```

the question asks whether its free spectrahedron is hyper-Reinhardt exactly
when it is invariant under every quiver-unitary transformation

```text
X_j -> W_(j-1)^* X_j W_j,       j=1,...,g.
```

The final `P_A` in the source display is a local typo for `P_B`; otherwise
the sentence is not well-typed, and both the preceding lemma and its proof
make the intended reading unambiguous.

## Full result

Yes.  Let `B` be a minimal monic defining tuple with every coordinate active.
The displayed invariance holds at every matrix level if and only if there is
an orthogonal decomposition

```text
H = H_0 direct-sum H_1 direct-sum ... direct-sum H_g
```

such that

```text
B_j = P_(j-1) B_j P_j.
```

Thus, after unitary change of coefficient basis, each `B_j` has exactly the
single `(j-1,j)` block prescribed in the source's definition.  This is the
complete structural characterization.  If coordinate slices are normalized
to radius one, those blocks automatically have norm one, giving the source's
normalization verbatim.  Inactive coordinates are covered by allowing zero
blocks (or deleting and reinserting them).

## Proof mechanism

Fix `n` and expand each `X_j` in matrix units `E_ab`, with new free variables
`Y_(j,ab)`.  The original and transformed pencils then have coefficient
tuples

```text
C_(j,ab) = B_j tensor E_ab,
D_(j,ab) = B_j tensor W_(j-1)^* E_ab W_j.
```

The assumed symmetry at all auxiliary levels says the two expanded free
spectrahedra are equal.  Matrix-unit inflation preserves minimality, so the
Linear Gleichstellensatz makes `C` and `D` unitarily equivalent.

At `n=2`, start from `E_11 E_21=0` and choose the quotient of two independent
vertex unitaries to be the flip matrix.  The transformed matrix-unit product
is nonzero, so unitary equivalence forces precisely

```text
B_j B_k   = 0 unless k=j+1,
B_j B_k^* = 0 for j!=k,
B_j^* B_k = 0 for j!=k.
```

Writing `R_j=ran(B_j)` and `S_j=ran(B_j^*)`, these identities make

```text
H_0=R_1,
H_r=S_r+R_(r+1),
H_g=S_g
```

pairwise orthogonal.  Minimality removes the common zero complement, and the
required path form follows.  The converse is exactly the block-diagonal
conjugation already used in the source.

## Verification and novelty

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2107.11641_hyper_reinhardt_unitary_invariance_characterization/code/verify_matrix_unit_relations.py
```

The script checks the exact matrix-unit witness, all zero-product identities
on a nontrivial three-arrow path pencil, and the block-conjugation identity.
The Gleichstellensatz and minimality argument are formal proofs, not inferred
from computation.

Bounded searches on 2026-08-13 found no later claimed answer.  The closest
papers are arXiv:2012.02289, which classifies the weaker scalar-torus
Reinhardt symmetry, and arXiv:2301.02746, which later uses quiver-unitary
invariance only as a necessary test for being hyper-Reinhardt.  Novelty
confidence is moderate.

## Human-review focus

Prioritize the lemma that matrix-unit inflation preserves minimality, then the
application of the Linear Gleichstellensatz to the expanded pencils.  The
remaining matrix-unit and range-space arguments are elementary and exact.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem and full proof.
- `source_paper.pdf`: official 33-page source PDF.
- `supporting_paper_2012.02289.pdf`: graph characterization of weaker
  Reinhardt symmetry.
- `supporting_paper_1604.05756.pdf`: source of the Linear
  Gleichstellensatz used here.
- `figures/open_problem_crop.png`: official full-width Remark 4.4 crop.
- `code/`: reproducible cropper and exact relation checker.
- `verification.md`: proof audit, literature bounds, visual QA, and hashes.
