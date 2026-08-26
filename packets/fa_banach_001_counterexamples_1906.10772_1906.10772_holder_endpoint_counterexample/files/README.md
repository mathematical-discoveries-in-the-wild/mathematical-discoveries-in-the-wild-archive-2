# Endpoint counterexample to the Hölder conjecture

Status: `candidate_counterexample_likely_valid`  
Source: arXiv:1906.10772, Open Question (ii)  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Result

The conjectured multiplication theorem is false in its stated range, which
includes `p=infinity`. For every `q in (1,infinity)`, there are

```text
f in T_infinity^(1)(t),
g in T_q^(1)(t),
```

such that `fg` is not even in `L^q`, hence not in `T_q^(1)(t)`. The example
belongs to the natural completion of the Schwartz core, not only to the
maximal class defined by finite endpoint norm.

Near zero, with `L(t)=log(e/t)`, choose

```text
f(t) = L(t)^a,
g(t) = t^(-1/q) L(t)^(-a-1/q),       0<a<1,
```

and smoothly cut both off. Then `t f'(t)` is bounded and tends to zero,
`t g'(t)` is in `L^q`, but

```text
|f(t)g(t)|^q = 1 / (t log(e/t)),
```

which is not integrable at zero.

## Contents

- `solution_packet.pdf`: complete proof, endpoint repair, and exact source
  excerpt.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv:1906.10772 PDF.
- `source_excerpt_open_questions_page_41.pdf`: exact conjecture page.
- `source_excerpt_tinfty_page_13.pdf`: exact proposed endpoint norm and the
  source's unbounded logarithm observation.
- `figures/`: rendered source pages.
- `verification.md`: proof, provenance, build, and visual-QA record.

## Scope

Open Question (ii) is answered negatively as written. The finite-exponent
noninteger-order subproblem, and source questions (i) and (iii), remain
outside this result.
