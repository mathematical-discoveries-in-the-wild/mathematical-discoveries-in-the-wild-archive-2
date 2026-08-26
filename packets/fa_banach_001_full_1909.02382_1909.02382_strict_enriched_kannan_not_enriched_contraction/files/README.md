# Full Result: A Strictly Enriched Kannan Map Outside the Enriched Banach Class

Status: `full` (candidate; subject to human review)

Source: Vasile Berinde and Mădălina Păcurar, *Approximating fixed points of enriched contractions in Banach spaces*, arXiv:1909.02382.

## Answered Question

Remark 2(2) asks for a strictly enriched Kannan mapping—an enriched Kannan map which is not an ordinary Kannan map—that is also not an enriched Banach contraction.

## Explicit Answer

On the Banach space `R`, define

```text
T(x) = -x          if x <= 2,
       -x - 2/3    if x > 2.
```

Then `T` is `(1,1/7)`-enriched Kannan. It is not ordinary Kannan because the pair `x=1, y=-1` forces every Kannan constant to be at least `1/2`. It is not an enriched Banach contraction because it is discontinuous at `2`, while every enriched Banach contraction is Lipschitz.

## Proof Mechanism

Let `S=(I+T)/2`, so `S(x)=0` for `x<=2` and `S(x)=-1/3` for `x>2`. A one-case check shows that `S` is Kannan with constant `1/7`. The identity `T=2S-I` converts this ordinary Kannan inequality exactly into the enriched Kannan inequality for `T` with enrichment parameter `k=1`.

## Files and Verification

- `solution_packet.pdf`: rendered full proof packet.
- `source_paper.pdf`: original open-problem paper.
- `supporting_paper_1909.02379.pdf`: companion source for the enriched Kannan definition.
- `figures/open_problem_crop.png`: rendered crop of the exact source remark.
- `code/make_open_problem_crop.py`: reproducibly crops and stitches the source remark from rendered pages 4--5.
- `verification.md`: proof audit and bounded novelty-search record.

The proof is entirely analytic and has no computer-assisted dependency.

## Novelty Status

Local corpus/index searches and bounded web searches on August 11, 2026 found later papers using the definitions but no construction or claimed answer to the exact open problem. Novelty is plausible, not certified.

## Human Review Recommendation

Check the cross-branch Kannan estimate for `S` and the source convention for “strictly enriched Kannan.” If those pass, this is a complete explicit answer.
