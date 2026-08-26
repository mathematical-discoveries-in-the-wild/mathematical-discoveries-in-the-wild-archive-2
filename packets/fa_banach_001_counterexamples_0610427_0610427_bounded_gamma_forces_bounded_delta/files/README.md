# Bounded Gamma forces bounded Delta

This packet gives a candidate full negative answer to the existence question
and conjecture in Remark 5.5 of arXiv:math/0610427v2.

For every admissible probability measure `P`, the entrywise relation
`Gamma_ij = sqrt(Delta_ij)` gives the exact identity

```text
||Delta_n(P)||_infinity = ||Gamma_n(P)||_(2 -> infinity)^2.
```

Since the `2 -> infinity` norm never exceeds the spectral `2 -> 2` norm,

```text
||Delta_n(P)||_infinity <= ||Gamma_n(P)||_2^2.
```

Thus bounded Gamma norms always force bounded Delta norms.  The sequence
conjectured in the source cannot exist.

Files:

- `main.tex`: source question, universal matrix lemma, full proof, checks, and
  literature audit.
- `solution_packet.pdf`: rendered candidate full-disproof packet.
- `VERIFICATION.md`: mathematical, source, novelty, and artifact audit.
- `source_paper.pdf`: latest arXiv version (v2).
- `figures/open_problem_crop.png`: Remark 5.5 from source page 11.

Status: candidate full disproof, high confidence; independent review is
recommended because the conclusion reverses the source's stated conjecture.
