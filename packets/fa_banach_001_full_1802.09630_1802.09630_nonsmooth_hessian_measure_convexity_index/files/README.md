# Nonsmooth Hessian-measure convexity index

Status: `candidate full solution, likely valid`

Source: Youri Davydov, Elina Moldavskaya, and Ričardas Zitikis,
*Searching for, and quantifying, non-convexity of functions*,
arXiv:1802.09630 (future problem on page 15, Section 5).

## Result

The source asks how to modify its Hessian/eigenvalue convexity index for
nondifferentiable limits such as `min{g(x),g(y)}` and `max{g(x),g(y)}`.
The packet gives a full extension to every function whose distributional
Hessian is a finite symmetric matrix-valued Radon measure.

For `D²h = Aρ`, take the pointwise spectral parts and define
`(D²h)± = A±ρ`. The negative mass is exactly the nuclear
total-variation distance from `D²h` to the cone of positive-semidefinite
matrix measures. The positive mass divided by total spectral mass is the new
convexity index. It agrees with the source for smooth functions, equals one
exactly for convex functions, and has a Radon–Nikodym pointwise version on
singular curvature sets.

For two smooth branches, the switching ridge contributes

`+|∇(u-v)| n⊗n H^{d-1}` for `max(u,v)` and
`-|∇(u-v)| n⊗n H^{d-1}` for `min(u,v)`.

The packet also proves that the smooth power-mean indices converge to these
nonsmooth indices as beta tends to plus or minus infinity.

## Concrete check

For the source function on `[0.1,0.9]²`, the exact measure index is
`0.4454880619053803` for the minimum and `1` for the maximum. An 800×800
midpoint computation gives `0.4462763224` at beta `-100` and `1` at beta
`+100`.

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1802.09630_nonsmooth_hessian_measure_convexity_index/code/verify_formulas.py
```

## Files

- `solution_packet.pdf`: full theorem, proof, formulas, limitations, and review notes
- `source_paper.pdf`: original arXiv paper
- `supporting_paper_2112.06209.pdf`: later Hessian–Schatten variation framework
- `figures/open_problem_crop.png`: source page 15
- `code/verify_formulas.py`: numerical sanity checks

## Novelty status

A bounded search found later literature defining nonsmooth Hessian–Schatten
variation, but no exact signed PSD-measure projection theorem, convexity index,
min/max interface formula, or power-mean index convergence answering this
future problem. Novelty is plausible but not certified.

Human review should focus on the strict nuclear convergence theorem and the
endpoint-exhaustion caveat for the source's singular `g`.
