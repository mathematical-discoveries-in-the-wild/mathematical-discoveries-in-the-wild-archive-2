# Finite Blaschke Symbols Give Bounded Restricted Toeplitz Operators

Status: `partial_solution_likely_valid`

## Source question

Carlo Bellavita and Marco M. Peloso, "On Toeplitz operators on
`H^1(C^+)`," arXiv:2503.07281v1 (2025), Question 1 on PDF page 12.

The question asks whether there are inner functions other than the
exponentials `exp(i tau z)` for which

`T_{bar Theta}:H^1_Theta -> H^1(C^+)`

is bounded. By Theorem 1.3 of the source, this is equivalent to

`H^1_Theta = K^1_Theta direct-sum Theta H^1`.

## Result

Every nonconstant finite Blaschke product `B` on the upper half-plane has this
property:

`H^1_B = K^1_B direct-sum B H^1`.

Consequently the restricted Toeplitz operator `T_{bar B}:H^1_B -> H^1` is
bounded. In particular,

`B(z)=(z-i)/(z+i)`

already answers the existence part of Question 1 affirmatively. More strongly,
the packet classifies the entire rational-inner subcase: every nonconstant
rational inner function on the upper half-plane works.

This is a substantial partial answer, not a classification of all inner
functions. Infinite Blaschke products, singular inner functions, and general
meromorphic inner functions remain untreated.

## Proof Intuition

If `B` has degree `N`, division by `B` imposes exactly `N` zero-jet
conditions, so `H^1/BH^1` is `N`-dimensional. The annihilator `H^1_B` is one
hyperplane above `BH^1`, hence `H^1_B/BH^1` has dimension `N-1`.

The endpoint model space has exactly the same dimension. Writing the lower
half-plane pole polynomial as `Q`, a Fourier-support argument proves

`K^1_B={P/Q: deg P <= N-2}`.

Thus `K^1_B` injects into the `(N-1)`-dimensional quotient
`H^1_B/BH^1` with the full dimension and must fill it. This gives the desired
direct-sum identity. The degree-one case is especially transparent:
`K^1_B=0` and `H^1_B=BH^1`.

## Verification

- Repeated zeros are handled by Hermite jets through multiplicity minus one.
- The description of `K^1_B` is proved in the packet using analytic and
  anti-analytic Fourier supports; it is not assumed from a `p>1` projection.
- The `N=1` endpoint gives `K^1_B={0}`, consistent with the dimension count.
- The sum is topological: `BH^1` is closed and `K^1_B` is finite-dimensional,
  so the decomposition projections are bounded.
- No computation is used.

## Bounded novelty search

On 9 August 2026, the run's registry, solution, attempt, and proof-gap indexes
were searched for arXiv:2503.07281 and the core Toeplitz/Hardy/model-space
terms. Web searches used the exact paper title, the notation `H^1_Theta` and
`K^1_Theta`, the quoted equality, finite Blaschke products, and later work by
the source authors. The search found the source paper and general model-space
background but no separate work recording the finite-Blaschke answer. This is
a bounded search and does not guarantee novelty.

## Files

- `main.tex`: theorem, self-contained proof, verification, and references.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: official arXiv v1 PDF.
- `figures/open_problem_crop.png`: Question 1 on source PDF page 12.
- Attempt history:
  `runs/fa_banach_001/attempts/2503.07281_finite_blaschke_toeplitz.md`.

## Human review recommendation

Prioritize the Fourier-support proof of the exact formula for `K^1_B`, the
identification `ker J=BH^1` at the `H^1` endpoint, and the one-dimensional
drop from `H^1/BH^1` to `H^1_B/BH^1`.
