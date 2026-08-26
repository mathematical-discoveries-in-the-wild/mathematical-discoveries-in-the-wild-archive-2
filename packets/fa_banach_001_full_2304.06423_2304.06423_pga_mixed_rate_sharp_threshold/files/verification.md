# Verification report

Status: `candidate_full_likely_valid`

## Exact target

- Source: arXiv:2304.06423v1, Introduction, PDF page 5.
- Question: does the mixed PGA upper rate `m^{-alpha/2}` continue for
  `alpha>1/3`?
- Answer proved: it holds precisely for
  `0<alpha<=alpha_*=0.365551412606085...` and fails above `alpha_*`.

## Proof audit

1. PGA energy satisfies `a_{m+1}=a_m-d_m^2`.
2. With `b_0=||f||_{A_1}` and `b_{m+1}=b_m+d_m`, one has
   `||r_m||_{A_1}<=b_m` and `d_m>=a_m/b_m`.
3. Hence `a_m b_m^{-2}<=(m+1)^{-1}`.
4. The cross-iteration estimate
   `d_l >= (a_k-d_k(b_l-b_k))/b_k` follows by pairing `r_l` with `r_k`.
5. Piecewise-linear interpolation turns that estimate into Sil'nichenko's
   scalar envelope inequality for energy as a function of accumulated mass.
6. The independent rescaling `Phi(z)=F(Az)/h^2` preserves the envelope
   inequality exactly and normalizes `Phi(1)=1`.
7. Sil'nichenko's barrier therefore gives the strengthened invariant
   `a_m b_m^Gamma<=C h^2 A^Gamma`.
8. Multiplying the two invariants with powers `2/(2+Gamma)` and
   `Gamma/(2+Gamma)` cancels `b_m`; square roots yield the endpoint
   `alpha_*=Gamma/(2+Gamma)`.
9. Interpolating the endpoint with energy monotonicity proves every smaller
   alpha.
10. The signed-orthonormal example gives a matching lower rate in the valid
    range.
11. For alpha above the threshold, choose a lower exponent
    `p_*<p<alpha/2` in the fixed-target Klusowski--Siegel theorem. The mixed
    denominator is then a fixed constant, contradicting the target rate.

## Source evidence

`figures/source_question.png` is rendered from page 5 of the official arXiv
PDF and contains the exact open question and the source's old `0.3796`
obstruction.

The decisive supporting sources are included under `supporting/`.

## Numerical audit

High-precision evaluation of the uniquely specified root gives

- `Gamma = 1.1523436882652335431743134935...`
- `alpha_* = Gamma/(2+Gamma) = 0.3655514126060854335...`
- `p_* = alpha_*/2 = 0.1827757063030427168...`

These decimals are informational only; the theorem uses the exact root
characterization.

## Novelty audit

The run indexes, parsed corpus, exact equation, source question, and primary
web sources were searched through 11 August 2026. The 2025 sharp matching
pursuit paper and Temlyakov's 2025 survey give the standard exponent, but no
located source states the two-scale invariant or the resulting sharp mixed
threshold. Novelty confidence is moderate because the rescaling is concise
and could be implicit folklore.

## Artifact audit

The LaTeX packet is compiled with references resolved. Its log is checked for
missing references, overfull boxes, and layout warnings. Every rendered page
is visually inspected. The question crop is rendered from the official PDF.

## Reviewer focus

Check the interpolation of the discrete cross inequality into the scalar
envelope, the invariance of that envelope under `F(Az)/h^2`, and the exact
fixed-dictionary/fixed-target quantifiers of the Klusowski--Siegel lower
theorem. The result concerns rate order; it does not claim the source's unit
upper constant beyond `alpha=1/3`.
