# A surjective isometry with no semigroup embedding

Status: `candidate_counterexample_likely_valid`.

For arXiv:0808.2419, Question 3.4 asks when the kernel/range necessary
condition is sufficient for embedding an operator into a strongly continuous
semigroup. Remark 5.4 explicitly asks for a non-trivial operator satisfying
that condition but not embeddable.

On the complex Banach space `C(T)`, let

```text
(Vf)(z) = z f(z).
```

Then `V` is an invertible surjective isometry, so its kernel and range defect
are both zero. If `S^n=V`, then `S` commutes with `V` and `V^-1`, hence with
all multiplication operators by density of trigonometric polynomials. Thus
`S=M_h` for `h=S1`, and `h^n(z)=z`. Winding numbers give
`n deg(h)=1`, impossible for every `n>=2`. Therefore `V` has no square root
and cannot be a time-one semigroup operator.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/question_3_4_crop.png`: source theorem and Question 3.4.
- `figures/nontrivial_request_crop.png`: source Remark 5.4.

The packet does not settle the separate compact-operator question in Remark
5.4 or attempt a classification of all positive classes.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```
