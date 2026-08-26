# Verification report

**Verdict:** `likely valid; human review recommended`

## Mathematical checks

- The source statement was verified on page 10, Remark 3.3, of the local source
  PDF.  The crop includes the whole question and its displayed formula.
- The integer-radius issue was checked exactly.  If
  `a^2-D b^2=1`, `K=J b v`, `N=J a`, and `v.q=0`, then
  `|K+q|^2=N^2-J^2+|q|^2`; hence `|K+q|<=N` iff `|q|<=J`.
- The Fock limit was checked symbolically from the polar-coordinate density.
  Under normalized `|e_K|^p` mass, each `t_j=pi|z_j|^2` is Gamma with shape
  `pK_j/2+1` and rate `p/2`.  The exact Gamma moment formula in the proof gives
  convergence of each fixed monomial ratio to 1 in `L^p`.
- The lattice `H_v={q:v.q=0}` has rank `d-1` because `v` is primitive.  When
  `d>=3`, the transferred cutoff is an ellipsoid multiplier in dimension at
  least two, where Fefferman's theorem applies after de Leeuw dilation.
- Endpoint failure does not rely on endpoint transference: the tensor slice
  `g tensor h_0 tensor ... tensor h_0` reduces the spherical sum exactly to the
  one-dimensional Hermite partial sum on `g`; `p=infinity` follows by duality.

## Computational check

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2601.04893_spherical_hermite_sums_d_ge_3/code/verify_pell_and_gamma.py
```

The script checks the first eight Pell solutions for representative dimensions
`d=3,4,5,9,16`, radii `J=1,2,5`, and many bounded vectors in the orthogonal
lattice.  It also prints Gamma-moment errors for positive and negative shifts
at growing base indices.  This supports, but does not replace, the proof.

## Novelty check

Bounded search performed on 2026-08-11:

- local registry, solution, attempt, and proof-gap indexes for arXiv:2601.04893
  and the core phrases;
- exact source title and `spherical partial sums Hermite modulation spaces`;
- `ball multiplier Fock spaces monomial partial sums`;
- `Bargmann Fock monomial multipliers converse Fourier multipliers`;
- `Pell equation Fock space multiplier transference`.

The search found the source preprint, general Hermite-multiplier work, classical
Fock-space literature, and standard ball-multiplier references, but no later
answer to Remark 3.3 and no matching Pell-slice proof.  Novelty confidence is
bounded rather than exhaustive.

## Human-review focus

1. Confirm the normalization-independent Fock-to-torus limit lemma.
2. Confirm that the standard de Leeuw dilation theorem applies to the
   discontinuous ellipsoid indicator via its null boundary.
3. Confirm the `M^1-M^infinity` adjoint identification for the endpoint claim.
4. Keep the result classified as partial because the intermediate `d=2` range
   remains open.
