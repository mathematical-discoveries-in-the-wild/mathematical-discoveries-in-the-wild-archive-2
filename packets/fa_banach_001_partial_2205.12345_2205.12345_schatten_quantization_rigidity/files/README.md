# Schatten rigidity for scaled Fock quantization

Status: `candidate_partial_result_likely_valid`  
Source: arXiv:2205.12345, final problem in Section 5  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

For every Schatten exponent `1 <= p <= n`, a bounded symbol `f` satisfies

```text
||T_f^(t) T_g^(t) - T_fg^(t)||_{S_p} -> 0
```

for every bounded `g` if and only if `f` is constant. This completely
answers the source's Hilbert--Schmidt question in complex dimensions at
least two, and its trace-class question in every dimension. The range
`p > n`, including Hilbert--Schmidt in dimension one, remains open.

The proof tests with `g = conjugate(f)`, uses the exact positive Hankel-square
identity, scales Hu--Virtanen's Schatten/IDA theorem, and proves a new
first-order analytic-distance rigidity lemma by mollification.

## Contents

- `solution_packet.pdf`: theorem, complete proof, intuition, exact source
  screenshot, limitations, and references.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv:2205.12345 PDF.
- `source_excerpt_open_problem_page_10.pdf`: exact question page.
- `supporting_2012.13768v2_schatten_ida.pdf`: official theorem paper.
- `supporting_excerpt_theorem_1_1_page_3.pdf`: exact supporting theorem page.
- `supporting_2012.13768v4_corrigendum.pdf` and
  `supporting_excerpt_corrigendum_page_1.pdf`: later correction record.
- `figures/`: rendered source/support pages.
- `verification.md`: proof, provenance, build, and visual-QA record.

## Scope

The characterization is complete only for `1 <= p <= n`. The proof gives a
precise obstruction at `p > n`: the induced analytic-distance rate is
sub-first-order, and even smooth compactly supported symbols pass the
necessary `g = conjugate(f)` test there.
