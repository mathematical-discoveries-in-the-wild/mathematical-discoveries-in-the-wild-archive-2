# Riesz--Kantorovich modulus question from arXiv:1501.01685

Status: `literature_already_answered`

Source paper: V. G. Troitsky and F. Xanthos, *Spaces of regular abstract
martingales*, arXiv:1501.01685.

Supporting answer: Michael Elliott, *The Riesz--Kantorovich formulae*,
`Positivity` 23 (2019), 1245--1259,
DOI [10.1007/s11117-019-00661-9](https://doi.org/10.1007/s11117-019-00661-9).

## Identification

In Section 2, on page 5 of the locally rendered source PDF, Troitsky and
Xanthos recall the open problem whether the modulus of a linear operator,
whenever it exists, must be given by the Riesz--Kantorovich formula.  The paper
uses this operator problem as an analogy before disproving the corresponding
Krickeberg-formula conjecture for martingales.

Elliott's 2019 paper explicitly calls the operator problem long-standing and
resolves it negatively.  Its main theorem constructs a compact Hausdorff space
`K` and a regular operator

```text
R : L^1[0,1] -> C(K)
```

whose modulus exists but is not described by the Riesz--Kantorovich formula.
Thus the exact general question recalled in arXiv:1501.01685 has a negative
answer in later literature.

## Scope

The literature answer concerns the general existence-of-a-modulus question.
Elliott notes that a narrower question remains: if the entire regular-operator
space is itself a vector lattice, must its lattice operations satisfy the
Riesz--Kantorovich formulae?  This packet does not claim to answer that
stronger structural variant.  The martingale-specific questions advertised by
arXiv:1501.01685 are answered inside that same source paper and are not counted
as separate literature results.

## Search evidence

Cheap run indexes were searched for the arXiv id, title, `regular abstract
martingales`, `Riesz-Kantorovich`, and `modulus of an operator`; no prior packet
or attempt for this exact source was found.  A bounded primary-literature
search for the exact open-problem phrase and counterexamples located Elliott's
publisher record and article.  The article introduction explicitly traces the
problem to Aliprantis--Tourky, the same monograph cited by the source sentence,
and states that its theorem resolves the issue.

## Files

- `source_paper.pdf`: locally rendered arXiv:1501.01685 source.
- `supporting_paper_elliott_2019.pdf`: decisive 2019 supporting article.
- `main.tex` and `solution_packet.pdf`: compact status note.

Ledger: `runs/fa_banach_001/ledger/results/1501.01685_riesz_kantorovich_answered_by_elliott_2019.json`.

