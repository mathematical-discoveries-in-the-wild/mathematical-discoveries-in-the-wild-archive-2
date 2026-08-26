# All-cocancelling endpoint Lorentz question answered

Status: `literature_already_answered`

## Source question

Felipe Hernandez and Daniel Spector, *Fractional Integration and Optimal
Estimates for Elliptic Systems*, arXiv:2008.05639, Calc. Var. PDE 63 (2024),
Paper No. 117.

Section 2, arXiv PDF page 9, says it was unknown whether the optimal estimate

`||I_alpha F||_{L^{d/(d-alpha),1}} <= C ||F||_1`

holds for every homogeneous cocancelling constraint `L(D)F=0`.

## Separate literature answer

Dmitriy Stolyarov, *Hardy--Littlewood--Sobolev inequality for p=1*,
arXiv:2010.05297, Sb. Math. 213 (2022), 844--889, answers this in stronger
form. Theorem 1.2 (arXiv PDF page 7) maps every closed translation- and
dilation-invariant constrained space without point masses into the endpoint
Besov--Lorentz space. Equation (1.18) and Corollary 1.7 (page 3) yield the
requested Lorentz estimate.

For `W = ker L(D)`, a nonzero `a tensor delta_0` belongs to `W` exactly when
`a` belongs to the intersection of the kernels of the symbols `L(xi)`.
Therefore Stolyarov's no-point-mass hypothesis is exactly cocancellation and
his theorem covers every homogeneous order.

Breit, Cianchi, and Spector, *Riesz potential estimates under co-canceling
constraints*, arXiv:2512.06352, independently make the identification
explicit. Equation (1.8) on arXiv PDF page 3 states the precise endpoint
Lorentz estimate for arbitrary homogeneous cocancelling operators, and the
authors attribute the first-order and higher-order cases to the intervening
literature. Theorem 3.1, page 10, is a further rearrangement-invariant
extension.

The Euclidean all-cocancelling question is fully answered. The distinct torus
question mentioned on source PDF page 4 is outside this packet.

Files:

- `source_paper.pdf`: exact compiled arXiv source for arXiv:2008.05639.
- `supporting_paper_2010.05297.pdf`: Stolyarov's arXiv PDF.
- `supporting_paper_2512.06352.pdf`: exact compiled arXiv source for the later
  explicit synthesis/generalization.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.
