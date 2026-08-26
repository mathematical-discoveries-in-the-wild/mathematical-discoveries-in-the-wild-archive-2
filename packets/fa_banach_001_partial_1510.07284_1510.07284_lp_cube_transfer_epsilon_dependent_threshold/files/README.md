# Cube transfer for logarithmic-p randomized Dvoretzky

Status: **candidate strong partial result, likely valid**, pending specialist
human review.

Source: G. Paouris, P. Valettas and J. Zinn, *Random version of
Dvoretzky's theorem in* $\ell_p^n$, arXiv:1510.07284, Section 6, item 5 and
Proposition 6.2 (PDF page 39).

## Result

For a subspace $E\subset\mathbb R^n$, let $D_q(E)$ be the oscillation ratio
of the $\ell_q$ norm on the Euclidean unit sphere of $E$.  The elementary
comparison

$$
D_\infty(E)\le n^{1/p}D_p(E)
$$

and Tikhomirov's sharp randomized cube theorem imply the quantitative bound

$$
k\le C\,\frac{\delta\log n}{\log(1/\delta)},
\qquad
\delta=(1+\varepsilon)n^{1/p}-1,
$$

whenever a Haar-random $k$-subspace is $(1+\varepsilon)$-spherical in
$\ell_p^n$ with probability greater than $3/4$ and $0<\delta<1/2$.

Consequently:

- the source's desired sharp $\varepsilon/\log(1/\varepsilon)$ upper bound
  holds whenever $p\ge C\varepsilon^{-1}\log n$;
- uniformly in $0<\varepsilon<1/3$ and for $k\ge2$, Proposition 6.2 remains
  true already for
  $p\ge C(\log n)^2/\log\log n$, improving its stated
  $p>(\log n)^2$ range.

The full question remains open in the wedge
$p\asymp\log n$ and $\varepsilon\ll(\log n)/p$.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: packet source.
- `verification_report.md`: independent proof audit.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question and Proposition 6.2.
- `code/crop_source.py`: reproducible source crop.

