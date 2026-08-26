# Logarithmic-p randomized Dvoretzky: candidate full resolution

Status: **candidate full solution, likely valid**, pending specialist human
review.

Source: G. Paouris, P. Valettas and J. Zinn, *Random version of
Dvoretzky's theorem in* $\ell_p^n$, arXiv:1510.07284, Section 6, item 5 and
Proposition 6.2 (PDF page 39).

## Result

There are absolute constants $C_0,C,n_0$ such that, for $n\ge n_0$,
$p\ge C_0\log n$, $0<\varepsilon<1/3$, and $k>1$, if more than three
quarters of Haar-random $k$-subspaces of $\mathbb R^n$ are
$(1+\varepsilon)$-spherical in $\ell_p^n$, then

$$
k\le C\frac{\varepsilon\log n}{\log(1/\varepsilon)}.
$$

This supplies the sharp logarithmic denominator throughout the asymptotic
range $p\gtrsim\log n$ asked about in the source paper.

## Mechanism

For an $n\times d$ Gaussian matrix, align one coefficient direction with its
longest row. Its $\ell_p$ image norm dominates the maximum of $n$
independent $\chi_d$ variables. An orthogonal direction, conditioned on that
longest row, has projections stochastically dominated by independent scalar
Gaussians. At $p\ge C_0\log n$ this scalar Gaussian $\ell_p$ norm stays below
the sharp maximum threshold with fixed positive probability. The relative
$\chi_d$ excess is

$$
c\frac{d\log(e\log n/d)}{\log n},
$$

and inversion gives the claimed bound. Gaussian singular-value control
passes from coefficient directions to the ambient Euclidean sphere.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: packet source.
- `verification_report.md`: independent-style line-by-line proof audit.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question and Proposition 6.2.
- `code/crop_source.py`: reproducible source crop.

No computation is used as proof evidence. The result is not human verified.
