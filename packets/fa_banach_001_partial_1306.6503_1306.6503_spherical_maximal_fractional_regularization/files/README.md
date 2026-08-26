# Scale-sharp fractional regularity for the low-exponent spherical maximal problem

Status: `candidate_substantial_partial_likely_valid_human_review_needed`

Source: Piotr Hajlasz and Zhuomin Liu, *Sobolev spaces, Lebesgue points
and maximal functions*, arXiv:1306.6503, Question 1.4 (PDF page 5).

## Result

Let `pc=n/(n-1)`, `1<p<n`, and `p*=np/(n-p)`. For every

```text
max(p,pc) < q < p*,
alpha = 1 - n(1/p-1/q),
```

the spherical maximal operator satisfies the scale-invariant estimate

```text
sup_(h != 0) |h|^(-alpha)
  ||tau_h(Su)-Su||_q <= C ||grad u||_p.
```

Consequently `S:W^{1,p}->W^{s,q}` for every `0<s<alpha`. At the
critical source exponent `p=pc`, this yields every fractional order `s<1`
with `q>pc` sufficiently close to `pc`.

For `n>=3` and `1<p<pc`, Bourgain's endpoint Lorentz theorem gives the
critical refinement

```text
sup_(h != 0) |h|^(-beta)
  ||tau_h(Su)-Su||_(L^{pc,infinity}) <= C ||grad u||_p,
beta = n(1-1/p).
```

The exponents are forced by scaling.

## Proof mechanism

Translation invariance and sublinearity reduce an output translation
difference to `S(tau_h u-u)`. The difference has an order-one `L^p` bound
and an order-zero `L^{p*}` bound. Interpolation puts it in an exponent where
the strong spherical-maximal theorem applies. Real interpolation plus the
endpoint Lorentz spherical-maximal theorem gives the critical refinement in
dimensions at least three.

## Limitation

Critical Besov regularity at a larger integrability exponent does not embed
back into `W^{1,p}`; the embedding direction is the reverse. Eight focused
upgrades tested direct difference quotients, endpoint Lorentz theory,
critical embeddings, the maximal-potential representation, maximizing-radius
cancellation, singular radial counterexamples, and vector-valued scale
summability. None supplies the missing full derivative. The source conjecture
therefore remains open.

## Files

- `solution_packet.pdf`: theorem, proofs, sharpness, and obstruction audit.
- `source_paper.pdf`: source arXiv paper.
- `figures/source_question_crop.png`: Question 1.4 and the source's endpoint comment.
- Attempt log: `runs/fa_banach_001/attempts/1306.6503_spherical_maximal_fractional_regularization.md`.

Human review should focus on the Lorentz real-interpolation step and the
precise strong/endpoint spherical-maximal conventions. No computational
dependency is used.
