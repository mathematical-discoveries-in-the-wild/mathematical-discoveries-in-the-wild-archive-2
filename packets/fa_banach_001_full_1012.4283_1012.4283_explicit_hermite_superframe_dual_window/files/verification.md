# Verification report

Verdict: likely valid explicit dual-window construction; novelty provisional.

## Algebraic checks

- With `S=sigma^N=z^N q`, the function `q` is holomorphic and nonzero at
  zero, so every Taylor truncation of `1/q` is well-defined.
- The identity `q [1/q]_{N-1-j}=1+O(z^{N-j})` implies
  `E_j=z^j/j!+O(z^N)`. Therefore its derivatives of orders `0,...,N-1` at
  zero are exactly the Kronecker data required by the Hermite interpolation
  problem.
- At every nonzero point of the conjugate adjoint lattice, `q` has a zero of
  order `N`. Hence all derivatives through order `N-1` of every `E_j` vanish
  there.
- Restoring the scale `s(Lambda) sqrt(pi^j j!)` matches the unnormalized
  Bargmann–Hermite formula in arXiv:0804.4613 exactly. Substitution gives
  `s(Lambda)^(-1) <gamma_j, pi_mu H_l> = delta_(mu,0) delta_(j,l)`, the full
  matrix Wexler–Raz relation. In particular, the proof does not make the
  invalid shortcut of combining scalar duals, which would not kill the
  off-diagonal terms.

## Functional-analytic checks

- The modified sigma estimate has Gaussian exponent
  `pi N s(Lambda)/2`. Since `N s(Lambda)<1`, multiplication by the Fock
  weight leaves an integrable Gaussian. The finite Laurent-looking sum has
  no singularity at zero because the Taylor identity makes `E_j` entire.
- The Bargmann characterization of `M^1` therefore places every dual
  component in the Feichtinger algebra. Both vector Gabor systems are
  Bessel, so Wexler–Raz applies.
- Finite-component analysis and synthesis maps with `M^1` windows are
  bounded on coordinatewise vector modulation spaces. The Hilbert identity
  consequently extends by density to `M^p`, with the standard weak-star
  endpoint interpretation.
- Applying the polyanalytic Bargmann transform componentwise yields the
  displayed explicit sampling kernel and the same lattice phases as the
  source's scalar formula.

## Low-order checks

- `N=1`: the formula is a constant multiple of `sigma_Omega(z)/z`, the
  familiar scalar explicit dual.
- `N=2`: direct Taylor multiplication gives
  `E_0=q(q_0^(-1)-q_1 q_0^(-2)z)` and `E_1=zq/q_0`; their jets are
  `(1,0)` and `(0,1)` respectively.
- Symbolic checks with generic Taylor coefficients through `N=8` confirmed
  `E_j=z^j/j! mod z^N` for every `j`.

## Literature check

The run indexes and full local arXiv-source corpus were searched for the
source id/title, `dual vectorial window`, `dual superwindow`, `explicit dual
Hermite`, and `Gabor superframe`. The arXiv API was queried for the exact
phrase and for Hermite-superframe/dual-window combinations. The only directly
relevant records found were arXiv:0804.4613 and arXiv:0901.4386. The former
contains the implicit triangular ansatz but not the inverse-Taylor formula.

## Visual verification

- `source_paper.pdf` opens as a 17-page letter-size PDF.
- The source remark was located on page 15, rendered at 180 dpi, and cropped
  from the real source page.
- The final packet was compiled with `latexmk` and all rendered pages were
  visually inspected for clipping, overflow, broken equations, and figure
  legibility.

