# A negative answer to the Borel-representative problem

Status: **literature-implied full negative answer; proof supplied for review**.

This packet answers Open Problem 5.3 of arXiv:1509.02326. For every
`1 <= p < infinity`, it constructs a compact complete metric measure space
and a bounded `u in N^{1,p}` having no Borel representative.

The space is the snowflaked interval
`([0,1], |x-y|^alpha, mu)`, where `0<alpha<1` and `mu` is an explicit complete,
finite, non-Borel-regular extension of Lebesgue measure obtained from a
Bernstein set. The snowflake has no nonconstant rectifiable curves, so
`N^{1,p}=L^p` and `C_p(E)=mu(E)`. The witness is the characteristic function
of the Bernstein set.

The result is classified as literature-implied rather than novel because
Theorem 1.1 of arXiv:2410.21434 proves that Borel regularity is equivalent to
the existence of Borel representatives for all measurable functions. That
paper does not mention the source problem or Newtonian spaces; this packet
supplies the snowflake identification and the explicit counterexample.

Files:

- `main.tex`: self-contained construction and proof.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: locally compiled arXiv:1509.02326.
- `supporting_paper_2410.21434.pdf`: locally compiled supporting paper.
- `figures/source_problem.png`: source Open Problem 5.3.
- `figures/support_theorem.png`: supporting Theorem 1.1.
- `verification.md`: mathematical, provenance, and rendering audit.
- `tmp/`: compilation and page-rendering intermediates.
