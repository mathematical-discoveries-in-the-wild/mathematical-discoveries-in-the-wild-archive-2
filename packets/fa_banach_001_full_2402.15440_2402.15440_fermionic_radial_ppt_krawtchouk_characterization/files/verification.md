# Verification

## Formal proof audit

- For `q(A)=binom(|A|,2)`, `u_A=i^q(A)s_A` is a Hermitian unitary and the
  `u_A` form a Hilbert--Schmidt orthogonal basis.
- The reversal anti-automorphism fixing all Clifford generators is ordinary
  matrix transpose followed by a unitary conjugation. Its adapted maximally
  entangled projector and Choi state are therefore local-unitary conjugates
  of the standard ones; the paired first-leg reversal has the standard PPT
  spectrum even when reversal is of symplectic-transpose type.
- Reversal gives `Theta(u_A)=(-1)^q(A)u_A`.
- The normalized maximally entangled projector has coefficient `N^{-2}` in
  the unnormalized Pauli basis. Since `N^2=2^n`, the final normalization is
  `2^{-n}`.
- The commutation parity is
  `omega(A,C)=|A||C|-|A intersection C| (mod 2)`.
- Summing `(-1)^|A intersection C|` over `|A|=r` is exactly the binary
  Krawtchouk polynomial `K_r(|C|)`.
- The Bell vectors indexed by all subsets `C` are orthonormal and exhaustive,
  giving multiplicity `binom(n,c)` for the eigenvalue indexed by `c`.
- For the OU threshold, sufficiency uses `|(n-2c)theta|<=pi/4`. Necessity
  beyond the first sign change uses the semigroup law and preservation of PPT
  under local completely positive postcomposition, preventing later
  re-entry into the PPT region.
- The elementary entanglement-breaking region is a direct convex
  decomposition into the separable states proportional to
  `I tensor I +/- u tensor u`.

## Computational check

Run:

`conda run --no-capture-output -n sandbox python code/verify_spectrum.py`

The script constructs Jordan--Wigner Clifford matrices for `n=2,4,6`, forms
the normalized Choi matrix and its explicit partial transpose, and compares
all numerical eigenvalues with the signed Krawtchouk formula. It also compares
the OU Krawtchouk sum with the trigonometric closed form. The maximum observed
errors are at floating-point roundoff. This check is not used as proof.

## Source and novelty

- The open question is in Section 8, PDF page 36, of arXiv:2402.15440v6.
- The stored `source_paper.pdf` was rendered locally from the official v6
  arXiv TeX source because the already-ingested artifact was source-only.
- Searches on 11 August 2026 used the exact title and combinations of
  `fermionic radial multiplier`, `PPT`, `Krawtchouk`, `Clifford diagonal
  channel`, and `fermionic Ornstein--Uhlenbeck entanglement breaking time`.
  They found the source and general Bell-diagonal literature, but no later
  answer to this exact question or the displayed signed transform.

## Build and visual checks

- `latexmk -pdf` completed successfully with no warnings, overfull boxes,
  underfull boxes, or unresolved references in the final log.
- The final packet has four pages.
- All four pages were rendered at 125 dpi and inspected individually. The
  source crop, signed transform, adapted-transpose paragraph, OU threshold,
  EB interval, scope statement, and reference are legible with no clipping or
  layout defects.
