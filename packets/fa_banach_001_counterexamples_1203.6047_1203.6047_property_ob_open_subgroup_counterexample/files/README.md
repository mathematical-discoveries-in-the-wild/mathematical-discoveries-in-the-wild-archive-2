# Counterexample: Property (OB) Need Not Pass to Open Subgroups

Status: `candidate_counterexample_likely_valid_novelty_unconfirmed`

Model: `GPT5.6`

Source: Christian Rosendal, *Global and local boundedness of Polish groups*,
arXiv:1203.6047, Problem 1.16 on PDF page 14 (published numbering;
Problem 1.17 in another version), DOI 10.1512/iumj.2013.62.5133.

## Claimed contribution

The answer to Rosendal's question is negative. Let

```text
N = Z^N,
P = S_infinity,
G = N semidirect P,
```

where `P` has the pointwise-convergence topology, `N` has the product
topology, and `P` permutes the coordinates of `N`. Then `G` is a Polish group
with property (OB). However,

```text
H = N semidirect Stab_P(0)
```

is an open subgroup without property (OB): the coordinate map
`(a,p) -> a_0` is a continuous surjective homomorphism from `H` to `Z`, so
its absolute value is an unbounded continuous length function on `H`.

## Proof mechanism

For a finite set `A` of coordinates, let `U_A` consist of pairs `(a,p)` for
which `a` vanishes on `A` and `p` fixes `A` pointwise. These subgroups form a
neighbourhood basis at the identity of `G`.

Choose a disjoint finite block `B` of the same size and let `tau` exchange
`A` with `B`. Every base vector is a product in

```text
U_A tau U_A tau.
```

Moreover, the pointwise stabilizer `P_A` has only finitely many double cosets
in `P`: they are classified by the finite partial bijection from `A` to `A`
induced by a permutation. If `E` is a finite set of double-coset
representatives, every element of `G` therefore lies in

```text
U_A tau U_A tau U_A E U_A.
```

Thus, for a finite `F`, `G = (F U_A)^4`. Passing from an arbitrary nonempty
symmetric open set `V` to an identity neighbourhood inside `V^2` gives
`G = (F' V)^8`. Rosendal's bounded-width characterization of property (OB)
then proves that `G` has property (OB).

## Verification

The argument is exact and does not use numerical computation. The detailed
self-verifier report is in `VERIFICATION.md`. Its verdict is
`counterexample_likely_valid`. The main audit points are:

- the semidirect-product action is continuous, so `G` is Polish;
- `U_A` really is a neighbourhood-basis subgroup;
- the double cosets of `P_A` are classified by partial bijections of `A`;
- the displayed factorization has the correct semidirect-product order;
- the coordinate map is a homomorphism precisely because the permutation
  part of `H` fixes coordinate `0`.

## Novelty and scope

The bounded novelty check on 2026-08-11 searched the four lightweight run
indexes for arXiv:1203.6047, the exact problem, property (OB), open-subgroup
inheritance, semidirect products, and wreath products. It also searched the
web/arXiv-facing index with the exact problem wording, both labels "Problem
1.16" and "Problem 1.17", and combinations of `property (OB)`, `open
subgroup`, `counterexample`, `wreath product`, and `Z^N semidirect S_infinity`.
Only the source question and background results were found; no later paper
claiming an answer was located.

This is a bounded, non-exhaustive search, so novelty is not asserted. The
packet should be checked against citation databases and by an expert in Polish
group geometry before any public originality claim.

Human review recommendation: high priority. The proof is short and appears to
fully answer the source problem. The most important review point is the
bounded-width factorization proving property (OB) for the unrestricted wreath
product.

Files:

- `source_paper.pdf`: arXiv:1203.6047.
- `figures/open_problem_crop.png`: source PDF page 14, Problem 1.16.
- `main.tex`, `solution_packet.pdf`: full counterexample packet.
- `VERIFICATION.md`: explicit proof-audit report.

