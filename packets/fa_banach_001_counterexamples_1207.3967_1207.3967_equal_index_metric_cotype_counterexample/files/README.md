# Equal-index Orlicz nonembeddability via metric cotype

Status: candidate full counterexample, likely valid; human review recommended.

Source: Michal Kraus, *Coarse and uniform embeddings between Orlicz sequence
spaces*, arXiv:1207.3967.  The open question is on page 11.

Result: for every `p>2`, define `N(t)=t^p` and
`M(t)=t^p/(1-log t)` on `(0,1]`, with the tangent linear extension for
`t>=1`.  Then

```text
alpha_M = beta_M = beta_N = p,
```

but `h_M` admits neither a coarse nor a uniform embedding into
`h_N=ell_p`.  This answers the source question affirmatively for every
allowed common index.

The proof combines the asymptotic estimate

```text
||e_1+...+e_n||_{h_M} = o(n^(1/p))
```

with the optimal-scale metric-cotype inequality for `ell_p`.  A trigonometric
embedding of discrete tori into `h_M` has antipodal coordinate jumps much
larger than its diagonal steps.  After scaling, the metric-cotype inequality
contradicts either the coarse lower modulus or uniform continuity.

Files:

- `solution_packet.pdf`: complete theorem and proof.
- `source_paper.pdf`: original paper containing the open question.
- `supporting_paper_0506201.pdf`: Mendel--Naor metric-cotype paper.
- `figures/open_problem_crop.png`: page-11 source evidence.

Novelty check: bounded searches on 2026-08-09 used the exact question,
arXiv id/title, and combinations of the equal-index formula with Orlicz,
coarse embedding, uniform embedding, and Matuszewska--Orlicz.  No later paper
claiming this endpoint answer was found.  This is evidence, not a guarantee of
novelty.

Verifier focus: confirm the specialization of Mendel--Naor Theorem 4.1 to
`ell_p`, the short-step Luxemburg-norm bound, and the two modulus
contradictions.
