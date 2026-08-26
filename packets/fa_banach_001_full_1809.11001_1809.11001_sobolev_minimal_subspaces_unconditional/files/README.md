# Full solution packet: unconditional Sobolev minimal-subspace membership

Status: `full_solution_likely_valid`, pending human review.

## Source question

Ali and Nouy, *Singular Value Decomposition in Sobolev Spaces: Part I*,
arXiv:1809.11001, Remark 3.6 and Proposition 3.7 (PDF page 9).

For `u in H^1(product_j Omega_j)`, the paper defines `U_j^min(u)` as the
`H^1(Omega_j)` closure of the contractions of `u` against `L^2` functionals
in every other variable. Under the assumption that the `H^1`-orthogonal
projection onto each `U_j^min(u)` is `L^2`-bounded, Proposition 3.7 proves

```text
u in closure_H1 (tensor_a,j U_j^min(u)).
```

Remark 3.6 conjectures that this conclusion fails for some `u` without the
projection assumption.

## Result

The packet proves the conclusion for every `u`; the conjectured
counterexamples do not exist. The projection assumption is unnecessary.

For `U_j = U_j^min(u)`, let `M_j` be its closure in `L^2`, and consider the
positive operator `K_j = J_j^* J_j` induced by the inclusion
`J_j: U_j -> M_j`. The spectral projection

```text
E_{j,eps} = 1_[eps,infinity)(K_j)
```

is an `H^1` contraction. It also extends to the `L^2`-orthogonal projection
onto its range and is an `L^2` contraction. On that range the two norms are
equivalent. Tensoring these cutoffs gives approximants converging to `u` in
every directional Sobolev tensor norm. At a fixed cutoff, equivalence of all
factor norms makes finite tensors from the `U_j` dense in the intersection
norm. A diagonal argument proves the result.

The proof is given first as an abstract theorem for finite intersections of
Hilbert tensor products, then specialized to `H^1`.

## Files

- `main.tex`: self-contained proof.
- `solution_packet.pdf`: compiled and visually inspected packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: exact definition, assumption, conjecture,
  and conditional proposition from source PDF page 9.
- `NOVELTY.md`: bounded literature search and comparison.
- `VERIFICATION.md`: proof and artifact verification record.

Model: GPT5.6.
