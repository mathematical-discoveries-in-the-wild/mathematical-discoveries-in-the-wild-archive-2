# Partial Result: The endpoint Lorentz case has the expected Hardy envelope

- **Source:** K. Leśnik, *Toeplitz and Hankel operators between distinct Hardy spaces*, arXiv:1708.00910.
- **Target:** Question 5.8 (Question 4 in the arXiv source), asking whether `H[Z]^ = H[Z^]` for every separable rearrangement-invariant quasi-Banach function space `Z` contained in `L^1`.
- **Status:** `candidate_full_solution_lorentz_endpoint_likely_valid; general_question_open`.
- **Model:** `GPT5.6`.

## Result

For every `0 < q < 1`,

```text
Banach-envelope(H[L^{1,q}(T)]) = H^1(T)
                                 = H[Banach-envelope(L^{1,q}(T))]
```

with equivalent norms.  This is an endpoint case not covered by the source lemma: `L^{1,q}` has upper Boyd index `1`, so the Riesz projection is not bounded on the ambient quasi-Banach lattice.

The packet also proves a general atom criterion.  If `Z^ = L^1` and the analytic projections of normalized real `H^1` atoms are uniformly bounded in `Z`, then the desired envelope identity holds for `Z`.

## Proof idea

The Banach envelope of `L^{1,q}` is `L^1`.  A normalized real `(1,2)` Hardy atom supported on an arc of length `delta` has analytic projection `b=P_+a` satisfying

```text
b*(t) <= C (delta t)^(-1/2),  t <= C delta,
b*(t) <= C delta/t^2,         t >= C delta.
```

Both pieces have uniformly bounded `L^{1,q}` quasi-norm.  A finite real-`H^1` atomic decomposition of the real part of an analytic polynomial therefore decomposes the polynomial into `H[L^{1,q}]` vectors with total cost controlled by its `H^1` norm.  The reverse inequality follows from `L^{1,q} -> L^1`.

An outer-truncation lemma shows that analytic polynomials are dense in `H[Z]` for every separable rearrangement-invariant quasi-Banach lattice `Z -> L^1`: truncate an outer factor by a contractive outer multiplier, approximate the resulting bounded analytic function radially, and use order-continuous dominated convergence.  Hence the two norm estimates on polynomials identify the completed spaces.

## Scope

This completely answers the source question for the full endpoint Lorentz family `L^{1,q}`, `0<q<1`, and supplies a reusable criterion for other spaces whose Banach envelope is `L^1`.  The general question remains open: an arbitrary `Z` need not have envelope `L^1`, and even in that case its quasi-norm need not uniformly control the projected Hardy atoms used here.

## Files

- `main.tex` — theorem, proof, density lemma, scope, and novelty audit.
- `solution_packet.pdf` — compiled proof packet.
- `source_paper.pdf` — official arXiv source PDF.
- `VERIFICATION.md` — mathematical and presentation checks.
