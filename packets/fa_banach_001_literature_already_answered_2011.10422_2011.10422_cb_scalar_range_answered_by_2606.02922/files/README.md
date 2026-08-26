# Literature answer: scalar-range completely bounded Crouzeix abstraction

Run: `fa_banach_001`  
Agent: `agent_lane_15`  
Result type: `literature_already_answered`

## Result

The explicit question on arXiv:2011.10422v3 PDF page 9 asks whether the
completely bounded conjecture holds for the disk algebra when the antilinear
map has scalar range. Hartz--McCarthy, arXiv:2606.02922, answer this
affirmatively and in greater generality. Their Theorem 1.2 implies

```text
||theta||_cb <= max(1, ||theta + beta I||_cb).
```

Writing `alpha(f)=lambda(f)1` and `beta(f)=conj(lambda(f))` gives
`2 theta_alpha = theta + beta I`, hence `||theta||_cb <= 2`.

## Scope

This does not settle the source's unrestricted norm or completely bounded
conjectures. The August 2026 Lorist--Schwenninger preprint proves classical
Crouzeix and an abstract variant assuming complete positivity, which is
strictly stronger than the source's ordinary contractivity hypothesis.

## Evidence and files

- `source/2011.10422v3.pdf`: official source paper; question on PDF page 9.
- `source/2606.02922.pdf`: official answering paper; decisive theorem on page 2
  and proof in Section 4.
- `source/2608.03841.pdf`: official current-status paper; classical proof and
  complete-positive abstract variant.
- `source/source_question_page9.png`: real crop from the official source PDF.
- `main.tex`: literature-status packet with proof intuition and reduction.
- `solution_packet.pdf`: final packet after render verification.
- `VERIFICATION.md`: mathematical, provenance, visual, and checksum audit.

## Human review recommendation

Check the conjugation in `beta(f)=conj(lambda(f))`, Theorem 1.2 of
arXiv:2606.02922, and the scope distinction between ordinary contractivity and
complete positivity.
