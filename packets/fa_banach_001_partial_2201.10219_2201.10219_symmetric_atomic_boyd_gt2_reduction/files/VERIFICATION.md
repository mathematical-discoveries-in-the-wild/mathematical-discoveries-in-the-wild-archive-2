# Verification record

## Mathematical checks

- The exact questions were checked on page 23 of the locally compiled
  arXiv:2201.10219 source.
- The source factorization lemmas and projection fundamental-function
  identities were checked on pages 18--21.
- The statement that the standard atomic/algebraic equality remains open was
  checked on page 14 of arXiv:2001.08775.
- Proposition 3.9 (standard crude `(p,2)` atoms decompose into `(p,2)` atoms)
  was checked on pages 10--11 of that paper.
- Theorem 4.3 (every `(p,2)` atom decomposes into `(p,infinity)` atoms with
  controlled `ell_p` coefficients) was checked on page 17.
- Every exponent conversion in the crude-atom argument was independently
  recomputed: `1/u=1/p-1`, `1/s=1/p-1/2`,
  `1/v=(1/2)(1/p-1/q)`, and
  `1/s-1/v=(1-p)/(2p)+1/(2q)>0`.
- The proof uses only equivalent norm comparisons, so the equivalent
  Banach renorming of `E^(1/2)` changes constants but not the resulting
  atomic space.

## Computational check

`code/check_exponents.py` checks the exact rational identities and strict
embedding inequality for 9,900 admissible pairs `(p,q)` (69,300 exact checks)
and also verifies the atom-normalization exponent cancellations.

## Artifact checks

- `source_paper.pdf`: 25 pages.
- `supporting_atomic_paper.pdf`: 32 pages.
- `source_factorization_and_question.pdf`: 6 pages; the factorization, atom
  definition, and open-question pages were visually inspected.
- `supporting_atomic_results.pdf`: 4 pages; the open-problem and
  `(p,infinity)`-decomposition pages were visually inspected.
- `solution_packet.pdf`: 3 pages; compiled twice with no warnings, overfull
  boxes, underfull boxes, or unresolved references.
- The final packet was rendered to 3 RGB PNGs at 170 dpi and every page was
  visually inspected after the final compilation.
- Packet SHA-256:
  `07ed88daff6a08f50209844c7920054cdd6b15cf1e701c82370b7500533eaf6b`.
