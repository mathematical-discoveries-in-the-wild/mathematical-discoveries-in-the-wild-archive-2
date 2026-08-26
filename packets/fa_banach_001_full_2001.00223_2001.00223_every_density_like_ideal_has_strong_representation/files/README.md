# Every density-like ideal has a strongly-density-like representation

## Status

`candidate_full_solution_likely_valid`

This packet gives a self-contained negative answer to Question 5 of Adam Kwela and Paolo Leonetti, *Density-Like and Generalized Density Ideals* (arXiv:2001.00223, Section 6, source PDF p. 25). The argument has not been human verified. The principal review points are the concavity of the gauge, preservation of the exhaustive ideal, and the dyadic constants in the strong-density estimate.

## Source question

The paper asks:

> Does there exist a density-like ideal \(\mathcal I\) such that \(\mathcal I\ne\operatorname{Exh}(\varphi)\) for each strongly-density-like lscsm \(\varphi\)?

The original statement is reproduced in `figures/open_problem_crop.png`; the complete paper is copied as `source_paper.pdf`.

## Answer

No. In fact, a stronger representation theorem holds.

**Theorem.** Let \(\varphi\) be any density-like lower semicontinuous submeasure on \(\omega\). There is a bounded, continuous, increasing, concave function
\[
f:[0,\infty]\longrightarrow[0,1],
\qquad f(0)=0,\quad f(t)>0\ (t>0),
\]
such that \(\psi=f\circ\varphi\) is a strongly-density-like lower semicontinuous submeasure, with witnessing constant \(c=1/4\), and
\[
\operatorname{Exh}(\psi)=\operatorname{Exh}(\varphi).
\]

Thus every density-like ideal admits a strongly-density-like representing submeasure.

## Idea of proof

Density-likeness supplies a modulus only scale by scale. Choose rapidly decreasing scales \(t_n\) so that smallness below \(t_{n+1}\) activates the density-like conclusion at target \(t_n\). Map those scales to dyadic values by a piecewise-affine gauge \(f(t_n)=2^{-n}\). The extra separation \(t_{n+1}<t_n/4\) makes the slopes increase toward the origin, hence makes \(f\) concave and therefore subadditive. After the change of scale, the implication becomes linear:
\[
\psi(F_k)<\varepsilon/4
\quad\Longrightarrow\quad
\psi\left(\bigcup_{k\in I}F_k\right)<\varepsilon
\]
for some infinite \(I\).

Because \(f\) is continuous at zero and vanishes only at zero, composing with it does not change which tail submeasure values tend to zero, so it preserves the exhaustive ideal.

## Contents

- `main.tex`: complete theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: full-width crop containing Question 5.
- `code/check_concave_gauge.py`: deterministic numerical stress test of the gauge construction.
- `verification.md`: proof audit, computation record, and bounded novelty screen.

## Reproduction

From this directory:

```sh
conda run --no-capture-output -n sandbox python code/check_concave_gauge.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex
```

The computation is only a sanity check; the proof is analytic and does not depend on it.

## Novelty screen

A bounded search on 2026-08-09 used the exact question wording, the term `strongly-density-like`, the paper title, arXiv, and OpenAlex. It found the source paper but no later mathematical work answering Question 5. OpenAlex listed one citing record, which was only the cover/back matter for the same journal issue. This is evidence of no located prior answer, not a claim of exhaustive priority.

