# Sharp weak-star FPP stability constant: answered by arXiv:1611.02133

Status: `literature_already_answered` (full answer).

## Original question

Emanuele Casini, Enrico Miglierina, Łukasz Piasecki, and Roxana Popescu, *Weak-star Fixed Point Property in ell_1 and Polyhedrality in Lindenstrauss Spaces*, arXiv:1604.07587.

Remark 3.5 on source PDF page 8 obtains the stability estimate `2/(1+r)`, notes sharpness at `r=0`, and says that proving sharpness for `0<r<1` remains open.

## Answer

The same authors' later paper, *Stability constants of the weak-star fixed point property for the space ell_1*, arXiv:1611.02133 / JMAA 452 (2017), 673-684, explicitly cites the source and settles the question. Proposition 2.4 proves the missing reverse inequality, and Theorem 2.5 on supporting PDF page 7 states

```text
gamma*(X) = 2/(1+r*(X))
```

for every predual `X` of `ell_1` having the relevant weak-star fixed point property. This includes the source's open regime `0<r*(X)<1` and proves sharpness.

## Provenance

This is an explicit answer, not an agent-inferred theorem match: the supporting paper identifies arXiv:1604.07587 as its reference [7], restates its lower bound, and says its main result supplies the reverse inequality.

## Files

- `main.tex`, `solution_packet.pdf`: compact identification note.
- `source_paper.pdf`: arXiv:1604.07587.
- `supporting_paper_1611.02133.pdf`: decisive answer paper.

## Human review recommendation

Accept as a full `literature_already_answered` identification. Verify source Remark 3.5 (PDF p. 8), supporting Proposition 2.4 and Theorem 2.5 (PDF p. 7), and the explicit citation of the source as reference [7].
