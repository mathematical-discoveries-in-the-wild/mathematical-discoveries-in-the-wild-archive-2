# Mixing implies disjoint mixing of all powers on weak-topology spaces

Status: `partial_result_likely_valid` (full weak-topology subcase of Question 3.4)

## Source question

Rodrigo Cardeccia and Santiago Muro, *Multiple recurrence and
hypercyclicity*, arXiv:2104.15033; *Mathematica Scandinavica* 128 (2022),
517–532.

Question 3.4 on arXiv PDF page 7 asks whether every mixing continuous linear
operator on a separable Fréchet space is multiply recurrent, equivalently
`AP`-hypercyclic.

## New partial theorem

If a topological vector space carries a weak topology and `T` is mixing, then
for every `m`, the tuple `(T,T^2,...,T^m)` is disjoint mixing. In particular,
`T` is multiply recurrent. Consequently every hypercyclic operator on
`omega = K^N` is `AP`-hypercyclic.

Shkarin proved that mixing on a weak-topology space is equivalent to the dual
operator `T'` having no nonzero finite-dimensional invariant subspace. For a
finite-dimensional dual subspace `L`, the module `K[t]L` is then a finitely
generated torsion-free `K[t]`-module and hence free. Polynomial supports show
that

```text
L + (T')^n L + ... + (T')^(mn) L
```

is a direct sum for all sufficiently large `n`. Weak neighborhoods involve
only finitely many functionals, so this directness makes the finite evaluation
map onto and solves all simultaneous orbit constraints exactly.

## Remaining obstruction

The full Fréchet-space question remains open. Outside weak topologies, the
polar of a neighborhood is generally infinite-dimensional. The finite-module
directness argument therefore does not give uniform control of the infinitely
many dual constraints defining a norm or seminorm ball. Eight focused upgrade
routes were audited in the packet; none removed this obstruction or produced
a mixing counterexample.

## Files

- `source_paper.pdf`: arXiv:2104.15033.
- `supporting_paper_1209.0979.pdf`: Shkarin's dual characterization.
- `figures/question_3_4_crop.png`: exact source question.
- `figures/shkarin_theorem_1_1.png`: decisive supporting theorem.
- `main.tex`, `solution_packet.pdf`: theorem, proof, and upgrade audit.

Ledger:
`runs/fa_banach_001/ledger/results/2104.15033_mixing_weak_topology_disjoint_powers.json`.
