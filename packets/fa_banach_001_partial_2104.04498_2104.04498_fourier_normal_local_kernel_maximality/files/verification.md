# Verification report

Verdict: candidate substantial partial result, likely valid.

## Exact target and scope

Question 2 of arXiv:2104.04498 asks whether the coefficient integral is at
most `pi^2/2` everywhere in the interior of `E(S^1)`, with equality exactly on
the embedded open hemisphere.  The packet proves a sharp second-variation
formula, global stationarity of the hemisphere profiles, and a nonlinear local
theorem at the north pole on the Fourier-normal slice.  It does not claim the
global inequality.

## Proof audit

1. For `a=cos(f)`, antiperiodicity and the slope inequality follow directly
   from `f(alpha+pi)+f(alpha)=pi` and `|f'|<=1`.
2. The displayed identity for `p-1` is a direct common-denominator expansion.
3. On odd Fourier mode `n`, translation orthogonality reduces the quadratic
   form to one scalar trigonometric integral.  The finite sine-sum identity
   gives exactly `-pi(n-1)`, including the zero first mode.
4. Splitting at angular separation `pi/2` writes `q` in terms of either
   `(a(alpha)-a(beta))^2` or `(a(alpha)+a(beta))^2`.  Antiperiodicity turns the
   latter into another short-distance difference quotient.  The standard
   circle `H^(1/2)` identity therefore bounds `int |q|` by the odd Fourier
   `sum n(A_n^2+B_n^2)`.
5. With the first mode absent, `n <= 3(n-1)/2`.  The exact nonlinear identity
   then makes every denominator correction `O(||a||_infinity^2)` times the
   negative spectral gap; the remaining quartic term has favorable sign.
6. For a hemisphere profile, the first variation reduces to two elementary
   weighted finite-Hilbert-transform integrals, which cancel exactly.

## Computational check

Run:

```sh
conda run --no-capture-output -n sandbox python code/verify_kernel.py
```

The midpoint quadrature converges to the exact eigenvalues for odd modes
1,3,5,7,9,11, and 1,000 random nonsingular pairs satisfy the exact nonlinear
identity to floating-point accuracy.  Earlier constrained searches at 12, 20,
and 32 nodes found no counterexample.  None of these finite checks is proof.

## Eight focused attempts

1. Cosine-coordinate/Gram-determinant reduction: successful.
2. Finite Lipschitz optimization: no violation; evidence only.
3. De Sitter/Lorentz reformulation: no global integral inequality.
4. Exact Fourier Hessian: successful.
5. Nonlinear remainder absorption: successful.
6. Full-hemisphere stationarity identity: successful strengthening.
7. Pointwise local-density factorization: explicitly false.
8. Global Fourier/Morse--Bott upgrade: blocked by nonlinear mode coupling and
   the absence of a global admissible gauge.

## Literature and novelty check

The cheap run indexes had no hit for arXiv:2104.04498 or the exact coefficient
inequality.  Bounded exact-phrase, title, author, citation, and keyword searches
found the source and papers citing its broader filling-area context, but no
later resolution of Question 2.  Novelty confidence is moderate pending a
specialist search.

## Recommended expert checks

1. Check the coefficient normalization in the full-square symmetrization.
2. Check the `H^(1/2)` estimate at both the diagonal and antipodal diagonal.
3. Check differentiability under the integral in the hemisphere-stationarity
   proposition.
4. Assess whether the stationarity identity can be combined with a weighted
   transverse Hessian to remove the north-pole/Fourier-normal restrictions.

