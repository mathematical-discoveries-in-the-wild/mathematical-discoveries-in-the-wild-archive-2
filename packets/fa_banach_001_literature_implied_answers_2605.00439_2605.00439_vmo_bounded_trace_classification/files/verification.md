# Verification report

Verdict: `same_paper_implied_literal_classification_verified`

## Source audit

The official source PDF is arXiv:2605.00439v3, Auscher--Bechtel,
*Existence and uniqueness of weak solutions to quasilinear PDEs with critical
data*. Definition 1.2 requires global spacetime essential boundedness and a
distributional initial trace. Corollary 1.5 proves existence for all bounded
data satisfying the range condition. Proposition 3.4(b) already shows that a
bounded linear solution has an `L^infinity` initial trace; freezing the
quasilinear coefficient applies it here. The concluding existence bullet must
therefore intend a changed solution class if genuinely unbounded VMO data are
in view.

## Trace audit

The essential spacetime bound gives an `L^infinity` slice bound outside a
null set of times. Taking a sequence of such times to zero bounds the trace
functional by `M ||psi||_1`. Density and `(L^1)^*=L^infinity` give an
`L^infinity` representative of the trace. This remains valid even if the
definition's limit is specified through a weakly continuous representative,
because the same limit holds along the selected full-measure sequence.

## VMO/CMO audit

The example `log(log(e^e+|x|))` is locally bounded and unbounded only at
spatial infinity. Its global Lipschitz bound gives small-ball vanishing. A
radial integral estimate gives centered large-ball oscillation `O(1/log R)`;
balls with center at most twice their radius reduce to centered balls, while
the remaining balls are controlled by the decaying gradient. Fixed balls
translated to infinity are controlled by the same gradient. These are
Uchiyama's three CMO conditions, so the example lies in the smaller of the
two common global VMO spaces.

## Status audit

Necessity comes from the trace lemma and does not use the PDE. Sufficiency is
exactly source Corollary 1.5. The counterexample coefficient `a=I`, `O=R`
satisfies every source assumption. Thus the classification is exact under
the source range condition.

## Classification audit

The literal classification is already implied by the current v3 source; it is
not promoted as a new mathematical answer. Uchiyama's 1978 CMO
characterization is used only to certify that the trace obstruction excludes
data lying in even the smaller standard global VMO convention.

## Computational sanity check

`code/check_vmo_profile.py` numerically integrates centered-ball mean
oscillations in several dimensions and verifies decay consistent with the
symbolic `O(1/log R)` estimate. The classification proof is analytic and does
not rely on this computation.

## Render audit

Final `latexmk` compilation completed without warnings, overfull/underfull
boxes, or unresolved references.  All four rendered pages were inspected at
full resolution and are clean, legible, and free of clipping or layout
defects.  The SHA-256 digest of `solution_packet.pdf` is
`a62dc884ffc809f05b2397c713ef6c4d1409ef565bfb2f79241af80a9d699d35`.

## Human verifier focus

1. Check the reduction from arbitrary large balls to the two center/radius
   cases in Lemma 3.
2. Check compatibility of the source's unspecified VMO convention; the CMO
   example is designed to cover both common conventions.
3. Confirm that the source intended to retain its bounded-solution definition
   in the final VMO bullet; a different solution class is outside this result.
