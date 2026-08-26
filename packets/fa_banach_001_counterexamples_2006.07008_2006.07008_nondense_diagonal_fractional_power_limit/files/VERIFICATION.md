# Verification report

Verdict: candidate full counterexample to the open problem as stated, likely valid, requiring expert review.

## Structural audit

1. **Banach space and domain.** (X=\ell^\infty(\mathbb N)). If
   (x\in D(A)), then (x_k=O(k^{-1})), so (D(A)\subset c_0). Finite
   sequences lie in (D(A)), hence \(\overline{D(A)}=c_0\ne X\).
2. **Closedness.** If (x^{(j)}\to x) and (Ax^{(j)}\to y) in
   \(\ell^\infty\), coordinate evaluation gives (y_k=kx_k). Thus
   ((kx_k)=y\in\ell^\infty), so (x\in D(A)) and (Ax=y).
3. **Positivity.** For \(\lambda>0\),
   \((\lambda+A)^{-1}\) is multiplication by \((\lambda+k)^{-1}\), maps
   (X) onto (D(A)), and
   \(\|\lambda(\lambda+A)^{-1}\|\le1\). Also (0\in\rho(A)), with
   (A^{-1}) multiplication by (k^{-1}). Hence (A) is positive in the
   source's terminology.
4. **Fractional powers.** The bounded operator (B=A^{-1}) is diagonal with
   entries (k^{-1}). Its Balakrishnan--Komatsu power is diagonal with
   entries (k^{-\alpha}), by the scalar beta integral (and the integral
   converges in operator norm). Since the source defines
   (A^\alpha=(B^\alpha)^{-1}) when (0\in\rho(A)),
   \(D(A^\alpha)=\{x:(k^\alpha x_k)\in\ell^\infty\}\) and
   \((A^\alpha x)_k=k^\alpha x_k\).
5. **Admissible parameters and vector.** For \(\alpha=n+it\) with
   (n\in\mathbb N\) and (t\ne0), let \(\beta=\alpha+1\). Then
   \(\alpha,\beta\in\mathbb C_+\) and
   \(\operatorname{Re}\beta>\operatorname{Re}\alpha\). The vector
   (x_k=k^{-\alpha}) lies in (Xcap D(A^\alpha)), and
   (A^\alpha x=\mathbf1\).
6. **Bochner integrability at finite cutoff.** For every (N<\infty), the
   integrand in (2.37) is norm integrable over ((0,N)). Near zero its norm
   after division by \(\lambda\) is (O(\lambda^{n-1})); away from zero it
   is norm continuous.
7. **Exact integral evaluation.** Coordinate (k) of the normalized
   truncated expression is obtained from
   \(((\lambda+A)^{-\beta}z)_k=(\lambda+k)^{-\beta}z_k\) and
   \((A^\beta z)_k=k^\beta z_k\), and is
   \[
     \alpha\int_0^N \lambda^{\alpha-1}k(\lambda+k)^{-\alpha-1}\,d\lambda
     =\alpha\int_0^{N/k}u^{\alpha-1}(1+u)^{-\alpha-1}\,du
     =\left(\frac{N}{N+k}\right)^\alpha,
   \]
   because the integrand is the derivative of
   \((u/(1+u))^\alpha\). Principal powers are unambiguous on positive real
   scalars.
8. **Failure of norm convergence.** Each truncated sequence lies in (c_0).
   For each fixed (k), its (k)-th coordinate tends to (1). If the
   truncations converged in \(\ell^\infty\), continuous coordinate
   evaluations would force the limit to be \(\mathbf1\), but closedness of
   (c_0) would force the limit to lie in (c_0), a contradiction.
9. **Exact target conclusion.** The vector satisfies the premise
   (x\in D(A^\alpha)), but the limit in (2.37) does not exist. This gives a
   negative answer to Remark 2.11 in the paper's nondense-domain generality.

## Adversarial checks

- Replacing the exceptional exponent by any \(\alpha\in\mathbb C_+\) leaves
  the computation unchanged, confirming that the mechanism is domain density,
  not a branch singularity at integer real part.
- The proof does not infer operator-norm convergence from coordinatewise
  convergence; it uses precisely their failure to agree on \(\ell^\infty\).
- Choosing \(\beta=\alpha+1\) is permitted even though it is nonreal: only
  positive real parts and the strict real-part inequality are required.
- (A) is invertible in the unbounded-operator sense: (A:D(A)\to X) is
  bijective and (A^{-1}\in\mathcal L(X)). Surjectivity of the bounded inverse
  as a map (X\to X) is not required; its range is (D(A)).
- No cancellation or conditional improper integration is used at finite (N).

## Computational check

`code/verifier.py` compares midpoint quadrature of the coordinate integral
against the closed form for several cutoffs and coordinates at
\(\alpha=1+0.7i\), and reports finite-section distances from the constant-one
vector. This is a sanity check only; the exact derivative computation is the
proof.

## Literature and novelty audit

- No hit in `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  or `proof_gaps/index.tsv` for the arXiv id, source title, or core phrases.
- Searched the exact source title/arXiv id, “mystery of imaginary powers,” the
  exact \(n+it\) formulation, the cited Chen--Li characterization, and later
  title/citation variants.
- Searched combinations of fractional powers of non-densely defined
  operators, diagonal operators on \(\ell^\infty\), (c_0), and the gamma
  normalized integral.
- Background papers on non-densely defined fractional powers were found, but
  no explicit later answer to Remark 2.11 and no matching diagonal
  counterexample was located.

Novelty confidence: moderate and provisional.

## Reviewer focus

The decisive scope check is whether the open problem is read literally in the
paper's general framework, which explicitly permits non-densely defined
operators. The decisive mathematical checks are the fractional-power domain
of the diagonal operator and the one-line antiderivative. If density was
silently intended, the construction instead proves that a density hypothesis
cannot be omitted.

## Packet QA

The final six-page PDF compiled without substantive warnings. Every page was
rendered to PNG and visually inspected. The two source crops together include
the complete normalized limit (2.37), Lemma 2.10, and Remark 2.11 at readable
review scale; the separate introduction crop documents the nondense-domain
scope. No proof text, display, citation, or source statement is clipped.
