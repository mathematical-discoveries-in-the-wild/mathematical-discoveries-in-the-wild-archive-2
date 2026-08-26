# Full candidate: equation (4) has a sharp endpoint at `q=1`

Status: `full_solution_likely_valid` (awaiting specialist review).

For every `1<p<2` and `1<=q<=2`, this packet resolves equation (4) in
Blasco--Botelho--Pellegrino--Rueda:

```text
L(ell_p, ell_q; K) = Pi_(p;2,1)(ell_p, ell_q; K)
```

holds if and only if `q=1`.

At `q=1`, Grothendieck factorization and the little Grothendieck theorem give
the stronger conclusion that every bilinear form is absolutely
`(1;2,1)`-summing.  For each `1<q<=2`, uniformly complemented Rademacher
Euclidean blocks yield an explicit compact operator `T:ell_q->ell_(p')` whose
associated bilinear form is not absolutely `(p;2,1)`-summing.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `proof_intuition.md`: proof architecture in plain language.
- `VERIFICATION.md`: logical and computational audit record.
- `NOVELTY.md`: bounded literature-search record and novelty limitations.
- `source_paper.pdf`: arXiv:1404.1322.
- `supporting_pisier_1101.4195.pdf`: supporting survey for the two classical
  Grothendieck theorems.
- `figures/open_problem_crop.png`: source statement on page 9.
- `code/verify_rademacher_blocks.py`: finite checks of the block identities
  and divergence exponent (not part of the proof).

Primary verifier focus: audit the endpoint factorization argument at `q=1`
and the normalization `Q_(a,d) E_(a,d)=I` in the compact counterexample.
