# Outward cusps refute fixed-exponent self-improvement

Status: candidate full counterexample; likely valid; urgent expert review recommended.

Model: GPT5.6.

Source: Riddhi Mishra and Kaushik Mohanta, *How to Recognise Extension domains*,
arXiv:2604.23598v1 (2026), Theorem 1.6 and the question immediately following it.

## Result

For every `n>=2`, `p>1`, and `1/p<s<1`, there is a bounded outward power-cusp
domain `Omega` such that

- `Omega` is a `(1,s,p)` extension domain;
- `H^{n-1+(sp-1)/p}(boundary Omega)=0`;
- `Omega` is not a `(1,p)` extension domain.

Thus the packet does not merely show that the Hausdorff hypothesis cannot be
relaxed: subject to review, it refutes Theorem 1.6 under its stated hypothesis.

The explicit planar instance uses `p=2`, `s=3/4`, and
`Omega={(t,x):0<t<=1, |x|<t^(6/5)} union {(t,x):1<=t<2, |x|<1}`.

## Proof mechanism

Koskela--Zhu's sharp cusp theorem gives a linear
`W^{1,p}(Omega)->W^{1,q}(R^n)` extension for a `q` strictly above the scaling
threshold `np/(n+(1-s)p)`. A direct translation interpolation then gives the
strict embedding `W^{1,q}(R^n)->W^{s,p}(R^n)`. The Poincare property of outward
cusps makes the composition homogeneous. The cusp boundary is
`(n-1)`-rectifiable, whereas measure density fails at the tip, excluding
first-order `p` extension.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `source_paper.pdf`: arXiv:2604.23598v1.
- `supporting_paper_2110.07565.pdf`: cusp extension theorem.
- `supporting_paper_2507.07072.pdf`: homogeneous/nonhomogeneous cusp extension
  equivalence and Poincare property.
- `figures/open_problem_crop.png`: readable source theorem/question crop.
- `figures/cusp_extension_theorem_crop.png`: supporting theorem crop.
- `verification_report.md`: independent audit checklist and novelty bounds.

No computation is used in the proof. Human review should prioritize the
composition of the two extension results, the homogeneous normalization, and
the strict fractional embedding.
