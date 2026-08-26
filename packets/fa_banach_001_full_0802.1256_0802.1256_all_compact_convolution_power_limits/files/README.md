# All nonsymmetric convolution-power limits on compact quantum groups

Status: candidate full analytical answer, likely valid, awaiting specialist
review. Novelty is provisional because the blockwise ingredients are standard.

Franz and Skalski ask in Section 4 of arXiv:0802.1256 for the limit behaviour
of nonsymmetric convolution powers on an arbitrary compact quantum group. This
packet gives a complete Peter--Weyl answer.

For a state `phi` and an irreducible unitary corepresentation `U^alpha`, put

`A_alpha=(id tensor phi)(U^alpha)`.

Every `A_alpha` is a finite contraction. The full weak-star cluster set of
`(phi^{*n})` is a compact monothetic group obtained by simultaneously rotating
the unit-circle eigenspaces of all the matrices `A_alpha`. Consequently:

- `phi^{*n}` converges iff every peripheral eigenvalue of every `A_alpha` is
  `1`;
- when it converges, its limit is the idempotent state whose Fourier matrices
  are the fixed-space projections of the `A_alpha`;
- the limit is Haar iff every nontrivial irreducible `A_alpha` has spectral
  radius strictly below `1`;
- the associated convolution operators converge point-norm on `C(G)` and
  strongly in the Haar GNS `L^2` realization;
- without convergence, all cluster states and their convolution law are still
  explicitly described.

The GNS reformulation identifies a peripheral phase with a vector on which the
corepresentation acts deterministically. This is the exact noncommutative
replacement for the classical periodic-coset obstruction at the analytical
level. The result permits atypical idempotent limits, as it must.

Contents:

- `main.tex` and `solution_packet.pdf`: theorem and self-contained proof.
- `source_paper.pdf`: arXiv:0802.1256.
- `figures/open_question_crop.png`: the source question.
- `VERIFICATION.md`: mathematical, literature, source, and PDF checks.
