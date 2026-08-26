# 1707.08890 — weighted stable-domain obstructions

Status: `candidate_full_counterexamples_human_review_needed`.

Model: `GPT5.6`.

Source: István Berkes and Robert Tichy, *Lacunary series and stable
distributions*, arXiv:1707.08890.

## Results

The source's broad uniform weighted extension has two independent
obstructions.

1. If the fixed stable distribution may be nonsymmetric, iid positive
   strictly `1/2`-stable variables and coefficients in alternating sign blocks
   give endpoint limits `X` and `-X`. The source's raw negligibility condition
   holds, but no positive normalization and centering can make the limits
   agree. This example lies inside a strict normal domain.

2. Under the broader balanced regularly-varying-tail reading, take symmetric
   `X` with `P(|X|>x)=1/(x log x)`. Positive coefficient blocks can satisfy
   `max a_k / sum a_k -> 0` while each stage endpoint is asymptotic, at its only
   possible nondegenerate scale, to one copy of the original nonstable `X`.
   Thus no normalization or centering gives a stable limit.

Both base sequences are iid, so no subsequence selection can help.

## Files

- `main.tex`: complete statements and proofs.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof and scope audit.
- `source_paper.pdf`: source PDF downloaded from arXiv.
- `figures/open_question_crop.png`: source theorem and open-question paragraph.

## Scope

The slowly varying example is not claimed against the strict symmetric normal-
domain reading: `1/log x` is not asymptotically constant. The sign example is
strict-normal but nonsymmetric. The packet separates these cases because the
source wording and its broader regularly-varying conjectural text use
different domain terminology.

A bounded local and external search on 2026-08-13 found no later resolution of
the source question. Specialist proof, terminology, and novelty review remain
appropriate.
