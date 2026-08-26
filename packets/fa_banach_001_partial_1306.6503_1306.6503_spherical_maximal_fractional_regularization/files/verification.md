# Verification report

Status: `candidate_substantial_partial_likely_valid_human_review_needed`

1. The source crop was rendered from PDF page 5 and visually checked against
   Question 1.4.
2. The output translation inequality follows from translation invariance and
   `|sup_r |A_r f|-sup_r |A_r g|| <= sup_r |A_r(f-g)|`; the positive-average
   convention obeys the same inequality via `||f|-|g||<=|f-g|`.
3. For `g_h=tau_h u-u`, the `L^p` estimate has one power of `|h|`, and the
   `L^{p*}` estimate has none. Interpolation with
   `1/q=alpha/p+(1-alpha)/p*` gives exactly
   `alpha=1-n(1/p-1/q)`.
4. Dilation independently forces `alpha-n/q=1-n/p`.
5. In the Lorentz refinement, real interpolation gives
   `(L^p,L^{p*})_(theta,1)=L^{pc,1}`. The exponent of the order-one endpoint
   is `beta=1-n(1/p-1/pc)=n(1-1/p)`.
6. The endpoint spherical-maximal input is used only for `n>=3`; the packet
   explicitly excludes the false circular endpoint.
7. The fractional Sobolev corollary follows by integrating
   `r^{q(alpha-s)-1}` near zero and using the `L^q` norm for large
   translations.
8. Eight distinct upgrade attempts were recorded. None is silently used as
   a lemma in the promoted theorem.

Human review should check the Lorentz interpolation normalization and the
chosen convention for the spherical maximal operator. No computational
claim is part of the proof.
