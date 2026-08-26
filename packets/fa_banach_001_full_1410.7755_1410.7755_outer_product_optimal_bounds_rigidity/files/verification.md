# Verification record

Verdict: `candidate_full_solution`, likely valid, expert review requested.

## Proof audit

1. The induced outer-product Gram matrix is
   `H_ij=|<phi_i,phi_j>|^2`, is positive semidefinite, and has trace `M`.
2. Frame-potential plus Rayleigh quotient gives `lambda_1>=M/N`.
3. Trace averaging gives
   `lambda_M <= (M-lambda_1)/(M-1) <= M(N-1)/(N(M-1))`.
4. Equality at the final lower bound forces equality throughout: the spectrum
   is `M/N` once and `M(N-1)/(N(M-1))` with multiplicity `M-1`.
5. The resulting rank-one perturbation of a scalar matrix has unit diagonal,
   hence every coordinate of its exceptional eigenvector has modulus
   `1/sqrt(M)`.
6. Every off-diagonal entry is already a nonnegative real squared inner
   product, so its fixed modulus forces the common value
   `(M-N)/(N(M-1))`.
7. The resulting frame potential is `M^2/N`; equality in Cauchy--Schwarz for
   the frame-operator eigenvalues forces tightness.
8. The converse follows by diagonalizing `(1-c)I+cJ`.
9. The optimal-gap statement follows by adding the two nonnegative defects
   `B-M/N` and `M(N-1)/(N(M-1))-A`.

## Edge-case audit

- `M>N>1` ensures the two spectral values are distinct and the common squared
  angle is positive.
- Lower equality is positive, so it automatically implies that the outer
  products are a Riesz sequence.
- Upper equality alone is weaker and is not claimed to force equiangularity.
- If no ETF with parameters `(N,M)` exists, the universal lower bound and
  minimum gap are strict for every frame.

## Provenance

- Archived arXiv source SHA-256:
  `a5a16c45b32b26caf68119dfa8fefe35ef32a49ef36af28ea965afecc3bd27d8`.
- Compiled `source_paper.pdf` SHA-256:
  `f67fce2f940e3d813656bfd4d9d527b1188a8a26871180f64babcab55ef24601`.
- `figures/source_bounds_crop.png` SHA-256:
  `024b6de9f5be5b324ccdc752ee9f08abd6cc808455ee37b4d731a50a0ad5cf97`.
- `figures/source_question_crop.png` SHA-256:
  `d8c4d34090b133924a8f98aa53e1d9437eae0728225fa1088645f20be84a0bf4`.
- Both crops were rendered at 180 dpi and visually inspected.

## Novelty search bounds

Checked the run's cheap indexes and parsed arXiv corpus for `1410.7755`, the
exact title, the authors, `outer product` near `Riesz bound`, and
`equiangular` near `outer product`.  The only later parsed arXiv source found
citing the paper was arXiv:1710.07561, whose citation is unrelated to the
optimal-bound equality case.  No duplicate or later answer was found in the
local corpus.  Novelty confidence is moderate pending specialist review.

## Mechanical check

`verify_constants.py` uses exact rational arithmetic for all
`2 <= N < M <= 80` and verifies the identities for `alpha`, `beta`, `c`, the
two eigenvalues of `(1-c)I+cJ`, and the optimal gap.

## Final packet QA

- Final packet: 3 US-letter pages.
- `tmp/main.log` contains no LaTeX warnings, overfull or underfull boxes, or
  unresolved-reference messages.
- Ghostscript `nullpage` validation and full `txtwrite` extraction succeeded.
- All three rendered pages were visually inspected at original detail; no
  clipping, collisions, stray blank pages, or unreadable evidence were found.
- Final `solution_packet.pdf` SHA-256:
  `a8f7c454fe2563c1a2b3dec367c15aa9cd4472cf1e81735e67d6797b72548469`.
