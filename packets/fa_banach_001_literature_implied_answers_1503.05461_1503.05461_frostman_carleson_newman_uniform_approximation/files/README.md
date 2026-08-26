# Literature-implied partial answer: Frostman-Carleson-Newman class

status: `literature_implied_answer (partial subcase)`

source: Isabelle Chalendar, Pamela Gorkin, and Jonathan R. Partington,
*Inner functions and operator theory*, arXiv:1503.05461.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1503.05461_frostman_carleson_newman_uniform_approximation/`

ledger: `runs/fa_banach_001/ledger/results/1503.05461_frostman_carleson_newman_uniform_approximation.json`

## Identification

Page 4 of the source paper asks whether every Blaschke product can be
approximated in the `H^infinity` norm by an interpolating Blaschke product.

Let `M` be the Mortini-Nicolau class of inner functions `Theta` for which every
nonzero Frostman shift

`phi_a o Theta = (a-Theta)/(1-conj(a)Theta)`

is a Carleson-Newman Blaschke product. Two known results combine directly:

1. a finite product of interpolating Blaschke products can be approximated in
   norm by one interpolating Blaschke product (Marshall-Stray, 1996); and
2. every nonzero Frostman shift of a member of `M` is such a finite product,
   by the definition and characterizations of `M`.

For `F_a=(Theta-a)/(1-conj(a)Theta)`, one has

`||F_a-Theta||_infinity <= 2|a|/(1-|a|)`.

Taking `a -> 0` and then applying Marshall-Stray proves that every member of
`M` is a uniform limit of interpolating Blaschke products.

## Strictly larger than the previously obvious class

This implication is not limited to Carleson-Newman targets. Borichev,
Nicolau, Ounaies, and Thomas record that every Blaschke product whose zeros lie
in a Stolz angle belongs to `M`, while such a product need not itself be
Carleson-Newman. Their explicit example has zeros `1-2^{-j}` with multiplicity
`j`. It is therefore covered by the approximation theorem although it is not
a finite product of interpolating Blaschke products.

## Scope and provenance

The full question remains open. Xin and Hou explicitly describe the density
of interpolating Blaschke products in the full inner-function space as open in
2023. The packet records an agent-identified implication between existing
theorems; none of the supporting papers is represented as explicitly answering
the 2015 survey question through this exact combination.

The packet contains a compact complete proof and the exact quantitative shift
estimate. It does not claim that every Blaschke product belongs to `M`.

## Files

- `main.tex` / `solution_packet.pdf`: compact theorem and proof.
- `source_paper.pdf`: arXiv:1503.05461; the question is on PDF page 4.
- `supporting_paper_marshall_stray_1996.pdf`: the approximation theorem for
  finite products of interpolating Blaschke products.
- `supporting_paper_2501.05143.pdf`: the class `M`, its SIP subfamily, and a
  non-Carleson-Newman Stolz-angle example.
- `supporting_status_paper_2302.00830.pdf`: 2023 confirmation that the full
  density problem remains open.
