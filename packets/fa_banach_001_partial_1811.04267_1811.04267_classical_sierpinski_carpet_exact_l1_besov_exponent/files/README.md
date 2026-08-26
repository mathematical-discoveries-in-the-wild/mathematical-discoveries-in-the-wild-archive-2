# Exact L1 Besov critical exponent of the classical Sierpiński carpet

Status: `candidate_partial_result_likely_valid`.

Source: Alonso Ruiz, Baudoin, Chen, Rogers, Shanmugalingam, and Teplyaev,
*Besov class via heat semigroup on Dirichlet spaces I: Sobolev type
inequalities*, arXiv:1811.04267, Example 5.10 on p. 25.

## Result

For the classical planar Sierpiński carpet, in both its compact and standard
unbounded realizations,

```text
lambda_1^* = lambda_1^# = log(4)/log(3),
alpha_1^*  = alpha_1^#  = log(4)/(d_W log(3)).
```

The new step is an endpoint argument. The annular discrete `1`-capacity on
the level-`n` carpet graphs is a min-cut of order `2^n`. Hölder comparison on
the `O(8^n)` annular edges then proves that the `p`-capacity exponent tends to
the endpoint as `p -> 1`. Combining this with the 2025 exact `p>1` critical
Besov theorem gives the upper bound. The 2022 indicator construction gives
the matching density lower bound.

## Scope

This is a complete theorem for the classical carpet and a substantial partial
answer to the source's broader question about Sierpiński carpets. Generalized
carpets and the sharper weak Bakry–Émery conjecture remain outside the claim.

Human-review recommendation: review as a likely-valid full classical-carpet
answer. The key point to inspect is the uniform nested-wall upper cut in
Lemma 1 of the packet; the remaining interpolation argument is formal.

Files:

- `solution_packet.pdf`: proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:1811.04267.
- `supporting_paper_1903.10078.pdf`: the known matching lower bound.
- `supporting_paper_murugan_shimizu_2025.pdf`: the exact `p>1` critical theorem.
- `figures/open_problem_crop.png`: source-page crop.
- `code/capacity_probe.py`: small max-flow/min-cut sanity check.
- `verification_report.md`: proof and artifact checks.

Ledger: `runs/fa_banach_001/ledger/results/1811.04267_classical_sierpinski_carpet_exact_l1_besov_exponent.json`.
