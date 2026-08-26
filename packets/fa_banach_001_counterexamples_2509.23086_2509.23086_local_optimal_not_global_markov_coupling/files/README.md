# Three-state Markovian-coupling counterexample

Status: `full_counterexample_likely_valid`.

This packet answers Remark 2.20 of arXiv:2509.23086 negatively.  A unique
instantaneously `c`-optimal coupling generator on a three-point state space is
strictly worse at time two than a coupling differing at one joint state.

## Contents

- `solution_packet.pdf` — self-contained statement and exact proof.
- `main.tex` — packet source.
- `source_paper.pdf` — source paper containing Remark 2.20.
- `figures/open_question_crop.png` — source-question excerpt.
- `code/verify_counterexample.py` — exact finite-state audit.
- `novelty.md` — bounded novelty search.
- `verification_report.md` — proof and artifact checks.

## Reproduction

Run:

```sh
conda run --no-capture-output -n sandbox python code/verify_counterexample.py
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The exact semigroup gap is `2*exp(-4)*(exp(2)-5) > 0`.

