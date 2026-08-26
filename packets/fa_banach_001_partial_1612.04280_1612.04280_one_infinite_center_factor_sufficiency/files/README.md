# Weak amenability with one infinite-center rank-one factor

Status: `candidate substantial partial result; likely valid; human review requested`

Source: Søren Knudby, *Weak amenability of Lie groups made discrete*, arXiv:1612.04280, source p. 2.  Supporting source: Søren Knudby, *Weak amenability and simply connected Lie groups*, arXiv:1505.00984, Theorem 1.10.

## Result

Let `G` be a connected Lie group with Levi algebra

```text
g = r semidirect (direct_sum_i s_i).
```

Assume every `s_i` has real rank zero, or has real rank one and commutes with `r`.  If at most one rank-one ideal is of type `su(n,1)` (including `su(1,1)=sl(2,R)`), then `G` is weakly amenable and has the expected Cowling--Haagerup constant

```text
Lambda_WA(G) = product_i Lambda_WA(S_i),
```

where the right side is the local-isomorphism-invariant simple-factor value.

This proves the conjectured sufficiency direction for a genuinely intermediate-topology class: the fundamental group may be infinite, the Levi factor may have infinite center, and the Levi factor may even be dense.

## Mechanism

After a finite compact quotient, the universal-cover presentation reduces to

```text
Q = (A x U)/D,
```

with `A` amenable, `Z(U) ~= Z`, and `D` discrete central.  The closure `N` of the image of `U` has amenable quotient in `Q`.  After dividing out `D intersect A`, the remaining kernel is cyclic.  The closure of its projection to `A` is either a closed infinite cyclic group, in which case `N ~= U`, or compact, in which case `N` is a compact-central extension of `U/Z(U)`.  Standard permanence and the semisimple constant theorem give `Lambda_WA(Q)=Lambda_WA(U)` in both cases.

With two infinite cyclic Levi centers, a rank-two kernel can project densely into a noncompact real central direction (`(m,n) -> m + alpha n`), so this dichotomy genuinely stops.  The packet does not claim the remaining multi-factor cases or the full necessity direction.

## Files

- `main.tex`, `solution_packet.pdf`: theorem, proof, upgrade audit, and novelty audit.
- `source_paper.pdf`: official arXiv PDF for arXiv:1612.04280.
- `supporting_paper_1505.00984.pdf`: official arXiv PDF containing the simply connected classification.
- `figures/open_problem_crop.png`: the source passage identifying the open intermediate cases.
- `verification.md`: proof and artifact audit.

Human-review focus: verify the compact-quotient factorization in the main theorem and the topology of the cyclic-closure lemma.  The proof spells both points out.
