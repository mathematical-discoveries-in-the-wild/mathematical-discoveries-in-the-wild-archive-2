# Verification report

Verdict: candidate substantial partial result, likely valid.

## Exact target and scope

Bayart's Question 4.6 asks whether Corollaries 4.4 and 4.5 remain true for
polynomials instead of linear forms.  The packet completely proves the
weighted-backward-shift half, under a weaker hypothesis.  It does not claim
the parabolic-composition half.

## Proof audit

### 1. Canonical measure

With `s_n=(w_1...w_n)^{-1}` and `s in ell^p`, the random series
`X=(s_n gamma_n)` belongs to `ell^p` almost surely because its expected
`p`-th norm power is finite.  In the complex case the coordinates are
standard circular complex Gaussians.  Its law is Gaussian and has full support
over the relevant real or complex scalar field.
The coordinate identity `w_{n+1}s_{n+1}=s_n` proves invariance.  Cylinder
functions become independent after a sufficiently large shift, and density
of cylinders proves strong mixing.

### 2. Diagonal multilinear lemma

For an `r`-linear form `A` on `ell^p`, `r<p`, every block diagonal
`(A(u_n^1,...,u_n^r))` with the `u_n^j` supported in coordinate `n` lies in
`ell^t`, `t=p/(p-r)`.  After complexifying the underlying real space, average
the `r` inputs after multiplying their `n`-th coordinate blocks by the same
independent `r`-th root of unity; only the pure block-diagonal terms remain.  This gives a
bounded functional on `ell^{p/r}`, hence the claimed dual exponent.  The real
case follows by complexification.  For `r>=p`, boundedness is enough.

### 3. Random derivative coefficients

`D^rP(X)[e_n,...,e_n]` is a Gaussian polynomial of uniformly bounded degree.
Fixed-degree Gaussian polynomial `L^q` norms are uniformly equivalent.  This
can be proved from Gaussian hypercontractivity and Paley--Zygmund, so it is
independent of the number of active Gaussian coordinates.

Setting the `n`-th Gaussian coordinate to zero is also uniformly bounded on
the degree-bounded Gaussian polynomial subspace.  Expanding in Hermite
polynomials of that coordinate makes this a finite-dimensional coefficient
extraction estimate.  This avoids the false independence assumption that
would arise by Taylor expanding around a vector containing the replacement
Gaussian.

### 4. Physical dependence

In the stationary extension

    Y_k=P((s_n gamma_{n+k})_{n>=0})-E P(X),

replacing `gamma_0` has no effect for `k>0`, and for `k=-n` it changes only
coordinate `n`.  Taylor expansion around the vector with that coordinate
deleted yields

    delta_{-n,2} <= sum_{r=1}^d C_r s_n^r b_{n,r}.

For `r<p`, `(b_{n,r})` lies in `ell^{p/(p-r)}` and `(s_n^r)` lies in
`ell^{p/r}`.  For `r>=p`, the first sequence is bounded and `sum s_n^r` is
finite.  Thus the physical-dependence sum is finite.

### 5. CLT and zero variance

Proposition 2 of El Machkouri--Volný--Wu gives absolute covariance
summability and variance convergence.  If the long-run variance is positive,
their Theorem 1 applies to intervals because the partial-sum variance then
diverges linearly.  If it is zero, variance convergence directly gives
`S_N/sqrt(N) -> 0` in `L^2`.  Hence a Gaussian limit, possibly degenerate,
holds in every case.

## Eight focused attempts

1. **Canonical Gaussian coding (successful).**  The exact invariant-measure
   condition `s in ell^p` gives an explicit independent-coordinate Gaussian
   model and an exact orbit formula.
2. **Global polynomial Lipschitz estimate (rejected).**  It gives only
   `delta_n=O(s_n)` and wrongly demands `s in ell^1`, so it loses the sharp
   Banach-space duality.
3. **Coordinate Taylor expansion (successful).**  Splitting by Taylor order
   exposes `s_n^r` and diagonal coefficients of `D^rP`.
4. **Diagonal multilinear summability (successful).**  Root-of-unity
   averaging yields the sharp exponent `p/(p-r)`, exactly conjugate to
   `p/r`.
5. **Independent deletion expansion (successful repair).**  Expanding around
   the input with the changed coordinate set to zero restores independence;
   Hermite coefficient extraction controls the deleted-coordinate value.
6. **Exact summability upgrade (successful).**  The proof needs only
   `sum W_n^{-p}<infinity`, not a pointwise polynomial lower bound on `W_n`.
7. **Gaussian eigenvector-field route for the parabolic operator (blocked).**
   The available Hölder exponent is below `1/2`; the resulting correlation or
   innovation bounds are not summable, even before nonlinear products.
8. **Source Bernoulli coding for the parabolic operator (blocked).**  The
   source obtains a summable aggregate cancellation for linear forms, but
   individual translation vectors decay only as `n^{-beta}`, `beta<1`.
   Polynomial Taylor terms destroy the linear aggregate cancellation, and no
   summable physical-dependence bound results.

## Literature check

The cheap run indexes had no hit for arXiv:1304.2621 or the exact polynomial
question.  Bounded web searches used the exact wording of Question 4.6, the
paper title and author, and combinations of `weighted backward shift`,
`Gaussian invariant measure`, `polynomial`, and `central limit theorem`.
They found no later resolution.  The supporting physical-dependence theorem
was checked in arXiv:1109.0838 and in its published version, DOI
10.1016/j.spa.2012.08.014.

## Recommended expert checks

1. Check the real complexification constant in the diagonal lemma.
2. Check the two-real-component reduction for circular complex Gaussians and
   the Hermite coefficient-extraction estimate uniformly in `n`.
3. Check the exact use of Proposition 2 and Theorem 1 of the supporting CLT
   paper in the zero and positive long-run variance cases.
4. Assess novelty against specialist weighted-shift and Gaussian dynamical
   systems literature.
