# Verification notes

Status: `likely valid`; recommended for expert review.

## Line-by-line audit

1. **Gauge sublevels.** For a star body `K`, the identity
   `{rho_K<=r}=rK` holds up to an irrelevant boundary convention. Hence its
   volume is exactly `r^m vol(K)`.
2. **Pushforward density.** The distribution function of the gauge radius is
   `r^m vol(K)`. Its Lebesgue--Stieltjes measure on `(0,infinity)` is
   `m vol(K) r^{m-1}dr`; the origin has zero Lebesgue mass.
3. **Product formula.** Applying the one-block pushforward independently in
   `n` coordinates is a direct use of product measures/Tonelli. No angular
   regularity or smooth boundary is assumed.
4. **Outer constraint.** The indicator of the positive `l_q^n` unit ball is
   Borel and the weighted radial integral is finite. For `q=infinity` this
   radial region is simply `[0,1]^n`.
5. **Identification.** With `K=B_p^m`, the block gauge is exactly `||.||_p`,
   including the usual modifications at `p=infinity`. With `L=B_q^m`, the
   outer `l_q` sum of the inner `l_q` gauges is the ordinary `l_q` gauge on
   `R^{mn}`.
6. **Quasi-Banach exponents.** Nothing uses the triangle inequality or
   convexity. Homogeneity of `l_p` quasi-balls is enough for `0<p<1` or
   `0<q<1`.
7. **No circularity.** The common radial integral is never evaluated. Taking
   a ratio cancels it, so the proof does not use Dirichlet's or the source's
   gamma formula.
8. **Transport form.** Normalized cone measures of centrally symmetric star
   bodies in dimension at least two are nonatomic standard probability
   spaces, hence are isomorphic modulo null sets. Homogeneous extension of
   such an isomorphism preserves gauge radius and has the asserted constant
   measure-scaling factor. The symmetric one-dimensional case is the explicit
   matching of the two endpoints.

## Edge checks

- `n=1`: both sides reduce to `vol(B_p^m)`.
- `m=1`: `B_p^1=B_q^1=[-1,1]`, so the factor is one and the mixed ball is
  `B_q^n`.
- `p=q`: the volume ratio is one and `B_{p,p}^{m,n}=B_p^{mn}`.
- `q=infinity`: the mixed ball is the Cartesian product `(B_p^m)^n`, and the
  formula becomes `vol(B_p^m)^n`; the theorem gives this immediately.

## Bounded novelty/literature search

Search date: 11 August 2026.

Sources searched:

- the run's solution, attempt, proof-gap, and ledger indexes;
- arXiv:1505.05867 full source and exact closing-question sentence;
- title/citation and exact-formula searches;
- combinations of `geometric interpretation`, `mixed sequence spaces`,
  `mixed-norm unit ball`, `volume ratio`, `block polar`, and `cone measure`;
- later papers on mixed-norm volumes and arXiv:1906.04997 on Lorentz-ball
  volumes.

The 2019 Doležalová--Vybíral paper answers the source's first closing question
about finite-dimensional Lorentz balls. No source found in this bounded search
gave the block-shell ratio theorem above as an answer to the second question.
This supports, but does not establish, novelty.

## Human-review recommendation

Verify the gauge-pushforward identity with the preferred boundary convention
and confirm that “non-analytical” is interpreted as gamma-free geometric shell
disintegration. The mathematical identity itself is a direct consequence of
homothety and product measure.
