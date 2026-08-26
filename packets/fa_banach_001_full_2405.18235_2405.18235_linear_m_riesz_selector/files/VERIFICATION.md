# Verification audit

## Source match

Source page 26 states Corollary 4.8 with block size
(Cm^2B/\varepsilon^2), then asks whether this is asymptotically optimal as
(m\to\infty). The packet keeps (B) and (\varepsilon) fixed when discussing
the (m)-exponent, exactly as the source's phrasing “as (m\to\infty)”
indicates.

## Upper-bound proof obligations

1. **Normalization.** If (u_i^{(j)}) has norm one and Bessel bound (B),
   then (a_i^{(j)}=B^{-1/2}u_i^{(j)}) has Bessel bound one and squared norm
   (\eta=1/B).
2. **Naimark complements.** Source Lemma 4.3 supplies a Bessel-one family
   (v^{(j)}) with squared norms (1-\eta). On any subset, lower Riesz bound
   (\delta) for (a^{(j)}) is equivalent to Bessel bound (1-\delta) for
   (v^{(j)}).
3. **One simultaneous selector.** Apply source Corollary 3.4 to all (2m)
   families. Their norm parameters sum to
   (m\eta+m(1-\eta)=m). The same selector gives excess
   (E_r=1/r+2\sqrt{m/r}) for every original and complement family.
4. **Error budget.** If (r\ge16mB^2/\varepsilon^2), then
   (2\sqrt{m/r}\le\varepsilon/(2B)) and
   (1/r\le\varepsilon/(2B)), hence (E_r\le\eta\varepsilon).
5. **Upper Riesz bound.** The original normalized family has Bessel bound at
   most (\eta(1+\varepsilon)).
6. **Lower Riesz bound.** The complement has Bessel bound at most
   (1-\eta+\eta\varepsilon=1-\eta(1-\varepsilon)). Lemma 4.3 therefore gives
   lower bound (\eta(1-\varepsilon)) for the normalized original.
7. **Scale back.** Multiplication by (B^{1/2}) multiplies Riesz bounds by
   (B=1/\eta), yielding (1-\varepsilon,1+\varepsilon).

## Lower-bound proof obligations

1. For each shift, the first block is an orthonormal basis and the second is
   an orthonormal family whose cross-Gram matrix is (\alpha) times a cyclic
   permutation.
2. The full Gram matrix has eigenvalues (1-\alpha) and (1+\alpha), so the
   Bessel bound is (1+\alpha\le B).
3. Every pair selected from the two blocks is aligned by one of the first
   (r\le m) cyclic shifts and has inner product (\alpha>\varepsilon).
   Its two-vector Gram matrix has eigenvalues (1\pm\alpha), so it fails the
   requested Riesz bounds.
4. At (B=2), take (\alpha=1); the witness pair is literally duplicated and
   has Gram eigenvalues zero and two.

## Computational verification

`code/check_linear_selector.py` uses exact rational arithmetic to check 4,050
upper-bound scalar cases and exhausts 22,140 selector pairs in the cyclic
construction, for 26,190 total exact checks. The code is a guard against
constant and indexing errors, not evidence replacing the proof.

## Upgrade, novelty, and limitations

After finding the linear upper bound, a distinct lower-bound construction was
pursued and succeeded, identifying the exact (m)-exponent. A further attempt
to retain both linear (m)- and linear (B)-dependence stalled: the one-step
argument pays (B^2), whereas the source's two-stage argument pays (m^2B).
Combining them gives the joint upper bound
(O(\varepsilon^{-2}\min\{mB^2,m^2B\})). The optimal joint dependence on
(m,B,\varepsilon) remains open.

Four cheap run indexes and bounded exact-title, exact-question,
simultaneous-selector, and Naimark-complement searches found no duplicate or
later resolution through 11 August 2026. Because the proof is a short new
combination of two results in the source paper, unindexed-folklore risk is
real; novelty confidence is moderate. Human review should focus on the single
simultaneous application of Corollary 3.4 and the Naimark-complement scaling.

