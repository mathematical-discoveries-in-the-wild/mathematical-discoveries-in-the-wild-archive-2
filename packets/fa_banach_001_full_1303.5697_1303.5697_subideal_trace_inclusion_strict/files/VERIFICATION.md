# Verification Report

Candidate: arXiv:1303.5697, question after Definition 5.11.

## Claim checked

There is a principal `K(H)`-ideal `I` that is not a `B(H)`-ideal and a linear
functional on `I` which is invariant under `U_{K(H)}(H)` but not invariant
under `U^I(H)`. Hence the inclusion displayed after Definition 5.11 is proper.

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source match | valid | PDF page 9 asks exactly whether the Definition 5.11 trace class can be properly contained in the Definition 5.3 class on a non-`B(H)` subideal. |
| Compact generator | valid | `S=D direct_sum (-D)` is compact and has infinite rank. |
| Non-`B(H)` property | valid | `s_m(S)=1/ceil(m/2)`. For every fixed integer `k>1`, `s_{kn}(S)/s_n(S)` tends to `1/k`, not zero. The Fong-Radjavi equivalence quoted on source PDF page 3 therefore shows `(S)_{K(H)}` is not a `B(H)`-ideal. |
| Coefficient uniqueness | valid | The principal-subideal structure theorem and non-`B(H)` property give the direct decomposition `I = C S + I^0`, where `I^0=JS+SJ+J(S)J`; this is exactly the argument in source Example 5.5. |
| Small-unitary invariance | valid | For `V=1+A` with `A in J`, `VSV*-S` lies in `I^0`, and conjugation preserves `I^0`. Thus the scalar coefficient is unchanged. |
| Normalizer membership | valid | The block swap `W` satisfies `WJW*=J` and `WSW*=-S`, so `W I W*=(-S)_J=I`. Hence `W in U^I(H)`. |
| Strictness | valid | `tau(S)=1` while `tau(WSW*)=tau(-S)=-1`. Therefore `tau` belongs to the Definition 5.3 class but not the Definition 5.11 class. |
| Proper subideal | valid | `I` is a `J`-ideal and is not a `B(H)`-ideal by the singular-value test. |

## Counterexample search

The construction was checked against the two possible failure modes. The
normalizing unitary genuinely lies outside `1+K(H)`: `W-1` acts as `-2` on the
infinite-dimensional antisymmetric subspace. The coefficient functional is
not the ordinary operator trace and does not require `S` to be trace class.

## External dependencies

The proof uses two results reproduced in arXiv:1303.5697:

- the Fong-Radjavi criterion for a principal `K(H)`-ideal to be a `B(H)`-ideal;
- the principal `J`-ideal structure and coefficient functional of Example 5.5.

All new identifications involving the signed generator and block swap are
proved directly in the packet.

## Gaps

No mathematical gap found. The main novelty risk is that this short
construction may be folklore despite not appearing in the bounded search.

## Confidence

Score: 97/100.

## Human review recommendation

Check the principal-subideal direct-sum decomposition first, then the
normalizer computation. The final separation is immediate once those are
accepted.

