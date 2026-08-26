# Verification report

Status: **candidate counterexample, likely valid, literal scope; expert review
recommended**.

## Definition audit

- `A=C([0,1])` is unital.
- `Delta f(s,t)=f(min(s,t))` is a unital star homomorphism into the smaller
  algebra `C([0,1]^2)`, hence into the bidual tensor product required by the
  source definition.
- Associativity of `min` is exactly coassociativity of `Delta`.
- Symmetry of `min` is exactly cocommutativity.
- Every slice against a finite measure is continuous because the integrand is
  uniformly continuous on the compact square. Thus the nontrivial slice
  requirement in Definition 2.3 is met.

## Non-classification audit

The packet gives two independent obstructions.

1. If `C([0,1])` were a group `C*`-algebra, its commutativity would force the
   group to be abelian. Pontryagin duality identifies the algebra with
   `C_0(G-hat)`. Unitality makes `G-hat` compact, and Gelfand duality would make
   `[0,1]` homeomorphic to a compact group. This is impossible: compact groups
   are homogeneous, while deleting an interval endpoint preserves
   connectedness and deleting an interior point does not.
2. Every function in the span `Delta(A)(1 tensor A)` is constant in the first
   variable on the line `t=0`; this persists under uniform closure. The target
   function `(s,t) -> s` stays at distance at least `1/2`, so cancellation
   density fails.

## Exact sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python code/verify_semilattice.py
```

Output:

```text
checked associativity/commutativity on 41^3 triples
only the identity is invertible on the grid
finite-grid cancellation obstruction = 1/2
all exact checks passed
```

The finite-grid script is illustrative and not used to prove the continuous
claims.

## Scope audit

Remark 3.19 does not formally define “arise from” and says “somewhat as in
Remark 3.18(b).” The packet therefore labels itself throughout as a
counterexample only to the direct `C*`-bialgebra isomorphism reading. It makes
no claim about broader embedding or compactification interpretations.

Recommended human-review focus: whether this literal reading captures a
meaningful intended conjecture. The mathematical counterexample under that
reading is elementary and complete.

