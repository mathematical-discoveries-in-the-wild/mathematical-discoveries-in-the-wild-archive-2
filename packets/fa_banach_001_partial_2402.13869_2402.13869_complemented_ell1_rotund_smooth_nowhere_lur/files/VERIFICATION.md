# Verification report

Verdict: **candidate partial solution likely valid**.

## Exact claim checked

For every separable real Banach space `X` containing a complemented copy of `ell_1`, the packet constructs an equivalent norm `M` which is rotund, Gâteaux smooth, and octahedral. Hence no point of `S_(X,M)` is LUR.

This answers the source Problem 3.7 only on the complemented-`ell_1` class.

## External input checked

Cobollo–Hájek, arXiv:2408.03737:

- Theorem 1.1 gives an equivalent Gâteaux-smooth octahedral norm on every Banach space admitting a Gâteaux-smooth norm and containing a complemented copy of `ell_1`.
- Their decomposition is `X=X_0⊕ell_1`, with canonical vectors `e_n` and partial projections `P_n`.
- Proposition 2.6 gives, for every `eta>0` and all sufficiently large `n`,
  `N(P_(n-1)x + alpha e_n) >= (1-eta)(N(P_(n-1)x)+|alpha|)`.
- The defining unit-sphere formula and `f_n(1)=1` give `N(e_n)=1`.

The source paper’s Theorem 3.3 already guarantees a Gâteaux-smooth equivalent norm on every separable `X`, so the supporting theorem’s smooth-renormability hypothesis is satisfied.

## Internal construction audit

1. Since `X_0` is separable, a countable weak-star dense sequence in `B_(X_0*)` separates points.
2. Its weighted evaluation map into `ell_2` is bounded and injective. The pullback Hilbert norm `q_0` is continuous, strictly convex, and Gâteaux smooth away from zero.
3. `r_0=N|_(X_0)+q_0` is equivalent and Gâteaux smooth. Equality in its triangle inequality forces equality for `q_0`, hence positive collinearity, so `r_0` is strictly convex.
4. The norm
   `h(x_0+sum a_j e_j)^2 = r_0(x_0)^2 + sum 4^(-j)|a_j|^2`
   is continuous, injective, strictly convex, and Gâteaux smooth. It need not be equivalent. Crucially, `h(e_n)=2^(-n)` and the `n`th coordinate is Hilbert-orthogonal to `P_(n-1)X`.
5. `M=N+h` is equivalent because `N` is equivalent and `h` is continuous. It is Gâteaux smooth as a sum. Equality for `M` implies equality for `h`, so strict convexity of `h` makes `M` rotund.

## Octahedral estimate audit

Fix finite-dimensional `F`, `0<epsilon<1`, and `eta=epsilon/4`. Strong convergence `P_n→I` is uniform on the compact `M`-unit sphere of `F`; hence for large `n`, with `p=P_(n-1)y` and `E=M(y-p)`, one has `E<=eta M(y)`.

Let `c_n=M(e_n)=1+2^(-n)` and `u_n=e_n/c_n`. For large `n`, `1/c_n>=1-eta`. The supporting tail estimate and the orthogonality of `h` yield

`M(y+alpha u_n)`

`>= (1-eta)(M(p)+|alpha|/c_n)-E`

`>= (1-3eta+eta^2)M(y)+(1-eta)^2|alpha|`.

Both coefficients are at least `1-epsilon` for `eta=epsilon/4`. This proves octahedrality. No unproved uniformity or limiting interchange remains.

For any `x` on the unit sphere, octahedrality on `span{x}` produces unit `u_k` with both `M(x+u_k)→2` and `M(x-u_k)→2`. Therefore `x` is not LUR.

## Deep-upgrade attempts

1. **Full all-separable upgrade via octahedrality:** blocked structurally, because octahedral renormability is equivalent to containing `ell_1`; this omits spaces such as `ell_2`.
2. **Remove complementability:** Cobollo–Hájek explicitly leave this smooth-octahedral extension open. Proving it would enlarge the class to spaces containing non-complemented `ell_1`, but would still not solve the source problem.
3. **Arbitrary octahedral norm plus compact injective perturbation:** a selected compact-small sequence does not automatically retain one uniform octahedral witness sequence, and the Gâteaux-smooth octahedral input is unavailable in the non-complemented setting. Not promoted.
4. **Equivalent rotund perturbation:** creates a fixed positive cost on normalized witnesses and can destroy the asymptotic constant. Replaced by the continuous non-equivalent `h` with vanishing witness cost.

No credible line from this mechanism remains toward spaces without `ell_1`; moving on after promotion is justified.

## Novelty bounds

The four cheap run indexes and bounded arXiv/web searches were checked on 2026-08-11 for the arXiv id and close phrases including “rotund octahedral”, “strictly convex octahedral Gâteaux smooth”, and “complemented ell_1 no LUR points”. The decisive later paper arXiv:2408.03737 proves smooth octahedrality but does not state the rotund or nowhere-LUR strengthening. No exact prior statement was found. This supports only **moderate**, not exhaustive, novelty confidence.

## Human-review focus

- Verify that the supporting norm’s full-space notation indeed gives the quoted Proposition 2.6 estimate with `N(e_n)=1`.
- Verify Gâteaux differentiability of `h` at points where one direct-sum component is zero (the squared norm has derivative zero at zero).
- Verify the explicit constants in the octahedral estimate.
- Keep the result scoped to real scalars and complemented `ell_1`.

No computational code was used; the verification is deductive.
