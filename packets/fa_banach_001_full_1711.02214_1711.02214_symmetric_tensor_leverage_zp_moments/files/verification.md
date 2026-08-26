# Verification report

## Algebraic audit

- The feature normalization satisfies
  `<t^{tensor k}, x^{tensor k}> = <t,x>^k`.
- The lifted denominator is exactly
  `<t^{tensor k}, A t^{tensor k}>^{1/2}`.
- If `A` is singular, `Phi(X)` lies in `ran(A)` almost surely because every
  vector in `ker(A)` has zero squared pairing in expectation.
- The expected leverage score is `tr(A^dagger A) = rank(A)`.
- `dim Sym^k(R^n) = binom(n+k-1,k)` and the binomial estimate used for the
  constants has the correct exponent.
- Both polarity directions were checked directly from their unit balls.

## Computational check

`code/verify_tensor_leverage.py` tested 80 weighted finite distributions in
R^2, including lifted moment matrices with rank below `dim Sym^k(R^2)`, for
k=1,...,5. It verifies the leverage trace identity and samples 60,001
rank-one directions for each support point. Result:

    PASS: 80 finite-distribution cases
    checked E leverage = rank, including singular lifted matrices
    smallest sampled rank-one/full-tensor squared ratio: 0.797074

This check validates normalization and pseudoinverse handling only. The proof
in `main.tex` is exact and does not rely on numerical approximation.

## Reviewer focus

1. Confirm the rank-one-to-full-tensor supremum enlargement.
2. Confirm the simultaneous almost-sure range argument for singular A.
3. Confirm that `M_r <= a M_p` implies `Z_p <= a Z_r`.
4. Treat the result as solving Problem 1's first formulation; do not infer a
   solution of Problem 2 for q > p.
