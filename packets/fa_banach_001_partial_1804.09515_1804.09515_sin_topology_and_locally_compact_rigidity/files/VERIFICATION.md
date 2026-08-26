# Verification report

Verdict: candidate partial result, likely valid.

## Mathematical audit

1. The Dowerk–Thom normal-generation estimates give a uniform exponent on
   every set where the relevant projective length is at least epsilon.
2. In a Hausdorff SIN topology, a sufficiently small invariant neighbourhood
   has an `N`th power missing a fixed nonidentity element. It therefore cannot
   contain any element of projective length at least epsilon. This proves the
   topology-refinement lemma with the correct direction.
3. In the II1 case, the projective 1-length and projective 2-metric induce the
   same topology by `ell_1 <= ell_2` and `ell_2^2 <= 2 ell_1`.
4. Invariant automatic continuity applies to the identity map from the strong
   topology into any separable SIN topology, giving the reverse refinement.
5. The Rademacher symmetries are uniformly separated in projective 1-length,
   so the strong topology is not precompact.
6. A continuous nest of projections in a diffuse abelian subalgebra gives an
   uncountable family of symmetries separated by `sqrt(2)` in projective norm;
   hence the type III projective norm topology is nonseparable.
7. Hausdorff precompact groups are SIN. Pulling a compact target topology back
   along a nontrivial homomorphism is legitimate because algebraic simplicity
   makes the homomorphism injective.
8. Strong uncountable cofinality applies to abstract isometric actions. In a
   second-countable locally compact group, Struble's proper left-invariant
   metric makes a bounded image have compact closure.

No computational experiment is used as proof.

## Literature/novelty audit

Searched exact source-question phrases and combinations of:

- `unique separable SIN group topology`
- `projective unitary group locally compact homomorphism`
- `PU(M) compact group II_1 factor`
- `type III factor separable SIN topology`
- arXiv:1804.09515 and the Dowerk–Thom citations arXiv:1506.08549 and
  arXiv:1606.00409

No explicit statement of the packet theorem was found through 17 August 2026.
The result is a short synthesis of published quantitative theorems, so the
novelty verdict is moderate rather than definitive.

## Packet audit

- Source PDF copied locally.
- Both source crops visually inspected and readable.
- LaTeX compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Every rendered packet page inspected at 144 dpi.
- Final log checked for overfull boxes, undefined references, and LaTeX
  warnings.

Human-review focus: the uniform-away-from-identity consequence of the cited
normal-generation functions and the precompact-topology argument.
