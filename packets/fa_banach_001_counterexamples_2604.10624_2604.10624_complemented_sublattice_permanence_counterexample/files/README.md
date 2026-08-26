# Semiprojectivity is not inherited by complemented sublattices

Status: `counterexample` (scoped to bounded linear complementation)

## Source problem

Tomasz Kania and Mariusz Niwiński, *Semiprojective Banach lattices*,
arXiv:2604.10624v1 (2026).

Question 5.14, arXiv PDF page 16, asks which permanence properties
semiprojectivity enjoys and explicitly lists passage to complemented
sublattices. The question also asks about finite direct sums and other
operations; those parts are not settled here.

## Counterexample

The semiprojective Banach lattice `C[0,1]` contains a lattice-isometric copy
`Y` of `c_0` that is the range of a bounded linear projection of exact norm 2.
The source paper's Corollary 5.8 proves that `c_0` is not semiprojective.
Consequently, semiprojectivity does not pass to complemented sublattices in
the standard bounded-linear-complementation sense.

Take pairwise disjoint intervals converging to 0 and triangular positive bumps
`u_n` on them. Their closed span is lattice-isometric to `c_0`. If `t_n` is
the peak and `a_n` the left endpoint, then

```text
P f = sum_n (f(t_n)-f(a_n)) u_n
```

is a projection from `C[0,1]` onto that span and `||P||=2`.

## Scope caveat

The projection is not claimed positive or lattice-homomorphic. Thus this does
not contradict Proposition 2.6 of the source, which proves inheritance under
contractive lattice-homomorphic retracts. If “complemented sublattice” in
Question 5.14 was intended in that narrower categorical sense, that variant
remains open. The packet answers the literal standard Banach-space meaning.

Files:

- `source_paper.pdf`: arXiv:2604.10624v1.
- `figures/open_problem_crop.png`: Question 5.14 on source PDF page 16.
- `main.tex`, `solution_packet.pdf`: theorem, construction, proof, and scope.

Ledger:
`runs/fa_banach_001/ledger/results/2604.10624_complemented_sublattice_permanence_counterexample.json`.
