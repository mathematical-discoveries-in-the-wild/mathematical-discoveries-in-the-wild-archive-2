# Verification record

## Statement audit

- The source question is transcribed verbatim from Remark 3.8.
- The model `n=N=1`, `D=-i d/dx`, `B=I` satisfies the source assumptions.
- The source explicitly gives `I_{D,I}=(1,infinity)`.
- With `delta=1/p-1/q`, the source constant reduces to
  `c_{p,q}=(1-delta)^-1`, so its requested range is
  `K<sigma(1-delta)`.
- The candidate theorem proves the stronger range `K<=sigma+delta` at
  `tau=delta`.

## Proof audit

1. Fourier diagonalization gives multiplier `g(xi)psi(t xi)`.
2. Normalization `eta=t xi` gives `h_t(eta)=g(eta/t)psi(eta)`.
3. Cauchy disks of radius comparable to `|eta|` remain in a fixed bisector
   component; positive scaling preserves the component. Hence the derivative
   estimates are uniform in `t` and depend on `g` through `||g||_infinity`.
4. On frequency `|eta|~2^j`, the normalized amplitude is
   `2^(j sigma)` for `j<=0` and `2^(-j delta)` for `j>0`.
5. Rescaling plus repeated integration by parts gives
   `|k_{t,j}(x)| <= C_M 2^j a_j(1+2^j|x|)^(-M)`.
6. The sum of bandwise `L^1` norms is finite. Splitting the pointwise sum at
   `2^j|x|~1` gives near-zero power `delta-1` and far power `-1-sigma`.
7. Scaling back yields domination by
   `t^(-delta)|x|^(delta-1)`, exactly the one-dimensional Riesz kernel.
8. Hardy--Littlewood--Sobolev gives the global `L^p -> L^q` estimate.
9. For separated sets, Young's inequality with
   `1/r=1-delta` and the far kernel tail gives power `sigma+delta`.
10. The displayed explicit symbol is holomorphic on each bisector component,
    lies in `Psi_sigma^delta`, and has `r^delta psi_0(r)->1`; therefore it lies
    in no faster-decay class.

## Logical boundary

The result disproves necessity of the strict condition in general. It does not
show that `tau>=n/p-n/q` suffices uniformly for every admissible rough
perturbed Dirac operator. This distinction is stated in the packet.

## Novelty audit

The run indexes were searched by arXiv id, exact title, exact remark,
`Psi_sigma^tau`, and critical endpoint terminology. Bounded web searches were
restricted to primary technical sources and found the source and adjacent
functional-calculus papers but no later answer. Priority is not asserted.

## Human review focus

- Check the annular Cauchy bounds for the two disconnected sector components.
- Check the low- and high-frequency dyadic sums at `|x|=1`.
- Confirm the intended interpretation of “necessary” in Remark 3.8.
- A specialist citation search should precede any public novelty claim.
