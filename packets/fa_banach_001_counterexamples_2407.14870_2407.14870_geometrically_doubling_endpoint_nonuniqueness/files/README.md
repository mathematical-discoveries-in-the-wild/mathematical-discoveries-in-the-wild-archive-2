# Candidate counterexample: lacunary endpoint generators

**Status:** `candidate_counterexample_likely_valid` (human verification required)

For every `1 <= p < 2` and every eventually geometrically doubling weight
`W`, this packet constructs two non-quasi-equivalent generating distributions
for each endpoint Orlicz scale

```text
M_-(t) ~ t^p / W(log(1/t)),
M_+(t) ~ t^2 W(log(1/t)).
```

The two distributions use the full height grid `exp(2^k)` and its odd-indexed
subgrid. Their `L_p+L_2` modulars remain comparable, but their tails differ by
doubly exponential factors in the omitted gaps. For `W(s)=s`, the upper
construction generates `ell_(t^2 log(e/t))` and directly contradicts the
tail conclusion of Braverman (1993), Theorem 4.2, as printed, as well as the
uniqueness conclusion repeated in Astashkin's 2024 survey, Remark 5.1.

## Packet contents

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: arXiv:2407.14870.
- `supporting_braverman_1993.pdf`: the cited 1993 theorem source.
- `figures/open_problem_crop.png`: the current source's natural question.
- `figures/braverman_theorem_4_2_crop.png`: the contradicted printed theorem.
- `code/check_endpoint_examples.py`: log-domain numerical stress test.
- `verification.md`: adversarial proof and novelty audit.

## Reproduction

From this packet directory:

```bash
conda run --no-capture-output -n sandbox python code/check_endpoint_examples.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

## Human-review recommendation

Check three isolated points in order:

1. the two threshold modular estimates in equations (8)--(15);
2. the fixed-rescaling tail separation on the full and odd grids;
3. the identification of the upper `W(s)=s` modular with Braverman's
   `Psi_2(t) ~ t^2 log(e/t)` coefficient estimate.

The general uniqueness characterization remains open; the result is a broad
endpoint family and a counterexample to the printed quadratic-endpoint claim.
