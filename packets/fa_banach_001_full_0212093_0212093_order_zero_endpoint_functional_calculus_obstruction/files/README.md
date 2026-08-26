# Order-zero endpoint obstruction for arXiv:math/0212093

**Status:** candidate full solution, likely valid; human review requested.

Narinder S. Claire's *Functional Calculus for Semi-Bounded Operators*
(arXiv:math/0212093), Remark 1.4, conjectures that the Davies calculus on
`A = union_{beta<0} S^beta` cannot be extended to the endpoint `beta <= 0`.
This packet confirms the strong natural formulation: there is a closed,
densely defined operator `H` on `c_0` with spectrum `{e^n:n>=1}` and

```text
||(z-H)^(-1)|| <= 2*pi/|Im z|,
```

but no algebra homomorphism `Gamma:S^0(R)->B(c_0)` can extend the established
Davies--Helffer--Sjöstrand calculus on `A`.

The construction uses the summing basis `s_n=e_1+...+e_n` and the Schauder
multiplier `H s_n=e^n s_n`. Resolvent coefficients have bounded variation,
giving the strongest source exponent `alpha=0`. A smooth symbol
`f(t)=chi(t) cos(pi log t)` lies in `S^0` and takes values `(-1)^n` at the
eigenvalues. Multiplicativity and compactly supported spectral localizers
would force `Gamma(f)` to be the unbounded alternating-sign multiplier on the
summing basis.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_conjecture_crop.png`: source PDF crop containing Remark 1.4.
- `tmp/`: build products and rendered-page verification images.

The result does not rule out adjoining constants or other proper subalgebras
of `S^0`. Novelty confidence is moderate after bounded index and web searches;
expert literature review is still recommended.
