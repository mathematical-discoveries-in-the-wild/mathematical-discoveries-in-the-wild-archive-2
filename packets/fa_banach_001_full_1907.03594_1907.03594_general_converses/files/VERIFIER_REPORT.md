# Verification Report

Candidate: arXiv:1907.03594, full answer to the final converse question

## Verdict

`likely valid` (candidate full result)

## Claim-by-claim audit

| Check | Status | Reason |
| --- | --- | --- |
| Exact source target | valid | Source PDF p. 13 explicitly asks whether the converses of Results 3.2 and 3.3 hold in general. |
| Result 3.2 quantifiers | valid | It concerns continuous linear `delta:A->A**` for an arbitrary C*-algebra, with conclusion `delta=d+eta(.)`, `eta` central in `A**`. |
| First ordinary identity | valid | Substitution gives `d(ab)+2 eta ab`; centrality justifies `a eta b=eta ab`. |
| Second ordinary identity | valid | Interchanging `a,b` gives `d(ba)+2 eta ba`. |
| Result 3.3 quantifiers | valid | Its conclusion supplies both representations with star derivations; the converse calculation itself does not use a unit. |
| First star identity | valid | The left representation gives `d_1(ab*)+ab* eta*+eta ab*=0`. |
| Second star identity | valid | The right representation gives `d_2(b*a)+eta* b*a+b*a eta=0`. |
| Involution convention | valid | A star derivation satisfies `d(b)^*=d(b*)`, exactly what both calculations use. |
| Bidual products | valid | The canonical A-bimodule structure on `A**` is associative, so every rearrangement except the explicitly central one is formal. |
| Strengthening | valid | No centrality condition on `eta` is used in the converse of Result 3.3. |

## Adversarial readings

- If “converse” has its standard logical meaning, the proof is complete.
- The structural statements are not replaced by Proposition 3.4's inner
  formulas; the proof uses exactly the conclusions of Results 3.2 and 3.3.
- The codomain is retained as `A**`, so no hidden assumption that derivations
  or multiplier terms land back in `A` is introduced.
- Continuity is not used in the reverse implications, but retaining it causes
  no mismatch with the source.
- The first proof cannot omit centrality of `eta`; the second proof genuinely
  can omit real-part centrality because each multiplier term already contains
  the relevant zero product.

## Literature audit

Exact-title, exact-sentence, and topic searches through 2026-08-17 found no
stated answer.  OpenAlex lists 21 citing works; their titles and available
primary texts address adjacent zero-product, Lie-centralizer, and
anti-derivable-map questions, not these two formal converses.  Novelty is
plausible, not certified.

## Rendering audit

Compiled with `latexmk` under TeX Live 2026.  The final packet has three US
Letter pages.  Every page was rasterized at 150 dpi with Poppler and inspected
at original resolution.  There is no clipping, overlap, missing glyph,
malformed equation, or illegible source crop.

Final SHA-256 values:

- `solution_packet.pdf`: `0c9352cc75254ec052f4ad8a90dcc25819a850868d84a7401061fb5714e84f80`
- `source_paper.pdf`: `3f72a3a309312ffd972bd7064404e744958f39ede99ce48b534c3a3e1be12693`
- `main.tex`: `baa8ed18ab88ed351109fe37e276bf412aa03c379c8cec660d5b85a038146f93`
- `figures/open_question_crop.png`: `92ae18d499385edb2f2ca26066a40d25ceabfb264d92cd384c82d0e1135405c5`

## Confidence

98/100 after mathematical and typography audit.  The remaining uncertainty is interpretation
of the source's final sentence, not the algebra under the ordinary reading.

## Human review recommendation

`send to human`

Ask the reviewer to confirm the intended meaning of “converses” and compare
the two decompositions in Result 3.3 with the two zero-product identities.
