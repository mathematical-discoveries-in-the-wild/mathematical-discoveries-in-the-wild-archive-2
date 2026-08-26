# Subspace-power counterexample to the proposed Morrey weight class

Status: `candidate_counterexample_likely_valid`  
Source: arXiv:1910.13285, final open question on page 16  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

The proposed sufficiency of

```text
A_{p+lambda/n} intersect RH_{n/(n-lambda)}
```

is false, already for the Hardy--Littlewood maximal operator and already at
strong exponent `p=2`.

In the explicit example

```text
n=2, p=2, lambda=1,
w(x_1,x_2)=|x_2|^(5/4),
```

the weight belongs to `A_(5/2) intersect RH_2`.  Nevertheless, for the
indicators `f_t` of bounded horizontal strips of width `2t`,

```text
||f_t||_{L^(2,1)(w)} = O(t^(9/8)),
||M f_t||_{W L^(2,1)(w)} >= c t.
```

Their quotient grows like `t^(-1/8)`.  Thus `M` is not even bounded from the
strong weighted Morrey space to its weak version.

The packet proves a general codimension-`m` family.  If
`R^n=R^d x R^m`, `d>=lambda`, and

```text
m(p-1) < beta < m(p-1+lambda/n),
```

then `w(y,z)=|z|^beta` belongs to the proposed class but bounded tubes around
`R^d` disprove weak Morrey boundedness of `M`.

## Contents

- `solution_packet.pdf` — full counterexample proof and exact source excerpt.
- `main.tex` — packet source.
- `source_paper.pdf` — arXiv:1910.13285.
- `supporting_2010.00250.pdf` — later intrinsic-weight follow-up used in the
  bounded literature audit.
- `supporting_2211.07974.pdf` — later global/local maximal-operator note used
  in the bounded literature audit.
- `figures/open_question_crop.png` — page-16 source crop.
- `code/check_scaling.py` — exact rational parameter and exponent checks.
- `verification.md` — proof, build, source, and visual-QA record.

## Reproduce the parameter check

```bash
conda run --no-capture-output -n sandbox python code/check_scaling.py
```

The proof is analytic and has no computational dependency.

## Literature boundary

The run indexes and bounded exact-class, title/author, hyperplane-power,
subspace-distance, and citation searches through 2026-08-11 found no matching
resolution.  The 2020 and 2022 supporting papers retain unresolved global
weighted-Morrey characterization questions and do not contain this tube
construction.  This is a bounded novelty audit, not a priority claim.

