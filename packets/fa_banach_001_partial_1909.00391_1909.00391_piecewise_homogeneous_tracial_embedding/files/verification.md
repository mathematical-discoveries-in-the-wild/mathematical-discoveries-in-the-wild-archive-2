# Verification record

## Mathematical audit

1. The supporting input is exactly Theorem 4.7 of arXiv:2307.04452: for every
   tracial `JW*`-factor with separable predual and every `1 <= p < infinity`,
   its nonassociative `L^p`-space is the range of a positive contractive
   projection on the `L^p`-space of a finite von Neumann algebra.
2. For a finite measure space, the exact vector-valued interpolation identity
   with endpoint exponents infinity and one gives
   `(L^infinity(Omega;F), L^1(Omega;F_*))_{1/p}
   = L^p(Omega;(F,F_*)_{1/p})` isometrically.  Thus tensoring/pointwise
   applying the factor projection has precisely the desired homogeneous
   nonassociative range.
3. A normal finite faithful trace on a countable central sum has strictly
   positive summand weights.  Both associative and nonassociative `L^p`
   norms decompose as the same weighted `ell^p` norm.  Therefore the
   coordinatewise direct sum of the homogeneous projections remains positive,
   idempotent, and contractive.
4. No claim is made for non-piecewise-constant measurable fields.  No claim is
   made for nontracial states or for the full forward implication of
   Conjecture 6.1.

## Artifact audit

- `source_paper.pdf`: 32 pages; exact conjecture is on PDF page 27.
- `supporting_paper_2307.04452.pdf`: 26 pages; factor theorem is Theorem 4.7
  (PDF page 19), and the remaining tracial conjecture/direct-integral
  obstruction is on PDF page 20.
- `figures/open_conjecture_crop.png` is generated from page 27 by
  `code/make_crop.py`.
- `solution_packet.pdf` is compiled from `main.tex` and every rendered page is
  visually inspected after the final build.
- Final packet SHA-256:
  `89dec24eca38d9bc0bf701a2a68192aa8690523a9dc83999b06051dacb9c4a72`.
