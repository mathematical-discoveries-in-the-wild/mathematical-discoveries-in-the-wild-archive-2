# Verification report

## Claim

For every absolutely continuous probability measure `mu` on `R^n` with finite
second moment and covariance `0 < Sigma <= I`,

```text
(1/2) W_2(gamma,mu)^2 - H(mu|gamma)
  <= (1/2) log det(Sigma) - tr(sqrt(Sigma)) + n.
```

If `Sigma <= beta I`, this implies the source conjecture with right side
`n(1 + log(beta)/2 - sqrt(beta))`.

## Independent line-by-line audit

1. **Transport identity.**  Let `X ~ gamma` and let `T = grad(phi)` be the
   Brenier map with `T(X) ~ mu`.  With `A = grad(T)`, change of variables gives

   ```text
   H(mu|gamma)
     = (1/2) E[|T(X)|^2-|X|^2] - E[log det(A)].
   ```

   Since `W_2^2 = E|T(X)-X|^2`, subtraction yields

   ```text
   deficit = n - E[X dot T(X)] + E[log det(A)].
   ```

2. **Gaussian integration by parts.**  If `M = E[A]`, then
   `E[X dot T(X)] = tr(M)`.  Also

   ```text
   M = E[(T(X)-E T(X)) X^T].
   ```

   Thus `M` is both the mean Jacobian and the cross-covariance matrix.  Since
   every `A` is symmetric positive semidefinite, so is `M`.

3. **Jensen step.**  Matrix `log det` is concave, so

   ```text
   E[log det(A)] <= log det(E[A]) = log det(M).
   ```

4. **Covariance step.**  The covariance of the joint vector `(T(X),X)` is

   ```text
   [ Sigma  M ]
   [ M      I ],
   ```

   which is positive semidefinite.  Its Schur complement gives
   `M^2 <= Sigma`.  Operator monotonicity of the square root gives
   `M <= sqrt(Sigma)`.

5. **Loewner monotonicity.**  Define

   ```text
   F(B) = log det(B) - tr(B) + n.
   ```

   If `0 < A <= B <= I`, then along `C_t=A+t(B-A)`,

   ```text
   d/dt F(C_t) = tr[(C_t^(-1)-I)(B-A)] >= 0.
   ```

   Hence

   ```text
   deficit <= F(M) <= F(sqrt(Sigma))
           = (1/2)log det(Sigma)-tr(sqrt(Sigma))+n.
   ```

6. **Scalar specialization.**  `Sigma <= beta I < I` gives
   `sqrt(Sigma) <= sqrt(beta) I`; applying the same monotonicity once more
   yields the source constant exactly.

7. **Equality.**  Equality in strict concavity of `log det` forces `A` to be
   constant almost everywhere.  Hence `T(x)=Mx+a` and `mu` is Gaussian.  The
   covariance and monotonicity equalities force `M=sqrt(Sigma)`.  In the
   scalar statement equality further forces `Sigma=beta I`.  Translations do
   not affect the deficit.

8. **Regularity.**  The proof is literal for smooth nondegenerate transport
   maps.  In general, let `A` be the Alexandrov derivative (the density of the
   absolutely continuous part of the distributional Hessian) and define `M`
   by cross-covariance.  Distributional Gaussian integration by parts gives
   `E[A] <= M`, since the singular Hessian measure is positive semidefinite.
   Hence `E log det(A) <= log det(E[A]) <= log det(M)`, which is exactly the
   inequality needed in place of smooth equality.  The generalized
   Monge--Ampere formula supplies the transport identity.  If relative entropy
   is infinite, the asserted inequality is immediate.

## Computational sanity check

Run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/verify_gaussian_formula.py
```

The script checks 10,000 random dimensions, covariance eigenvalue lists, and
translations.  It verifies that the closed-form Gaussian deficit equals the
anisotropic right side and that the latter is bounded by the scalar source
constant.  This checks formulas only; the proof is the analytic chain above.

## Novelty and scope

The cheap run indexes and a bounded primary-source search through 2026-08-09
found no explicit later resolution or statement of the anisotropic theorem.
The search included arXiv:2201.12478, arXiv:1906.05904, arXiv:1507.01086,
exact title/author searches, and combinations of “Talagrand deficit,” “small
covariance,” “Brenier,” and “log det.”  This is bounded novelty evidence.

## Human review focus

The finite-dimensional matrix chain is elementary once the transport identity
is accepted.  A human reviewer should focus on the approximation passage for
the source's full density class and on whether a prior paper contains the same
short argument under different notation.
