# Verification

## State-space counterexample

- A singleton is a closed analytic strongly orthogonal family under the usual
  pairwise-distinct convention.
- A state has nonzero support because it takes value one on the identity.
- If `supp(phi)=1`, no state can be strongly orthogonal to `phi`.
- The normalized trace on `M_2` has support `I`.
- For `A=K(ell_2)+C1`, the standard bidual is `B(ell_2) direct-sum C`.
- The chosen density `diag(2^-n)` has trivial kernel and trace one; positive
  weights on both bidual summands give support `(I,1)`.

## Lambda correction

- Along a fixed word of length `n`, the recursive cylinder mass is a product
  of `n` independent uniform factors; replacing a factor by `1-U` preserves
  its distribution.
- `integral_0^1 sqrt(u)du=2/3`.
- Cauchy--Schwarz gives
  `sum_{|s|=n}sqrt(mu(U_s)) <= 2^(n/2)`.
- The decay constant is `2sqrt(2)/3`, whose square is `8/9<1`.
- Hellinger affinity is bounded above by every partition affinity and vanishes
  exactly for mutually singular measures.
- Countable intersections preserve probability one.
- The second-moment recursion for atomlessness uses
  `E[U^2+(1-U)^2]=2/3` and correctly handles all possible atoms via a countable
  union over mass thresholds.

## Source and novelty

- The official arXiv page identifies v5 from 13 May 2022 as the latest version.
- The source questions are on PDF page 18 and Question 3.6 / Claim 3.7 are on
  PDF page 19.
- Exact-phrase searches found the claim repeated in the author's 2026 thesis
  and found no correction or exact reverse result.

## Build and visual checks

- `latexmk` completed successfully with all citations and references resolved.
- The final packet has four pages and a clean log with no overfull or
  underfull boxes.
- All four pages were rendered to PNG at 130 dpi and visually inspected.
- Both source crops are legible; no packet text, equations, or figures are
  clipped or overlapping.
