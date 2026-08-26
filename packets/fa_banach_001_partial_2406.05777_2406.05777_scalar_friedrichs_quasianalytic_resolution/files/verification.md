# Verification Report

Candidate: arXiv:2406.05777v2, Question 3, scalar models
`A_c=-d/dx+c(x)`.

## Claim checked

For every `c in L^2_loc(R)` with `0<delta<=Re c<=M`, the maximal closed
realization is Krylov-solvable for every quasi-analytic datum. The packet also
gives an exact weighted-derivative criterion for all smooth data, proves the
positive class is dense, and retains a constant-coefficient Schwartz datum
whose solution is not Krylov and whose Carleman series converges.

## Verdict

Likely valid coefficient-wide strong partial result. Confidence: 94/100.

The result covers the entire scalar coefficient class in (4.5), subject only
to mild local regularity needed to define the integrating factor, and includes
(4.4). Since Question 3 is worded as an open-ended investigation rather than a
binary conjecture, `partial` is the conservative protocol class. Under the
natural scalar formulation “find a broad sharp sufficient class and determine
whether smoothness suffices,” the packet is a full resolution.

## Step-by-step audit

| Step | Status | Verification |
| --- | --- | --- |
| Stable inverse formula | valid | Exponential stability makes `R=int_0^infinity T(t)dt` converge in operator norm. The integrated generator identity and closedness give `AR=I`; differentiating an orbit gives `RA=I` on `dom A`. |
| Smooth scalar orbit | valid | A `C^infinity(A)` vector has `phi_h^(n)(t)=<T(t)(-A)^n g,h>`; group boundedness on compact time intervals gives derivative bounds uniform in `t`. |
| Carleman criterion | valid | For `M_n=C_I ||A^n g|| ||h||` and `beta_n=inf_{k>=n} M_k^(1/k)`, `1/beta_n >= M_n^(-1/n)`. Thus the vector Carleman sum implies the Denjoy-Carleman criterion on every compact interval. |
| Orbit in Krylov closure | valid | If `h` annihilates the Krylov closure, every derivative of `phi_h` at zero vanishes. Quasi-analyticity forces the whole scalar orbit to vanish, hence every `T(t)g` belongs to the Krylov closure. Its Bochner integral belongs there as well. |
| Weighted unitary | valid | `Uq=e^C q` satisfies `||Uq||_2=||q||_{L^2(omega dx)}` exactly for `omega=e^(2 Re C)`; no bounded-similarity assumption is made. |
| Differential expression and domain | valid | The weak product rule gives `UBU^(-1)f=-f'+cf`. Defining `A_c` unitarily gives the maximal distributional domain. If `c` is bounded, this reduces to `H^1`. |
| Translation group | valid | Local comparability of the weight gives a strongly continuous two-sided translation group. For positive time, `omega(y-t)/omega(y)<=e^(-2 delta t)`; for negative time the upper real-part bound gives local exponential growth. |
| Physical group formula | valid | Conjugation gives `T_c(t)g(x)=exp(-int_0^t c(x+s)ds)g(x+t)`, with norm at most `e^(-delta t)` for `t>=0`. |
| Exact criterion | valid | Under `U^(-1)`, powers of `A_c` become signed derivatives of `q=e^(-C)g`; signs do not affect their span. The inverse becomes the weighted-space tail integral, yielding the stated if-and-only-if condition. |
| Pointwise tail integral | valid | Cauchy-Schwarz with `omega^(-1)` and `omega(y)>=omega(x)e^(2 delta(y-x))` gives absolute convergence on every right half-line. |
| Dense analytic vectors | valid | Every `C_0` group has a global exponential bound. Gaussian convolution is an approximate identity; integration by parts and Hermite `L^2` estimates give `||A^n x_s||<=C_s D_s^n sqrt(n!)||x||`, so the regularized vectors are analytic and dense. |
| Constant Fourier model | valid | With `m=1-i xi`, the isometry `J_g(p)=p g-hat` identifies the closed Krylov space with the weighted polynomial closure, and the inverse with `r=(1-i xi)^(-1)`. |
| Exponential-tail density | valid | A polynomial-orthogonal witness defines a finite measure with an analytic bilateral Laplace transform flat at zero; analytic continuation and Fourier uniqueness force it to vanish. |
| Lognormal obstruction | valid | The explicit sine perturbation annihilates every integer moment. Cauchy-transform injectivity supplies an affine alignment with a nonzero resolvent pairing. The square-root density is Schwartz after zero extension and affine transport. |
| Counterexample outside QA class | valid | On `log X in [2n,2n+1]`, the `2n`th lognormal moment contributes at least `c exp(2n^2)`, so `||A^n g||>=c_1(a/2)^n exp(n^2)` and the Carleman series converges. |

## Adversarial checks

- A naive integrating factor is unbounded on ordinary `L^2`; the proof avoids
  this by changing the Hilbert-space weight so the map is unitary.
- A semigroup orbit defined only for positive time would put the flat point at
  an endpoint of the scalar interval. The hypothesis and application use a
  full group, so Denjoy-Carleman uniqueness is applied around zero.
- Bounds on `Re c` alone do not make multiplication by `c` bounded. The proof
  asserts the `H^1` domain only for bounded `c`; otherwise it uses the maximal
  unitarily defined domain.
- Moment indeterminacy alone does not imply that the particular inverse
  multiplier lies outside the polynomial closure. The affine Cauchy-transform
  alignment provides the required nonzero pairing.
- A smooth counterexample does not contradict a quasi-analytic theorem. The
  explicit power-norm lower bound proves the counterexample's Carleman sum is
  finite.

No contradiction or unproved finite-dimensional/numerical dependency was
found.

## Computational regression check

`code/lognormal_sanity.py` evaluates the exact moment formula for `n=0,...,8`
and numerically samples the unshifted Cauchy pairing at `z=-i` using 80-digit
quadrature. This is only a sanity check; the proof uses an existential Cauchy
transform argument.

Run with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2406.05777_scalar_friedrichs_quasianalytic_resolution/code/lognormal_sanity.py
```

## Literature audit

The source paper and arXiv:1811.08202, 2001.08127, 2102.13626, and 2210.04752
were inspected; exact-title/author and close-phrase arXiv/web searches were
also performed. Chernoff's 1975 article was checked as the classical
Denjoy-Carleman/quasi-analytic-vector reference. No later paper explicitly
resolving Question 3, and no stable-group theorem in the exact Krylov form
used here, was located. This is a bounded novelty check, not proof of novelty.

## Remaining verifier focus

1. Confirm the chosen formulation of the Denjoy-Carleman criterion directly
   against Chernoff or a standard monograph.
2. Check the maximal distributional-domain identification for coefficients
   with unbounded imaginary part under the stated `L^2_loc` hypothesis.
3. Compare the abstract stable-group theorem with later semigroup cyclicity
   literature not captured by the bounded search.
4. Decide whether the source's open-ended “investigate” wording merits
   promotion from a strong partial packet to a full scalar-resolution packet.

## Human review recommendation

Send to an operator theorist familiar with `C_0` groups and quasi-analytic
vectors. The central proof is short and self-contained modulo the classical
Denjoy-Carleman theorem. The strongest novelty claim should remain provisional
until specialist literature review.

