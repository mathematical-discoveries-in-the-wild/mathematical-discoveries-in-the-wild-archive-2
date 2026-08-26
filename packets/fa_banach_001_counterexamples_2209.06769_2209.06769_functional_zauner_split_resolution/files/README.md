# Split resolution of the functional Zauner conjectures

Status: `candidate_full_likely_valid_mixed_resolution`.

For arXiv:2209.06769:

- the non-Archimedean field axiom forces every positive integer to have
  absolute value one; repeated copies of a norming vector-functional pair
  solve Question 2.4 for all `d,n` and the stated Zauner conjecture for the
  standard maximum norm;
- the p-adic Functional Zauner Conjecture is false for every dimension `d`
  divisible by `p`; tightness forces `b=d`, and its diagonal identity says a
  p-adically small number equals `1` plus p-adically small terms;
- in dimension one, the p-adic equality question has solutions exactly for
  `p` not dividing `n`;
- both functional equiangular-line problems have unbounded cardinality at
  `(a,gamma)=(1,1)` because repetitions are not prohibited.

The p-adic counterexample is independent of norm choice. The positive
non-Archimedean construction is stated for the standard maximum norm and,
more generally, norms admitting a norming vector-functional pair.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: arXiv source.
- `figures/nonarch_zauner_crop.png`: Conjecture 2.5.
- `figures/padic_zauner_crop.png`: Conjecture 3.4.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```
