# A compact semilattice counterexample to the literal cocommutative classification

Status: **candidate counterexample, likely valid, literal scope; expert review
requested**.

Remark 3.19 of Das--Mrozinski, *On a quantum version of Ellis joint
continuity theorem* (arXiv:1502.02469), says it is tempting to conjecture that
all cocommutative compact semitopological quantum semigroups arise from group
`C*`-algebras of locally compact groups.

On the direct isomorphism/classification reading, the compact semilattice

```text
S = [0,1],       st = min(s,t)
```

is a counterexample. Set `A=C(S)` and
`Delta(f)(s,t)=f(min(s,t))`. The product is jointly continuous, associative,
and commutative, so `(A,Delta)` is a cocommutative compact semitopological
quantum semigroup. Yet `A` cannot be a group `C*`-algebra: if `C*(G)` were
commutative then `G` would be abelian and `C*(G)=C_0(G-hat)`; unitality would
make `G-hat` a compact group homeomorphic to `[0,1]`, impossible because a
topological group is homogeneous while the interval is not. Independently,
the coproduct fails Woronowicz cancellation.

The packet explicitly limits the conclusion to the literal universal
classification. Remark 3.19 does not define the broader phrase “arise from”
and qualifies it by “somewhat as in Remark 3.18(b)”; no claim is made about an
unspecified embedding, compactification, or representation interpretation.

Packet contents:

- `solution_packet.pdf`: precise statement, proof, and scope limitation;
- `main.tex`: reproducible LaTeX source;
- `source_paper.pdf`: the source paper;
- `figures/open_problem_crop.png`: full-width crop of Remark 3.19, page 12;
- `code/verify_semilattice.py`: exact finite-grid sanity checks;
- `VERIFICATION.md`: proof audit;
- `novelty_search.md`: bounded search record.

