# Verification record

## Formal checks

1. For the Euclidean witness, the projection identity is a rank-one
   decomposition of the identity. Its trace is bounded by Cauchy--Schwarz,
   while random phases identify the square sum of the output vectors with a
   lower bound for the operator norm.
2. For `H_q={z in C^(q+1): sum z_i=0}`, any `q` distinct evaluations form an
   isomorphism. Its unique inverse copies the sampled values and assigns
   their negative sum to the omitted coordinate, so the norm is exactly
   `q`.
3. In the block construction, injectivity consumes exactly the ambient
   dimension `n` as compulsory samples. Since `k+1` hard blocks cannot all
   receive an extra sample from a budget of `k`, one remains at the exact
   interpolation threshold.
4. In the upper bound, adjoining `1` makes the sparse measure mass equal to
   its squared norm on the constant function. The upper BSS frame bound
   therefore gives `nu(D)<=gamma`, which is the step needed to control
   arbitrary bounded inputs.
5. Weighted least squares is an orthogonal projection for the discrete
   inner product. The lower BSS inequality makes this inner product definite
   on the reconstruction space.

## Computational checks

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2401.02220_sampling_projection_tradeoff/code/verify_finite_witnesses.py
```

The script checks exact-sampling hyperplanes through dimension 12, the block
count formula for a grid of `(n,k)`, and the scalar simplification of the
upper bound.

An additional scratch LP tested tensor-product candidates. It found best
norms `3,2` for `H_2 tensor H_2` with `4,5` samples and `4,3,2` for
`H_2 tensor H_3` with `6,7,8` samples. This ruled out the naive tensor route
as an upgrade mechanism; it is not part of the proof.

## Literature/novelty checks

- Exact arXiv-id/title and exact open-phrase searches.
- Keyword searches for `n+k sampling projection`, near-critical
  oversampling, weighted BSS, coordinate projections, and few-facet norming
  sets.
- arXiv:2202.12625 for the complex preconditioned BSS estimate.
- arXiv:2603.02459 for the 2026 weighted norming-set consequence.

The survey already contains the weighted norming-set ingredient, so novelty
is not claimed for sparsification itself. No located source states the
block-hyperplane lower bound or `Pi(n,n+1)=Theta(n)`.
