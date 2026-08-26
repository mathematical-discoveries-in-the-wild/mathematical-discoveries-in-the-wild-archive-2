# Exact convergence criterion for Binet factorial series

Status: `candidate full solution (likely valid; expert review requested)`

Source: P. Van Mieghem, *Binet's factorial series and extensions to Laplace
transforms*, arXiv:2102.04891v7, Section 8.4, PDF page 38.

## Result

For fixed `beta>0`, `alpha in C`, put

`G(u)=(1-u)^(-alpha) f(-beta Log(1-u))=sum a_m u^m`

and `w=beta*z+alpha`. The source factorial expansion is

`beta sum a_m B(m+1,w)`.

For every `Re(w)>0`, it converges if and only if the ordinary Dirichlet series

`sum_(m>=1) a_m m^(-w)`

converges. The equivalence includes conditional convergence; absolute
convergence is equivalent as well. The proof uses the gamma quotient as a
two-way bounded-variation multiplier.

This gives a sharp transformed-radius trichotomy:

- `R_G>1`: absolute convergence at every relevant parameter;
- `R_G<1`: divergence everywhere, since terms do not tend to zero;
- `R_G=1`: exact ordinary Dirichlet-series abscissae and boundary behavior.

The transformation from the analytic germ of `f` to `G` is bijective, so
arbitrary Dirichlet coefficients can occur. This proves the criterion is
optimal in the generality asked.

Finally, the packet gives two Laplace-transformable functions with the same
Taylor radius `R_f=log(5/2)`: one has `R_G=3/2` and converges absolutely
throughout `Re(z)>0`, while the other has `R_G<1` and diverges for every fixed
`z`. Thus `R_f` alone cannot answer the question.

## Files

- `main.tex`, `solution_packet.pdf`: full theorem and proof.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: readable full-width crop of PDF page 38.
- `verification_report.md`: proof and rendering audit.
- `novelty.md`: bounded literature-search record and conservative novelty
  assessment.

The packet does not claim that conditional convergence alone always justifies
termwise evaluation of the improper Laplace integral. It proves equality under
absolute convergence, where Tonelli applies.
