# Verifier report

## Scope

The verifier checks the algebraic example used in Proposition 3 of the
packet.  For each `n=2,...,7`, it exhaustively enumerates all nonempty subsets
of the finite semigroup

```text
S_n = (Z/nZ) x {0,1},
(g,i)(h,j) = (g+h mod n, min(i,j)).
```

It tests associativity and commutativity, identifies every left ideal, checks
that `L=(Z/nZ)x{0}` is itself a left ideal and is contained in every left
ideal, and confirms that the two types of principal left ideal are exactly
`L` and `S_n`.

## Result

All assertions pass for every tested `n`.  The exact output is stored in
`code/verification_output.txt`.

## Independent mathematical checks

- The closure of a left ideal is a left ideal because fixed left
  multiplication is continuous.
- Separate weak continuity in the semigroup variable and weak lower
  semicontinuity of a continuous seminorm preserve each contraction
  inequality on closing a witness ideal.
- An intersection of nonempty left ideals is a left ideal.
- For infinite `kappa`, adding the one principal ideal `S t` to at most
  `kappa` witness ideals still yields a family of size at most `kappa`.
- In the compactification lemma, the net indexed by finite subsets is
  eventually contractive on each fixed pair; a subnet remains cofinal, so
  weak lower semicontinuity gives global nonexpansiveness of the cluster map.

## Limitation

The script is a finite consistency check, not a proof of the general
theorems.  The complete proofs are in `solution_packet.pdf`.
