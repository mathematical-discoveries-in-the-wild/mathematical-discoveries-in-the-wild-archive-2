# Verification Report

Candidate: arXiv:2511.04565, uniform regular-polygon extension

## Claim checked

For `N >= 1`, `c > 0`, and `xi` on the unit circle, let

`mu = c sum_{j=0}^{N-1} delta_{xi exp(2 pi i j/N)}`.

The Cauchy dual of multiplication by `z` on the Dirichlet-type space
`D(mu)` is subnormal exactly for `N=1,2`.

## Verdict

`likely valid` (substantial partial result)

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Rotation reduction | valid | Rotating the measure gives the cited unitary equivalence up to a unimodular scalar, which preserves subnormality. |
| Root-of-unity norm sum | valid | Expanding `(z^N-1)/(z-zeta_j)` and summing over `j` kills all unequal Fourier modes, leaving `N` terms each contributing `N`. |
| Spectral factor | valid | `rho+rho^{-1}=2+cN^2` gives `2+cN^2-z^N-bar(z)^N=rho^{-1}|z^N-rho|^2` on the unit circle; `rho>1` puts all roots of `q` outside the closed disk. |
| Formula for `f_j` | valid | Direct differentiation gives `O'(zeta_j)=-N sqrt(rho) zeta_j^{-1}/(rho-1)`; polynomial division gives the displayed Fourier numerator. |
| Gram entries | valid | The diagonal logarithmic derivative is `(N-1)/(2 zeta_i)+N/(zeta_i(rho-1))`; the off-diagonal Costara formula and `(rho-1)^2=cN^2rho` give the circulant matrix in the packet. |
| DFT eigenvalues | valid | For `u_m=(zeta_j^{-m})`, the sum `sum_{k=1}^{N-1} omega^{(m+1)k}/(1-omega^k)=m-(N-1)/2` yields `c(N/(rho-1)+m)`. All eigenvalues are positive. |
| Finite-kernel coefficients | valid | Orthogonality of the Fourier vectors, with the conjugated inverse Gram matrix in the Costara kernel formula, yields `h_m=N rho(rho-1)/(N+m(rho-1))`. Conjugation/indexing was checked independently in code. |
| Numerator polynomial | valid | Subtracting `(1-t) sum h_m t^m` from `(rho-1)(rho-t^N)` gives zero constant term and `A_k=h_{k-1}-h_k` (with the correct last endpoint); this simplifies to the positive formula in the packet. |
| Collision-safe forbidden atoms | valid | Equal pole products are grouped. For fixed nonzero `d`, all `N` summands have the same numerator and denominator, giving `C_d=P(a^2 omega^d)/(N rho^2 a^2 omega^d)`. This avoids relying on a distinct-cross-product corollary. |
| Root contradiction | valid | If all forbidden values vanished, `P(x)/x` would have exactly the `N-1` nontrivial rotated roots. Comparing the constant and linear coefficients forces `A_2/A_1=a^{-2}`. The explicit ratio violates this for `N>2`; the derivative argument is strict. |
| Positive cases | valid by citation | `N=1` is the known one-atom case; `N=2` is the known antipodal two-atom case. |

## Computational reconstruction

`code/verify_uniform_ngon.py` constructs the Costara Gram matrix directly,
numerically inverts it, reconstructs the full numerator kernel, and compares
its coefficients to the closed formula.  The suite tested

- `N = 2,3,4,5,8`,
- `c = 0.03,0.37,1,9`,
- positivity of every `A_k`,
- the `N=2` forbidden-value cancellation,
- nonvanishing in every tested `N>=3` case, and
- the strict coefficient-ratio inequality used in the proof.

All 20 cases passed.  The largest coefficient reconstruction error was below
`7.3e-9` (the assertion tolerance is `2e-7` in the largest-scale case).

## Counterexample / loophole search

- A separate general three-atom reconstruction was tested on asymmetric
  support and unequal masses; it produced nonzero forbidden atoms.
- Optimization for simultaneous off-diagonal Gram zeros moved toward the
  collision/extreme-mass boundary rather than finding an interior zero.
- The proof does not infer pairwise vanishing when pole products collide; it
  uses the grouped necessary measure and therefore closes that potential
  loophole.
- `N=2` was included as a regression test and does cancel exactly, matching
  the known positive theorem rather than falsely proving non-subnormality.

## External dependencies

- Costara's finitely-supported Dirichlet-space kernel formulas.
- Chavan--Ghara--Reza's rational de Branges--Rovnyak model and necessary
  forbidden-atom measure condition.
- Their established one-atom and antipodal two-atom subnormality results.

The new algebra after those quoted results is explicit and independently
reconstructed by the verifier.

## Gaps and scope limitations

- No proof gap was found in the regular-polygon theorem.
- The source's full conjecture for arbitrary three distinct support points and
  arbitrary positive masses remains open.
- The novelty search is bounded; originality is plausible, not certified.

## Confidence

Score: 97/100

The residual uncertainty is concentrated in literature novelty and human
confirmation that the published numbering/formulation of the cited necessary
condition matches the arXiv source.  The mathematical calculation itself has
multiple independent checks.

## Human review recommendation

`send to human`

Primary review focus: the conjugation convention in the finite-kernel formula,
the DFT eigenvalue indexing, and the grouped coefficient `C_d`.

