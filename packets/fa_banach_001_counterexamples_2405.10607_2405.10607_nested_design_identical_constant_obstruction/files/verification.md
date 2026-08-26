# Verification report

Status: candidate full counterexample, likely valid, pending human review.

## Analytic checks

- Subtracted the two unnormalized equal-weight quadrature identities and
  checked that the added multiset is exactly a lower-strength design.
- Checked that the Delsarte--Goethals--Seidel lower bound quoted in the source
  has asymptotic constant `2^(1-d)/d!` times `s^d` in both parity cases.
- Compared `C_d((n+1)^d-n^d)=O(n^(d-1))` with the layer lower bound
  `Omega(n^d)`.
- Checked the stronger asymptotic-leading-coefficient formulation.
- Checked that summing strict consecutive layers gives `Omega(T^(d+1))`.
- For the circle construction, checked root-set containment, exact Fourier
  moments through the required strength, and both cardinality inequalities.

## Scope checks

- The negative theorem is tied to the source's explicit exact-coefficient
  definition of “of order” and its identical-constant clause.
- Merely comparable cardinalities with unrelated constants remain open for
  dimensions `d>=2`.
- The chain lower bound assumes a nonempty new layer at each consecutive
  strength.

## Build and visual audit

The final packet is compiled with `latexmk -pdf` in a temporary directory.
Every final page is rendered with `pdftoppm` and visually inspected. Source
PDF pages 6 and 12 are cropped reproducibly by `code/crop_source.py`.

Final outcome on 11 August 2026: `latexmk` completed with no remaining
warnings, undefined references, overfull boxes, or underfull boxes. Text
extraction found four pages and 7,474 characters. All four pages were rendered
at 150 dpi and visually inspected after the final edit; no clipping, overlap,
illegible formula, or malformed crop was found. The packet SHA-256 is
`811391d82d8fd50d5b4c29b412ae6eeb374505fda942e4bec4aa245f6c59678b`.
The 19-page source PDF has SHA-256
`f8d982d7e82844ce7f968221d78110a10d137fd8ed8f2ce4bc09568d6ce0f812`.

## Literature check

Bounded searches on 11 August 2026 covered the exact arXiv id, title,
conjecture wording, and the main obstruction keywords. The 2024 journal
article retains the conjecture. A January 2026 survey still describes the
optimal-order bound as believed and cites only the source's special-ratio
case. A later draft on random weighted quadrature gives empirical discussion,
not the equal-weight complement theorem. No direct resolution found in this
search. This is not an exhaustive novelty guarantee.

## Human-review recommendation

Verify the interpretation of “identical constants” against the source's page
6 definition and confirm that the quoted lower bound is being used under the
same multiset convention. The proof itself is otherwise a direct moment
subtraction and cardinality comparison.
