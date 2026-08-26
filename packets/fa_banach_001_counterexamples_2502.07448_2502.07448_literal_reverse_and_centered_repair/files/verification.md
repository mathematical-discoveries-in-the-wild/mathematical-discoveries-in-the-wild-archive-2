# Verification report

Status: `candidate_full_counterexample_and_repair_likely_valid_needs_human_review`

## Mathematical audit

### 1. Literal counterexample

The source conjectures a lower bound for every absolutely continuous `f`.
Its left side sums only coefficients of degrees `k>=1`. For `f=1`, all of
those coefficients and `f'` vanish, but

```text
integral log^2(e+|x|) dmu > 0.
```

This disproves the exact published statement with no endpoint or regularity
qualification.

### 2. Hyperbolic-secant identities

For `nu(dx)=dx/[2 cosh(pi x/2)]`, the source generating function

```text
G(x,z)=exp(x arctan z)/sqrt(1+z^2)=sum P_n(x)z^n
```

has orthonormal coefficients. Differentiation in `z` and `x` directly gives

```text
x P_n=(n+1)P_{n+1}+nP_{n-1},
P_n'=sum_{r odd, r<=n} (-1)^((r-1)/2)P_{n-r}/r.
```

The proof packet derives both identities directly from the exact generating
function.

### 3. Derivative estimate

The derivative coefficient matrix has entries of magnitude `1/(n-m)` for
`n>m` of opposite parity. On an input block `n` of size about `2^j`, the near
output has convolution norm at most `C(j+1)` and occupies only neighboring
dyadic scales. The far output matrix has uniformly bounded Hilbert--Schmidt
norm because every denominator is at least `2^(j-1)`. Bounded overlap,
Minkowski, and Cauchy--Schwarz give

```text
||f'||_2^2 <= C sum_n log^2(e+n)|c_n|^2.
```

No cancellation in the alternating signs is needed.

### 4. Spatial logarithm

The Jacobi recurrence makes multiplication by `x` unitarily equivalent to

```text
J e_n=(n+1)e_{n+1}+n e_{n-1}.
```

With `B e_n=(n+1)e_n` and `A=(I+J^2)^(1/2)`, the two shifts give
`||A c||^2<=5||B c||^2`.

For a positive self-adjoint `T>=I`, quadratic `K`-functional minimization and
the spectral theorem give

```text
K_T(t,u)^2 = integral t^2 lambda^2/(1+t^2 lambda^2) d||E_T(lambda)u||^2.
```

Integrating this against `log(1/t)dt/t` on `(0,1)` produces a scalar weight
comparable to `(1+log lambda)^2`. Endpoint boundedness from `(H,D(B))` to
`(H,D(A))` therefore yields the logarithmic graph bound. Spectral calculus
then identifies it with

```text
integral log^2(e+|x|)|f|^2 dnu
  <= C sum_n log^2(e+n)|c_n|^2.
```

### 5. Measure transfer and the repaired equivalence

Under `y=pi x/2`, `nu` becomes density `1/[pi cosh y]`, universally
comparable with `exp(-|y|)/2`. Comparable measures have comparable best
polynomial approximation tails. Abel summation transfers every increasing
coefficient weight, including `log^2(e+k)`. The derivative and weighted
physical norms are also comparable.

Subtracting the constant coefficient before applying the two new model
estimates proves `Q_mu<=C S_mu`. Applying the source theorem to `f-a` and
taking the infimum proves `S_mu<=C Q_mu`. Closure of multiplication and weak
differentiation extends the result from polynomials to the full form domain.

### 6. Exact high-frequency stress family

For `f_t(x)=exp(itx)` in the `nu` model, the coefficients are exactly

```text
c_n=sech(t)[i tanh(t)]^n.
```

Their squared magnitudes are geometric with typical degree `exp(2|t|)`, so
the logarithmic coefficient form is of order `t^2`, matching
`||f_t'||_2^2=t^2`. This independently confirms the sharp scale.

## Upgrade-attempt audit

Seven focused passes are recorded in
`attempts/2502.07448_reverse_polynomial_inequality.md`:

1. the literal constant-kernel counterexample;
2. exact Meixner--Pollaczek matrices and finite-section stress testing;
3. a full dyadic proof of the derivative estimate;
4. a full limiting-interpolation proof of the spatial estimate;
5. bounded-density transfer and closure of the canonical two-sided repair;
6. the exact oscillatory stress family;
7. current-version and novelty searches.

The initial trivial counterexample was therefore upgraded to a full theorem
settling the intended invariant formulation.

## Computational audit

The included script tested dimensions `16,32,64,128,256` with 512 padding
modes. Largest generalized eigenvalues of repaired-right-side versus
coefficient form were

```text
1.995499, 1.995569, 1.995590, 1.995577, 1.995536.
```

At dimension 512, separate spatial and derivative maxima were `1.649397` and
`0.770385`. These checks are evidence only; no numerical assertion is used in
the proof.

## Literature and scope audit

- The run's four cheap indexes had no prior row for arXiv:2502.07448 or this
  reverse inequality.
- The June 17, 2025 authors' version and December 2025 journal publication
  still print the literal conjecture on PDF page 3 with the quantifier “any
  absolutely continuous function.”
- Bounded searches through 11 August 2026 used the exact arXiv id, conjecture
  wording, title plus reverse inequality, authors plus Meixner--Pollaczek, and
  later citations. No correction or answer was found.
- One later preprint cites the forward approximation result but does not
  discuss the conjecture.
- The packet claims only the one-dimensional symmetric exponential theorem.
  It does not assert a tensorized reverse theorem.
- The observations could be folklore or independently known; no priority
  claim is made.

## Rendering audit

- Final PDF: five US-Letter pages, 296537 bytes.
- `latexmk` completed all cross-reference passes.
- The final log contains no warnings, undefined references, overfull boxes,
  or underfull boxes.
- All five pages were rasterized at 130 dpi and visually inspected. The
  status box, source crop, theorem statements, proof-ending symbols,
  equations, references, margins, and page transitions are clean.
- `solution_packet.pdf` and `tmp/main.pdf` are byte-identical.
- Final SHA-256:
  `575e2d9bdbdf6fb717903b64ff9fcd5eec6dd311ebc0de04d26d4b6a76020e59`.

## Human-review focus

First confirm the published universal quantifier. Then independently verify
the scalar `K`-functional integral, the scale change in logarithmic graph
interpolation, and the Abel-summation transfer under comparable measures.
Those are the only nonroutine steps in the strengthened repair.
