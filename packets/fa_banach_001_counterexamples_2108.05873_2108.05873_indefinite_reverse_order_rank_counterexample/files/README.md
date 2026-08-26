# Counterexample to removing the indefinite reverse-order rank hypothesis

Status: `candidate_counterexample_likely_valid`

Source: K. Kamaraj, P. Sam Johnson, and Athira Satheesh K., *Reverse
Order Law for Generalized Inverses with Indefinite Hermitian Weights*,
arXiv:2108.05873; published in *Filomat* 37 (2023), 699--709. Section 4
on PDF page 10 asks whether the rank assumption in Theorem 3.16 can be
removed, or whether there is a counterexample.

## Claimed contribution

The rank assumption cannot be removed. Work on `C^3` with weight

```text
J = diag(1,1,-1)
```

and put

```text
B = [[1,0,0],
     [0,0,0],
     [0,0,0]],

A = [[1,1,-1],
     [1,1,-1],
     [1,1,-1]].
```

Both matrices are `J`-Hermitian idempotents, hence
`A^[dagger]=A` and `B^[dagger]=B`. Moreover,

```text
AB = [[1,0,0],       (AB)^[dagger] = [[1,1,-1],
      [1,0,0],                          [0,0, 0],
      [1,0,0]],                         [0,0, 0]]
```

and the displayed inverse is exactly `BA=B^[dagger]A^[dagger]`.
Nevertheless `A^[*] A B B^[*]=AB` is not range Hermitian: its range is
`span{(1,1,1)^T}`, while the range of its `J`-adjoint `BA` is
`span{(1,0,0)^T}`. Thus condition (i), and hence every equivalent condition
in Theorem 3.5, fails.

The omitted rank hypothesis fails sharply as well: its left block matrix has
rank 1, whereas `[A^[*]  B]` has rank 2.

## Proof mechanism

Let `u=(1,0,0)^T` and `v=(1,1,1)^T`. Both have `J`-norm one, but
`[u,v]_J=1` although they are distinct. Their span is a degenerate plane, a
configuration impossible for a positive-definite inner product. The matrices
`B=u u^*J` and `A=v v^*J` are the corresponding `J`-orthogonal rank-one
projections. The equality `[u,v]_J^2=[u,u]_J[v,v]_J` makes both products
`AB` and `BA` idempotent even though `A` and `B` do not commute. It also makes
`BA` the indefinite Moore--Penrose inverse of `AB`.

## Verification

The exact symbolic checker verifies the two weighted adjoint identities, the
two idempotencies, all four Penrose equations for `AB` and `BA`, the reverse
order law, failure of Theorem 3.5(i) and (iv), and the ranks 1 and 2 in the
source hypothesis:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2108.05873_indefinite_reverse_order_rank_counterexample/code/verify_counterexample.py
```

Result: all exact checks pass.

Verifier focus:

- Confirm that the source's three spaces may all use the same invertible
  Hermitian weight `J`.
- Confirm uniqueness of the Moore--Penrose inverse once the four defining
  equations are checked (this is part of the source's definition).
- Confirm that failure of range Hermiticity of `A^[*]ABB^[*]` is precisely
  failure of Theorem 3.5(i), so the example directly refutes the implication
  sought in Section 4.

## Novelty and scope

The bounded novelty search on 2026-08-09 covered all four lightweight run
indexes and web searches for the exact arXiv id and title, the exact rank
equality phrase, `indefinite reverse order law counterexample`, and the core
expression `A^[*]ABB^[*]`. It located the arXiv source and its 2023 published
version, but no later paper explicitly answering Section 4. This supports,
but cannot certify, novelty.

The packet answers the source's open question negatively with real `3 x 3`
matrices. It does not seek a replacement characterization of the reverse
order law under indefinite weights or prove minimality of dimension three.

Human review recommendation: send to a matrix-analysis reviewer. The proof is
elementary and exact; the main audit is alignment with the source's weighted
adjoint conventions.

Files:

- `source_paper.pdf`: arXiv:2108.05873.
- `figures/open_problem_crop.png`: source PDF page 10, Section 4.
- `main.tex`, `solution_packet.pdf`: full counterexample packet.
- `code/verify_counterexample.py`: exact symbolic audit.

