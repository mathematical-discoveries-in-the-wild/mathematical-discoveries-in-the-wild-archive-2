# Strong Zeno product convergence: answered by arXiv:2012.15061

Status: `literature_already_answered`.

On PDF page 5 of arXiv:0907.1199, Exner and Neidhardt leave open whether

```text
(P exp(-itB/n) P)^n -> exp(-itC)
```

strongly under the natural dense quadratic-form-domain hypothesis.

Theorem 1.1 of Exner and Ichinose, arXiv:2012.15061 (statement beginning on
PDF page 1), proves precisely this limit, in Hilbert-space norm for every
vector and uniformly on bounded time intervals. Their introduction explicitly
says that upgrading the earlier averaged convergence to strong-operator
convergence is the aim of the paper.

The notation matches by taking the later paper's `H=B`. The condition that
`H^(1/2)P` be densely defined is equivalent to density of
`dom(B^(1/2)) intersect ran(P)` in `ran(P)`, and the later operator
`H_P=(H^(1/2)P)^*(H^(1/2)P)` restricts on `ran(P)` to the source's form
operator `C`.

Files:

- `main.tex`: compact source/theorem matching note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:0907.1199.
- `supporting_paper_2012.15061.pdf`: later answer.
- `tmp/`: build and render intermediates.
