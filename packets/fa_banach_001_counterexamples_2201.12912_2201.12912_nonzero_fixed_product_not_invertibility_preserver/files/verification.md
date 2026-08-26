# Verification report

## Claim checked

Problem 3.5 of arXiv:2201.12912 has a negative answer, even for a separable
commutative algebra, an involutive linear map, and `c=d` a nonzero idempotent.

## Hypothesis checklist

- The weight `rho_n=exp(-n^2)` is submultiplicative because
  `rho_(m+n) <= rho_m rho_n`.
- Weighted `ell_1` convolution is therefore a commutative Banach algebra.
- Two nonzero series have a nonzero coefficient at the sum of their least
  nonzero indices, so the algebra is an integral domain.
- For the generator `z`, `||z^n||^(1/n)=exp(-n)->0`. Finite polynomials in
  `z` are dense; spectral mapping and spectral-radius subadditivity for
  commuting elements show that every element is quasinilpotent. Thus the
  algebra is radical.
- In the unitization `A`, exactly the elements with nonzero scalar coordinate
  are invertible. Hence `A` is a domain with dense invertible group.
- The coefficient functional at `z` is bounded. Consequently
  `A=C1 direct-sum Cz direct-sum R_0` topologically, and the map swapping `1`
  and `z` is a bounded complex-linear involution.
- `E=C x A` is a separable commutative unital Banach algebra with dense
  invertibles.
- If `xy=(1,0)` in `E`, the second coordinates have product zero in the
  domain `A`, so one is zero. This proves the required fixed-product identity
  for every such pair, not merely a dense family.
- `d=(1,0)` is nonzero. The unit `(1,1_A)` maps to `(1,z)`, whose second
  coordinate is not invertible. Thus the exact proposed conclusion fails.

## Proof-risk review

The construction does not assume that a nonzero element of a radical algebra
is invertible. The radical algebra is first unitized; radicality is used only
to show `lambda 1+r` invertible when `lambda != 0`. Conversely, the quotient
onto `C` proves that an element with scalar coordinate zero is not invertible.
The direct product is essential: it makes `d` nonzero while retaining a zero
product in the domain coordinate.

No finite computation is used as proof. Earlier finite-dimensional searches
are recorded only in the attempt note.

## Source and artifact checks

- Source PDF: 9 pages, arXiv version dated May 2022.
- Open question: Problem 3.5, source PDF page 6.
- The screenshot crop was rendered from that PDF at 180 dpi and visually
  checked for complete readable text.
- The final packet PDF was compiled with `latexmk`, checked for LaTeX
  warnings/errors, rendered page-by-page, and visually inspected.

## Novelty audit

On 2026-08-11 the local registry, solution, attempt, and proof-gap indexes
were searched using the arXiv id, title, and core terms. External exact/close
searches used the Problem 3.5 wording and combinations of `fixed product
preserving`, `invertibility`, `counterexample`, `integral domain`, `radical
Banach algebra`, and `dense invertibles`. The audit included the source and
publisher pages and search-indexed portions of Hayden Julius's 2026 chapter
*Fixed Product Preserving Mappings on Rings and Algebras*. No prior explicit
answer or matching construction was found. The publisher lists seven citing
works, but not all full texts were individually inspected. Novelty confidence
is therefore **moderate**, not definitive.

