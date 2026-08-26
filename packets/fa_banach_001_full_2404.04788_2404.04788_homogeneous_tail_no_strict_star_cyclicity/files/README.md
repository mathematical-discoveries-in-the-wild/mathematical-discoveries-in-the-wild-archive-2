# Homogeneous tails rule out strict adjoint cyclicity

Status: `candidate full solution; likely valid; human review requested`

Source: David P. Blecher and Raphaël Clouâtre, *Null projections and noncommutative function theory in operator algebras*, arXiv:2404.04788v2, source p. 24 after Theorem 5.11.

## Result

For every regular unitarily invariant Hilbert function space `H` on the unit ball, the full multiplier algebra `M(H)` has no strictly `*`-cyclic vector. More generally, no norm-closed subalgebra of `M(H)` has one. In particular,

```text
A(H)^* xi != H
```

for every `xi in H`, where `A(H)` is the multiplier-norm closure of the polynomial multipliers.

This completely answers the source's characterization question within its stated class: every such `H` has the nonexistence property. It also removes hypothesis (i) from source Theorem 5.11. Thus, if `q` is closed, `q A(H)=q T(H)`, and a nonempty `M(H)`-totally null set exists, then `q` is `M(H)`-totally null and hence `A(H)`-null.

## Proof mechanism

Let `H_{>=n}` be the homogeneous-degree tail. Every multiplier preserves every tail, and the tail projections converge strongly to zero.

If `A^*xi=H`, the open mapping theorem gives a uniform constant `C` such that each unit `y` can be written `a^*xi=y` with `||a||<=C`. Choose unit `y_n in H_{>=n}`. Since `a_n y_n` remains in the same tail,

```text
1 = |<a_n^*xi,y_n>|
  <= C ||P_{>=n}xi|| -> 0,
```

a contradiction.

## Scope

- The result concerns strict `*`-cyclicity, meaning exact equality, not ordinary dense cyclicity.
- The source's independent assumption that a nonempty totally null set exists remains necessary for the quoted null-projection corollary.
- No statement is made about finite-dimensional truncated analytic spaces without arbitrarily high nonzero homogeneous tails.

## Files

- `main.tex`, `solution_packet.pdf`: full theorem, proof, strengthened source corollary, stress tests, and novelty audit.
- `source_paper.pdf`: official arXiv v2 PDF.
- `figures/open_problem_crop.png`: source p. 24, including Theorem 5.11 and the open characterization statement.
- `verification.md`: mathematical and artifact audit.

Human-review focus: verify the standard exhaustive homogeneous decomposition under the source's regular unitarily invariant hypotheses and the open-mapping uniform preimage step.
