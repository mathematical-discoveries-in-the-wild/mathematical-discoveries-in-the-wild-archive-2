# Carleson-packed product-BMO lower bounds for bi-commutators

Status: `candidate_partial_likely_valid`

Source: Tuomas Hytönen, *The L^p-to-L^q boundedness of commutators with
applications to the Jacobian operator*, arXiv:1804.11167, Section 1.6(2),
printed page 7.

## Result

The unrestricted diagonal bi-commutator characterization remains open.  This
packet proves two structural classes.

1. Fix a tensor-product dyadic/Meyer wavelet basis.  If the first-coordinate
   wavelet intervals on which the symbol has a nonzero coefficient form a
   Carleson family of packing constant `Lambda`, then

   ```text
   ||b||_(product BMO) <= sqrt(Lambda) ||b||_(rectangular BMO).
   ```

   The same holds with the coordinates interchanged.  Combining this with the
   surviving rectangular lower bound for nondegenerate bi-commutators gives a
   full boundedness characterization on this class.  In particular, symbols
   using at most `M` wavelet scales in either coordinate satisfy the missing
   lower bound with loss `sqrt(M)`.

2. For pure tensor symbols `b(x1,x2)=u(x1)v(x2)`, the repeated commutator
   factors as a Hilbert-space tensor product of the two one-parameter
   commutators.  A weighted layer-cake proof shows
   `||u tensor v||_(product BMO) ~ ||u||_BMO ||v||_BMO`, giving a
   dimension-free full characterization on the pure-tensor class even when
   every scale is active.

## Main mechanism

For each first-coordinate wavelet interval `I`, rectangular BMO makes the
second-coordinate coefficient sequence Carleson.  If `Omega_I` is the union
of all dyadic `J` with `I x J` contained in an open set `Omega`, this bounds
the coefficient mass over that slice by
`B^2 |I| |Omega_I|`.  Layer cake converts the support-family packing bound
into `sum_I |I| |Omega_I| <= Lambda |Omega|`.  This is exactly the open-set
Carleson estimate defining product BMO.

## Verification and scope

- The proof is analytic and uses no numerical verifier.
- Eight focused upgrade attempts were recorded in the attempt file.  The old
  quadrant argument, modulation, randomization, frequency-band projection,
  and a direct bootstrap all fail to remove the restriction because they do
  not uniformly control arbitrarily deep incomparable rectangle families.
- The related dyadic result of Holmes--Treil--Volberg assumes alternating
  (“even-even”) Haar scales.  It is stronger in a different direction but does
  not contain the Carleson-packed class or settle the continuous
  Hilbert-transform problem.
- The crop script only reproduces the source evidence; it is not a verifier.

## Novelty check

A bounded search through 2026-08-11 covered the four run indexes, the local
source corpus for arXiv:1804.11167 and arXiv:2101.00763, the current
Airta--Hytönen--Li--Martikainen--Oikari paper arXiv:2005.03548, and official
arXiv queries using `product BMO`, `rectangular BMO`, `finite scales`,
`Carleson family`, and `bi-commutator`.  It found the known alternating-scale
dyadic theorem, but no statement matching the support-packing lemma or the
resulting continuous finite-complexity classification.  This is not a
priority claim.

## Human review recommendation

Check the passage from rectangular oscillation BMO to the fixed wavelet
rectangular norm, the maximal-dyadic-interval step defining `Omega_I`, and the
weighted layer-cake argument for pure tensors.  Preserve the explicit
restriction: the general diagonal product-BMO lower bound remains open.

