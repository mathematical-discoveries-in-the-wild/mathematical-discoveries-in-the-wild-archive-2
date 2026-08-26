# Uniform propagation removes the extra diagonal factor

Status: candidate_partial_likely_valid

Source: Théo Belin and Pauline Lafitte, *Quantitative estimates of
L^p maximal regularity for nonautonomous operators and global existence for
quasilinear equations*, arXiv:2403.00386, Theorem 2.5 and Remark 3.4.

## Result

Let I=(a,b) have length T, let A have L^p maximal regularity, and suppose its
zero-initial solution operator is represented by an evolution family U(t,s)
on X with

    ess sup_{a<s<t<b} ||U(t,s)|| = M < infinity.

Then every real diagonal shift satisfies

    [A+lambda] <= (1 + M |1-exp(-lambda T)|) [A].

This removes the source estimate's extra factor |lambda|T in both directions:
the bound is O(1) as lambda tends to positive infinity and O(exp(mu T)) for
lambda=-mu tending to negative infinity.

For A=0 on the scalar space, a normalized source supported in [0,1/mu] gives
the matching lower bound

    [-mu] >= c_p T exp(mu T).

Thus the exponential rate for negative shifts is sharp; only the extra
polynomial loss is removed.

## Scope

This does not settle the question for arbitrary nonautonomous maximally
regular A. Maximal regularity alone controls traces in an interpolation space
and does not automatically yield a uniformly X-bounded evolution family.
That trace-space versus X-space gap is the precise remaining obstruction.

A bounded search by arXiv id, exact question text, and the core terms
nonautonomous maximal regularity, diagonal perturbation, evolution family,
and sharp constant found no later resolution or exact statement of this
partial theorem. Novelty confidence is bounded, not definitive.

## Packet contents

- main.tex, solution_packet.pdf: theorem, complete proof, sharp scalar lower
  bound, and scope analysis.
- source_paper.pdf: arXiv:2403.00386v2.
- figures/open_problem_crop.png: source PDF page 14 containing the estimate
  and open sharpness remark.
- verification_report.md: proof, compilation, and rendering checks.

Human review should focus on whether a given application supplies the exact
Green representation on X assumed in the theorem; no claim is made that bare
maximal regularity supplies it.
